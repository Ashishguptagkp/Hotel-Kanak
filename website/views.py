from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html");
   
   
   
   
def about(request):
    return render(request, 'about.html');   

def rooms(request):
    return render(request, 'rooms.html');   

def gallery(request):
    return render(request, 'gallery.html');   

def contact(request):
    return render(request, 'contact.html');   