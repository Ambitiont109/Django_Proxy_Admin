from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserAddForm, UserUpdateForm
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'UserAdmin/index.html')


def list_user(request):
    users = User.objects.exclude(is_superuser=True)
    return render(request, 'UserAdmin/list_user.html', {'users': users})


def add_user(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User Added Successfully')
            return redirect('UserAdmin:list_user')
        print(form.errors)
        return render(request, 'UserAdmin/add_user.html', {'form': form})
    if request.method == 'GET':
        form = UserAddForm()
        print(form.errors)
        return render(request, 'UserAdmin/add_user.html', {'form': form})


def detail_user(request, pk):
    user = get_object_or_404(User.objects.exclude(is_superuser=True), pk=pk)
    form = UserUpdateForm(instance=user)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        print("==========")
        print(form)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User updated Successfully')
            return redirect('UserAdmin:list_user')
    print(form)
    return render(request, 'UserAdmin/detail_user.html', {'form': form})


def delete_user(request, pk):
    if request.method == 'POST':
        user = get_object_or_404(User.objects.exclude(is_superuser=True), pk=pk)
        user.delete()
        messages.add_message(request, messages.SUCCESS, 'User Deleted Successfully')
        return redirect('UserAdmin:list_user')


def set_password(request, pk):
    if(request.method == 'POST'):
        password = request.POST['password']
        user = get_object_or_404(User.objects.exclude(is_superuser=True), pk=pk)
        user.password = password
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Change Password Successfully')
        return redirect('UserAdmin:detail_user', pk=pk)

