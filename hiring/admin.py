from pickletools import markobject
from django.contrib import admin
from .models import Tags, Hiring

class AdminHiring(admin.ModelAdmin):
    list_display = (
        'id',
        'company',
        'title',
        'min_salary', 
        'max_salary',
        'currency',
        'occupation',
        'first_phone_number',
        'second_phone_number',
    )
    list_display_links = ('id', 'company', 'title',)
    list_filter = ('company',)
    search_field = ('id', 'company', 'title', )


admin.site.register(Hiring, AdminHiring)


class AdminTags(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title')

admin.site.register(Tags, AdminTags)

# Register your models here.
