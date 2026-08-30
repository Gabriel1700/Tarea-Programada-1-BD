from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(db_column='Nombre', max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    salario = models.DecimalField(db_column='Salario', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empleado'