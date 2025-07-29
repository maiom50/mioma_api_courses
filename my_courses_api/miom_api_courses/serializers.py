from rest_framework import serializers
from .models import University, Course, UniversityCourse


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class UniversityCourseSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = UniversityCourse
        fields = '__all__'