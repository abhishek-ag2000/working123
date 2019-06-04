from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from sorl.thumbnail import ImageField, get_thumbnail
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.
class HelpCategories(models.Model):
	Name1 = (
		('Getting Started','Getting Started'),
		('Pricing','Pricing'),
		('Integration','Integration'),
		('Security','Security'),
		('Product Professionals','Product Professionals'),
		('About Products','About Products'),

		)
	Title = models.CharField(max_length=40, default='Getting Started')
	image = ImageField(upload_to='help_image', null=True, blank=True)
	
	def __str__(self):
		return self.Title

	def save(self, *args, **kwargs):
		if self.image:
			imageTemporary = Image.open(self.image).convert('RGB')
			outputIoStream = BytesIO()
			imageTemporaryResized = imageTemporary.resize( (400,400) ) 
			imageTemporaryResized.save(outputIoStream , format='png', quality=300)
			outputIoStream.seek(0)
			self.image = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
			super(HelpCategories, self).save(*args, **kwargs)



class Articles(models.Model):
	Article_title   	= models.CharField(max_length=255,unique=True)
	Description 		= RichTextUploadingField(blank=True, null=True,config_name='description')
	Article_Category 	= models.ForeignKey(HelpCategories,on_delete=models.CASCADE,related_name='category')

	def __str__(self):
		return self.Article_title

	class Meta:
		ordering = ['-id']

class Article_Questions(models.Model):
	User 				= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Article  	    	= models.ForeignKey(Articles,on_delete=models.CASCADE,related_name='Article')
	text 				= models.TextField()
	Date 				= models.DateTimeField(auto_now_add=True)
	Question_title 		= models.CharField(max_length=255,unique=True)
	def __str__(self):
		return self.text

	class Meta:
		ordering = ['-id']

class Article_Answers(models.Model):
	User 			     = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Questions  			 = models.ForeignKey(Articles,on_delete=models.CASCADE,related_name='Article_Question')
	text  	 			 = models.TextField()
	Date 	 			 = models.DateTimeField(auto_now_add=True)
	Article         	 = models.ForeignKey(Articles,on_delete=models.CASCADE,related_name='category')
	Answers 	        = models.ForeignKey(Article_Questions,on_delete=models.CASCADE,related_name='answers')
	def __str__(self):
		return self.text
