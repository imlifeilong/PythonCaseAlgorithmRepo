from django.contrib import admin

from authxs.models import User, CommonBook, SVIPBook, VIPBook

admin.site.register(CommonBook)
admin.site.register(SVIPBook)
admin.site.register(VIPBook)
admin.site.register(User)

