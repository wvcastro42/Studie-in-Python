from django.contrib import admin
from .models import Post

#Registra o modelo para aparecer na interface / para exibir o APP no Admin do Django - Listar
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated') #colunas a serem exibidas
    prepopulated_fields = {'slug': ('title',)} #preenche o slug automaticamente com o título do post