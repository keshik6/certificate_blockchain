import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ethcert_blockchain.settings')

import django
django.setup()

#Faker script
import random
from main_web_portal.models import UserProfile
from faker import Faker
from django.contrib.auth.models import User

fakeGenerator = Faker()

def createUser():
    fake_name = fakeGenerator.user_name()
    passwordFake = "Test@SUTDgergsd"
    emailFake = fakeGenerator.free_email()
    newUser = User.objects.get_or_create(username=fake_name,password=passwordFake,email=emailFake)
    print(newUser)
    return newUser

def populateUserProfile(N = 5):
    for i in range(N):
        uProfile = UserProfile.objects.get_or_create(user=createUser()[0])

if __name__ == '__main__':
    print("populating")
    populateUserProfile()
    print("Completed running population script")
