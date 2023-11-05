from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render,HttpResponse,redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from .models import Registration
from .forms import ContactForm, RegistrationForm, PasswordChangingForm
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,'app/home.html')

def aboutus(request):
    return render(request,template_name='app/about.html')

def contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            Name = form.cleaned_data['Name']
            Email = form.cleaned_data['Email']
            Subject = form.cleaned_data['Subject']
            Message = form.cleaned_data['Message']

            html = render_to_string('app/email.html',{
                'Name':Name,
                'Email':Email,
                'Subject':Subject,
                'Message':Message
            })
            send_mail('The contact from the subject','This is the message','azeemaze500@gmail.com',['azeemvbm@gmail.com'],html_message=html)
            return HttpResponse("Thanks for Your Enquiry,We will reach you soon")
        else:
            form = ContactForm
    return render(request,'app/contact.html',{'form':form})

def RegistrationF(request):

        form =RegistrationForm(request.POST,request.FILES)
        rgn = Registration()
        if form.is_valid():
            rgn.First_Name = form.cleaned_data['First_Name']
            rgn.Last_Name = form.cleaned_data['Last_Name']
            rgn.Gender = form.cleaned_data['Gender']
            rgn.Date_of_Birth = form.cleaned_data['Date_of_Birth']
            rgn.Email = form.cleaned_data['Email']
            rgn.Mobile = form.cleaned_data['Mobile']
            rgn.Country = form.cleaned_data['Country']
            rgn.State = form.cleaned_data['State']
            rgn.City = form.cleaned_data['City']
            rgn.Hobbies = form.cleaned_data['Hobbies']
            rgn.Upload_image = form.cleaned_data['Upload_image']
            rgn.save()
            return HttpResponse("Student Registration Done")

        return render(request,'app/registration.html',{'form':form})


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = User.objects.make_random_password(length=8, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")
        print(pass1)

        user = User.objects.create_user(uname, email, pass1)
        user.save()
        subject = "Your temperory password"
        message = ""
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]

        html = render_to_string('app/pswd.html', {
            'password': pass1,

        })

        send_mail(subject, message,
                  email_from, recipient_list, html_message=html, fail_silently=False, )
        return redirect('login')

    return render(request, 'app/signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user1 = authenticate(request, username=username, password=pass1)

        if user1 is not None:
            auth.login(request, user1)
            request.session['user_status'] = 'you are successfully logged in'
            request.session['username']= user1.username
            request.session.set_expiry(3600)
            return render(request,'app/logout.html',
                            {'status2':request.session['user_status'],'status':request.session['username']})
        else:
            return HttpResponse("Username or password is incorrect")

    return render(request, 'app/login.html')


def LogoutPage(request):
    request.session['user_status'] = 'logged out'
    request.session['username'] = ''
    return redirect('home')

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'app/password_success.html', {})

def courses(request):
    return render(request,'app/courses.html')
