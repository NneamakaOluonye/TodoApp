from django import forms
from .models import hiitTodo
from django.contrib.auth.forms import UserCreationForm

# class TodoForm(forms.Form):
#     Firstname = forms.CharField(max_length = 50)
#     Lastname = forms.CharField(max_length = 50)
#     Email = forms.EmailField()
#     Username = forms.CharField(max_length = 20)
# class Meta:
#     fields = ('Firstname', 'Lastname','Email','Username')

class TodoForm(forms.ModelForm):
    class Meta:
        model = hiitTodo
        fields = '__all__'
        fields = ['title']

# class LoginForm(forms.Form):
#     Username = forms.CharField(max_length = 50)
#     Password = forms.CharField(max_length= 100)

