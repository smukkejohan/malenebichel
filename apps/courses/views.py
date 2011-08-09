from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from models import Course
from forms import CourseSignupForm

def signup(request):

    try:
        cid = request.GET['course']
    except MultiValueDictKeyError:

        courses = Course.signup_objects.all()
        return render(request, 'courses/course_signup_list.html', {'course_list': courses})

    try:
        course = Course.signup_objects.get(id=cid)
    except Course.DoesNotExist:
        raise Http404


    if request.method == 'POST':
        form = CourseSignupForm(request.POST)
        if form.is_valid():

            sup = form.save(commit=False)
            if request.user.is_authenticated():
                sup.user = request.user

            sup.course = course
            sup.save()

            return HttpResponse("thanks, you are now signed up")

    else:
        form = CourseSignupForm()

    return render(request, 'courses/course_signup.html', {'form': form, 'course': course})




    


def detail(request, slug):
    course = Course.objects.get(slug=slug)

    return render(request, 'courses/course_detail.html', {'course': course})
