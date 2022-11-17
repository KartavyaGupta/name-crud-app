from django.shortcuts import render,redirect
from .models import Member

# Create your views here.
def index(request):
    members=Member.objects.all()
    params={
        'members':members
    }
    return render(request,'index.html',params)

def delete(request,id):
    member=Member.objects.get(pk=id)
    member.delete()
    return redirect('basehome')

def create(request):
    if(request.method=="POST"):
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        print(firstname,lastname)
        member=Member(firstname=firstname,lastname=lastname)
        member.save()
    return redirect('basehome')
    

def edit(request,id):
    print(id)
    member=Member.objects.get(pk=id)
    params={
        'member':member
    }
    return render(request,'edit.html',params)

def update(request,id):
    member=Member.objects.get(pk=id)
    member.firstname=request.POST.get('firstname')
    member.lastname=request.POST.get('lastname')
    member.save()
    return redirect('basehome')
