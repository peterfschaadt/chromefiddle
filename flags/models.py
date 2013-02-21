from django.db import models


class Flag(models.Model):
    """
    Chrome experimental flag.
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    # Operating system compatibility
    is_mac = models.BooleanField()
    is_windows = models.BooleanField()
    is_linux = models.BooleanField()
    is_chrome_os = models.BooleanField()
    is_android = models.BooleanField()

    # Timestamps
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # Print name of flag
    def __unicode__(self):
        return self.name

    def __str__(self):
        return str(self.name)
