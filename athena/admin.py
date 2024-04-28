from django.contrib import admin
from .models import *

# Register your models here.

class UserTaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'completion', 'grade')

class UserSubjectAdmin(admin.ModelAdmin):  
    list_display = ('subject', 'user', 'completion', 'grade')

class TaskAdmin(admin.ModelAdmin):  
    list_display = ('name', 'subject')

admin.site.register(Task, TaskAdmin)
admin.site.register(Subject)
admin.site.register(UserSubject, UserSubjectAdmin)
admin.site.register(UserTask, UserTaskAdmin)
