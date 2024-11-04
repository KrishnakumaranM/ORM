from django.db import models
from django.contrib import admin
class customer(models.Model):
  cid=models.CharField(max_length=20,primary_key="cid")
  name=models.CharField(max_length=50)
  mobilenumber=models.IntegerField()
  age=models.IntegerField()
  accountno=models.IntegerField()


class customerAdmin(admin.ModelAdmin):
    list_display=('cid','name','mobilenumber','age','accountno')

