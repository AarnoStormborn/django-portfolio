from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import SpecialSkills, Project, ContactUs, WorkExp, Education, Skills
from django.conf import settings

def index(request):
    data = SpecialSkills.objects.all()
    context = {'special':data}
    return render(request, 'index.html', context)

def projects(request):
    data = Project.objects.all()
    context = {'projects' : data, 'media_url': settings.MEDIA_URL}
    return render(request, 'projects-grid-cards.html', context)

def project_specific(request, project_id):
    
    try:
        data = Project.objects.get(pk=project_id)
    except:
        messages.warning(request, 'No Project for this ID')
        return redirect('projects')
    context = {'project':data, 'media_url': settings.MEDIA_URL}
    return render(request, 'project.html', context)
        
def contact(request):

    if request.method =='POST':
        username = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        if username == '' or email == '':
            messages.warning(request, 'Please fill both Name and Email ID')
            return redirect('contact')
        else:
            messages.success(request, 'We recieved your email and will respond shortly!')
            contactRequest = ContactUs(name=username, email=email, message=message)
            contactRequest.save()

            subject = f'Contact request from {username}'
            content = f'Name: {username}\nEmail: {email}\nMessage: {message}'
            email_from = email
            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, content, email_from, recipient_list)

            return redirect('contact')


    return render(request, 'contact.html')

def resume(request):
    workData = WorkExp.objects.all()
    eduData = Education.objects.all()
    skillData = Skills.objects.all()
    context = {'work':workData, 'education':eduData, 'skills':skillData}
    return render(request, 'cv.html', context)