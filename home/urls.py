from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('projects', views.projects, name='projects'),
    path('projects/<int:project_id>', views.project_specific, name='spec_projects'),
    path('resume', views.resume, name='resume'),
    path('contact/', views.contact, name='contact')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)