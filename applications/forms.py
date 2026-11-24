
from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            'company_name',
            'job_title',
            'job_location',
            'job_type',
            'salary',
            'application_date',
            'status',
            'job_description',
            'job_link',
        ]

        widgets = {
            'application_date': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'job_description': forms.Textarea(
                attrs={'rows': 4}
            ),
        }
