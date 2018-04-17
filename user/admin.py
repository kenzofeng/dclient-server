from django.contrib import admin

from .models import aws, log, dockerfile, Access


class LogAdmin(admin.ModelAdmin):
    list_display = ('ip', 'content')


class dockerfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')


class AccessAdmin(admin.ModelAdmin):
    list_display = ['docker_registry']


admin.site.register(Access, AccessAdmin)
admin.site.register(log, LogAdmin)
admin.site.register(dockerfile, dockerfileAdmin)
