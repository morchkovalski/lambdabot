from django.contrib import admin

from discordbot.models import DiscordServer, DiscordCommand, DiscordServerUser, DiscordUser, \
    DiscordServerUserPermission, DiscordServerPermission


class DiscordServerPermissionAdmin(admin.ModelAdmin):
    list_display = ('server', 'permission', 'allow')
    search_fields = ('permission', 'server__server_id', 'server__name', 'server__context__short_name')
    ordering = ('server', 'permission')

admin.site.register(DiscordServerPermission, DiscordServerPermissionAdmin)


class DiscordServerPermissionInline(admin.TabularInline):
    model = DiscordServerPermission
    extra = 0


class DiscordServerAdmin(admin.ModelAdmin):
    list_display = ('server_id', 'name', 'context')
    ordering = ('name', 'server_id')
    search_fields = ('server_id', 'name', 'context__short_name')
    inlines = [DiscordServerPermissionInline]

admin.site.register(DiscordServer, DiscordServerAdmin)


class DiscordCommandAdmin(admin.ModelAdmin):
    list_display = ('cmd', 'help', 'message', 'hidden', 'restricted')
    ordering = ('cmd',)
    search_fields = ('cmd',)


admin.site.register(DiscordCommand, DiscordCommandAdmin)


class DiscordServerUserInline(admin.TabularInline):
    model = DiscordServerUser
    extra = 0


class DiscordUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id')
    search_fields = ('user_id', 'name')
    ordering = ('name',)
    inlines = [DiscordServerUserInline]

admin.site.register(DiscordUser, DiscordUserAdmin)


class DiscordServerUserPermissionAdmin(admin.ModelAdmin):
    list_display = ('server_user', 'permission', 'allow')
    search_fields = ('permission', 'server_user__nickname', 'server_user__user__user_id', 'server_user__user__name',
                     'server_user__server__name')
    ordering = ('server_user', 'permission')

admin.site.register(DiscordServerUserPermission, DiscordServerUserPermissionAdmin)


class DiscordServerUserPermissionInline(admin.TabularInline):
    model = DiscordServerUserPermission
    extra = 0


class DiscordServerUserAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'user', 'server')
    search_fields = ('nickname', 'user__user_id', 'user__name', 'server__name')
    ordering = ('server', 'nickname')
    inlines = [DiscordServerUserPermissionInline]

admin.site.register(DiscordServerUser, DiscordServerUserAdmin)