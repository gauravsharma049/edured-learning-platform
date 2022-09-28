
from django.shortcuts import render
from .models import course, topic
# Create your views here.
def index(request):
    courses = course.objects.all()
    print(courses)
    
    params = {"course": courses, "range": range(len(courses))}
    return render(request, 'company/index.html', params)

def blog(request):
    return render(request, 'company/blog.html')

def about(request):
    return render(request, 'company/about.html')

def contact(request):
    return render(request, 'company/contact.html')

def lessons(request, course_id):
    
    
    
    topics = topic.objects.all()
    
    courses = course.objects.get(course_id=course_id)
    print(courses.course_name + 'ho gaya')
    params = {"data":courses, "topics":topics}
    return render(request, 'company/lessons.html', params)

def topics(request, course_id, topic_id):
    courses = course.objects.get(course_id=course_id)
    topics = topic.objects.all()
    topicid = topic.objects.get(topic_id=topic_id)
    params ={"topics":topics, "topic_id":topicid, "courses":courses}
    return render(request, 'company/topics.html', params)

