from django.db import models


# =========================================================
# CONTACT
# =========================================================

class Contact(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


# =========================================================
# PROJECT
# =========================================================

class Project(models.Model):

    title = models.CharField(
        max_length=100
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="projects/"
    )

    github_link = models.URLField(
        blank=True
    )

    live_demo = models.URLField(
        blank=True
    )

    technologies = models.CharField(
        max_length=200,
        help_text="Example: Python, Django, Bootstrap"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title


# =========================================================
# SKILL
# =========================================================

class Skill(models.Model):

    name = models.CharField(
        max_length=100
    )

    percentage = models.PositiveIntegerField()

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Bootstrap Icon Class (e.g. bi bi-filetype-py)"
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


# =========================================================
# CERTIFICATE
# =========================================================

class Certificate(models.Model):

    title = models.CharField(
        max_length=200
    )

    issued_by = models.CharField(
        max_length=200
    )

    issue_date = models.DateField()

    image = models.ImageField(
        upload_to="certificates/"
    )

    certificate_link = models.URLField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title


# =========================================================
# EDUCATION
# =========================================================

class Education(models.Model):

    degree = models.CharField(
        max_length=150
    )

    institute = models.CharField(
        max_length=200
    )

    branch = models.CharField(
        max_length=100,
        blank=True
    )

    start_year = models.PositiveIntegerField()

    end_year = models.PositiveIntegerField()

    percentage = models.CharField(
        max_length=20,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.degree