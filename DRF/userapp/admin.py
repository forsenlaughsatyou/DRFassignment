from django.contrib import admin
from .models import User ,Product
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserAdminModel(BaseUserAdmin):
 

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdminModel
    # that reference specific fields on auth.User.
    list_display = ('email', 'username','phone','role','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Userdetails', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('phone','role')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdminModel
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','phone','role', 'password1', 'password2'),   
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User,UserAdminModel)
admin.site.register(Product)
