from django.contrib import admin
from .models import Services,NewsLetter,ContactUs

class AdminServices(admin.ModelAdmin):
    list_display = ['title','content','status']
    list_filter = ['status']
    search_fields = ['title']
    fields = ['title']




admin.site.register(Services, AdminServices)
admin.site.register(NewsLetter)
admin.site.register(ContactUs)