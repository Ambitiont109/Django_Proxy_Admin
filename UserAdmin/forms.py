from django.forms import ModelForm
from .models import User


class UserAddForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
