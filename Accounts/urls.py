from django.urls import path
from .views import *

app_name = 'Accounts'
urlpatterns = [
    path('register/',register,name="register"),
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name ='logout'),
    path('delete/',delete_account,name ='delete'),
    # path('verify_email/<str:token>/',verify_email_view,name ='verify_email'),
]