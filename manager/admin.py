from django.contrib import admin
from .models import ExtendedAuthUser

@admin.register(ExtendedAuthUser)
class ExtendedAuthUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'is_client', 'role', 'created_on')  # Customize the displayed fields in the admin list view
    search_fields = ('user__username', 'user__email', 'phone')  # Add fields you want to search by
    list_filter = ('is_client', 'role', 'gender')  # Add filters for quick navigation
    # Add more customization as needed

    fieldsets = (
        ('User Information', {
            'fields': ('user', 'phone', 'is_client', 'role', 'created_on')
        }),
        ('Profile Information', {
            'fields': ('initials', 'bgcolor', 'followers', 'following', 'upvotes', 'downvotes', 'articles',
                    'company', 'profile_pic', 'bio', 'nickname', 'facebook', 'twitter', 'instagram', 'github',
                    'shipping_address', 'gender', 'birthday')
        }),
    )


    readonly_fields = ('created_on',) 
