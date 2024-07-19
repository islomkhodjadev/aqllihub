from .models import Savollar, Category, Javoblar
from django import forms
from django.contrib.auth import get_user_model 



class AddSavol(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label= "Turkum", empty_label=None,
                                      widget=forms.Select(attrs={"class": "form-control"}))
    
    class Meta:
        model = Savollar

        fields = ("question", "category")
        labels = {
            "question":"Savol",
    
        }
        widgets = {
            "question" : forms.TextInput(attrs={"class": "form-control", "placeholder":"Savolni kiriting"},)
        }
        
        
        
class AddJavob(forms.ModelForm):
    
    
    class Meta:
        model = Javoblar

        fields = ("javob", )
        
        widgets = {
            "javob": forms.TextInput(attrs={"class":"form-control", "placeholder": "Javobingizni kiriting"})
        }
        labels = {
            "javob": "Javob"
        }

        
        
        
        
class RegisterUSer(forms.ModelForm):
    
    class Meta:
        model = get_user_model()

        fields = ("username", "email", "password", "image", "info")
        
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
             "email": forms.TextInput(attrs={"class": "form-control", "type": "email"}),
              "password": forms.TextInput(attrs={"class": "form-control", "type": "password"}),
            
              "info": forms.Textarea(attrs={"class": "form-control", "type": "text"}),
        }
        
        labels = {
            "username": "Unikal ism",
            "email": "Pochta",
            "password": "Parol",
            "image":"rasm",
            "info": "Malumot"
        }
        
    
    
     
class EditUser(forms.ModelForm):
    
    class Meta:
        model = get_user_model()

        fields = ("username", "email", "image", "info")
        
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
             "email": forms.TextInput(attrs={"class": "form-control", "type": "email"}),
              
            
              "info": forms.Textarea(attrs={"class": "form-control", "type": "text"}),
        }
        
        labels = {
            "username": "Unikal ism",
            "email": "Pochta",
            "image":"rasm",
            "info": "Malumot"
        }
        
       
class LoginUser(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "type": "text"}), label="Unikal ism", max_length=150)
    password = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "type": "password"}), label="Parol", max_length=200)

