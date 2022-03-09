import imp
from multiprocessing.spawn import import_main_path
from django.shortcuts import render
from student.models.students import Student

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        adm = request.POST.get("adm")
        print(name)
        print(adm)
        try:
            student = Student(name=name,adm=adm)
            student.save()
            print("done")
        except:
            print("Fail")
    student = Student.objects.all().order_by('-id')
    data = {
      "students" : student
    }
    return render(request,'index.html',data)