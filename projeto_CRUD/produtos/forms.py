from django import forms
from .models import Produto

PALAVRAS_PROIBIDAS = [
    'merda', 'porra', 'caralho', 'puta', 'desgraça', 'fdp', 'foda', 'bosta', 
    'inferno', 'maldito', 'arrombado', 'imbecil', 'idiota', 'corno', 'viado', 
    'buceta', 'cuzão', 'escroto', 'retardado', 'otário'
]

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade_estoque']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do produto', 'rows': 3}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
            'quantidade_estoque': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade em estoque'}),
        }

    def verificar_palavroes(self, texto):
        for palavra in PALAVRAS_PROIBIDAS:
            if palavra.lower() in texto.lower():
                raise forms.ValidationError("O texto contém termos não permitidos.")
        return texto

    def clean_nome(self):
        return self.verificar_palavroes(self.cleaned_data.get('nome'))

    def clean_descricao(self):
        return self.verificar_palavroes(self.cleaned_data.get('descricao'))

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco is None or preco <= 0:
            raise forms.ValidationError("O preço deve ser um valor positivo.")
        return preco

    def clean_quantidade_estoque(self):
        quantidade = self.cleaned_data.get('quantidade_estoque')
        if quantidade is None or quantidade < 0:
            raise forms.ValidationError("A quantidade em estoque não pode ser negativa.")
        return quantidade
