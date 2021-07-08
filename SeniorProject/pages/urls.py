from django.urls import path,re_path
from django.urls.resolvers import URLPattern
from pages.views import index,SignUpPageView,pages

urlpatterns=[
    #home page
    path('',index,name='home'),
    
    path('signup/', SignUpPageView.as_view(), name='register'),
    re_path(r'^.*\.*', pages, name='pages'),
    #matches any html file
    
]