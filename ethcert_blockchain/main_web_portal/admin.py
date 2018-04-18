from django.contrib import admin
from main_web_portal.models import UserProfile,User

class UserAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'verification_code_lvl_1',
                    'verification_code_lvl_2',
                    'address',
                    'url',
                    'auth1',
                    'auth2',
                    'eth_address',
                    'received_cert',
                    'sent_cert',
                   )

    def received_cert(self, obj):
        return "{}".format(obj.ReceivedCertificates.certificate_id)

    def sent_cert(self, obj):
        return "{}".format(obj.SentCertificates.certificate_id)

    received_cert.short_description = "received"
    sent_cert.short_description = "sent"




# Register your models here.
admin.site.register(UserProfile, UserAdmin)
