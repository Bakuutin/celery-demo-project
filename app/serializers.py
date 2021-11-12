from typing import Any, Dict

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'date_requested', 'date_completed', 'data', 'url']