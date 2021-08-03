from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest, HttpResponse
from account.forms import profileRegisterForm, password_form
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
    context = {"formData": profile_Register_form}
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

            if not request.user.check_password(current_password_entered):
                return HttpResponse(content="Unauthorized", status=401)

            request.user.set_password(new_password2)
            request.user.save()
            return render(request, "account/login.html", {})

    else:
        form = password_form()
    context = {"form": form}
    return render(request, "account/password.html", context)


def passwordReset(request):
    return render(request, "account/emailpassword.html", {})
