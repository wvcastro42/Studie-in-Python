'''
Views podem ser exibidas por Classes, exemplo acima, ou métodos...
pesquisar e implementar opção com métodos como "tarefa"!
'''

from django.views.generic import DetailView, ListView
from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post



