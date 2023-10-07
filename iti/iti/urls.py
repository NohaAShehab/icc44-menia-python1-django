"""
URL configuration for iti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from students.views import helloworld, sayHi, sayHifriend, students_index, students_profile
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello', helloworld, name='helloworld'),
    # path('hi', sayHi, name='hi'),
    # path('hi/<friendname>', sayHifriend,name='hifriend'),
    # path('students', students_index, name='students_index'),
    # path('students/profile/<int:id>',students_profile, name='student.profile' ),

    # include urls files located students application ?
    path('students/', include('students.urls'))


]
