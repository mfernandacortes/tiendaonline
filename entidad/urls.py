from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('shop', views.shop, name="shop"),
    path('contacto', views.contacto, name="contacto"),
    path('remeras', views.remeras, name="remeras"),
    path('remera/<int:id_ropa>', views.remera, name="remera"),
    path('nueva_remera', views.nueva_remera, name="nueva_remera")
]