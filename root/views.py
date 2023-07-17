from django.shortcuts import render
from .models import Services


app_name = 'root'
def home(request):
    services = Services.objects.all()
    context={
        'service':Services
    }
    return render(request,"root/index.html",context=context)


def about(request):
    return render(request,"root/about.html")

def contact(request):
    return render(request,"root/contact.html")