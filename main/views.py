from django.shortcuts import render, HttpResponse
from django.views.generic import View

class Sabado (View):
	def get(self,request):
		#return HttpResponse('Hola Mundo')
		return render(request, 'Hola.html')
# Create your views here.
