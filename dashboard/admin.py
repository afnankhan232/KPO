from django.contrib import admin
from .models import Project, Team, KPI, BPO

admin.site.register(BPO)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(KPI)
