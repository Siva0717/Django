
from django.urls import path
from  . import views
from .views import getSiva, delete, post, patch, put, api1, api2,api3,api4,api5,api7,api6,api8




urlpatterns=[

    path('room/<str:pk>', views.room),
    path('home/', views.home),
    path('main/', views.main),
    
    path('create/', views.create),
    
    path('dep/', views.dep),
    path('final/',views.final),
  
    path('Sk/', views.shop),
    path('final', views.final),
    path('office/', views.office),
    path('post/', post),
    
    path('GET/', getSiva),
    path('delete/<int:id>/', delete),
    path('patch/<int:id>/', patch),
     path('put/<int:id>/', put),
     path('api1/', api1),
    path('api2/<int:id>/', api2),
    path('api3/<str:name>/', api3),
    path('api4/', api4),
     path('api5/<int:id>/', api5),
     path('siva/<int:id>/',api7),
     path('siva2/', api6),
     path('siva3/<int:id>/', api8),
]

