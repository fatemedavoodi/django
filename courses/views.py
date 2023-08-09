from django.shortcuts import render
from .models import Course
from .models import Category





def courses(request,cat=None,teacher=None):
    if cat:
        course = Course.objects.filter(category__name=cat)
    elif teacher:
        course = Course.objects.filter(teacher__info__username=teacher)
    else:
        course = Course.objects.filter(status=True)

    category = Category.objects.all()

    context = {
        'courses':course,
        'category':category
    }
    return render(request,'course/courses.html',context=context)
