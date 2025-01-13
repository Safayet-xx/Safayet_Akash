from django.contrib import admin

# Register your models here.
# Register your models here.
from django.contrib import admin
from.models import ResearchPaper
from ckeditor.widgets import CKEditorWidget
from django.db import models

@admin.register(ResearchPaper)

class ResearchPaperAdmin(admin.ModelAdmin):

    list_display = ('title', 'publication_date', 'link')  # Include the new field
    search_fields = ('title', 'abstract', 'link')

    
    # Override the TextField to use CKEditor for the body field
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
    