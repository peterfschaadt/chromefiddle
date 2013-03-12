from django.core import serializers
from flags import models

"""
Serialize all Flags to JSON file.
"""

# Retrieve and serialize all Flags from database
data = serializers.serialize('json', modes.Flag.objects.all())
# Create JSON file to store Flags
output = open('flags.json', 'w')
# Write and Close
output.write(data)
output.close()
