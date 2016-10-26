from django.db import models


class Cheque(models.Model):
    cheque_no = models.CharField(max_length=20)
    valor = models.IntegerField(default=0)
    cheque_fecha = models.DateTimeField('cheque fecha')
    cheque_mes = models.CharField(max_length=20)
    def __str__(self):
        return self.cheque_no


class Factura(models.Model):
    factura_archivo = models.CharField(max_length=50)
    cheque = models.ForeignKey(Cheque, on_delete=models.CASCADE)
    folio = models.CharField(max_length=60)
    total = models.IntegerField(default=0)
    factura_fecha = models.DateTimeField('factura fecha')
    def __str__(self):
        return self.folio