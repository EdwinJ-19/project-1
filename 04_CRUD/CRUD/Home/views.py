from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from Home.models import Entry

# Create your views here.
def home(request):
    return render(request,"home.html")

def show(request):
    data = Entry.objects.all()
    return render(request,"show.html",{'data':data})

def send(request):
    if request.method == 'POST':
        ID = request.POST['id']
        Name = request.POST['Name']
        Contact = request.POST['Contact']
        Entry(ID = ID,Name=Name,Contact=Contact).save()
        msg="Data Stored Successfully"
        return render(request,"home.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")
    
def delete(request):
    ID = request.GET['id']
    Entry.objects.filter(ID=ID).delete()
    return HttpResponseRedirect("show")

def edit(request):
    ID = request.GET['id']
    Name = Contact = "Not Available"
    for data in Entry.objects.filter(ID=ID):
        Name = data.Name
        Contact= data.Contact
    return render(request,"edit.html",{'ID':ID,'Name':Name,'Contact':Contact})

def RecordEdited(request):
    if request.method == 'POST':
        ID = request.POST['id']
        Name= request.POST['Name']
        Contact= request.POST['Contact']
        Entry.objects.filter(ID=ID).update(Name=Name,Contact=Contact)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")