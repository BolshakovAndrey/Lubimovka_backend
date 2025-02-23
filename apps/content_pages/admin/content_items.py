from django.contrib import admin

from apps.content_pages.models import Image, Link, Preamble, Quote, Text, Title, Video
from apps.core.mixins import AdminImagePreview


@admin.register(Image)
class ImageAdmin(AdminImagePreview, admin.ModelAdmin):
    list_display = (
        "id",
        "image_preview_list_page",
    )
    readonly_fields = ("image_preview_change_page",)


admin.site.register(Preamble)
admin.site.register(Link)
admin.site.register(Quote)
admin.site.register(Text)
admin.site.register(Title)
admin.site.register(Video)
