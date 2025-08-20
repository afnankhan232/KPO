import csv
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Project, Team, KPI, BPO
from .forms import BPOForm, ProjectForm, TeamForm, KPIForm
from django.contrib import messages

def bpos_list(request):
    if request.GET.get('export') == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="bpos.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Description'])
        for bpo in BPO.objects.all():
            writer.writerow([bpo.name, bpo.description])
        return response
    query = request.GET.get('q', '')
    bpos = BPO.objects.all()
    if query:
        bpos = bpos.filter(name__icontains=query)
    if request.method == 'POST':
        form = BPOForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'BPO added successfully!')
    else:
        form = BPOForm()
    return render(request, 'dashboard/bpos_list.html', {'bpos': bpos, 'form': form, 'query': query})

def bpo_detail(request, pk):
    bpo = get_object_or_404(BPO, pk=pk)
    projects = Project.objects.filter(bpo=bpo)
    return render(request, 'dashboard/bpo_detail.html', {'bpo': bpo, 'projects': projects})

def bpo_edit(request, pk):
    bpo = get_object_or_404(BPO, pk=pk)
    if request.method == 'POST':
        form = BPOForm(request.POST, instance=bpo)
        if form.is_valid():
            form.save()
            messages.success(request, 'BPO updated successfully!')
            return render(request, 'dashboard/bpo_detail.html', {'bpo': bpo, 'projects': Project.objects.filter(bpo=bpo)})
    else:
        form = BPOForm(instance=bpo)
    return render(request, 'dashboard/bpo_edit.html', {'form': form, 'bpo': bpo})

def bpo_delete(request, pk):
    bpo = get_object_or_404(BPO, pk=pk)
    if request.method == 'POST':
        bpo.delete()
        messages.success(request, 'BPO deleted successfully!')
        return bpos_list(request)
    return render(request, 'dashboard/bpo_delete.html', {'bpo': bpo})

def dashboard_view(request):
    projects = Project.objects.all()
    teams = Team.objects.all()
    kpis = KPI.objects.all()
    if kpis:
        avg_kpi = sum(k.value for k in kpis) / len(kpis)
    else:
        avg_kpi = None
    return render(request, 'dashboard/dashboard.html', {
        'projects': projects,
        'teams': teams,
        'kpis': kpis,
        'avg_kpi': avg_kpi,
    })

def projects_list(request):
    if request.GET.get('export') == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="projects.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Client', 'Status', 'Start Date', 'End Date', 'BPO'])
        for project in Project.objects.all():
            writer.writerow([project.name, project.client, project.status, project.start_date, project.end_date, project.bpo.name if project.bpo else ''])
        return response
    query = request.GET.get('q', '')
    projects = Project.objects.all()
    if query:
        projects = projects.filter(name__icontains=query)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully!')
    else:
        form = ProjectForm()
    return render(request, 'dashboard/projects_list.html', {'projects': projects, 'form': form, 'query': query})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'dashboard/project_detail.html', {'project': project})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return render(request, 'dashboard/project_detail.html', {'project': project})
    else:
        form = ProjectForm(instance=project)
    return render(request, 'dashboard/project_edit.html', {'form': form, 'project': project})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return projects_list(request)
    return render(request, 'dashboard/project_delete.html', {'project': project})

def teams_list(request):
    if request.GET.get('export') == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="teams.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Members', 'Project'])
        for team in Team.objects.all():
            writer.writerow([team.name, team.members, team.project.name])
        return response
    query = request.GET.get('q', '')
    teams = Team.objects.all()
    if query:
        teams = teams.filter(name__icontains=query)
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team added successfully!')
    else:
        form = TeamForm()
    return render(request, 'dashboard/teams_list.html', {'teams': teams, 'form': form, 'query': query})

def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'dashboard/team_detail.html', {'team': team})

def team_edit(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team updated successfully!')
            return render(request, 'dashboard/team_detail.html', {'team': team})
    else:
        form = TeamForm(instance=team)
    return render(request, 'dashboard/team_edit.html', {'form': form, 'team': team})

def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        messages.success(request, 'Team deleted successfully!')
        return teams_list(request)
    return render(request, 'dashboard/team_delete.html', {'team': team})

def kpis_list(request):
    if request.GET.get('export') == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="kpis.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Value', 'Target', 'Project', 'BPO'])
        for kpi in KPI.objects.all():
            writer.writerow([kpi.name, kpi.value, kpi.target, kpi.project.name if kpi.project else '', kpi.bpo.name if kpi.bpo else ''])
        return response
    query = request.GET.get('q', '')
    kpis = KPI.objects.all()
    if query:
        kpis = kpis.filter(name__icontains=query)
    if request.method == 'POST':
        form = KPIForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'KPI added successfully!')
    else:
        form = KPIForm()
    return render(request, 'dashboard/kpis_list.html', {'kpis': kpis, 'form': form, 'query': query})

def kpi_detail(request, pk):
    kpi = get_object_or_404(KPI, pk=pk)
    return render(request, 'dashboard/kpi_detail.html', {'kpi': kpi})

def kpi_edit(request, pk):
    kpi = get_object_or_404(KPI, pk=pk)
    if request.method == 'POST':
        form = KPIForm(request.POST, instance=kpi)
        if form.is_valid():
            form.save()
            messages.success(request, 'KPI updated successfully!')
            return render(request, 'dashboard/kpi_detail.html', {'kpi': kpi})
    else:
        form = KPIForm(instance=kpi)
    return render(request, 'dashboard/kpi_edit.html', {'form': form, 'kpi': kpi})

def kpi_delete(request, pk):
    kpi = get_object_or_404(KPI, pk=pk)
    if request.method == 'POST':
        kpi.delete()
        messages.success(request, 'KPI deleted successfully!')
        return kpis_list(request)
    return render(request, 'dashboard/kpi_delete.html', {'kpi': kpi})

def about(request):
    return render(request, 'dashboard/about.html')
