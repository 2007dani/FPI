from django.shortcuts import redirect, render
import os
from django.http import HttpResponse
from .form import PersonForms

# Create your views here.
from FPPI import models
def index(request):
    context = {
        "Person": models.Person.objects.all()
    }
    return render(request, "FPPI/index.html", context=context)


def add(request):
    context = {
        "f_list": models.Father.objects.all(),
        "m_list": models.Mother.objects.all(),
        "s_list": models.Souse.objects.all(),
        "dayList":range(1,32),
        "monthList":range(1,13),        
        "yearList":range(1300,1410),
        "form" : PersonForms(),  
    }
    return render(request, "FPPI/add.html", context=context)


def Sumbit(request):
    name = request.POST['name']
    family = request.POST['family']
    code = request.POST['code']
    sex = request.POST['gender']
    birth = request.POST['year'] +"/" + request.POST['month'] +  "/" + request.POST['day']
    moreinfo = request.POST["MoreInfo"]
    if code == "":
        code="نامعلوم"
    x = models.Person(Name=name, Family=family, CodeNational=code, sex=sex,
                      Birth=birth, MoreInfo=moreinfo)
    x.save()
    if request.method == 'POST':
        try:
            form = PersonForms(instance=x,files=request.FILES)
            form.save()
        except:
            pass

        ####################################################################################

def Show(request, id):
    per = models.Person.objects.get(pk=id)
    class null:
        Name = "نامعلوم"
    try:
        mother = models.Mother.objects.get(pk=per.Mother_id)
    except:
        mother = null()
    try:
        father = models.Father.objects.get(pk=per.Father_id)
    except:
        father = null()

    context = {
        'person': per,
        'mother': mother,
        'father': father,
    }
    return render(request, "FPPI/show.html", context)
def Edit(request):
    context = {
        "Person": models.Person.objects.all()
    }
    return render(request, "FPPI/edit.html", context=context)
def EditSelect(request,id):
    x=models.Person.objects.get(pk=id)
    context = {
        "Person": models.Person.objects.get(pk=id),
        "f_list": models.Father.objects.all(),
        "m_list": models.Mother.objects.all(),
        "f": x.Father,
        "m":x.Mother,
        "year":x.Birth.split("/")[0],
        "month":x.Birth.split("/")[1],
        "day":x.Birth.split("/")[2],

        "dayList":range(1,32),
        "monthList":range(1,13),        
        "yearList":range(1300,1410),
    }

    return render(request, "FPPI/edit_select.html", context=context)
def Edit_Sumbit(request):
    name = request.POST['name']
    family = request.POST['family']
    code = request.POST['code']
    sex = request.POST['gender']
    birth = request.POST['year'] +"/" + request.POST['month'] +  "/" + request.POST['day']
    moreinfo = request.POST["MoreInfo"]
    pk = request.POST['id']

    if code=="":
        code="نامعلوم"
    x=models.Person.objects.get(pk=int(pk))
    x.Name=name
    x.Family=family
    x.Birth=birth
    x.CodeNational=code
    x.save()
    x=models.Person.objects.get(pk=int(pk))
    try:
        os.remove("."+x.upload.url)
    except:
        pass
    try:
        if request.method == 'POST':
            form = PersonForms(request.POST,request.FILES ,instance=x)
            form.save()
    except:
        pass

    ##########################################################################################

    return redirect('/')
def Delete(request):
    pk=int(request.POST["id"])

    models.Person.objects.get(pk=pk).delete()


    return redirect("/")