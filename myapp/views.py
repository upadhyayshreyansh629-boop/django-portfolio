from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .models import (
    Project,
    Contact,
    Skill,
    Certificate,
    Education,
)


# =========================================================
# HOME
# =========================================================

def index(request):

    project_count = Project.objects.count()
    certificate_count = Certificate.objects.count()

    technologies = set()

    for project in Project.objects.all():

        if project.technologies:

            tech_list = project.technologies.split(",")

            for tech in tech_list:
                technologies.add(tech.strip())

    context = {
        "project_count": project_count,
        "certificate_count": certificate_count,
        "technology_count": len(technologies),
    }

    return render(request, "index.html", context)


# =========================================================
# ABOUT
# =========================================================

def about(request):

    educations = Education.objects.filter(
        is_active=True
    )

    return render(
        request,
        "about.html",
        {
            "educations": educations
        }
    )


# =========================================================
# PROJECTS
# =========================================================

def projects(request):

    projects = Project.objects.all()

    return render(
        request,
        "project.html",
        {
            "projects": projects
        }
    )


# =========================================================
# PROJECT DETAIL
# =========================================================

def project_detail(request, id):

    project = get_object_or_404(
        Project,
        id=id
    )

    return render(
        request,
        "project_detail.html",
        {
            "project": project
        }
    )


# =========================================================
# SKILLS
# =========================================================

def skills(request):

    skills = Skill.objects.filter(
        is_active=True
    )

    return render(
        request,
        "skills.html",
        {
            "skills": skills
        }
    )


# =========================================================
# CERTIFICATES
# =========================================================

def certificates(request):

    certificates = Certificate.objects.filter(
        is_active=True
    )

    return render(
        request,
        "certificate.html",
        {
            "certificates": certificates
        }
    )


# =========================================================
# CONTACT
# =========================================================

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # -------------------------------------------------
        # Save message in database
        # -------------------------------------------------

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        # -------------------------------------------------
        # Email to Admin
        # -------------------------------------------------

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

            recipient_list=[
                settings.EMAIL_HOST_USER
            ],

            fail_silently=False,
        )

        # -------------------------------------------------
        # Auto Reply to User
        # -------------------------------------------------

        send_mail(
            subject="Thank You for Contacting Me!",

            message=f"""
Hi {name},

Thank you for contacting me through my portfolio website.

I have received your message successfully.

I will get back to you as soon as possible.

--------------------------------------

Regards,

Shreyansh Upadhyay

Portfolio Website
""",

            from_email=settings.EMAIL_HOST_USER,

            recipient_list=[
                email
            ],

            fail_silently=False,
        )

        # -------------------------------------------------
        # Success Message
        # -------------------------------------------------

        messages.success(
            request,
            "✅ Your message has been sent successfully."
        )

        return redirect("contact")

    return render(
        request,
        "contact.html"
    )