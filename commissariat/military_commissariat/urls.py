from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_data_request/', views.add_data_request, name='add_data_request'),
    path('delete_records/', views.delete_records, name='delete_records'),
    path('save_data/', views.save_data, name='save_data'),

    path('military_commissariat/', views.military_commissariat_list, name='military_commissariat_list'),

    path('official/', views.official_list, name='official_list'),

    path('conscript/', views.conscript_list, name='conscript_list'),

    path('personal_data/', views.personal_data_list, name='personal_data_list'),

    path('fitness_for_service/', views.fitness_for_service_list, name='fitness_for_service_list'),

    path('summon/', views.summon_list, name='summon_list'),

    path('medical_examination/', views.medical_examination_list, name='medical_examination_list'),

    path('militaryrank/', views.militaryrank_list, name='militaryrank'),

    path('military_id/', views.military_id_list, name='military_id_list'),


]