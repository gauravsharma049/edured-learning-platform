from asyncio.windows_events import INFINITE

from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class course(models.Model):
    course_id = models.CharField(max_length=200, primary_key=True)
    
    course_name = models.CharField(max_length=40)
    course_img = models.ImageField(upload_to="company/images", default=None)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.course_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        self.related_course = self.course_name
        super().save(*args, **kwargs)
    
class topic(models.Model):
    
    course_rel = models.ForeignKey(course, on_delete=models.CASCADE, related_name="topic", default=None, null=True)
    related_course = models.CharField(max_length=200, null=True, blank=True)
    topic_id = models.CharField(max_length=50, primary_key=True)
    topic_name = models.CharField(max_length=50)
    topic_data = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.topic_name

    