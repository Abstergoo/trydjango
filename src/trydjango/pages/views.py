from django.http import  request, response
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})   #String of HTML Code

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html",{})  #String of HTML Code

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "This is about me",
        "my_number" : 123,
        "my_list" : [12, 25, "abc",  87, 68,]
    }
    return render(request, "about.html", my_context)   #String of HTML Code

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})   #String of HTML Code