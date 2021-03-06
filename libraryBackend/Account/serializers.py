from django.contrib.auth import authenticate
from .models import User, Student, Teacher, Librarian
from rest_framework import serializers

# Register Serializer
class RegisterSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            last_name=validated_data["last_name"],
            first_name=validated_data["first_name"],
        )

        return user


class StudentRegisterSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "sap_id",
            "department",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = Student.objects.create_user(
            email=validated_data["email"],
            sap_id=validated_data["sap_id"],
            password=validated_data["password"],
            department=validated_data["department"],
            is_student=True,
            is_teacher=False,
            is_librarian=False,
            last_name=validated_data["last_name"],
            first_name=validated_data["first_name"],
        )

        return user


class TeacherRegisterSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            "id",
            "email",
            "department",
            "sap_id",
            "first_name",
            "last_name",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = Teacher.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            department=validated_data["department"],
            sap_id=validated_data["sap_id"],
            is_student=False,
            is_teacher=True,
            is_librarian=False,
            last_name=validated_data["last_name"],
            first_name=validated_data["first_name"],
        )

        return user


class LibrarianRegisterSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "joined_on",
            "librarian_id",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = Librarian.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            is_student=False,
            is_teacher=False,
            is_librarian=True,
            joined_on=validated_data["joined_on"],
            librarian_id=validated_data["librarian_id"],
            last_name=validated_data["last_name"],
            first_name=validated_data["first_name"],
        )

        return user
