from django.shortcuts import redirect, render
import os
from django.http import HttpResponse

# Create your views here.
from FPPI import models
def index(request):
    context = {
        "Person": models.Person.objects.all()
    }
    import FPPI.Emma
    FPPI.Emma.Emma().CreateWordFile()
    return render(request, "FPPI/index.html", context=context)


def add(request):
    from .form import GeeksModel
    context = {
        "f_list": models.Father.objects.all(),
        "m_list": models.Mother.objects.all(),
        "s_list": models.Souse.objects.all(),
        "dayList":range(1,32),
        "monthList":range(1,13),        
        "yearList":range(1300,1410),
    
    }
    return render(request, "FPPI/add.html", context=context)


def Sumbit(request):
    name = request.POST['name']
    family = request.POST['family']
    code = request.POST['code']
    sex = request.POST['gender']
    birth = request.POST['year'] +"/" + request.POST['month'] +  "/" + request.POST['day']
    moreinfo = request.POST["MoreInfo"]

    if birth=="YYYY/MM/DD":
        birth="نامعلوم"
    else:  
        birth = birth


    x = models.Person(Name=name, Family=family, CodeNational=code, sex=sex,
                      Birth=birth, MoreInfo=moreinfo)
    x.save()
  

    if sex == "Man":
        y = models.Father(Name=name, Family=family, CodeNational=code, Birth=birth, person_id=x.id)
        y.save()

        z = models.Brother(Name=name, Family=family, CodeNational=code, Birth=birth, )
        z.save()

        a = models.Son(Name=name, Family=family, CodeNational=code, Birth=birth, )
        a.save()

        b = models.Souse(Name=name, Family=family, CodeNational=code, Birth=birth, )
        b.save()

    if sex == "Woman":
        y = models.Mother(Name=name, Family=family, CodeNational=code, Birth=birth, person_id=x.id)
        y.save()
        z = models.Sister(Name=name, Family=family, CodeNational=code, Birth=birth, )
        z.save()
        a = models.Dather(Name=name, Family=family, CodeNational=code, Birth=birth, )
        a.save()
        b = models.Souse(Name=name, Family=family, CodeNational=code, Birth=birth, )
        b.save()

        ####################################################################################

    return redirect('/')


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

    if birth=="YYYY/MM/DD":
        birth="نامعلوم"
    x=models.Person.objects.get(pk=int(pk))
    x.Name=name
    x.Family=family
    x.Birth=birth
    x.CodeNational=code
    x.save()

    ##########################################################################################

    return redirect('/')
def Delete(request):
    pk=int(request.POST["id"])

    if models.Person.objects.get(pk=pk).sex=="Man":
        models.Person.objects.get(pk=pk).delete()
        models.Son.objects.get(pk=pk).delete()
        models.Souse.objects.get(pk=pk).delete()
        models.Father.objects.get(pk=pk).delete()
        models.Brother.objects.get(pk=pk).delete()
    else:
        models.Person.objects.get(pk=pk).delete()
        models.Mother.objects.get(pk=pk).delete()
        models.Sister.objects.get(pk=pk).delete()
        models.Dather.objects.get(pk=pk).delete()
        models.Souse.objects.get(pk=pk).delete()

    return redirect("/")