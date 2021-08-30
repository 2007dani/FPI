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
    sex = request.POST['sex']
    birth = request.POST['birthday']
    father = request.POST['father']

    if father == 'null':
        father = None
    else:
        father = int(father)
    mother = request.POST['mother']
    if mother == 'null':
        mother = None
    else:
        mother = int(father)

    x = models.Person(Name=name, Family=family, CodeNational=code, sex=sex, Father_id=father, Mother=mother,
                      Birth=birth, )

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
                          Birth=birth)
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
    try:
        mother = models.Mother.objects.get(pk=per.Mother_id)
        father = models.Father.objects.get(pk=per.Father_id)
    except:
        class null:
            Name = "نامعلوم"

        mother = null()
        father = null()

    context = {
        'person': per,
        'mother': mother,
        'father': father,
    }
    return render(request, "FPPI/show.html", context)
