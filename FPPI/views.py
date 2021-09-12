from django.shortcuts import redirect, render
import playsound
from gtts import gTTS, gTTSError
import os
from django.http import HttpResponse
# Create your views here.
from FPPI import models
import os


def index(request):
    context = {
        "Person": models.Person.objects.all()
    }
    return render(request, "FPPI/index.html", context=context)


def add(request):
    context = {
        "f_list": models.Father.objects.all(),
        "m_list": models.Mother.objects.all(),
    
    }
    return render(request, "FPPI/add.html", context=context)


def Sumbit(request):
    name = request.POST['name']
    family = request.POST['family']
    code = request.POST['code']
    sex = request.POST['gender']
    birth = request.POST['birthday']
    father = request.POST['father']
    moreinfo = request.POST["MoreInfo"]
    adr=request.POST["Adr"]

    if birth=="YYYY-MM-DD":
        birth="نامعلوم"
    if father == 'null':
        father = None
    else:
        father = int(father)
    mother = request.POST['mother']
    if mother == 'null':
        mother = None
    else:
        mother = int(mother)

    x = models.Person(Name=name, Family=family, CodeNational=code, sex=sex, Father_id=father, Mother=mother,
                      Birth=birth, MoreInfo=moreinfo,Adr=adr)
    if sex == "Man":
        x.save()
        y = models.Father(Name=name, Family=family, CodeNational=code, Birth=birth, person_id=x.id)
        y.save()

        z = models.Brother(Name=name, Family=family, CodeNational=code, Birth=birth, )
        z.save()

        a = models.Son(Name=name, Family=family, CodeNational=code, Birth=birth, )
        a.save()

        b = models.Souse(Name=name, Family=family, CodeNational=code, Birth=birth, )
        b.save()

    if sex == "Woman":
        x = models.Person(Name=name, Family=family, CodeNational=code, sex=sex, Father=father, Mother=mother,
                          Birth=birth, MoreInfo=moreinfo)
        x.save()
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
        "m":x.Mother
    }

    return render(request, "FPPI/edit_select.html", context=context)
def Edit_Sumbit(request):
    name = request.POST['name']
    family = request.POST['family']
    code = request.POST['code']
    sex = request.POST['gender']
    birth = request.POST['birthday']
    father = request.POST['father']
    moreinfo = request.POST["MoreInfo"]
    adr=request.POST["Adr"]
    pk = request.POST['id']

    if birth=="YYYY-MM-DD":
        birth="نامعلوم"
    if father == '':
        father = None
    else:
        father = int(father)
    mother = request.POST['mother']
    if mother == '':
        mother = None
    else:
        mother = int(mother)
    x=models.Person.objects.get(pk=int(pk))
    x.Name=name
    x.Family=family
    x.Birth=birth
    x.CodeNational=code
    x.Father=father
    x.Mother=mother
    x.MoreInfo=moreinfo
    x.Adr=adr
    x.save()

    if sex == "Man":
        x.save()
        y = models.Father(Name=name, Family=family, CodeNational=code, Birth=birth, person_id=x.id)
        y.save()

        z = models.Brother(Name=name, Family=family, CodeNational=code, Birth=birth, )
        z.save()

        a = models.Son(Name=name, Family=family, CodeNational=code, Birth=birth, )
        a.save()

        b = models.Souse(Name=name, Family=family, CodeNational=code, Birth=birth, )
        b.save()

    if sex == "Woman":
        x = models.Person(Name=name, Family=family, CodeNational=code, sex=sex, Father=father, Mother=mother,
                          Birth=birth, MoreInfo=moreinfo)
        x.save()
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
