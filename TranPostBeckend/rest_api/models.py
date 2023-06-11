from django.db import models

# Create your models here.
class employee(models.Model):
    GPF_No=models.CharField(max_length=20)
    Name=models.CharField(max_length=100)
    Designation=models.CharField(max_length=30)
    Curr_office=models.CharField(max_length=50)
    Curr_block=models.CharField(max_length=50)
    Curr_post_year=models.IntegerField()
    First_post_office=models.CharField(max_length=50)
    First_post_office_block=models.CharField(max_length=50)
    Second_post_office=models.CharField(max_length=50)
    Second_post_office_block=models.CharField(max_length=50)
    Dept_office=models.CharField(max_length=50)
    Dept_block=models.CharField(max_length=50)
    
class newemployee(models.Model):
    GPF_No=models.CharField(max_length=20)
    Name=models.CharField(max_length=100)
    Designation=models.CharField(max_length=30)
    Curr_office=models.CharField(max_length=50)
    Curr_block=models.CharField(max_length=50)
    Curr_post_year=models.IntegerField()
    First_post_office=models.CharField(max_length=50)
    First_post_office_block=models.CharField(max_length=50)
    Second_post_office=models.CharField(max_length=50)
    Second_post_office_block=models.CharField(max_length=50)
    Dept_office=models.CharField(max_length=50)
    Dept_block=models.CharField(max_length=50)
    Alloted_Block=models.CharField(max_length=50)
    Alloted_office=models.CharField(max_length=50)




   