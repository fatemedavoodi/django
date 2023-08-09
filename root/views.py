from django.shortcuts import render
from .models import Services
from courses.models import Course,Trainer
from courses.models import Category
from django.contrib.auth.models import User



def home(request):
    category = Category.objects.all()
    services = Services.objects.filter(status=True)
    last_three_course = Course.objects.filter(status=True)
    last_three_trainer = Trainer.objects.filter(status=True)
    service_count = Services.objects.filter(status=True).count()
    course_count = Course.objects.filter(status=True).count()
    trainer_count = Trainer.objects.filter(status=True).count()
    user_count = User.objects.filter(is_active=True).count()

    context={
        'service':services,
        'course':last_three_course,
        'trainer':last_three_trainer,
        'category':category,
        'sc':service_count,
        'cc':course_count,
        'tc':trainer_count,
        'uc':user_count,
    }
    return render(request,"root/index.html",context=context)


def about(request):
    category = Category.objects.all()
    context={
        'category':category
    }
    return render(request,"root/about.html",context=context)

def contact(request):
    category = Category.objects.all()
    context={
        'category':category
    }
    return render(request,"root/contact.html",context=context)

def trainer(request):
    category = Category.objects.all()
    context={
        'category':category
    }
    return render(request,"root/trainers.html",context=context)