from django.urls import path, include



from . import views as core_views


app_name = 'core'

urlpatterns = [
    path('', core_views.index, name='index'),
    path('pessoas/', 
        core_views.PessoaList.as_view(), name='pessoas'),
]
