from django.shortcuts import render,redirect
from .models import *
from .forms import * 
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required
# Create your views here.
def profilelistview(request):
    profiles =  Profile.objects.all()
    user = request.user
    return render(request, 'matrimony/index.html', 
    {
        'profiles':profiles,
        'user': user
    })
@login_required 
def profileviewdetail(request,profile_id):
    profile = Profile.objects.get(id=profile_id)
    user = request.user 
    return render(request, 'matrimony/profile_detail.html', {
        'profile': profile, 'user':user
    })
    

def profile_delete(request,profile_id):
    profile = Profile.objects.get(id = profile_id)
    user = request.user
    if user.email == profile.email:
        profile.delete()
    return redirect('Matrimony:index')
    

@login_required   
def contactview(request):
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"message: {form.cleaned_data['message']}")
        else:
            print("Wrong format...")    
    else:
        form = contactform()
    user = request.user    
    return render(request,'matrimony/form.html',{
        'form': form,
        'user': user
    })


@login_required
def newprofile(request):
    
    profile_formset = formset_factory(new_profile_form,extra = 1)
    if request.method == "POST":
        formset = profile_formset(request.POST, request.FILES)
        
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form.save()
            
            return redirect('Matrimony:index')
    else:
        formset = profile_formset()
    return render(request,'matrimony/new_profile.html',{
        'formset': formset
    })