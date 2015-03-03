from django.db import models



class MyClient(models.Model):

	username = models.CharField(max_length = 500 )
	message = models.TextField()
	onSending  = models.DateTimeField(auto_now = True)
	codeJava = models.TextField(max_length =5000 ,default = "")
	codePython = models.TextField(max_length = 5000, default = "")

	


	def __unicode__(self):
		return self.username


class MyAdmin(models.Model):
	username = models.CharField(max_length =500 )
	message = models.TextField()
	onSending = models.DateTimeField(auto_now = True)
	codeJava = models.TextField(max_length =5000, default = "")
	codePython = models.TextField(max_length = 5000, default = "")
