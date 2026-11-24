
from django.db import models


class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('APPLIED', 'Applied'),
        ('ASSESSMENT', 'Assessment'),
        ('INTERVIEW', 'Interview'),
        ('SELECTED', 'Selected'),
        ('REJECTED', 'Rejected'),
    ]

    company_name = models.CharField(max_length=150)

    job_title = models.CharField(max_length=150)

    job_location = models.CharField(max_length=150)

    job_type = models.CharField(max_length=50)

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    application_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='APPLIED'
    )

    job_description = models.TextField(blank=True)

    job_link = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

# Create your models here.
