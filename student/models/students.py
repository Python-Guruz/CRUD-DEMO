from statistics import mode
from django.db import models

class Student(models.Model):
    __tablename__="tbl_student"
    name = models.CharField(max_length=255,null=False,blank=False)
    adm = models.CharField(max_length=255,null=False,blank=False)

    def __str__(self):
        return f'{self.name} - {self.adm}'