from django.db import models



class Client(models.Model):
    id = models.AutoField(db_column='client_id', primary_key=True) # en la tabla se llama client_id pero hay que relacionarla con clase Site de abajo
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    joined_datetime = models.DateTimeField()

    def __str__(self):   # para mostrar el nombre en admin     
        return self.first_name + ' ' + self.last_name

    class Meta:
        managed = False
        db_table = 'clients'


class Site(models.Model):
    id = models.AutoField(db_column='site_id', primary_key=True) # El objeto lo voy a trabajar como id, la base de datos para query directa el dato de renombre 'site_id
    domain_name = models.CharField(max_length=100)
    created_datetime = models.DateTimeField()
    client=models.ForeignKey(Client, related_name="sites",on_delete=models.CASCADE) #client_id = models.IntegerField()

    def __str__(self):
        return self.domain_name


    class Meta:
        managed = False
        db_table = 'sites'


class Lead(models.Model):
    id = models.AutoField(db_column='leads_id',primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    registered_datetime = models.DateTimeField()
    email = models.CharField(max_length=50)
    site=models.ForeignKey(Site, related_name="leads", on_delete=models.CASCADE)#site_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leads'


class Documento(models.Model):
    id = models.AutoField(db_column='billing_id',primary_key=True)
    amount = models.FloatField()
    charged_datetime = models.DateTimeField()
    client=models.ForeignKey(Client, related_name="billing",on_delete=models.CASCADE)#client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'billing'

