from django.urls import path
from . import views
from  ProyectoWebApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="Home"),
    path('auto/', views.lista_autos, name='lista_autos'),
    path('auto/nuevo/', views.crear_auto, name='crear_auto'),
    path('auto/<int:pk>/', views.detalle_auto, name='detalle_auto'),
    path('auto/<int:pk>/editar/', views.actualizar_auto, name='actualizar_auto'),
    path('auto/<int:pk>/eliminar/', views.eliminar_auto, name='eliminar_auto'),
    


]

urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)