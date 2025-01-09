from django.db import models
from choices import *
from django.contrib.auth.models import User
import uuid


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField(auto_now=True)
    Updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Choices(BaseModel):
    Choices = models.CharField(max_length=200,null=True,blank=True)

class Question(BaseModel):
    question = models.CharField(max_length=200,null=True, blank =True)
    required = models.BooleanField(default=True)
    question_type  = models.CharField(choices=question_typeEnum.choices(),null=True, blank =True)
    Choices = models.ManyToManyField(Choices, related_name="question_choices",blank=True)

class Form(BaseModel):
    form_id = models.UUIDField(uuid.uuid5, primary_key= True,)
    form_name = models.CharField(max_length=100, null=True, blank=True)
    created_by= models.ForeignKey(User,on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, related_name="questions")
    bg_color = models.CharField(default="7FC6A4")


