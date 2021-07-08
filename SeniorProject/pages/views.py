from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django import template
# from django.views.generic import TemplateView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import loader
from .forms import CustomUserCreationForm

# Create your views here.

# HomePage View 
# class HomePageView(generic.TemplateView):
#     template_name='pages/home.html'
@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))



#SignUp Page View 

class SignUpPageView(generic.CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name='accounts/register.html'





