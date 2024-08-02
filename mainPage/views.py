from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout as loggin_out
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NewsletterForm
from .models import MainPageSlider, ExperienceSection, Category, About

def home(request):
    sliders = MainPageSlider.objects.all()
    experiences = ExperienceSection.objects.all()
    categories = Category.objects.all()
    about = About.objects.all()
    return render(request, 'index.html', {'sliders': sliders, 'about' : about, 'experiences' : experiences,  'categories' : categories})

def about(request):
    return render(request, 'about.html')

def categoryBlade(request):
    return render(request, 'category-detail.html')

def categories(request):
    return render(request, 'category.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')


def registerRequest(request):
    if request.method == 'POST':
        username = request.POST["username"]
        firstName = request.POST["first_name"]
        lastName = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(username = username, email = email, first_name = firstName, last_name = lastName, password = password)
        user.save()
        return render(request, 'login.html')



def logout_view(request):
    loggin_out(request)
    return redirect('login')


def newletter(request):
    form = NewsletterForm(request.POST)
    if form.is_valid():
            form.save()
            return render(request, 'index.html')



class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category-detail.html'
    context_object_name = 'category'


