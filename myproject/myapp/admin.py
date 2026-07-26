from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'grade_level', 'is_active', 'enrollment_date')
    list_filter = ('grade_level', 'is_active', 'enrollment_date')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at', 'enrollment_date')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone', 'date_of_birth')
        }),
        ('Academic Information', {
            'fields': ('grade_level', 'enrollment_date')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
