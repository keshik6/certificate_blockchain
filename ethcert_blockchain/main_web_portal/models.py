from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class UserProfile(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)

    # Add any additional attributes
    #transaction_list = ArrayField(models.CharField(max_length=64), default=list)

    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


class Transaction(models.Model):
    awarding_organization = models.ForeignKey(UserProfile)
    transaction_hash = models.CharField(max_length=64)
    access_token = models.CharField(max_length=64)
    transaction_time = models.DateTimeField(auto_now=True)
    transaction_amount = models.FloatField()
    receiver = models.CharField(max_length=64)
    validity = models.DurationField()

    #This is the actual certificate
    certificate = models.ImageField(upload_to='certificates',blank=True)

    def __str__(self):
        return self.transaction_hash
