from django.db import models
from django.contrib.auth.models import User

#cria a Tabela post, do APP Blob, com os seguintes campos:
class Post(models.Model): 
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True) # Ex: www.blog.com/introducao-ao-django 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str: # para aparecer o título do post quando exibir a lista de posts
        return self.title
