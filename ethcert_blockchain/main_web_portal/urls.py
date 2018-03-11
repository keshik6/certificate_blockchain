from django.conf.urls import url
from main_web_portal import views

# SET THE NAMESPACE!
app_name = 'main_web_portal'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^user_logout/$',views.user_logout,name='user_logout'),
    url(r'^send_cert/$',views.send_cert,name='send_cert'),
]
