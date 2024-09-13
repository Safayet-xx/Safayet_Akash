# research/models.py

from django.db import models

class ResearchPaper(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    publication_date = models.DateField()
    link = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.title

