from django.contrib import admin
from .models import Emplooyes , XUsers , HRs , Vactions
# Register your models here.
admin.site.register(XUsers)
admin.site.register(Emplooyes)
admin.site.register(HRs)
admin.site.register(Vactions)