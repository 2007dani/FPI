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
        "s_list": models.Souse.objects.all(),
    
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
    else:
        a = birth.split("-")
        b, c, d = a
        birth = jDate.miladi2shamci(b,c,d)
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
    x.save()
  
    if not father==None:
        f=models.Father.objects.get(pk=father)
        for c in f.person_set.all():
            z=c.id
            z=models.Sister()
            if c.sex=="Man":
                z=c.id
                z=models.Brother.objects.get(pk=z)
                x.Brother.add(z)
            if c.sex=="Woman":
                x.Sister.add(c)
                z=c.id
                z=models.Sister.objects.get(pk=z)
                x.Brother.add(z)
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
    if not father==None:
        x.Father=models.Father.objects.get(pk=father)
    if not mother==None:
        x.Mother=models.Father.objects.get(pk=mother)
    x.MoreInfo=moreinfo
    x.Adr=adr
    x.save()

        ####################################################################################

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