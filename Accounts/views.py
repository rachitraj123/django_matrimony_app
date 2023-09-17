from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.http import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import uuid
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from .models import CustomUser
from smtplib import SMTPDataError

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # user.is_email_verified = False
            # user.email_verification_token = str(uuid.uuid4())
            # user.save()
            # current_site = get_current_site(request)
            # print(f"{current_site}")
            # subject = 'Activate your account'
            # activation_link = f"http://{current_site}/accounts/verify_email/{user.email_verification_token}/"
            # message = f'Click the link to activate your account: {activation_link}'
            
            # try:
            #     send_mail(subject, message, 'matrimonyapp@gmail.com', [user.email,])
            #     return redirect('Accounts:login')
            # except SMTPDataError as e:
            #     # Handle the SMTPDataError here and provide user feedback
            #     error_message = f"SMTPDataError: {e}"
            #     return HttpResponse(error_message)
    else:
        form = RegistrationForm()
    return render(request, 'Accounts/register.html', {
        'form': form
    })
# def verify_email_view(request, token):
#     try:
#         user = CustomUser.objects.get(email_verification_token = token)
#         if user:
#             user.is_email_verified = True
#             user.email_verification_token = None
#             user.save()
#             return redirect('Accounts:login')
#     except:
#         return HttpResponse("<h1>Activation link is invalid.....</h1>")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Matrimony:index')
    else:
        form = AuthenticationForm()
    return render(request, 'Accounts/login.html', {
        'form': form
    })

@login_required
def logout_view(request):
    logout(request)
    if request.method == "POST":
        return JsonResponse({'success':True})
    return redirect('Accounts:login')

@login_required
def delete_account(request):
    request.user.delete()
    messages.success(request, "Your Account has been deleted")
    return redirect('Accounts:login')
