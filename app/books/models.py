from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class TimeMixin(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

# Create your models here.

class Books(TimeMixin):
    title = models.CharField(max_length=250, db_index=True)
    body = models.TextField(db_index=True)
    images = models.ImageField(upload_to="booksimage/")
    books_pdf = models.FileField(upload_to="bookspdf/")

    class Meta:
        ordering = ["-updated_at"]
        # app_label = "Kitoblar"
        db_table_comment = "Kitoblar-javoni"
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    @admin.display
    def colored_name(self):
        return format_html(
                '<span style="color: red;">{} {}</span>',
                self.title,
                self.created_at,
            )

