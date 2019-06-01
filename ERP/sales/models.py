from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=250)
	mobile = models.IntegerField()
	gender = models.CharField(choices=[("m","MALE"),('f',"FEMALE")],
		max_length=2)

	def __str__(self):
		return "%s--> %s"%(self.name,self.gender)
