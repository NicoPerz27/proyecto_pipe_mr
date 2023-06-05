from django import forms
from .models import documento

class CreateDocumentForm(forms.ModelForm):
    class Meta:
        model = documento
        fields = ["titulo", "contenido"]