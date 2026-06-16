from django.db import models

from dreamtech import settings


class Categorie(models.Model):
    COMPUTER = 'ordinateur'
    ACCESSOIRE = 'accessoire'
    FORMATION = 'fournisseur'
    SOFTWARE = 'logiciel'

    CHOICE_CATEGORIES = (
        (COMPUTER,'ordinateur'),
        (ACCESSOIRE,'accessoire'),
        (FORMATION,'fournisseur'),
        (SOFTWARE,'logiciel')
    )
    name = models.CharField(max_length=62,choices=CHOICE_CATEGORIES)

    def __str__(self):
        return self.get_name_display()


class Article(models.Model):
    image = models.ImageField(blank=True,)
    name = models.CharField(max_length=62,blank=True,verbose_name='Nom')
    description = models.CharField(max_length=1200,blank=True)
    price = models.DecimalField(max_digits=62,decimal_places=2,blank=True, null=True,verbose_name='prix')
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,verbose_name='cathegorie') 

    def __str__(self):
        return self.name
    

