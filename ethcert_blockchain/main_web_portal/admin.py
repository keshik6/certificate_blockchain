from django.contrib import admin
from main_web_portal.models import UserProfile,User


class UserAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'auth1',
                    'auth2',
                    'address',
                    'url',
                    'eth_address',
                   )

    filter_horizontal = ('sent_certificates', 'received_certificates')

# Register your models here.
admin.site.register(UserProfile, UserAdmin)
