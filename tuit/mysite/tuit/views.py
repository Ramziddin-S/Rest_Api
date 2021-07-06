from rest_framework import viewsets
from .models import *
from .serializers import FacultySerializers, GroupSerializers, SubjectSerializers, TeacherSerializers, StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from .services import *
from rest_framework.exceptions import NotFound


class FacultyView(GenericAPIView):
    serializer_class = FacultySerializers

    def get_object(self, *args, **kwargs):
        try:
            faculty = Faculty.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return faculty

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        faculty = Faculty.objects.get(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=faculty)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        faculty = Faculty.objects.get(pk=pk)
        faculty.delete()
        return Response({"detail": f"Faculty with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            faculty = get_faculty()
            if not faculty:
                raise NotFound("Faculty not found !")
            return Response(faculty, status=status.HTTP_200_OK)
        else:
            faculty = get_faculty()
            return Response(faculty, status=status.HTTP_200_OK)


class GroupView(GenericAPIView):
    serializer_class = GroupSerializers

    def get_object(self, *args, **kwargs):
        try:
            group = Group.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return group

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        group = Group.objects.get(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=group)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        group = Group.objects.get(pk=pk)
        group.delete()
        return Response({"detail": f"Group with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            group = get_group()
            if not group:
                raise NotFound("Froup not found !")
            return Response(group, status=status.HTTP_200_OK)
        else:
            group = get_group()
            return Response(group, status=status.HTTP_200_OK)


class SubjectVeiw(GenericAPIView):
    serializer_class = SubjectSerializers

    def get_object(self, *args, **kwargs):
        try:
            subject = Subject.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return subject

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=subject)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        subject.delete()
        return Response({"detail": f"Subject with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            group = get_subject()
            if not group:
                raise NotFound("Subject not found !")
            return Response(group, status=status.HTTP_200_OK)
        else:
            subject = get_subject()
            return Response(subject, status=status.HTTP_200_OK)


class TeacherVeiw(GenericAPIView):
    serializer_class = TeacherSerializers

    def get_object(self, *args, **kwargs):
        try:
            teacher = Teacher.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return teacher

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=teacher)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response({"detail": f"Teacher with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            teacher = get_teacher()
            if not teacher:
                raise NotFound("Teacher not found !")
            return Response(teacher, status=status.HTTP_200_OK)
        else:
            teacher = get_teacher()
            return Response(teacher, status=status.HTTP_200_OK)


class StudentVeiw(GenericAPIView):
    serializer_class = StudentSerializers

    def get_object(self, *args, **kwargs):
        try:
            student = Student.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return student

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=student)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response({"detail": f"Student with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            student = get_student()
            if not student:
                raise NotFound("Student not found !")
            return Response(student, status=status.HTTP_200_OK)
        else:
            student = get_student()
            return Response(student, status=status.HTTP_200_OK)