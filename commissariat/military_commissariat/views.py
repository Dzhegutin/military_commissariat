import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import MilitaryCommissariat, Official, Conscript, PersonalData, FitnessForService, Summon, MedicalExamination, MilitaryRank, MilitaryID
from .forms import MilitaryCommissariatForm, OfficialForm, ConscriptForm, PersonalDataForm, FitnessForServiceForm, SummonForm, MedicalExaminationForm, PositionForm, MilitaryIDForm

def index(request):
    return render(request, 'military_commissariat/index.html')

def list_view(model, template_name):
    def view(request):
        objects = model.objects.all()
        return render(request, template_name, {'objects': objects})
    return view


@csrf_exempt
def add_data_request(request):
    if request.method == 'POST':
        try:
            name = request.POST['field1']
            address = request.POST['field2']
            phone = request.POST['field3']

            # Валидация данных (можно добавить дополнительные проверки)
            if not name or not address or not phone:
                return JsonResponse({'status': 'error', 'message': 'Не все поля заполнены'}, status=400)

            new_record = MilitaryCommissariat.objects.create(name=name, address=address, phone=phone)
            return JsonResponse({'status': 'success', 'id': new_record.id})
        except KeyError:
            return JsonResponse({'status': 'error', 'message': 'Некорректный запрос'}, status=400)

def delete_records(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        record_ids = data.get('records', [])
        print(record_ids)
        MilitaryCommissariat.objects.filter(pk__in=record_ids).delete()
        return JsonResponse({'message': 'Records deleted successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'})


@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

        for item in data:
            pk = item['id']
            name = item['name']
            address = item['address']
            phone = item['phone']

            military_commissariat = MilitaryCommissariat.objects.get(pk=pk)
            military_commissariat.name = name
            military_commissariat.address = address
            military_commissariat.phone = phone
            military_commissariat.save()

        return JsonResponse({'message': 'Data saved successfully.'})
    else:

        return JsonResponse({'error': 'Invalid request method.'})

military_commissariat_list = list_view(MilitaryCommissariat, 'military_commissariat/military_commissariat_list.html')
official_list = list_view(Official, 'military_commissariat/official_list.html')
conscript_list = list_view(Conscript, 'military_commissariat/conscript_list.html')
personal_data_list = list_view(PersonalData, 'military_commissariat/personal_data_list.html')
fitness_for_service_list = list_view(FitnessForService, 'military_commissariat/fitness_for_service_list.html')
summon_list = list_view(Summon, 'military_commissariat/summon_list.html')
medical_examination_list = list_view(MedicalExamination, 'military_commissariat/medical_examination_list.html')
militaryrank_list = list_view(MilitaryRank, 'military_commissariat/militaryrank_list.html')
military_id_list = list_view(MilitaryID, 'military_commissariat/military_id_list.html')

