from django.contrib import admin

# Register your models here.
from .models import Candidate, Job, Skill



admin.site.register(Job)
admin.site.register(Candidate)
admin.site.register(Skill)