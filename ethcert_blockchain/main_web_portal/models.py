from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

    def getVerificationCode1(self):
        return 1;

    def getVerificationCode2(self):
        return self.verification_code_lvl_2

    def getAddress(self):
        return self.address

    def setAddress(self,address):
        self.address = address

    def setUrl(self,url):
        self.url = url

    def getUrl(self):
        return self.url
