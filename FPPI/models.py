from django.db import models


# Create your models here.

class Person(models.Model):
    Name = models.CharField(max_length=100, null=1)
    Family = models.CharField(max_length=100,null=1)
    sex = models.CharField(max_length=10, null=1)
    CodeNational = models.CharField(max_length=100, null=1)
    Birth = models.CharField(null=1,max_length=100)
    Father = models.ForeignKey("Father", models.CASCADE, null=True)
    Mother = models.ForeignKey("Mother", models.CASCADE, null=True)


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
