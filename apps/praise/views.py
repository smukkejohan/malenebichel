from django.shortcuts import render
from models import Praise

def index(request):
    praise_list = Praise.objects.all()
    return render(request, 'praises.html', {'praise_list': praise_list})