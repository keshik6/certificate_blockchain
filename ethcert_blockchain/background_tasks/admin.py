from django.contrib import admin
from background_tasks.models import Certificate

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_id',
                    'receiver_address',
                    'receiver_proof',
                    'sender_address',
                    'sender_proof',
                    'description',
                    'create_time',
                   )

    search_fields = ('certificate_id',
                     'receiver_address',
                     'sender_address',
                    )

    list_per_page = 50

# Register your models here.
admin.site.register(Certificate, CertificateAdmin)
