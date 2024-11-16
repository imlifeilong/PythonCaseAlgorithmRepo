from django.contrib import admin
from app.models import Book


class BookAdmin(admin.ModelAdmin):
    # 显示列
    list_display = ('title', 'author', 'create_time')
    # 搜索
    search_fields = ('title', 'author')
    # 过滤
    list_filter = ('author',)

    date_hierarchy = 'online_time'

    ordering = ('-create_time',)

    fields = ('title', 'author', 'price')

    exclude = ('translator',)

    readonly_fields = ('create_time',)

    def mark_as_sold(self, request, queryset):
        queryset.update(sold=True)

    mark_as_sold.short_description = "批量标记为已售"

    actions = [mark_as_sold]


admin.site.register(Book, BookAdmin)
