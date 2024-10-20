from django.contrib import admin

from authxs.models import User, Permission, Role

admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(User)
