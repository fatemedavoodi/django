from django.shortcuts import render
from .models import Course


def courses(request):
    course = Course.objects.all()
    context = {
        'courses':course
    }
    return render(request,'course/courses.html',context=context)
