from django.shortcuts import render
from main_web_portal.forms import UserForm,UserProfileInfoForm
from django.core.mail import send_mail, EmailMessage

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"main_web_portal/index.html")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return render(request,"main_web_portal/index.html")


def register(request):
    print("trying to register yo")
    registered = False

    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST,label_suffix='')
        profile_form = UserProfileInfoForm(data=request.POST)
        #print(user_form.cleaned_data)
        email = EmailMessage(
                        'Ethcert Verification Code',
                        'content_message',
                        'sender smtp gmail' +'<sender@gmail.com>',
                        ['keshik6@gmail.com'],
                        headers = {'Reply-To': 'contact_email@gmail.com' }
                    )
        email.send()

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            #print("Profile auth code 1 is : " + str(profile.getVerificationCode1()));

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'main_web_portal/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return render(request, 'main_web_portal/dashBoard.html', {})
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            # This seems to be a vulnerability
            print("Someone tried to login and failed.")
            #print("They used username: {} and password: {}".format(username,password))
            messages.error(request,'Username or Password not correct')
            return render(request, 'main_web_portal/login.html', {})

    else:
        #Nothing has been provided for username or password.
        return render(request, 'main_web_portal/login.html', {})

@login_required
def transaction(request):
    return render(request,"main_web_portal/transaction.html")


def team(request):
    return render(request,"main_web_portal/ourTeam.html")

def view_cert(request):
    if request.method == 'POST':
        # handle empty fields in javascript
        search_query = request.POST.get('searchtext')
        print("clicked, searching {}".format(search_query))
        return render(request, 'main_web_portal/viewCertificate.html', {"certID": search_query})

def dashboard(request):
    return render(request,'main_web_portal/dashBoard.html',{})
