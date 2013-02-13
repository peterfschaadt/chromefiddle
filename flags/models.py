from django.db import models

# Chrome experimental flag
class Flag(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	# Supported OS's for experimental flags
	OS_COMPATABILITY = (
		('Mac', 'Mac'),
		('Windows', 'Windows'),
		('Linux', 'Linux'),
		('Chrome OS', 'Chrome OS'),
        ('Android', 'Android')
	)
	compatability = models.CharField(max_length=10, choices=OS_COMPATABILITY)
	# Timestamps
	date_added = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	# Print name of flag
	def __unicode__(self):
		return self.name

	def __str__(self):
		return str(self.name)
