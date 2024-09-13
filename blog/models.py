from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = RichTextField()
    image = models.ImageField(upload_to='images/')
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)  # Field to upload PDF
    image_caption = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self): 
        return self.title
 
    def summary (self):
        return self.body [:100]
    

    def pub_date_pretty(self):
        return self.pub_date.strftime( ' %b %e %y ')

