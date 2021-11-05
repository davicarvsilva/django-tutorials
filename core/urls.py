from django.urls import path, include



from . import views as core_views


app_name = 'core'

urlpatterns = [
    path('', core_views.index, name='index'),
    path('cadastrar-pessoa/', 
        core_views.PessoaFormView.as_view(), name='cadastrar_pessoa'),
    path('cadastrar-musica/', 
        core_views.MusicaFormView.as_view(), name='cadastrar_musica')
]
