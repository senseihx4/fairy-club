from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, globalmail, MailReply


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'user_type', 'is_staff', 'is_active', 'is_verified')
    list_filter = ('user_type', 'is_staff', 'is_active', 'is_verified')
    search_fields = ('email', 'username')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'child_name', 'child_age', 'profile_picture')}),
        ('Membership', {'fields': ('user_type', 'court_type', 'membership_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_verified', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )


@admin.register(globalmail)
class GlobalMailAdmin(admin.ModelAdmin):
    list_display = ('mailtitel', 'created_at')
    search_fields = ('mailtitel', 'mailbody')
    ordering = ('-created_at',)


@admin.register(MailReply)
class MailReplyAdmin(admin.ModelAdmin):
    list_display = ('mail', 'user', 'created_at')
    search_fields = ('reply_content', 'user__email', 'mail__mailtitel')
    ordering = ('-created_at',)


