from django.urls import path
from inicio.views import mi_vista, inicio, vista_datos1, primer_template
urlpatterns = [
        path('mi-vista/', mi_vista),
        path('', inicio),
        path('vista-datos1/', vista_datos1),
        path('primer-template', primer_template)
]
