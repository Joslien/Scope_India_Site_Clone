
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('contact-scope-india.html',views.contact,name='contact'),
    path('about-scope-india.html',views.about,name='about'),
    path('courses-scope-india.html',views.courses,name='course'),
    path('registration-scope-india.html',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('firstlogin',views.firstlogin,name='firstlogin'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('forgot_pass',views.forgot,name='forgot'),
    path('editprofile',views.edit,name='editprofile'),
    path('courses',views.coursedetails,name='coursedetails'),
    path('enroll',views.enroll,name="enroll"),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),

    # path('states',views.load_states,name='states'),
    # path('city',views.load_city,name='city'),
]
