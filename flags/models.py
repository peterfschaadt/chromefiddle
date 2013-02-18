from django.db import models


class Flag(models.Model):
    """
    Chrome experimental flag.
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    # Supported OS's for experimental flags
    OS_COMPATIBILITY = (
        ('Mac OS X', 'Mac OS X'),
        ('Windows', 'Windows'),
        ('Linux', 'Linux'),
        ('Chrome OS', 'Chrome OS'),
        ('Android', 'Android')
    )
    compatibility = models.CharField(max_length=10, choices=OS_COMPATIBILITY)
    # Timestamps
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # Print name of flag
    def __unicode__(self):
        return self.name

    def __str__(self):
        return str(self.name)
