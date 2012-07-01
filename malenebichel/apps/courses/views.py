from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from django.template.context import Context, RequestContext
from django.template.loader import render_to_string
from django.utils.datastructures import MultiValueDictKeyError
from models import Course
from forms import CourseSignupForm
from django.conf import settings

def signup(request):

    """
        Saves signup for a course in database and notifies Malene through email.
    """

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

            send_mail('%s har tilmeldt sig %s' % (sup.first_name, sup.course.title) ,
                render_to_string('courses/signup_notice_email.txt',
                        {'sup': sup, }, RequestContext(request)),
                settings.DEFAULT_FROM_EMAIL,
                ['malenebi@gmail.com'])

            # confirmations are manual for now maybe change this.
            #confirmation_email_template = loader.get_template('courses/signup_confirmation_email.txt')
            #send_mail('Du har tilmeldt dig til ' % (sup.first_name, sup.course.title) , notice_email_template.render(context), settings.DEFAULT_FROM_EMAIL, ['malenebi@gmail.com'])


            return render(request, 'courses/course_signup_thanks.html', {'course': course})

    else:
        form = CourseSignupForm()

    return render(request, 'courses/course_signup.html', {'form': form, 'course': course})




    


def detail(request, slug):
    course = Course.objects.get(slug=slug)

    return render(request, 'courses/course_detail.html', {'course': course})
