from django.contrib import admin
from .models import Contact, Project , Skill , Certificate , Education

# Contact Register
admin.site.register(Contact)

# Project Admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "technologies",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "technologies",
    )

    list_editable = (
        "is_active",
    )

    ordering = (
        "-created_at",
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = ("name","percentage","is_active",)
    list_editable = ("percentage","is_active",)
    search_fields = ("name",)  

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = ("title","issued_by","issue_date","is_active",)
    list_filter = ("issued_by","is_active",)
    search_fields = ("title","issued_by",)
    list_editable = ("is_active",)
    ordering = ("-issue_date",)      

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):

    list_display = ("degree","institute","start_year","end_year","is_active",)
    list_filter = ("is_active","start_year",)
    search_fields = ("degree","institute",)
    list_editable = ("is_active",)
    ordering = ("-end_year",)    