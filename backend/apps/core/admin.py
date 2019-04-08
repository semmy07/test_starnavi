from django.contrib import admin

from .models import User, Post


class UserAdmin(admin.ModelAdmin):
    fields = (
        'password',
        'username',
        'first_name',
        'last_name',
        'email',
        'avatar',
        'city',
        'country',
        'phone',
    )

    search_fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'phone',
    )

    list_filter = (
        'city',
        'country',
        'is_staff',
    )

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'city',
        'country',
        'phone',
        'is_staff',
    )


admin.site.register(User, UserAdmin)
admin.site.register(Post)
