from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from .models import University, Course, UniversityCourse
from .serializers import UniversitySerializer, CourseSerializer, UniversityCourseSerializer

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class UniversityCourseViewSet(viewsets.ModelViewSet):
    queryset = UniversityCourse.objects.all()
    serializer_class = UniversityCourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['semester']
    ordering_fields = ['duration_weeks']
    search_fields = ['university__name', 'course__title']

    def get_queryset(self):
        university_id = self.kwargs.get('university_pk')
        if university_id:
            return self.queryset.filter(university_id=university_id)
        return self.queryset

    @action(detail=False, methods=['get'], url_path='stats')
    def course_stats(self, request, university_pk=None):
        queryset = self.get_queryset()
        stats = {
            "total_courses": queryset.count(),
            "average_duration": queryset.aggregate(
                avg_duration=Avg('duration_weeks')
            )['avg_duration'] or 0,
            "by_semester": {
                semester: queryset.filter(semester=semester).count()
                for semester in queryset.values_list(
                    'semester', flat=True).distinct()
            }
        }
        stats['average_duration'] = round(stats['average_duration'], 1)
        return Response(stats)