from django.shortcuts import redirect, render
from .models import Project
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages



# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def project(request):
    return render(request, "project.html")

def contact(request):
    return render(request, "contact.html")

def skills(request):
    return render(request,"skills.html")

from .models import Contact


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save message in database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        # Email to Admin
        send_mail(
            subject=f"📩 New Portfolio Contact - {subject}",
            message=f"""
You have received a new message from your portfolio website.

--------------------------------------

Name : {name}

Email : {email}

Subject : {subject}

Message :

{message}

--------------------------------------

Portfolio Website
            """,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        # Auto Reply to User
        send_mail(
            subject="Thank You for Contacting Me!",
            message=f"""
Hi {name},

Thank you for contacting me through my portfolio website.

I have received your message successfully.

I will get back to you as soon as possible.

--------------------------------------
--------------------------------------

Regards,

Shreyansh Upadhyay
--------------------------------------s
Portfolio Website
            """,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )

        messages.success(
            request,
            "✅ Your message has been sent successfully."
        )

        return redirect("contact")

    return render(request, "contact.html")
from .models import Project

def projects(request):
    projects = Project.objects.all()

    print("Total Projects:", projects.count())
    print(projects)

    return render(request, "project.html", {"projects": projects})

from django.shortcuts import get_object_or_404

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    return render(request,"project_detail.html",{"project": project})

from .models import Skill

def skills(request):
    skills = Skill.objects.filter(is_active=True)
    return render(request,"skills.html",{"skills": skills})

from .models import Certificate

def certificates(request):
    certificates = Certificate.objects.filter(is_active=True)
    return render(request,"certificate.html",{"certificates": certificates})

from .models import Education

def about(request):
    educations = Education.objects.filter(is_active=True)
    return render(request,"about.html",{"educations": educations})