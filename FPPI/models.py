from django.db import models

# Create your models here.
class Person(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100,null=1)
    sex = models.CharField(max_length=10, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.CharField(null=1,max_length=100)
    Adr = models.CharField(null=1, max_length=200)
    Father = models.ForeignKey("Father", models.CASCADE, null=1)
    Mother = models.ForeignKey("Mother", models.CASCADE, null=True)
    MoreInfo = models.CharField(max_length=3000 ,null=1,)
    Sister =  models.ManyToManyField("Sister")
    Brother =  models.ManyToManyField("Brother")
    Souse =  models.ManyToManyField("Souse")


class Souse(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.CharField(null=1,max_length=100)

class Sister(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.CharField(null=1,max_length=100)

class Brother(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.CharField(null=1,max_length=100)

class Father(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.CharField(null=1,max_length=100)
    person_id = models.CharField(null=1, max_length=50)


class Mother(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.CharField(null=1,max_length=100)
    person_id = models.CharField(null=1, max_length=50)


class Dather(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.CharField(null=1,max_length=100)
    Person = models.ForeignKey("Person", models.CASCADE, null=1)


class Son(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.CharField(null=1,max_length=100)
    Person = models.ForeignKey("Person", models.CASCADE, null=1)
