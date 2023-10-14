from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView
from django.views.generic.edit import  CreateView
from django.http import HttpResponse
from accounts.forms import AccountForm
# Create your views here.

def profile(request):
    # return HttpResponse("profile")
    url= reverse('students.index')
    return  redirect(url)


# create new user ?

class AccountCreateView(CreateView):
    form_class = AccountForm
    template_name = 'accounts/create.html'
    success_url = '/accounts/login/'

