from django.db import models

# Create your models here.

class Student(models.Model):
    """
    Student model for managing student records.
    Supports CRUD operations for student information.
    """
    GRADE_CHOICES = [
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField(auto_now_add=True)
    grade_level = models.CharField(max_length=10, choices=GRADE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['-enrollment_date']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['name']),
        ]
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    def get_full_info(self):
        """Return full student information"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'date_of_birth': self.date_of_birth,
            'enrollment_date': self.enrollment_date,
            'grade_level': self.grade_level,
            'is_active': self.is_active,
        }
