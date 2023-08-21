from django.shortcuts import render ,redirect
from .models import Services,NewsLetter
from courses.models import Course,Trainer
from courses.models import Category
from django.contrib.auth.models import User
from .forms import NewsletterForm
from django.contrib import messages



def home(request):
    if request.method == 'GET':
        
        print(request.GET)
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
    elif request.method == 'POST':
        new_email = NewsLetter()
        form = NewsletterForm(request.POST)
        if form.is_valid():
            new_email.email = request.POST.get('email')
            new_email.save()
            messages.add_message(request,messages.SUCCESS,'your email submited successfully')
            return redirect('root:home')
        else:
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:home')


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