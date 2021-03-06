from django.shortcuts import render
from blog.models import Postagem
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def home(request):
	postagens = Postagem.objects.all().order_by('-data_criacao')
	#import pdb;pdb.set_trace()

	return render(request, 'home.html', {'postagens': postagens})

def detalhe_post(request, pk):
	postagem = Postagem.objects.get(pk=pk)
	return render(request, 'detalhe_postagem.html', {'postagem': postagem})

def adicionar_postagem(request):
	if request.method  == 'POST':
		# Quando for para salvar
		form = PostForm(request.POST)
		if form.is_valid():
			postagem = form.save(commit=False)
			postagem.autor = request.user
			postagem.data_publicacao = timezone.now()
			postagem.save()
			return redirect('home') #como está na urls.py
	else:	
		#Primeiro acesso, serve apenas para mostrar o form
		form = PostForm()
	return render(request, 'editar_postagem.html', {'form': form})

def editar_postagem(request, pk):
	postagem = get_object_or_404(Postagem, pk=pk)
	if request.method  == 'POST':
		# Quando for para salvar
		form = PostForm(request.POST, instance=postagem)
		if form.is_valid():
			postagem = form.save(commit=False)
			postagem.autor = request.user
			postagem.data_publicacao = timezone.now()
			postagem.save()
			return redirect('home') #como está na urls.py
	else:	
		#Primeiro acesso, serve apenas para mostrar o form
		form = PostForm(instance=postagem)
	return render(request, 'editar_postagem.html', {'form': form})