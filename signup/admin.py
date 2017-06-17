from django.contrib import admin
from .models import signup

class signupadmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp"]
    class Meta:
        model = signup


admin.site.register(signup, signupadmin)

