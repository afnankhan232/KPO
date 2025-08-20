from django import forms
from .models import BPO, Project, Team, KPI

class BPOForm(forms.ModelForm):
    class Meta:
        model = BPO
        fields = ['name', 'description']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'client', 'status', 'start_date', 'end_date', 'bpo']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'members', 'project']

class KPIForm(forms.ModelForm):
    class Meta:
        model = KPI
        fields = ['name', 'value', 'target', 'project', 'bpo']
