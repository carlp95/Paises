from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
#from django.core.urlresolver import reverse
from .models import Pais, Ciudad
from django.views import generic
# Create your views here.

"""def index(request):
    Agregado_Reciente = Pais.objects.order_by('Nombre')[:5]
    context = {'Agregado_Reciente': Agregado_Reciente}
    return render(request, 'L4/index.html',context)

def detail(request, id_pais):
    pais = get_object_or_404(Pais,pk = id_pais)
    return render(request,'L4/detail.html', {'pais':pais})

def resultados(request, id_pais):
    pais = get_object_or_404(Pais, pk = id_pais)
    return render(request, 'L4/resultados.html', {'pais':pais})
"""

class IndexView(generic.ListView):
    model = Pais
    template_name = 'L4/index.html'
    context_object_name = 'Agregado_Reciente'

    def get_queryset(self):
        return Pais.objects.all()

class DetailView(generic.DetailView):
    model = Pais
    template_name = 'L4/detail.html'


class Resultados(generic.DetailView):
    model = Pais
    template_name = 'L4/resultados.html'

def ciudades(request, id_pais):
    p = get_object_or_404(Pais, pk = id_pais)
    try:
        ciudad_seleccionada = p.ciudad_set.get(pk = request.POST['ciudad'])
    except (KeyError, Ciudad.DoesNotExist):
        return render(request, 'L4/detail.html', {
            'pais': p,
            'error_message': "No has hecho ninguna seleccion.",
        })
    else:
        ciudad_seleccionada.save()
        return render(request,'L4/resultados.html', {'pais':p})
