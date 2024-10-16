from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_panel_information, name='create_panel_information'),
    path('data/<str:panel_id>/', views.get_panel_information, name='get_panel_information'),
    path('data/', views.get_all_panel_data, name='get_all_panel_data'),
    path('upload/', views.upload_excel, name='upload_excel'),
]