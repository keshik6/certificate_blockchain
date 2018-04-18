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

    def __str__(self):
        return str(self.certificate_id)

    def getSenderAddress(self):
        return self.sender_address

    def getReceiverAddress(self):
        return self.receiver_address


