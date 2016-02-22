from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from models import *
# Create your views here.

def home(request):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.all()
	template = "index.html"
	return render_to_response(template, locals())


def hora_actual(request):
	"""
	ahora = datetime.now()
	t = get_template("hora.html")
	c= Context({"hora": ahora, "usuario":"Manuel"})
	html = t.render(c)
	return HttpResponse(html)
	"""

	now = datetime.now()
	return render_to_response('hora.html', {'hora': now})
