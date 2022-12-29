from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from bookstore_account.models import user_profile

admin.site.unregister(Group)
class accountInline(admin.StackedInline):
  model = user_profile
  can_delete = False
  verbose_name_plural = "Accounts"

class customUserAdmin(UserAdmin):
  inlines = (accountInline, )

admin.site.unregister(User)
admin.site.register(User, customUserAdmin)
# admin.site.register(user_profile)