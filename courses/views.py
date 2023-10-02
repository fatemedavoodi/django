from django.shortcuts import render , get_object_or_404, redirect
from .models import Course, Comment, Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import CommentForm
from django.contrib import messages
from root.models import NewsLetter
from root.forms import NewsletterForm

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
            course = course.get_page(1) 


        context ={"courses": course,
                  'first_page': first_page,
                  'last_page': last_page,
                  'category' : category,
        }
        return render(request,'course/courses.html',context=context)
    
    elif request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect('courses:courses')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('courses:courses')


def course_detail(request, id):
    if request.method == 'GET':
        category = Category.objects.all()
        try:
            course = Course.objects.get(id=id)
            comments = Comment.objects.filter(which_course=id, status=True)
            id_list = []
            courses = Course.objects.filter(status=True)
            for cr in courses:
                id_list.append(cr.id)   

            id_list.reverse()

            if id_list[0] == id :
                next_course = Course.objects.get(id = id_list[1])
                previous_course = None  

            elif id_list[-1] == id :
                next_course = None
                previous_course = Course.objects.get(id = id_list[-2])  

            else:
                next_course = Course.objects.get(id=id_list[id_list.index(id)+1])
                previous_course = Course.objects.get(id=id_list[id_list.index(id)-1])   


            course.counted_views += 1
            course.save()
            context ={"course": course,
                      'next_course': next_course,
                      'previous_course': previous_course,
                      'comments': comments,
                      'category' : category,
            }
            return render(request,'course/course-details.html',context=context)
        except:
            return render(request,'course/404.html')
        
    elif request.method == 'POST' and len(request.POST) > 2:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited and publish as soon')
            return redirect (request.path_info)

        else:
            messages.add_message(request,messages.ERROR,'your comment data is not valid')
            return redirect (request.path_info)
        
    elif request.method == 'POST' and len(request.POST) == 2:
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect(request.path_info)   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect(request.path_info)
        


def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    cid = comment.which_course.id
    comment.delete()
    return redirect (f'/courses/course-detail/{cid}')