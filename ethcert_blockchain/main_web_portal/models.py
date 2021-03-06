from django.db import models
from django.contrib.auth.models import User
from background_tasks.models import Certificate
import time, os

# Use Singapore timezone
os.environ['TZ'] = 'Asia/Singapore'
time.tzset()

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
    address = models.CharField(default="NA",max_length = 64, null=True, blank=True)

    # website
    url = models.CharField(default="NA",max_length = 64, null=True, blank=True)

    # authentication parameters
    auth1 = models.BooleanField(default=False)
    auth2 = models.BooleanField(default=False)

    #Ethereum address
    eth_address = models.CharField(default="Not Setup",max_length = 64)

    # Certificates
    sent_certificates = models.ManyToManyField(Certificate,
                                               related_name="sent_certificates",
                                               blank=True)

    received_certificates = models.ManyToManyField(Certificate,
                                                   related_name="received_certificates",
                                                   blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

    def getVerificationCode1(self):
        return str(self.verification_code_lvl_1)

    def setVerificationCode1(self, code):
        self.verification_code_lvl_1 = code;

    def getVerificationCode2(self):
        return str(self.verification_code_lvl_2)

    def setVerificationCode2(self, code):
        self.verification_code_lvl_2 = code;

    def getAddress(self):
        print(self.address)
        return (self.address)

    def setAddress(self,address):
        self.address = address

    def setUrl(self,url):
        self.url = url

    def getUrl(self):
        print(self.url)
        return (self.url)

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

    def getSentCertificates(self):
        certs = self.sent_certificates.all()
        output = []

        for cert in certs:
            data = {}
            data['certificate_id'] = cert.certificate_id
            data['sender_address'] = cert.getSenderAddress()
            data['sender_proof'] = cert.sender_proof
            data['receiver_address'] = cert.getReceiverAddress()
            data['receiver_proof'] = cert.receiver_proof
            data['description'] = cert.description
            int_time = cert.create_time
            data['create_time'] = time.strftime('%A %b %d %Y %H:%M:%S GMT%Z',
                                                time.localtime(int_time))

            output.append(data)

        return output

    def getReceivedCertificates(self):
        certs = self.received_certificates.all()
        output = []

        for cert in certs:
            data = {}
            data['certificate_id'] = cert.certificate_id
            data['sender_address'] = cert.getSenderAddress()
            data['sender_proof'] = cert.sender_proof
            data['receiver_address'] = cert.getReceiverAddress()
            data['receiver_proof'] = cert.receiver_proof
            data['description'] = cert.description
            int_time = cert.create_time
            data['create_time'] = time.strftime('%A %b %d %Y %H:%M:%S GMT%Z',
                                                time.localtime(int_time))

            output.append(data)

        return output


    # Meta class to configure options
    # https://docs.djangoproject.com/en/1.11/ref/models/options/
    class Meta:
        managed = True
