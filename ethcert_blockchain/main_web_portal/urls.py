from main_web_portal import views
from django.conf.urls import include, url


# SET THE NAMESPACE!
app_name = 'main_web_portal'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^user_logout/$',views.user_logout,name='user_logout'),
    url(r'^transaction/$',views.transaction,name='transaction'),
    url(r'^team/$',views.team,name='team'),
    url(r'^viewcert/$',views.view_cert,name='view_cert'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^verify1/$',views.authForm1,name="verify1"),
    url(r'^verify2/$',views.authForm2,name="verify2"),
    url('updatePic/$',views.updateProfilePic, name="updatePic"),
]
