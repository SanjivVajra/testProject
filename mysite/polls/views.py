from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader, RequestContext
from .models import Question


# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    # output = ", ".join(q.question_text for q in latest_questions)
    #template = loader.get_template('polls/index.html')
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context))
    # return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("detail version of question %s" % question_id)

def results(request, question_id):
    return HttpResponse("detail vew of answer %s" % question_id)

def vote(request, question_id):
    return HttpResponse("vote Question %s" % question_id)