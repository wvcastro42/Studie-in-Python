'''
Views podem ser exibidas por Classes, exemplo acima, ou métodos...
pesquisar e implementar opção com métodos como "tarefa"!
'''
from django.http import HttpResponse
import datetime
from django.views.generic import DetailView, ListView
from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


def current_datetime(request):
    now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    html = '<html><body>It is now %s.</body></html>' %now
    return HttpResponse(html)