from django.db import models
import csv
# Create your models here.


class Catalizador(models.Model):
    num = models.CharField(max_length=10, default= '0')
    código = models.CharField(max_length=30, blank=False, default = 'null')
    precio = models.IntegerField(default=0)
    marca = models.CharField(max_length=20, blank=False, default = 'null')
    imagen = models.CharField(max_length=50, blank=False, default = 'null')
    familia = models.CharField(max_length=30, blank=False, default = 'null')


    def __str__(self):
        return self.código
 
#csv_filepathname="/Users/dAVID/Desktop/Django Data/precios.csv"
#dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
#for row in dataReader:
#    if row[0] != 'ID': 
#        print (row[0],row[1],row[2])
#        Catalizador.objects.update_or_create(
#            num = row[0], código = row[1],
#            defaults={'precio': row[2]},
#      )


