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


class Souse(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.DateField(null=1)
    Person = models.ForeignKey("Person", models.CASCADE, null=1)


class Sister(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.DateField(null=1)
    Person = models.ForeignKey("Person", models.CASCADE, null=1)


class Brother(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.DateField(null=1)
    Person = models.ForeignKey("Person", models.CASCADE, null=1)


class Father(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.DateField(null=1)
    person_id = models.CharField(null=1, max_length=50)


class Mother(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.DateField(null=1)
    person_id = models.CharField(null=1, max_length=50)


class Dather(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.DateField(null=1)
    Person = models.ForeignKey("Person", models.CASCADE, null=1)


class Son(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.DateField(null=1)
    Person = models.ForeignKey("Person", models.CASCADE, null=1)
