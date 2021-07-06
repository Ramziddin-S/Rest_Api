from rest_framework import serializers
from .models import *


class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

























