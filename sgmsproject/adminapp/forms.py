from django import forms
from .models import Faculty,Student

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        exclude = {"password"}
        labels = {"facultyid": "Enter Faculty ID", "gender" : "select Gender","fullname" : "Enter Full Name"}

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = {"password"}
        labels = {"studentid": "Enter Student ID", "gender" : "select Gender","fullname" : "Enter Full Name"}
