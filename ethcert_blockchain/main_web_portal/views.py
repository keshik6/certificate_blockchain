from main_web_portal.forms import UserForm, UserProfileInfoForm
from django.core.mail import send_mail, EmailMessage

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from faker import Faker
from main_web_portal.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "main_web_portal/index.html")


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return render(request, "main_web_portal/index.html")


def register(request):
    registered = False

    if request.method == 'POST':
        password = request.POST.get('password')
        confirmPassword = request.POST.get('passwordConfirm')
        if (password != confirmPassword):
            messages.error(request, 'Passwords do not match')
            user_form = UserForm()
            return render(request,'main_web_portal/registration.html',
                                  {'user_form':user_form,
                                   'registered':registered})

        # Get info from "both" forms
        # It appears as one form to the user on the .html page

        user_form = UserForm(data=request.POST, label_suffix='')
        # print(user_form.cleaned_data)

        #print(user_form.cleaned_data)
        # Check to see both forms are valid
        if user_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = UserProfile()

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            # if 'profile_pic' in request.FILES:
            #     print('found it')
            #     # If yes, then grab it from the POST form reply
            #     profile.profile_pic = request.FILES['profile_pic']
            profile.profile_pic = "profile_pics/default-profile-pic.jpg"

            fakeGenerator = Faker()
            vercode1 = fakeGenerator.bban()
            print("Profile auth code 1 is : " + vercode1)

            profile.setVerificationCode1(vercode1)
            print('Successfully registered')
            print("get profiles verification code " + profile.getVerificationCode1())

            profile.save()
            # Registration Successful!
            registered = True

            email = EmailMessage(
                            'ETHCERT Verification Code',
                            'Hi ' + str(profile.user.username) + ',\nThank you for registering.\nYour verification code is ' +
                            str(vercode1) + "\nLogin to ETHCERT Dashboard to continue.\n\nBest Regards,\nETHCERT Team",
                            'ETHCERT TEAM' +'<sender@gmail.com>',
                            [profile.user.email],
                        )

            email.send()
            print("Email sent Successfully")
            return render(request,'main_web_portal/registration.html',
                                  {'username':profile.user.username, 'email':profile.user.email,
                                   'registered':registered})

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)


    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        #profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.

    return render(request,'main_web_portal/registration.html',
                          {'user_form':user_form,
                           'registered':registered})



def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        User = authenticate(username=username, password=password)

        # If we have a user
        if User:
            # Check it the account is active
            if User.is_active:
                # Log the user in.
                login(request, User)
                # Send the user back to some page.
                # In this case their homepage.
                context = getUserContext(User)
                return render(request, 'main_web_portal/dashBoard.html', context)
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            # This seems to be a vulnerability
            print("Someone tried to login and failed.")
            # print("They used username: {} and password: {}".format(username,password))
            messages.error(request, 'Username or Password not correct')
            return render(request, 'main_web_portal/login.html', {})

    else:
        # Nothing has been provided for username or password.
        return render(request, 'main_web_portal/login.html', {})


@login_required
def transaction(request):
    return render(request, "main_web_portal/transaction.html")


def team(request):
    return render(request, "main_web_portal/ourTeam.html")


def view_cert(request):
    if request.method == 'POST':
        # handle empty fields in javascript
        search_query = request.POST.get('searchtext')
        print(representsInt(search_query))
        if (representsInt(search_query)):
            print("clicked, searching {}".format(search_query))
            return render(request, 'main_web_portal/viewCertificate.html',
                          {"certID": search_query})

        else:
            print("clicked, searching profile{}".format(search_query))
            userObject= User.objects.filter(username = search_query)
            print(userObject.count())
            if (userObject.count() != 0):
                print("user found: " + str(userObject[0]))
                profile = UserProfile.objects.filter(user = userObject[0])[0]
                print("hello" + str(profile))
                context = getUserContext(userObject[0])
                context['NA'] = False
                return render(request,'main_web_portal/publicProfile.html',context)

            else:
                context = dict()
                context['NA'] = True
                return render(request,'main_web_portal/publicProfile.html',context)

@login_required
def dashboard(request):
    User = request.user;
    context = getUserContext(User)

    if request.method == 'POST':
        profile = UserProfile.objects.filter(user = User)[0]
        code = request.POST.get('ethAddrInput')
        print(code)
        if (code != None):
            profile.setEthAddress(code)

        profile.save()
        User.save()
        print("done")

    return render(request, 'main_web_portal/dashBoard.html', context)


def handler404(request):
    return render(request, 'main_web_portal/404.html', status= 404)


def handler500(request):
    return render(request, 'main_web_portal/500.html', status= 500)


def getUserContext(User):
    profileList = UserProfile.objects.filter(user = User)
    profile = profileList[0]
    #print(profile.isAuthenticated1())
    picForm = UserProfileInfoForm()
    context = {'username' : profile.user.username,
    'isAuth1': profile.isAuthenticated1(),
    'isAuth2': profile.isAuthenticated2(),
    'email': profile.user.email,
    'profile_pic': profile.profile_pic.url,
    'ethAddress': profile.getEthAddress(),
    'picForm':picForm,
    'address':profile.getAddress(),
    'url': profile.getUrl()}
    return context;


@login_required
def authForm1(request):
    if request.method == 'POST':
        User = request.user
        profile = UserProfile.objects.filter(user = User)[0]
        code = request.POST.get('authCode1')
        print(code)
        print(profile.getVerificationCode1())
        if (code == profile.getVerificationCode1()):
            profile.setAuthenticated1()
            profile.save()
            User.save()
            return dashboard(request)
        else:
            messages.error(request, 'Email Verification code incorrect')
            return render (request,'main_web_portal/authlvl1.html',{})
    else:
        return render (request,'main_web_portal/authlvl1.html',{})


@login_required
def authForm2(request):
    if request.method == 'POST':
        User = request.user
        profile = UserProfile.objects.filter(user = User)[0]
        code = request.POST.get('authCode2')
        if (code == profile.getVerificationCode2()):
            profile.setAuthenticated2()
            profile.save()
            User.save()
            return dashboard(request)
        else:
            messages.error(request, 'Postal Verification code incorrect')
            return render (request,'main_web_portal/authlvl2.html',{})
    else:
        return render (request,'main_web_portal/authlvl2.html',{})

@login_required
def personalDetails(request):
    if request.method == 'POST':
        User = request.user
        profile = UserProfile.objects.filter(user = User)[0]

        address = request.POST.get('address')
        websiteUrl = request.POST.get('websiteUrl')

        profile.setAddress(address)
        profile.setUrl(websiteUrl)
        profile.save()
        User.save()
        return dashboard(request)

    return render (request,'main_web_portal/personalDetails.html',{})


@login_required
def updateProfilePic(request):
    if request.method == 'POST':
        picForm = UserProfileInfoForm(data = request.POST)

        User = request.user
        profile = UserProfile.objects.filter(user = User)[0]

        if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

                # Now save model
                profile.save()
                User.save()

    return dashboard(request)

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
