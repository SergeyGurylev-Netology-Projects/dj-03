from django.contrib import admin
from phones.models import Phone


# @admin.register(Phone)
# class LoginMonitorAdmin(admin.ModelAdmin):
#     change_list_template = "admin/phone_change_list.html"
#
#     def get_urls(self):
#         urls = super(LoginMonitorAdmin, self).get_urls()
#         custom_urls = [
#             url('^import/$', self.process_import, name='process_import'),]
#         return custom_urls + urls
#

@admin.register(Phone)
class PhoneModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    # list_display = ['id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug',]
    # list_filter = ['name', 'price', 'release_date', 'lte_exists',]
