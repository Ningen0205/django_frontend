from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

from .models import Question

#from .touch import *
#from .wait import start,stop,roop

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {
    'latest_question_list': latest_question_list,
  }
  return render(request,'polls/index.html',context)

def detail(request, question_id):
  question = get_object_or_404(Question,pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})
      
def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)

def auth_moter(request):
    try:
        with open('command.log.txt', 'w') as f:
            f.write('auth')
    except IOError as a:
        return HttpResponse("error")
    
    return HttpResponse("change_auth_mode")

def add_moter(request):
    try:
        with open('command.log.txt', 'w') as f:
            f.write('add')
    except IOError as a:
        return HttpResponse("error")
    
    return HttpResponse("change_add_mode")

def tmoter(request):
    if (request.method == 'POST'):
        return HttpResponse('post!')