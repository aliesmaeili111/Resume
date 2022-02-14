from django.contrib import admin
from . models import Article,Contacts
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
   list_display = ('age','email','status')
   list_filter = ('email','status')
   search_fields = ('email','status')


admin.site.register(Article,ArticleAdmin)
admin.site.register(Contacts)