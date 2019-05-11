from django.db import models

# Create your models here.
class FibonacciCheck(models.Model):
	latency = models.CharField(max_length=100, blank=True, null=True)
	numeric = models.BigIntegerField(blank=True, null=True)
	output = models.BigIntegerField(blank=True, null=True)
	
	#def __str__(self):
		#return self.output