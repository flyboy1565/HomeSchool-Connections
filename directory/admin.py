from django.contrib import admin

from .models import *

admin.site.register(Family)
admin.site.register(ParentContact)
admin.site.register(Child)
admin.site.register(SkillSet)
admin.site.register(VolunteerType)