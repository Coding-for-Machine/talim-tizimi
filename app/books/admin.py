from django.contrib import admin

# Register your models here.
from django.contrib.admin.models import ADDITION, LogEntry
from .models import Books
from django.utils.html import format_html

LogEntry.objects.filter(action_flag=ADDITION)
class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = "pub_date"

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', "colored_name", 'created_at', 'updated_at']
    list_editable = ["title"]
    list_filter = ["id", "body"]
    list_per_page = 2
    list_display_links =["body"]


    @admin.action(description='Enable selected releases', permissions=['change'])
    def enable(self, request, queryset):
        queryset.update()
        self.message_user(request, f'{queryset.count()} releases enabled.')
        self.message_user(request, f'{queryset.count()} releases enabled.')
        self.message_user(request, 'Nimadir xato', level='ERROR')
        self.message_user(request, "O'zgartirildi", level='WARNING')
    # prepopulated_fields 
