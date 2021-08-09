import uuid
import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from account.models import passwordResetModel
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from account.forms import profileRegisterForm, password_form, passwordResetForm, confirmForm
from account.models import profileModel


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return HttpResponseRedirect("/home")
        else:
            profile_Register_form = profileRegisterForm()
            context = {
                "source": "login",
                "username": username,
                "error": "کاربری با این مشخصات پیدا نشد",
                "formData": profile_Register_form
            }
            return render(request, "account/login.html", context)

    else:
        profile_Register_form = profileRegisterForm()
        context = {"formData": profile_Register_form}
        return render(request, "account/login.html", context)


@login_required()
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
                                            password=profile_Register_form.cleaned_data['password'],
                                            first_name=profile_Register_form.cleaned_data['first_name'],
                                            last_name=profile_Register_form.cleaned_data['last_name'],
                                            is_staff=True)

            user.save()
            profile_model = profileModel(user=user,
                                         Gender=profile_Register_form.cleaned_data['Gender'])
            profile_model.save()
    else:

        profile_Register_form = profileRegisterForm()
    context = {"form": profile_Register_form}
    return render(request, "account/profileRegister.html", context)


@login_required()
def logoutView(request):
    logout(request)
    return HttpResponseRedirect("/login")


@login_required()
def aboutView(request):
    return render(request, "account/about.html", {})


def homeView(request):
    return render(request, "account/home.html", {})


class hello(PasswordChangeView):
    form_class = PasswordChangeView
    success_url = reverse_lazy('home')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = password_form(request.POST)
        if form.is_valid():
            current_password_entered = form.cleaned_data['old_password']

            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']
            if new_password1 != new_password2:
                return HttpResponseBadRequest(content="The password reacted not equal!")

            if not request.cleaned_datapasswordResetFormuser.check_password(current_password_entered):
                return HttpResponse(content="Unauthorized", status=401)

            request.user.set_password(new_password2)
            request.user.save()
            return render(request, "account/login.html", {})

    else:
        form = password_form()
    context = {"form": form}
    return render(request, "account/password.html", context)


def passwordReset(request):
    if request.method == 'POST':
        form = passwordResetForm(request.POST)
        if form.is_valid():
            uid = uuid.uuid4()
            email = form.cleaned_data['email']

            link = F'http://localhost:8000/password-reset/{uid}'
            loo = passwordResetModel(email=form.cleaned_data['email'], uid=uid)
            loo.save()
            poker = User.objects.get(email=email)
            username = poker.username
            subject = 'reset password'
            message = F'for reset password please click in link{link}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [F'{email}', ]
            send_mail(subject, message, email_from, recipient_list)
            form = passwordResetForm()
            context = {'form': form}
            return render(request, "account/password_reset_done.html", context)
        else:
            form = passwordResetForm()
        context = {'form': form}
        return render(request, "account/emailpassword.html", context)

    else:
        form = passwordResetForm()
    context = {'form': form}
    return render(request, "account/emailpassword.html", context)


def passwordReset2(req, rock):
    form = confirmForm()
    context = {'form': form}
    return render(req, "account/resetpass.html", context)


def passwordReset4(req, havij):
    return HttpResponse("str")


def passwordReset5(req, havij):
    return HttpResponse("path")

# re.compile(r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}').findall()
