from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# functional views
## accept http request ?
def helloworld(request):
    return  HttpResponse("Hello World!, Al-menia --> Track")


def sayHi(request):
    return  HttpResponse("<h1 style='color:red';> Hi Friends ! </h1>" )

def sayHifriend(request, friendname):
    return  HttpResponse(f"<h1 style='color:red';> Hi {friendname} ! </h1>" )



students = [
    {"name": "John", "age":25, "track":'python', "id":1},
    {"name": "ahmed", "age":25, "track":'ai', "id":2},
    {"name": "ali", "age":25, "track":'php',"id":3 }
]


def students_index(request):
    return HttpResponse(students)



def students_profile(request, id):
    # print(type(id))
    # id= int(id)
    filtered_student= filter(lambda std:std['id']==id, students)
    filtered_student = list(filtered_student)
    print(filtered_student)
    if filtered_student:
        print(filtered_student[0])
        return HttpResponse(filtered_student[0])

    return HttpResponse("No such student Student ")