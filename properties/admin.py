from django.contrib import admin
from .models import Property, Tenant, Lease, Unit

admin.site.register(Property)
admin.site.register(Tenant)
admin.site.register(Lease)
admin.site.register(Unit)

