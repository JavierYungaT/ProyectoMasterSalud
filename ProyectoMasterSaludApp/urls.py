from django.urls import path
from ProyectoMasterSaludApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('contactos/', views.contactos, name="contactos"),
    path('about/', views.about, name="about"),
    path('encuesta/', views.encuesta, name="encuesta"),
    path('saludable/', views.saludable, name="saludable"),
    

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)