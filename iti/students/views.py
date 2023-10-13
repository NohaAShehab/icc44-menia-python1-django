from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from students.models import Student
from students.forms import  StudentForm

# Create your views here.


# functional views
## accept http request ?
def helloworld(request):
    return HttpResponse("Hello World!, Al-menia --> Track")


def sayHi(request):
    return HttpResponse("<h1 style='color:red';> Hi Friends ! </h1>")


def sayHifriend(request, friendname):
    return HttpResponse(f"<h1 style='color:red';> Hi {friendname} ! </h1>")


students = [
    {"name": "John", "age": 25, "track": 'python', "id": 1, "image": "pic1.png"},
    {"name": "ahmed", "age": 25, "track": 'ai', "id": 2, "image": "pic2.png"},
    {"name": "ali", "age": 25, "track": 'php', "id": 3, "image": "pic3.png"}
]


def students_index(request):
    return HttpResponse(students)


# def students_profile(request, id):
#     # print(type(id))
#     # id= int(id)
#     filtered_student = filter(lambda std: std['id'] == id, students)
#     filtered_student = list(filtered_student)
#     print(filtered_student)
#     if filtered_student:
#         print(filtered_student[0])
#         return HttpResponse(filtered_student[0])
#
#     return HttpResponse("No such student Student ")


def students_list(request):
    # send data to the template
    return render(request, 'students/index.html', context={"students": students})


def students_profile(request, id):
    # print(type(id))
    # id= int(id)
    filtered_student = filter(lambda std: std['id'] == id, students)
    filtered_student = list(filtered_student)
    print(filtered_student)
    if filtered_student:
        print(filtered_student[0])
        # return HttpResponse(filtered_student[0])
        return render(request, 'students/profile.html', context={"student": filtered_student[0]})

    return HttpResponse("No such student Student ")


def index(request):
    students = Student.objects.all()
    return render(request, 'students/crud/index.html', context={"students": students})


def show(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'students/crud/show.html', context={"student": student})


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    url = reverse('students.index')
    return redirect(url)
    # return HttpResponse("delete")


def create(request):
    print(request)
    if request.method == 'POST':
        # get data from request
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        grade = request.POST['grade']
        image = request.POST['image']
        student = Student()
        student.name = name
        student.email = email
        student.gender = gender
        student.grade = grade
        student.image = image
        student.save()
        return  redirect(student.get_show_url())
        # return  HttpResponse("data received")
    # return with form --> send data to server using it
    return render(request, 'students/crud/create.html')



def createViaForm(request):
    form = StudentForm()
    if request.method == 'POST':
        print('hiiiii')
        print(request.POST)
        print(request.FILES)
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            grade = form.cleaned_data['grade']
            image = form.cleaned_data['image']
            student = Student()
            student.name = name
            student.email = email
            student.gender = gender
            student.grade = grade
            student.image = image
            student.save()
            return redirect(student.get_show_url())


    return  render(request,'students/crud/form_create.html',
                   context={"form":form})