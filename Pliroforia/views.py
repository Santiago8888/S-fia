
# Create your views here.

from django.db.models import Q
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from .models import Catalizador

@login_required(login_url="login/")   
def busqueda(request):
    query = request.GET.get('q', '')
    if query:
            qset = (
                Q(código__icontains=query)
            )
            results = Catalizador.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("Pliroforia/searchCat.html", {
        "results": results,
        "query": query
    })
    
    

def logout_page(request):
 logout(request)
 return HttpResponseRedirect('/login')




