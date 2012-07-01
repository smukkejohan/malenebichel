from django import forms
from models import Signup

class CourseSignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        exclude = ('user', 'course')
