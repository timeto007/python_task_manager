from django.db import models

# Create your models here.
class non_comp_task_model(models.Model):
    task_name=models.CharField(max_length=100,default='none')
    task_created_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "non_comp_model"

class comp_task_model(models.Model):
    task_name=models.CharField(max_length=100,default='none')
    task_completed_time=models.DateTimeField(auto_now_add=True)
   # time_taken = models.CharField(max_length=100, default='none')


    class Meta:
        db_table="comp_model"