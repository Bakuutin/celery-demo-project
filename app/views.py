from typing import cast

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .tasks import calculate_report_data
from .utils import enqueue_on_commit
from .models import Report
from .serializers import ReportSerializer


class RootView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'ok': True})



class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer: ReportSerializer):  # type: ignore[override]
        super().perform_create(serializer)
        report = cast(Report, serializer.instance)
        enqueue_on_commit(calculate_report_data, report.id)
