# musicas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Musica
from .forms import MusicaForm


def index(request):
    q = (request.GET.get('q') or '').strip()
    musicas = Musica.objects.all()

    if q:
        musicas = musicas.filter(
            Q(nome__icontains=q) |
            Q(tom__icontains=q) |
            Q(descricao__icontains=q)
        )

    musicas = musicas.order_by('nome')
    return render(request, 'musicas/index.html', {'musicas': musicas, 'q': q})


def adicionar_musica(request):
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Música adicionada com sucesso!')
            return redirect('musicas:index')
        messages.error(request, 'Corrija os erros do formulário.')
    else:
        form = MusicaForm()

    return render(request, 'musicas/form.html', {'form': form, 'titulo': 'Adicionar música'})


def editar_musica(request, pk):
    musica = get_object_or_404(Musica, pk=pk)

    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            messages.success(request, 'Música atualizada com sucesso!')
            return redirect('musicas:index')
        messages.error(request, 'Corrija os erros do formulário.')
    else:
        form = MusicaForm(instance=musica)

    return render(request, 'musicas/form.html', {'form': form, 'titulo': 'Editar música'})


def deletar_musica(request, pk):
    """
    Deleta via GET (para compatibilidade com o <a> do template) e via POST.
    Observação: por segurança, o ideal é exigir POST com confirmação e CSRF.
    """
    musica = get_object_or_404(Musica, pk=pk)
    nome = musica.nome

    if request.method in ('POST', 'GET'):
        musica.delete()
        messages.success(request, f"Música '{nome}' excluída com sucesso!")
        return redirect('musicas:index')

    # Fallback (quase nunca cai aqui)
    messages.info(request, 'Ação de exclusão cancelada.')
    return redirect('musicas:index')
