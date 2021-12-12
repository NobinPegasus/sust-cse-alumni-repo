from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile
from .models import CustomUser



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    list_filter = ('user', )
    list_per_page = 20

admin.site.register(CustomUser)
admin.site.register(Profile, ProfileAdmin)

#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ('email', 'is_staff', 'is_active',)
#     list_filter = ('email', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
