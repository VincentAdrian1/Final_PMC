# contractor_app/admin.py
from django.contrib import admin
from .models import Skill, Experience, Contractor, Project

admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Contractor)
admin.site.register(Project)

