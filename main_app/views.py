from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Wish

# Create your views here.
def wishes_delete(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    wish.delete()
    return redirect('wishes_index')
    
class WishCreate(CreateView):
    model = Wish
    fields = '__all__'

def wishes_index(request):
    wishes = Wish.objects.all()
    return render(request, 'wishes/index.html', {'wishes': wishes})