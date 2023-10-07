from django.urls import path
from students.views import helloworld, sayHi, sayHifriend, students_index, students_profile
urlpatterns = [
    path('hello', helloworld, name='helloworld'),
    path('hi', sayHi, name='hi'),
    path('hi/<friendname>', sayHifriend,name='hifriend'),
    path('', students_index, name='students_index'),
    path('profile/<int:id>',students_profile, name='student.profile' ),

]
