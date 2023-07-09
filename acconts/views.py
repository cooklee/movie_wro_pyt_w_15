from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from acconts.forms import AddUserForm, LoginForm


class UserListView(View):

    def get(self, request):
        users = User.objects.all()
        return render(request, 'user_list.html', {'users':users})


class AddUserView(View):

    def get(self, request):
        form = AddUserForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('user_list')
        return render(request, 'form.html', {'form': form})


class LoginUserView(View):


    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form':form})


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username =form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            url = request.GET.get('next', 'index_template')
            if user is not  None:
                login(request, user)
            return redirect(url)
        return render(request, 'form.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('index_template')

