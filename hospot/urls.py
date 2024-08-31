from django.urls import path
from . import views

app_name='hospot'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('main/', views.main, name='main'), ##부위 고르게 하기
    path('hospital/', views.index, name='index'),
    path('hospital/<int:department_id>/page=<int:page_num>', views.department, name='department'),
    path('hospital/<int:department_id>/<int:hospital_size>/', views.size, name='size'),
    path('hospital/<int:hospital_size>/<int:department_id>/<int:code_id>/', views.profile, name='profile'),
]
