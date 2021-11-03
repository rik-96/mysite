from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={"tutorials": Tutorial.objects.all})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request=request,
                          template_name="main/register.html",
                          context={"form": form})

    form = NewUserForm
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/form')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="main/login.html",
                  context={"form": form})


def form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            params = []
            params.append(form.cleaned_data.get('param1'))
            params.append(form.cleaned_data.get('param2'))
            params.append(form.cleaned_data.get('param3'))
            params.append(form.cleaned_data.get('param4'))
            params.append(form.cleaned_data.get('param5'))
            params.append(form.cleaned_data.get('param6'))
            params.append(form.cleaned_data.get('param7'))
            params.append(form.cleaned_data.get('param8'))
            params.append(form.cleaned_data.get('param9'))
            params.append(form.cleaned_data.get('param10'))
            params.append(form.cleaned_data.get('param11'))
            for index, param in enumerate(params):
                if not param:
                    params[index] = 0

            return render(request, 'graph.html', {'param1': params[0], 'param2': params[1], 'param3': params[2], 'param4': params[3], 'param5': params[4], 'param6': params[5], 'param7': params[6], 'param8': params[7], 'param9': params[8], 'param10': params[9], 'param11': params[10]})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'form.html', {'form': form})


def graph(request):
    return render(request=request,
                  template_name='main/graph.html',
                  context={"tutorials": Tutorial.objects.all})
