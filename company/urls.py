from django.urls import path
from . import views
app_name = "company"
urlpatterns = [
    path('', views.index, name='Home'),
    path('blog/', views.blog, name="blog"),
    path('contact-us/', views.contact, name="contact"),
    path('about-us/', views.about, name="about"),
    path('<course_id>/<topic_id>',views.topics, name="topics" ),
    path('<course_id>/', views.lessons, name="lessons"),
    ]