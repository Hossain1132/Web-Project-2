from django.shortcuts import render
from crud.models import Member

def welcome(request):
    return render(request, 'crud/welcome.html')
def show(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/show.html', context)

def edit(request):	
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)