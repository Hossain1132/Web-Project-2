from django.shortcuts import render, redirect
from .models import Member

# Create your views here.

def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/index.html', context)

def create(request):
    member = Member(Sl=request.POST['sl'], Name=request.POST['name'], Diseases=request.POST['ds'], Price=request.POST['price'], Available=request.POST['avl'] )
    member.save()
    return redirect('/crud/')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.Sl = request.POST['sl']
    member.Name = request.POST['name']
    member.Diseases = request.POST['ds']
    member.Price = request.POST['price']
    member.Available = request.POST['avl']
    member.save()
    return redirect('/crud/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')