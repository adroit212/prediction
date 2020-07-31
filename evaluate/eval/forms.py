from django import forms
from .models import Users


class LoginForm(forms.Form):
    userid = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class RegdepartmentForm(forms.Form):
    dept_code = forms.CharField()
    dept_name = forms.CharField()


class RemdepartmentForm(forms.Form):
    delid = forms.CharField(widget=forms.HiddenInput())


class RegcourseForm(forms.Form):
    cse_code = forms.CharField()
    cse_title = forms.CharField()
    cse_dept = forms.CharField(widget=forms.Select)
    level = forms.CharField(widget=forms.Select)


class RemcourseForm(forms.Form):
    delid = forms.CharField(widget=forms.HiddenInput)


class RegstaffForm(forms.Form):
    staffname = forms.CharField()
    staffemail = forms.CharField()
    mobile = forms.CharField()
    deptcode = forms.CharField()
    # photo = forms.FileField()


class RemstaffForm(forms.Form):
    delid = forms.CharField(widget=forms.HiddenInput)


class RegstudentForm(forms.Form):
    studentname = forms.CharField()
    studentregno = forms.CharField()
    level = forms.CharField()
    mobile = forms.CharField()
    deptcode = forms.CharField()
    # photo = forms.FileField()


class RemstudentForm(forms.Form):
    delid = forms.CharField(widget=forms.HiddenInput)


class RegallocationForm(forms.Form):
    staffemail = forms.CharField()
    csecode = forms.CharField()


class RemallocationForm(forms.Form):
    delid = forms.CharField(widget=forms.HiddenInput)


class ViewtestForm(forms.Form):
    cse = forms.CharField()


class RegtestquestionForm(forms.Form):
    course = forms.CharField()
    question = forms.CharField(widget=forms.Textarea())
    optiona = forms.CharField()
    optionb = forms.CharField()
    optionc = forms.CharField()
    optiond = forms.CharField()
    answer = forms.CharField()


class RemtestForm(forms.Form):
    delid = forms.CharField(widget=forms.HiddenInput)


class ViewstudentForm(forms.Form):
    cse = forms.CharField()


class RegstudcseForm(forms.Form):
    course = forms.CharField()


class TaketestForm(forms.Form):
    cse = forms.CharField()


class SubmittestForm(forms.Form):
    questionid = forms.CharField(widget=forms.HiddenInput)
    answer = forms.CharField(widget=forms.HiddenInput)
    opt = forms.CharField(widget=forms.RadioSelect)
    csecode = forms.CharField(widget=forms.HiddenInput)
    deptcode = forms.CharField(widget=forms.HiddenInput)
