from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^platillo/nuevo/$', views.platillo_editar, name='platillo_editar'),
]
