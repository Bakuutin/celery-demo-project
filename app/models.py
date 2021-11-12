from django.db import models

import uuid

class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)
    date_requested = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, editable=False)
