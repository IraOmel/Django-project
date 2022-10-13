from django.contrib import admin
from .models import App, User, Projects

admin.site.register(App)
admin.site.register(User)
admin.site.register(Projects)