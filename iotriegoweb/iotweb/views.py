from django.shortcuts import render
from django.views import View

def index(request):
    #if request.method == 'POST':
        #humidity_data = request.POST.get('humidity')
        #print("Recibido:", humidity_data)
    return render(request, 'index.html', {'Nodo1': 0.00, 'Nodo2': 0.00,'Nodo3': 0.00})
    #else:
     #   return render(request, 'index.html')