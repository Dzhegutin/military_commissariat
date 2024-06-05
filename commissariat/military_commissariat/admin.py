from django.contrib import admin
from .models import MilitaryCommissariat, Official, Conscript, PersonalData, FitnessForService, Summon, MedicalExamination, MilitaryRank, MilitaryID

admin.site.register(MilitaryCommissariat)
admin.site.register(Official)
admin.site.register(Conscript)
admin.site.register(PersonalData)
admin.site.register(FitnessForService)
admin.site.register(Summon)
admin.site.register(MedicalExamination)
admin.site.register(MilitaryRank)
admin.site.register(MilitaryID)
