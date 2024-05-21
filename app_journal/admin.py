from django.contrib import admin

from .models import Category, Publication, Paper, Contact, Requirements, FAQ

admin.site.register(Category)
admin.site.register(Publication)
admin.site.register(Paper)
admin.site.register(Contact)
admin.site.register(Requirements)
admin.site.register(FAQ)
