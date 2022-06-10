from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('strescan/<uid>', views.scan),
    path('adminhome/', views.adhome),
    path('addstaff/', views.addstaff),
    path('mstaff/', views.mstaff),
    path('report/<uid>', views.report),
    
    path('stanalyse', views.stanalyse),
    
    path('delstf', views.delstf),
    path('pic', views.pic),
    path('picanalyse', views.picanalyse),
    path('logout', views.home),
]
