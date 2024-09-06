from django.contrib import admin
from .models import Person, Contact

class PersonAdmin(admin.ModelAdmin):
    list_display = ("username", "fullname", "email", "phone")

admin.site.register(Person, PersonAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("fname","email","phone","message")

admin.site.register(Contact, ContactAdmin)
