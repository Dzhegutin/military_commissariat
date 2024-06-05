from django.db import models

# Create your models here.
class MilitaryCommissariat(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Official(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    military_commissariat = models.ForeignKey(MilitaryCommissariat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

class PersonalData(models.Model):
    passport_series = models.CharField(max_length=4)
    passport_number = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.passport_series} {self.passport_number}'


class Conscript(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    personal_data = models.OneToOneField(PersonalData, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'



class FitnessForService(models.Model):
    category = models.CharField(max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.category



class Summon(models.Model):
    conscript = models.ForeignKey(Conscript, on_delete=models.CASCADE)
    appearance_date = models.DateField()
    appearance_time = models.TimeField()
    appearance_location = models.CharField(max_length=100)
    reason = models.TextField()
    issued_date = models.DateField()
    official = models.ForeignKey(Official, on_delete=models.CASCADE)

    def __str__(self):
        return f'Summon for {self.conscript} on {self.appearance_date}'

class MedicalExamination(models.Model):
    conscript = models.ForeignKey(Conscript, on_delete=models.CASCADE)
    examination_date = models.DateField()
    health_notes = models.TextField()
    fitness_for_service = models.ForeignKey(FitnessForService, on_delete=models.CASCADE)

    def __str__(self):
        return f'Medical Examination for {self.conscript} on {self.examination_date}'

class MilitaryRank(models.Model):
    rank = models.CharField(max_length=50)

    def __str__(self):
        return self.rank

class MilitaryID(models.Model):
    conscript = models.OneToOneField(Conscript, on_delete=models.CASCADE)
    issued_date = models.DateField()
    official = models.ForeignKey(Official, on_delete=models.CASCADE)
    fitness_for_service = models.ForeignKey(FitnessForService, on_delete=models.CASCADE)
    characteristic = models.CharField(max_length=200)
    assigned_rank = models.ForeignKey(MilitaryRank, on_delete=models.CASCADE)

    def __str__(self):
        return f'Military ID for {self.conscript}'
