
from django.urls import path
from .views import *

app_name = "documentos"

urlpatterns = [
    path('lista/', listDocumentView.as_view(), name="lista_documentos"),
    path('crear/', createDocumentView.as_view(), name="crear_documento"),
]
