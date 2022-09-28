from django.contrib import admin

from company.models import course, topic

# Register your models here.
from .models import course, topic
admin.site.register(course)
admin.site.register(topic)