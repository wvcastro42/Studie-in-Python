from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import User
from .forms import UserCreationForm, UserChangeForm

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos personalizados", {"fields": ("bio",)}),
    )