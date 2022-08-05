from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='meetup'),
    path('<slug:meetup_slug>/success', views.confirm_reg, name='confrim_reg'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-details'),
    
]