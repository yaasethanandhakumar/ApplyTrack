
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import JobApplication
from .forms import JobApplicationForm


def job_list(request):
    search_query = request.GET.get('search', '')

    applications = JobApplication.objects.all()

    if search_query:
        applications = applications.filter(
            Q(company_name__icontains=search_query) |
            Q(job_title__icontains=search_query)
        )

    applications = applications.order_by('-application_date') 

    total_applications = applications.count()
    assessments = applications.filter(status='ASSESSMENT').count()
    interviews = applications.filter(status='INTERVIEW').count()
    offers = applications.filter(status='SELECTED').count()

    context = {
        'applications': applications,
        'total_applications': total_applications,
        'assessments': assessments,
        'interviews': interviews,
        'offers': offers,
        'search_query': search_query,
    }

    return render(request, 'applications/job_list.html', context)


def add_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()

    return render(request, 'applications/add_application.html', {'form': form})


def edit_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=application)

        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=application)

    return render(
        request,
        'applications/edit_application.html',
        {'form': form, 'application': application}
    )

def delete_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)

    if request.method == 'POST':
        application.delete()
        return redirect('job_list')

    return render(
        request,
        'applications/delete_application.html',
        {'application': application}
    )