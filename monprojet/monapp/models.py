from django.db import models

class Personnes(models.Model) :
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    date_naissance = models.DateField()
        
    class Meta :
        db_table = 'personnes'
        

class Dog(models.Model) :
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    
    class Meta :
        db_table = 'dog'