from django.db import models


class Platforms(models.Model):
    """
    Supported operating systems.
    """
    OS_SUPPORT = (
        ('Mac OS X', 'Mac OS X'),
        ('Windows', 'Windows'),
        ('Linux', 'Linux'),
        ('Chrome OS', 'Chrome OS'),
        ('Android', 'Android')
    )
    support = models.CharField(max_length=15, choices=OS_SUPPORT)


class Flag(models.Model):
    """
    Chrome experimental flag.
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    # Operating system support
    compatibility = models.ManyToManyField(Platforms)

    # Timestamps
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # Print name of flag
    def __unicode__(self):
        return self.name

    def __str__(self):
        return str(self.name)
