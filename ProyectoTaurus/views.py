from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    es_admin = request.user.rol == 'admin'
    return render(request, 'index.html', {'es_admin': es_admin})
