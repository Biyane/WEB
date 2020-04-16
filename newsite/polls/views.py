from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader


# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404("Does not exists")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % id)


def vote(request, id):
    return HttpResponse("You're voting on question %s." % id)
