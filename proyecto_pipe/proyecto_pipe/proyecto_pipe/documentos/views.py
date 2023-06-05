from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import documento
from .forms import CreateDocumentForm
from django.shortcuts import render

class listDocumentView(ListView):
    model = documento
    template_name = 'list.html'  # Ruta a tu template HTML
    context_object_name = 'documentos'
    


class createDocumentView(CreateView):
    model = documento
    form_class = CreateDocumentForm
    template_name = 'create.html'
    success_url = "{% url 'documentos:lista_documentos' %}"