from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse ,HttpResponseRedirect
from .models import signup
from django.contrib import messages
from django.core import mail
from django.http import JsonResponse
from django.core.mail import send_mail,EmailMultiAlternatives

from random import randint,randrange

def validate(request):
    email = request.GET.get('email')
    data = {
        'is_taken': signup.objects.filter(email=email).exists()
    }
    return JsonResponse(data)


def base(request):


    try:

        email = request.session['email']
        flag = signup.objects.filter(email=email).exists()
        if flag:
            data = signup.objects.all()
            context = {
                'data': data,
                'title': 'All the data',
            }
            return render(request,'html/base.html',context)
        else:
            return HttpResponseRedirect('/login')

    except:
        return HttpResponseRedirect('/logout')

def details(request , id=None):

    try:
        email = request.session['email']
        flag = signup.objects.filter(email=email).exists()
        if flag:
            instance = get_object_or_404(signup, id=id)
            context = {
                'title': instance.id,
                'instance': instance,
            }
            return render(request,'html/details.html',context)
        else:
            return HttpResponseRedirect('/login')

    except:
        return HttpResponseRedirect('/login')

def sign(request):

    try:
        email = request.session['email']
        flag = signup.objects.filter(email=email).exists()

        if flag:
            return HttpResponseRedirect('/base')
    except:
        if request.method == 'POST':
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            date_of_birth = request.POST.get('date_of_birth')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            password = request.POST.get('create_password')
            x = randrange(100000, 1000000)

            signup.objects.create(first_name=firstname, last_name=lastname, date_of_birth=date_of_birth, gender=gender,
                                  email=email, password=password,one_time_password=x )

            subject, from_email, to = "hello "+firstname, 'avinashdewangan@codenicely.in', email
            text_content = 'This is an important message from codenicely.'
            html_content = '<p>Please enter<strong> ' + str(x) + ' </strong>this one time password to verify your email addres and complete your signup process</p> '
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect('/one_time_password')

    return render(request,'html/signup.html',{})

def one_time_password(request):
    try:
        if request.method == 'POST':
            otp = request.POST.get('one_time_password')
            data = signup.objects.filter(one_time_password=otp).exists()

            if data:
                return HttpResponseRedirect('/login')

    except:
        return HttpResponseRedirect('/one_time_password')


    return render(request, 'html/one_time_password.html')



def login(request):

    try:
        email = request.session['email']
        flag = signup.objects.filter(email=email).exists()

        if flag:
            return HttpResponseRedirect('/base')
    except:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            data = signup.objects.filter(email=email, password=password).exists()

            if data:
                request.session['email'] = email
                return HttpResponseRedirect('/base')
            else:
                messages.error(request, 'didnt exist')

    return render(request,'html/login.html')

def logout(request):

    try:
        email = request.session['email']
        flag = signup.objects.filter(email=email).exists()
        if flag:
            del request.session['email']
            return HttpResponseRedirect('/login')
        else:
            return HttpResponseRedirect('/login')

    except:
        return HttpResponseRedirect('/login')


