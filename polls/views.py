from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,you're at the polls index")

def detail(request,question_id):
    response = "You're look at the  question %s."
    return HttpResponse(response % question_id)

def results(request,question_id):
    response = "You're look at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    response = "You're voting on question %s."
    return HttpResponse(response %question_id)

