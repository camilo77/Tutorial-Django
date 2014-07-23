from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll
from django.template import RequestContext, loader

# Create your views here.

#def index(request):
#	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#	template = loader.get_template('polls/index.html')
#	context = RequestContext(request, {
#		'latest_poll_list': latest_poll_list,
#	})
#	return HttpResponse(template.render(context))

# version mejorada
def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	context = {'latest_poll_list':latest_poll_list}
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	return HttpResponse("you are looking at poll %s" %poll_id)

def results(request, poll_id):
	return HttpResponse("you are looking at the results of poll %s" %poll_id)

def vote(request, poll_id):
	return HttpResponse("you are voting on poll %s" %poll_id)