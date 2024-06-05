from django import forms
from .models import MilitaryCommissariat, Official, Conscript, PersonalData, FitnessForService, Summon, MedicalExamination, MilitaryRank, MilitaryID

class MilitaryCommissariatForm(forms.ModelForm):
    class Meta:
        model = MilitaryCommissariat
        fields = '__all__'

class OfficialForm(forms.ModelForm):
    class Meta:
        model = Official
        fields = '__all__'

class ConscriptForm(forms.ModelForm):
    class Meta:
        model = Conscript
        fields = '__all__'

class PersonalDataForm(forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = '__all__'

class FitnessForServiceForm(forms.ModelForm):
    class Meta:
        model = FitnessForService
        fields = '__all__'

class SummonForm(forms.ModelForm):
    class Meta:
        model = Summon
        fields = '__all__'

class MedicalExaminationForm(forms.ModelForm):
    class Meta:
        model = MedicalExamination
        fields = '__all__'

class PositionForm(forms.ModelForm):
    class Meta:
        model = MilitaryRank
        fields = '__all__'

class MilitaryIDForm(forms.ModelForm):
    class Meta:
        model = MilitaryID
        fields = '__all__'
