from django.contrib import admin

# Register your models here to be display in the admin dashboard.

from students.models import Student

admin.site.register(Student)
