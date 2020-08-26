from django.db import models


class Quiz(models.Model):
    ques_no = models.IntegerField(max_length=100, primary_key=True)
    question = models.CharField(max_length=300)
    opt1 = models.CharField(max_length=100, null=True)
    opt2 = models.CharField(max_length=100, null=True)
    opt3 = models.CharField(max_length=100, null=True)
    opt4 = models.CharField(max_length=100, null=True)
    crt_Ans = models.CharField(max_length=100, null=True)


class Answer(models.Model):
    ans = models.CharField(max_length=300)


