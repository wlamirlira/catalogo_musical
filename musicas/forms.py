# musicas/forms.py
from django import forms
from .models import Musica

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ["nome", "tom", "cifra", "bpm", "descricao"]  # ordem exata
        labels = {
            "nome": "Nome",
            "tom": "Tom",
            "cifra": "Cifra",
            "bpm": "BPM",
            "descricao": "Descrição",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex.: Grande é o Senhor"}),
            "tom": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex.: G"}),
            "cifra": forms.Textarea(attrs={"class": "form-control", "rows": 8, "placeholder": "Letra com acordes..."}),
            # BPM como TEXTO:
            "bpm": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex.: 120"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Observações"}),
        }

