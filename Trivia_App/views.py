from django.shortcuts import render, redirect
from .models import Quiz, Answer


def home(request):
    results = Quiz.objects.filter(ques_no = 0)
    return render(request, 'Home.html', {"Exam":results})


def quiz1(request):
    if request.method == 'POST':
        ans1 = request.POST['name']
        answer1=Answer(ans=ans1)
        answer1.save()

        results = Quiz.objects.filter(ques_no = 1)
        return render(request, 'quiz1.html', {"Exam": results})


def quiz2(request):
    if request.method == 'POST':
        ans2 = request.POST.get('option')
        answer2=Answer(ans=ans2)
        answer2.save()

        results = Quiz.objects.filter(ques_no = 2)
        return render(request, 'quiz2.html', {"Exam": results})


def quiz3(request):
    if request.method == 'POST':
        ans3 = request.POST.getlist("option")
        answer3=Answer(ans=ans3)
        answer3.save()
        answers = Answer.objects.all()
        results = Quiz.objects.all()
        range = len(answers)
        return render(request, 'quiz3.html', {"Exam": results, "answers":answers, "range":range})


def quiz4(request):
    return redirect("/")









