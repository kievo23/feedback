from django.contrib import admin
from .models import Company
# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	class Meta:		
		model = Company
	list_display = ["name","tag_line",]
	list_filter = ["name",]
