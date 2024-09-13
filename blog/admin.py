from django.contrib import admin
from .models import Blog
from ckeditor.widgets import CKEditorWidget
from django.db import models

class BlogAdmin(admin.ModelAdmin):
    # Display title, pub_date, and image_caption in the list view
    list_display = ('title', 'pub_date', 'image_caption')
    
    # Override the TextField to use CKEditor for the body field
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

# Register the Blog model with the custom BlogAdmin
admin.site.register(Blog, BlogAdmin)
