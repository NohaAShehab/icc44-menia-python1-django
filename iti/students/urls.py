from django.urls import path
from students.views import (helloworld, sayHi, sayHifriend, students_index, students_profile,students_list,
                            index, show, delete, create, createViaForm)
urlpatterns = [
    path('hello', helloworld, name='helloworld'),
    path('hi', sayHi, name='hi'),
    path('hi/<friendname>', sayHifriend,name='hifriend'),
    path('', students_index, name='students_index'),
    path('profile/<int:id>',students_profile, name='student.profile' ),
    path('list', students_list, name='students.list'),
    path('db', index, name='students.index' ),
    path('db/<int:id>', show, name='students.show'),
    path('db/<int:id>/delete',delete, name='students.delete' ),
    path('db/create', create, name='students.create'),
    path('db/form/create', createViaForm, name='students.forms.create')


]
