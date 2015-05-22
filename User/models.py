from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)		

class member(models.Model):
	
	user = models.OneToOneField(User)
	display_picture = models.FileField(upload_to = get_upload_file_name)
	location = models.CharField(max_length=200)
	about_me = models.TextField()
	
User.profile = property(lambda x : member.objects.get_or_create(user = x)[0])
