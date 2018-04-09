from django.db import models
from django.contrib.auth.models import User 

class ReceivedCertificates(models.Model):
    certificate_id = models.IntegerField(unique= True)
    receiver_address = models.CharField(max_length= 50)
    receiver_proof = models.CharField(max_length= 500)
    sender_address = models.CharField(max_length= 50)
    sender_proof = models.CharField(max_length= 500)
    description = models.CharField(max_length= 500)
    create_time = models.IntegerField()


class SentCertificates(models.Model):
    certificate_id = models.IntegerField(unique= True)
    receiver_address = models.CharField(max_length= 50)
    receiver_proof = models.CharField(max_length= 500)
    sender_address = models.CharField(max_length= 50)
    sender_proof = models.CharField(max_length= 500)
    description = models.CharField(max_length= 500)
    create_time = models.IntegerField()


# Create your models here.
class UserProfile(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)

    # Add any additional attributes
    #transaction_list = ArrayField(models.CharField(max_length=64), default=list)

    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    # field for lvl1 verification code
    verification_code_lvl_1 = models.CharField(default="", max_length = 64)

    # field for lvl2 verification code
    verification_code_lvl_2 = models.CharField(default="",max_length = 64)

    # address
    address = models.CharField(default="",max_length = 64)

    # website
    url = models.CharField(default="",max_length = 64)

    # authentication parameters
    auth1 = models.BooleanField(default=False)
    auth2 = models.BooleanField(default=False)

    # Ethereum address
    eth_address = models.CharField(default="Not Setup",max_length = 64)

    # certificates
    sent_cert = models.ForeignKey(SentCertificates,
                                  null = True,
                                  db_column='sentCerts',
                                  blank = True)
    received_cert = models.ForeignKey(ReceivedCertificates,
                                     null = True,
                                     db_column='receivedCerts',
                                     blank = True)


    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

    def getVerificationCode1(self):
        return str(self.verification_code_lvl_1);

    def setVerificationCode1(self, code):
        self.verification_code_lvl_1 = code;

    def getVerificationCode2(self):
        return self.verification_code_lvl_2

    def setVerificationCode2(self, code):
        self.verification_code_lvl_2 = code;

    def getAddress(self):
        return self.address

    def setAddress(self,address):
        self.address = address

    def setUrl(self,url):
        self.url = url

    def getUrl(self):
        return self.url

    def isAuthenticated1(self):
        return self.auth1

    def isAuthenticated2(self):
        return self.auth2

    def setAuthenticated1(self):
        self.auth1 = True;

    def setAuthenticated2(self):
        self.auth2 = True;

    def setEthAddress(self, address):
        self.eth_address = address

    def getEthAddress(self):
        return self.eth_address


