
from unicodedata import name
from django.contrib import admin
from django.urls import path
from student.views.students import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index")
]
