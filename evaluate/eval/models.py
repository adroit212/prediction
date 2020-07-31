from django.db import models

# Create your models here.
class Users(models.Model):
    userid = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10)
    department = models.CharField(max_length=50)


class Departments(models.Model):
    deptcode = models.CharField(max_length=50)
    deptname = models.CharField(max_length=150)


class Courses(models.Model):
    coursecode = models.CharField(max_length=30)
    coursetitle = models.CharField(max_length=80)
    deptcode = models.CharField(max_length=50)
    level = models.CharField(max_length=10)


class Allocations(models.Model):
    allocid = models.CharField(max_length=50)
    coursecode = models.CharField(max_length=30)
    staffemail = models.CharField(max_length=50)
    deptcode = models.CharField(max_length=50)


class Registercse(models.Model):
    regcseid = models.CharField(max_length=50)
    coursecode = models.CharField(max_length=30)
    studentregno = models.CharField(max_length=30)
    deptcode = models.CharField(max_length=50)


class Testquestion(models.Model):
    testquestid = models.CharField(max_length=50)
    coursecode = models.CharField(max_length=30)
    deptcode = models.CharField(max_length=50)
    staffemail = models.CharField(max_length=50)
    question = models.TextField()
    opta = models.CharField(max_length=50)
    optb = models.CharField(max_length=50)
    optc = models.CharField(max_length=50)
    optd = models.CharField(max_length=50)
    answer = models.CharField(max_length=5)


class Testresult(models.Model):
    testresid = models.CharField(max_length=50)
    studentregno = models.CharField(max_length=30)
    testquestid = models.CharField(max_length=50)
    coursecode = models.CharField(max_length=30)
    deptcode = models.CharField(max_length=50)
    scorederivable = models.CharField(max_length=10)
    scorederived = models.CharField(max_length=10)
    testdatetime = models.DateTimeField()


class Staffs(models.Model):
    staffemail = models.CharField(max_length=50)
    staffname = models.CharField(max_length=80)
    deptcode = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    photo = models.CharField(max_length=30)


class Student(models.Model):
    studentregno = models.CharField(max_length=30)
    studentname = models.CharField(max_length=80)
    deptcode = models.CharField(max_length=50)
    level = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    photo = models.CharField(max_length=30)
