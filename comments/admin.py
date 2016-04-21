from django.contrib import admin
from .models import Comment
# Register your models here.

#Use a decorator to register custom admin to admin.site

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):		
	model = Comment
	list_display = ["comment","phone","company_id"]
	list_filter = ["company_id"]

