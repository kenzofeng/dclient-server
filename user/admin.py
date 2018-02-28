from django.contrib import admin

from .models import aws, log, dockerfile


class LogAdmin(admin.ModelAdmin):
    list_display = ('ip', 'content')


class dockerfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')


admin.site.register(aws)
admin.site.register(log, LogAdmin)
admin.site.register(dockerfile, dockerfileAdmin)
