from django.contrib import admin
from testapp.models import Tips

# Register your models here.

@admin.register(Tips)
class TipsAdmin(admin.ModelAdmin):
    list_display = ('total_bill','sex','smoker','day','time','size','tip')
