from user.models import House
from user.models import Room
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ('location', 'city', 'state', 'area', 'floor', 'cost', 
                 'hall', 'kitchen', 'balcany', 'bedrooms', 'AC', 'desc', 'img')
        
        widgets = {
            'location': forms.TextInput(attrs={'placeholder': 'Amalbagh'}),
            'city': forms.TextInput(attrs={'placeholder': 'Lucknow'}),
            'state': forms.TextInput(attrs={'placeholder': 'Uttar pradesh'}),
            'area': forms.NumberInput(attrs={'style': 'width: 100%; height: 50px; margin-bottom: 10px;'}),
            'floor': forms.NumberInput(attrs={'style': 'width: 100%; height: 50px; margin-bottom: 10px;'}),
            'cost': forms.NumberInput(attrs={'style': 'width: 100%; height: 50px; margin-bottom: 10px;'}),
            'hall': forms.TextInput(attrs={'placeholder': 'Yes/No'}),
            'kitchen': forms.NumberInput(attrs={'placeholder': '1'}),
            'balcany': forms.TextInput(attrs={'placeholder': 'Yes/No'}),
            'bedrooms': forms.NumberInput(attrs={'style': 'width: 100%; height: 50px; margin-bottom: 10px;'}),
            'AC': forms.TextInput(attrs={'placeholder': 'Yes/No'}),
            'desc': forms.Textarea(attrs={'style': 'width: 100%'}),
            'img': forms.FileInput(attrs={'onchange': 'PreviewImage()'})
        }


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('location', 'city', 'state', 'dimention', 'cost', 
                 'hall', 'kitchen', 'balcany', 'bedrooms', 'AC', 'desc', 'img')
        
        widgets = {
            'location': forms.TextInput(attrs={'placeholder': 'Amalbagh'}),
            'city': forms.TextInput(attrs={'placeholder': 'Lucknow'}),
            'state': forms.TextInput(attrs={'placeholder': 'Uttar pradesh'}),
            'dimention': forms.TextInput(attrs={'placeholder': 'ex - 10 x 12 ft'}),
            'cost': forms.NumberInput(attrs={'style': 'width: 100%; height: 50px; margin-bottom: 10px;'}),
            'hall': forms.TextInput(attrs={'placeholder': 'Yes/No'}),
            'kitchen': forms.TextInput(attrs={'placeholder': 'Yes/No'}),
            'balcany': forms.TextInput(attrs={'placeholder': 'Yes/No'}),
            'bedrooms': forms.NumberInput(attrs={'style': 'width: 100%; height: 50px; margin-bottom: 10px;'}),
            'AC': forms.TextInput(attrs={'placeholder': 'Yes/No'}),
            'desc': forms.Textarea(attrs={'style': 'width: 100%'}),
            'img': forms.FileInput(attrs={'onchange': 'PreviewImage()'})
        }