from django.contrib import admin
from net_user_app.models import NetUser
from net.models import Net
# Register your models here.
admin.site.register(NetUser)
admin.site.register(Net)