from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from scrap_app.models import UserProfile,Scrap,Bids,Review


class Sign_up(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

        widgets={
         "username":forms.TextInput(attrs={"class":"form-control"}),
        
         "email":forms.TextInput(attrs={"class":"form-control"}),
         "password1":forms.TextInput(attrs={"class":"form-control"}),
         "password2":forms.TextInput(attrs={"class":"form-control"}),
         
        }

class Sign_inForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=('user',)

   

class ScrapForm(forms.ModelForm):
    class Meta:
        model=Scrap
        exclude=('user','status',)

        widgets={
         "name":forms.TextInput(attrs={"class":"form-control"}),
         "category":forms.Select(attrs={"class":"form-control"}),
         "price":forms.TextInput(attrs={"class":"form-control"}),
         "description":forms.TextInput(attrs={"class":"form-control"}),
         "location":forms.TextInput(attrs={"class":"form-control"}),
         "scrap_image":forms.FileInput(attrs={"class":"form-control"}),
         "condition":forms.TextInput(attrs={"class":"form-control"})
        }

class BidForm(forms.ModelForm):
    class Meta:
        models=Bids
        fields=["amount"]    

class ReviewForm(forms.ModelForm):
    class Meta:
        models=Review
        fields=["comment","rating"]


        




