from django.contrib import admin
from .models import Cargo, Servico, Funcionario, Features


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ("cargo", 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionariAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado')


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'icone', 'ativo', 'modificado')
