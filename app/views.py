from __future__ import unicode_literals

from django.shortcuts import render




# Create your views here.
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from app.models import FibonacciCheck
from django.views import View
import time


def fibonacci(num):
    if num < 2:
        return 1
    
    else:
        num_1 = 1
        num_2 = 1

        for numeric in range(2, num):
            value = num_1 + num_2
            num_1 = num_2
            num_2 = value 
        
        return num_2


class FibonacciView(View):
    def get(self, request):
        number = request.GET.get('value')

        if number is None:
            return render(request, 'index.html')

        else:
            start_time = time.time()
            numeric = int(number)
            output = fibonacci(numeric)
            end_time = time.time() - start_time
            latency = str(end_time)[0:3]
            


            db_QuerySet = FibonacciCheck.objects.create(numeric = numeric,output = output, latency = latency)

            db_QuerySet.save()

            data = {
                'numeric':numeric,
                'output':output,
                'latency': latency,
                }

        return render(request,'index.html',data)  

		    


