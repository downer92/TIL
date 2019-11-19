from django.shortcuts import render, redirect
from .models import Question, Choice

# Create your views here.
def new(request):
    if request.method=="POST":
        question = request.POST.get("question")
        q = Question()
        q.question = question
        q.save()
        return redirect("board:index")       
    else:
        return render(request, "board/new.html")

def index(request):
    questions = Question.objects.all()
    context = {
        "questions" : questions
    }
    return render(request, "board/index.html", context)

def detail(request, pk):
    question = Question.objects.get(id=pk)
    choices = question.choice_set.all()
    context = {
        "question" : question,
        "choices" : choices
    }
    return render(request, "board/detail.html", context)

def snew(request, pk):
    question = Question.objects.get(id=pk)
    survey = request.POST.get("survey")
    choice = Choice(survey = survey, question = question)
    choice.save()
    return redirect("board:detail", pk)

def delete(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()
    return redirect("board:index")

def update(request, pk):
    choice = Choice.objects.get(id=pk)
    if request.method == "POST":
        survey = request.POST.get("survey")
        choice.survey = survey
        choice.save()
        return redirect("board:detail", choice.question_id)
    else:
        context = {
            "choice" : choice
        }
        return render(request, "board/update.html", context)

def sdelete(request, pk):
    choice = Choice.objects.get(id=pk)
    choice.delete()
    return redirect("board:detail", choice.question_id)

def vote(request, pk):
    choice = Choice.objects.get(id=pk)
    if request.method == "POST":
        choice.votes += 1
        choice.save()
        return redirect("board:detail", choice.question_id)
    


