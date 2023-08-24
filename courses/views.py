from django.shortcuts import render,get_object_or_404,redirect
from .models import Course
from .models import Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from root.models import NewsLetter
from root.forms import NewsletterForm
from django.contrib import messages





def courses(request,cat=None,teacher=None):
    if request.method == 'GET':
        category = Category.objects.all()

        if cat:
            course = Course.objects.filter(category__name=cat)

        elif teacher:
            course = Course.objects.filter(teacher__info__username=teacher)

        elif request.GET.get('search'):
            course = Course.objects.filter(content__contains=request.GET.get('search'))

        else:
            course = Course.objects.filter(status=True)


        course = Paginator(course,2)
        first_page = 1
        last_page = course.num_pages

        try:
            page_number = request.GET.get('page')
            course = course.get_page(page_number)

        except EmptyPage:
            course = course.get_page(1)

        except PageNotAnInteger:
            course = Course.get_page(1)

        context = {
            'courses':course,
            'category':category,
            'firs_page':first_page,
            'last_page':last_page,
        }
    
        return render(request,'course/courses.html',context=context)
    
    elif request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submited successfully')
            return redirect('courses:courses')
        else:
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('courses:courses')


def course_detail(request,id):
    if request.method == 'GET':
        try:
            course = Course.objects.get(id=id)
            id_list = []
            courses = Course.objects.filter(status=True)
            for cr in courses:
                id_list.append(cr.id)
                
            id_list.reverse()

            if id_list[0] == id:
                next_course = Course.objects.get(id=id_list[1])
                previous_course = None

            elif id_list[-1] == id:
                next_course = None
                previous_course = Course.objects.get(id=id_list[-2])

            else:
                next_course = Course.objects.get(id=id_list[id_list.index(id)+1])
                previous_course = Course.objects.get(id=id_list[id_list.index(id)-1])

            course.counted_views += 1
            course.save()
            context={
                'course':course,
                'next_course':next_course,
                'previous_course':previous_course,
            }
            return render(request,'course/course-details.html',context=context)
        
        except:
            return render(request,'course/404.html')
    # elif request.method == 'POST':
    #     form = NewsletterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.add_message(request,messages.SUCCESS,'your email submited successfully')
    #         return redirect('courses:course_detail')
    #     else:
    #         messages.add_message(request,messages.ERROR,'Invalid email address')
    #         return redirect('courses:course_detail')
            