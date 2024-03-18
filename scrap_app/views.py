from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,View,UpdateView,TemplateView,DetailView
from scrap_app.forms import Sign_up,Sign_inForm,UserProfileForm,ScrapForm,BidForm
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from scrap_app.models import UserProfile,Scrap,Wishlist,Category
from scrap_app.decotators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib import messages


dec=[login_required,never_cache]
# Create your views here.
    
class Sign_up(CreateView):
    template_name="signup.html"
    form_class=Sign_up
    
    def get_success_url(self) :
        return reverse("sign")

class Sign_in(FormView):
   template_name="signin.html"
   form_class=Sign_inForm

   def post(self, request,*args, **kwargs):
       form=Sign_inForm(request.POST)
       if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=uname,password=pwd)
            if user_obj:
                login(request,user_obj)
                print(request.user)
                return redirect("index")
       return render(request,"signin.html",{"form":form})    
@method_decorator(dec,name="dispatch")      
class SignOutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        print(request.user)
        return redirect("sign")        
@method_decorator(dec,name="dispatch")
class UserProfileView(UpdateView):
    template_name='profile_add.html'
    form_class=UserProfileForm
    model=UserProfile

    def get_success_url(self):
        return reverse("index")
@method_decorator(dec,name="dispatch")
class ProfileListView(View):

    def get(self,request,*args, **kwargs):
        qs=UserProfile.objects.all().exclude(user=request.user)
        return render(request,"profile_list.html",{'data':qs})
@method_decorator(dec,name="dispatch")    
class ProfileView(View):
    def get(self,request,*args, **kwargs) :
        id=kwargs.get("pk")
        qs=UserProfile.objects.get(id=id)
        return render(request,"profile.html",{"data":qs}) 
@method_decorator(dec,name="dispatch")      
class UserProductsView(View):
    def get(self,request,*args, **kwargs):

        qs=Scrap.objects.filter(user=request.user)
        return render(request,"userscrap.html",{"data":qs})
            
@method_decorator(dec,name="dispatch")    
class ScrapAddView(CreateView):
    template_name="scrapadd.html"
    form_class=ScrapForm
    model=Scrap  



    def form_valid(self,form):
        form.instance.user=self.request.user 
        return super().form_valid(form)
    def get_success_url(self):
        return reverse("scrap_list")
    
@method_decorator(dec,name="dispatch")
class ScrapListView(View):
    def get(self,request,*args, **kwargs):
        data=Scrap.objects.all()
        qs=Wishlist.objects.filter(user=request.user)
        cat=Category.objects.all()
        return render(request,"scraplist.html",{"data":data,"qs":qs,"cate":cat}) 
@method_decorator(dec,name="dispatch")
class ScrapUpdateView(UpdateView):
    template_name="scrapupdate.html"
    form_class=ScrapForm
    model=Scrap


    def get_success_url(self) :
        return reverse("userscrap")
    
@method_decorator(dec,name="dispatch")
class ScrapDetailView(DetailView):
    template_name="scrapdetail.html"
    model=Scrap
    context_object_name='data'

@method_decorator(dec,name="dispatch")   
class  WishListView(View):
    def post(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        scrap_obj=Scrap.objects.get(id=id)
        action=request.POST.get("action")
        wishlist,created=Wishlist.objects.get_or_create(user=request.user)
        
        if action == "addwish":
            wishlist.scrap.add(scrap_obj)
        elif action == "remove":
            wishlist.scrap.remove(scrap_obj)
        return redirect("scrap_list")      
@method_decorator(dec,name="dispatch")
class IndexView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"index.html")  
    
@method_decorator(dec,name="dispatch")
class BidAddView(View):
    def Post(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Scrap.objects.get(id=id)
        form=BidForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.instance.scrap=qs 
            form.save()
            return render(request,"scrapdetails.html",{"data":qs,"form":form})   
        else:
            return render(request,"scrapdetails.html",{"data":qs,"form":form}) 

class WishView(View):
      def get(self,request,*args, **kwargs):

        qs=Wishlist.objects.filter(user=request.user)

        return render(request,"wishlist.html",{"data":qs,})
      

class ScrapdeleteView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        Scrap.objects.get(id=id).delete()
        return redirect('userscrap')  
    
    
class CatScrapview(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Scrap.objects.filter(category=id)

        return render(request,"categoryscrap.html",{"data":qs})    
    


  







      
            




