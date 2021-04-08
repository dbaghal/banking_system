from django.contrib import admin
from accounts.models import account
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.
admin.site.register(account,SimpleHistoryAdmin)
