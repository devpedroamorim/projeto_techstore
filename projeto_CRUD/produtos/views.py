from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoForm

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produto_list.html'
    context_object_name = 'produtos'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produtos/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')
