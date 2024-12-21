from django.contrib import admin
from . models import Room, Topic, Message, Student, school, shop, college, hotel

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list=['sno', 'sname', 'sclass', 'saddress']

class shopAdmin(admin.ModelAdmin):
    list=['department', 'stock', 'customer']

admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Student)
admin.site.register(school)
admin.site.register(shop)
admin.site.register(hotel)


admin.site.register(college)