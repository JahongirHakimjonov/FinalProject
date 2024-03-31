from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.task2.models import Vacancy
from apps.task2.api_endpoints.Vacancy.VacancyFilter.serializers import VacancyFilterSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class VacancyFilterAPIView(APIView):
    serializer_class = VacancyFilterSerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('salary_from', openapi.IN_QUERY, description="Minimum salary", type=openapi.TYPE_INTEGER),
        openapi.Parameter('salary_to', openapi.IN_QUERY, description="Maximum salary", type=openapi.TYPE_INTEGER),
        openapi.Parameter('salary', openapi.IN_QUERY, description="Exact salary", type=openapi.TYPE_INTEGER),
    ])
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=VacancyFilterSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Vacancy.objects.all()
        salary_from = self.request.query_params.get("salary_from")
        salary_to = self.request.query_params.get("salary_to")
        salary = self.request.query_params.get("salary")

        if salary_from is not None:
            queryset = queryset.filter(salary__gte=salary_from)
        if salary_to is not None:
            queryset = queryset.filter(salary__lte=salary_to)
        if salary is not None:
            queryset = queryset.filter(salary__exact=salary)

        return queryset
