from django.contrib import admin

from apps.task1.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "is_deleted"]
    search_fields = ["username", "email"]
    list_filter = ["is_deleted"]
    actions = ["delete_users"]

    def delete_users(self, request, queryset):
        queryset.update(is_deleted=True)
        self.message_user(request, "Selected users have been deleted")

    delete_users.short_description = "Delete selected users"
