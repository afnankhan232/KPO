from django.db import migrations

def create_dummy_data(apps, schema_editor):
    BPO = apps.get_model('dashboard', 'BPO')
    Project = apps.get_model('dashboard', 'Project')
    Team = apps.get_model('dashboard', 'Team')
    KPI = apps.get_model('dashboard', 'KPI')

    bpo1 = BPO.objects.create(name='Acme Outsourcing', description='Handles finance and HR processes.')
    bpo2 = BPO.objects.create(name='Globex Solutions', description='Customer support and IT services.')

    p1 = Project.objects.create(name='Project Alpha', client='Client A', status='Active', start_date='2025-01-01', end_date=None, bpo=bpo1)
    p2 = Project.objects.create(name='Project Beta', client='Client B', status='Completed', start_date='2024-06-01', end_date='2025-06-01', bpo=bpo2)
    p3 = Project.objects.create(name='Project Gamma', client='Client C', status='On Hold', start_date='2025-03-15', end_date=None, bpo=bpo1)

    t1 = Team.objects.create(name='Alpha Team', members=5, project=p1)
    t2 = Team.objects.create(name='Beta Team', members=3, project=p2)
    t3 = Team.objects.create(name='Gamma Team', members=4, project=p3)

    KPI.objects.create(name='Customer Satisfaction', value=85.5, target=90, project=p1)
    KPI.objects.create(name='Process Efficiency', value=78.2, target=80, project=p2)
    KPI.objects.create(name='Cost Reduction', value=12.0, target=15, project=p3)
    KPI.objects.create(name='BPO Revenue', value=100000, target=120000, bpo=bpo1)
    KPI.objects.create(name='BPO Tickets Closed', value=500, target=600, bpo=bpo2)

class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0003_kpi_bpo_alter_kpi_project'),
    ]

    operations = [
        migrations.RunPython(create_dummy_data),
    ]
