from django.contrib import admin
from userControl import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.site_title="NBA-data后台系统管理"
admin.site.site_header="NBA-data后台系统管理"
admin.site.index_title="管理员欢迎您"

admin.site.register(models.Teams)
admin.site.register(models.Games)
admin.site.register(models.League)
admin.site.register(models.UserInfo)
admin.site.register(models.Pos)

class GamesResource(resources.ModelResource):

    class Meta:
        model = models.Games


class GamesAdmin(ImportExportModelAdmin):
    resource_class = GamesResource



# Register your models here.
