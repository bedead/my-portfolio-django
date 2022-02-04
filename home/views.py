from django.shortcuts import redirect, render, HttpResponse
from home.models import Contact
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError


# Create your views here.


# index (Home portfolio page)
def index(request):
    return render(request, "index.html")


# about section of portfolio
def about(request):
    return render(request, 'about.html')


# list of projects page
def projects(request):
    return render(request, 'projects.html')

# droping a msg page.
def contact(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')

        if name and email and msg:
            contact = Contact(name=name, email=email, msg=msg)
            contact.save()

            # sending mail to myself from satyammishra.site@gmail.com gmail

            try:
                send_mail(
                f"Conatct - from {name}",
                f"{msg} \nfrom email: {email}",
                'satyammishra.site@gmail.com',
                ['satyam.work.only@gmail.com'],
                fail_silently=False,
            )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

        
            messages.success(request, 'hey, '+str(name)+' I have got your msg!')          
            return redirect('/')

        else:
            messages.error(request, "Make sure to fill all the Fields!")

            return render(request, 'contact.html')


    return render(request, 'contact.html')