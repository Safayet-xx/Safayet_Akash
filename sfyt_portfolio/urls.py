from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home,name = 'home'),
    path('research/', include('research.urls')),
    path('blog/', include ('blog.urls')),
    path('', include('contact.urls')),
    #path('', include('research.urls')),
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT )

