from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime

def hello(request):
	return HttpResponse("hello word")

#def current_datetime(request):
#	now = datetime.datetime.now()
#	t = get_template('current_datetime.html')
#	html = t.render(Context({'current_date':now}))
#	return HttpResponse(html)

# APLICANDO METODO RENDER TO RESPONSE para la vista anterior
def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date':now})

# APLICANDO EL METODO DE LOCALS PARA MAPEAR TODAS LAS VARIABLES LOCALES DE LA VISTA Y AHORRAR CODIGO
#def current_datetime(request):
#	current_date = datetime.datetime.now()
#	return render_to_response('current_datetime.html',locals()) 

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
	return render_to_response('hours_ahead.html', {'hours_offset':offset,'next_time':dt})