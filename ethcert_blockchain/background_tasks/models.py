from django.db import models

# Create your models here.
class Certificate(models.Model):
    certificate_id = models.IntegerField(unique= True)
    receiver_address = models.CharField(max_length= 50)
    receiver_proof = models.CharField(max_length= 500)
    sender_address = models.CharField(max_length= 50)
    sender_proof = models.CharField(max_length= 500)
    description = models.CharField(max_length= 500)
    create_time = models.IntegerField()

