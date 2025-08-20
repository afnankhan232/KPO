from django.db import models


class BPO(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=100)
	client = models.CharField(max_length=100)
	status = models.CharField(max_length=50)
	start_date = models.DateField()
	end_date = models.DateField(null=True, blank=True)
	bpo = models.ForeignKey(BPO, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=100)
	members = models.PositiveIntegerField()
	project = models.ForeignKey(Project, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class KPI(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
	bpo = models.ForeignKey(BPO, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=100)
	value = models.FloatField()
	target = models.FloatField()

	def __str__(self):
		if self.project:
			return f"{self.name} ({self.project.name})"
		elif self.bpo:
			return f"{self.name} ({self.bpo.name})"
		return self.name
