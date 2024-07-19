from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Savollar, Javoblar
from django.core.exceptions import ValidationError
from .forms import AddSavol, AddJavob, RegisterUSer, LoginUser, EditUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.db.models import Count

def index(request, exception=None):
    
    if exception is not None:
        # print(exception)
        return redirect("index")
    
    context = {
        "savollar": Savollar.objects.annotate(count_answers=Count("javob")).order_by("-count_answers").filter(count_answers__gt=0)[:10]
    }
    
    
    
    return render(request, "aqlihub/index.html", context=context)


def category(request):
    
    context = {
        "categories": Category.objects.all()
    }
    
    return render(request, "aqlihub/category.html", context=context)


def Login(request):
    
    
    form = LoginUser()
    message = ""
    if request.method == "POST":
        form = LoginUser(request.POST)

        if form.is_valid():
            
            data = form.cleaned_data
            # print(data)
            user = authenticate(username=data["username"], password=data["password"])
            if user:
                login(request, user)
            
                return redirect("profile")
            message = "Login noto'g'ri"
    
    context = {
        "message": message,
        "form": form
    }
    
    return render(request, "aqlihub/login.html", context=context)


def signup(request):
    form = RegisterUSer()
    
    
    if request.method == "POST":
        password = request.POST.get("password")
        print(request.FILES)
        form = RegisterUSer(request.POST, request.FILES)
        
        if form.is_valid():
            user = form.save(commit=False)
            
            user.set_password(password)
            
            user.save()
            
            return redirect("login")
            
            
    context = {
        "form": form
    }
    
    return render(request, "aqlihub/signup.html", context=context)

def profile(request, username=None):
    
    
    
    if username is not None and get_user_model().objects.filter(username=username).exists():
        user = get_user_model().objects.get(username=username)
    elif request.user.is_authenticated:
        user = request.user
    else: 
        user = None

    context = {
        "user": user
    }
    return render(request, "aqlihub/profile.html", context=context)

    



def savol(request, id):
    context = {
        "savol": Savollar.objects.get(pk=id),
       
    }
    
    
    return render(request, "aqlihub/savol.html", context=context)



def savollar(request, id=None, username=None):
     
    context = {
        "savollar": Savollar.objects.all()
    }
    
    if id is not None and username is not None:
        context = {
          "savollar": Category.objects.get(user=get_user_model().objects.get(username=username)).savollar.all()
        }
    elif username is not None and get_user_model().objects.filter(username=username).exists() and request.user == get_user_model().objects.get(username=username):
        context = {
          "savollar": get_user_model().objects.get(username=username).savollar.all()
        }
        
    return render(request, "aqlihub/savollar.html", context=context)
    
def add_savol(request):
    
    if not request.user.is_authenticated:
        return redirect("login")
    
    form = AddSavol()
    
    
    if request.method == "POST":
        form = AddSavol(request.POST)
        
        if form.is_valid():
            yangi_savol = form.save(commit=False)
            yangi_savol.user = request.user
            yangi_savol.save()
            
            return redirect("savol", id=yangi_savol.pk)
    
    
    data = {
        "form":form
    }
    
    return render(request, "aqlihub/add_savol_javob.html",context=data)



def add_javob(request, id=id):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if Savollar.objects.filter(id=id).exists():
            savol = Savollar.objects.get(id=id)
    else:    
            return redirect("savollar")
    
    form = AddJavob()
    
    if request.method == "POST":

            
            form = AddJavob(request.POST)
            if form.is_valid():
                javob = form.save(commit=False)
                javob.savol = savol
                javob.user = request.user
                javob.save()
                
                return redirect("savol", id=savol.id)
            
        
    
    data ={"form":form, 
           "savol":savol
           }
    
    return render(request, "aqlihub/add_savol_javob.html", context=data)




def qidirish(request):
    
    savol = request.GET.get("savol")
    
    savollar = Savollar.objects.filter(question__contains=savol)
    
    context = {
        "savollar":savollar
    }
    
    return render(request, "aqlihub/savollar.html", context=context)



def Logout(request):
    logout(request)
    
    return redirect("login")
    

def check(request, savol_id, javob_id):
    
    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.user.savollar.filter(pk=savol_id).exists() and \
    request.user.savollar.get(pk=savol_id).javob.filter(pk=javob_id):
        javob = request.user.savollar.get(pk=savol_id).javob.get(pk=javob_id)
        
        if javob.togri:
            javob.togri = False
        else:
            javob.togri = True

        javob.save()
        
    
    return redirect("savol", savol_id)


def edit_profile(request, username=None):
    if not (username is not None and get_user_model().objects.filter(username=username).exists() and request.user == get_user_model().objects.get(username=username)):
        return redirect("profile")
    
    form = EditUser(instance=request.user)
    
    
    if request.method == "POST":
        password = request.POST.get("password")
        print(request.FILES)
        form = EditUser(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            user = form.save()
            
            
            
            
            return redirect("profile")
            
            
    context = {
        "form": form
    }
    
    return render(request, "aqlihub/signup.html", context=context)



def delete_javob(request,savol_id, javob_id):
    
    if not ((Javoblar.objects.filter(pk=javob_id).exists() and request.user == Javoblar.objects.get(pk=javob_id).user) or \
        (Savollar.objects.filter(pk=savol_id).exists() and Savollar.objects.get(pk=savol_id).user == request.user)):
        return redirect("index")
    
    object = Javoblar.objects.get(pk=javob_id)
    object.delete()
    return redirect("savol", savol_id)



def delete_savol(request,savol_id):
    if not (Savollar.objects.filter(pk=savol_id).exists() and request.user == Savollar.objects.get(pk=savol_id).user):
        return redirect("index")
    
    object = Savollar.objects.get(pk=savol_id)
    category_id = object.category.pk
    object.delete()
    return redirect("savollar", category_id)