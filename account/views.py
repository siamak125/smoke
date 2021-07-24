from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from abc import abstractmethod
from account.forms import profileRegisterForm
from account.models import profileModel


def loginView(request):
    if request.method == 'POST':
        # if request.user.is_authenticated:
        #     return HttpResponse("You are login.")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return HttpResponse("GEORGE")
        else:
            context = {
                "username": username,
                "error": "کاربری با این مشخصات پیدا نشدprofileRegister"
            }
            return render(request, "account/login.html", context)

    else:
        return render(request, "account/login.html", {})


def profileView(request):
    profile = request.user.profile

    context = {
        "profile": profile
    }

    return render(request, "account/profile.html", context)


def profileRegisterView(request):
    if request.method == "POST":
        profile_Register_form = profileRegisterForm(request.POST)
        if profile_Register_form.is_valid():
            user = User.objects.create_user(username=profile_Register_form.cleaned_data["username"],
                                            email=profile_Register_form.cleaned_data['email'],
                                            first_name=profile_Register_form.cleaned_data['first_name'],
                                            last_name=profile_Register_form.cleaned_data['last_name'])

            user.save()
            profile_model = profileModel(user=user,
                                         Gender=profileRegisterForm.changed_data['Gender'])
            profile_model.save()
    else:
        profile_Register_form = profileRegisterForm()
    context = {"formData": profile_Register_form}
    return render(request, "account/profileRegister.html", context)
