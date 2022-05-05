from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from campingapp.auth.forms import SigninForm, SignupForm


def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            user = User.objects.get(username=username)
            raw_password = form.cleaned_data.get("password")

            if user.check_password(raw_password):
                login(request, user)
                return redirect("index")
            else:
                messages.add_message(request, messages.ERROR, "패스워드 틀림")
    else:
        form = SigninForm()

    context = {"form": form}
    return render(request, "auth/signin.html", context=context)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("index")
        else:
            # form 요청 유효하지 않음
            # error
            messages.error(request, "form이 유효하지 않음")
    else:
        # get 요청
        form = SignupForm()

    context = {"form": form}
    return render(request, "auth/signup.html", context)
