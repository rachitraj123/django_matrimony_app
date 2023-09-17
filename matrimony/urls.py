from django.urls import path,reverse
from .views import *



app_name = "Matrimony"


urlpatterns = [
    path('',profilelistview, name="index"),
    path('<int:profile_id>', profileviewdetail, name= "profile_detail"),
    path('<int:profile_id>/delete', profile_delete, name = "profile_delete"),
    path('contact',contactview,name='contact'),
    path('new_profile',newprofile,name='new_profile')
]