from django.shortcuts import render, redirect

from .models import Show

def index(request):
    return redirect("/home")

def home(request):
    ctx = {
        'shows': Show.objects.all()
    }
    return render(request, "home.html", ctx)

def new_show(request):
    return render(request, "add_show.html")

def create(request):
    Show.objects.create(title=request.POST['title'], network=request.POST['network'],release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect('/home')

def show (request, id):
    ctx ={
        'show':Show.objects.get(id=id)
    }
    return render(request, "show.html", ctx)

def edit_show(request, id):
    ctx ={
        'show':Show.objects.get(id=id)
    }
    return render(request, "edit_show.html", ctx)

def destroy(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/home")


def update(request):
    u = Show.objects.get(id=request.POST['id'])
    u.title = request.POST['title']
    u.network = request.POST['network']
    u.release_date = request.POST['release_date']
    u.save()
    return redirect("/home/"+str(u.id))