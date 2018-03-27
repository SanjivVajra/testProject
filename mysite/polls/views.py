from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Awesome, Index page of application')

def detail(request, question_id):
    return HttpResponse("deteil version of question %s" % question_id)

def result(request, question_id):
    return HttpResponse("detail vew of answer %s" % question_id)

def vote(request, question_id):
    return HttpResponse("vote Question %s" % question_id)