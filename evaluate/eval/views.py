import os

from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime

from .forms import *
from .models import *


def index(request):
    if 'uid' in request.session and 'role' in request.session:
        return redirect(dashboard)
    else:
        return render(request, 'eval/index.html')


def dashboard(request):
    if 'uid' in request.session and 'role' in request.session:
        return render(request, 'eval/dashboard.html')
    else:
        return redirect(index)


def admindepartment(request):
    if 'uid' in request.session and 'role' in request.session:
        department = Departments.objects.all();
        content_dict = {'departments': department}

        return render(request, 'eval/admindepartment.html', content_dict)
    else:
        return redirect(index)


def admincourse(request):
    if 'uid' in request.session and 'role' in request.session:
        course = Courses.objects.all();
        department = Departments.objects.all();
        content_dict = {'courses': course, 'departments': department}

        return render(request, 'eval/admincourse.html', content_dict)
    else:
        return redirect(index)


def signinform(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            # get form details
            f_userid = loginform.cleaned_data.get('userid')
            f_password = loginform.cleaned_data.get('password')

            # validate user
            user = Users.objects.get(userid=f_userid)

            if user.password == f_password and user.userid == f_userid:
                request.session['uid'] = f_userid
                request.session['role'] = user.role
                request.session['dept'] = user.department

                return redirect(dashboard)

    return render(request, 'eval/index.html', {'result': 'Incorrect username and password supplied'})


def signout(request):
    try:
        request.session.flush()
    except KeyError:
        print('failed to flush data')
    return redirect(index)


def regdepartment(request):
    if request.method == 'POST':
        regform = RegdepartmentForm(request.POST)

        if regform.is_valid():
            f_deptcode = regform.cleaned_data.get('dept_code')
            f_deptname = regform.cleaned_data.get('dept_name')

            new_entry = Departments(deptcode=f_deptcode, deptname=f_deptname)
            new_entry.save()
        return redirect(admindepartment)


def remdepartment(request):
    if request.method == 'POST':
        remform = RemdepartmentForm(request.POST)

        if remform.is_valid():
            f_deptcode = remform.cleaned_data.get('delid')
            department = Departments.objects.get(deptcode=f_deptcode)
            department.delete()
        return redirect(admindepartment)


def regcourse(request):
    if request.method == 'POST':
        regform = RegcourseForm(request.POST)

        if regform.is_valid():
            f_csecode = regform.cleaned_data.get('cse_code')
            f_csetitle = regform.cleaned_data.get('cse_title')
            f_dept = regform.cleaned_data.get('cse_dept')
            f_level = regform.cleaned_data.get('level')

            new_entry = Courses(coursecode=f_csecode, coursetitle=f_csetitle, deptcode=f_dept, level=f_level)
            new_entry.save()
            return redirect(admincourse)


def remcourse(request):
    if request.method == 'POST':
        remform = RemcourseForm(request.POST)

        if remform.is_valid():
            f_csecode = remform.cleaned_data.get('delid')
            course = Courses.objects.get(coursecode=f_csecode)
            course.delete()
        return redirect(admincourse)


def adminstaff(request):
    if 'uid' in request.session and 'role' in request.session:
        staffs = Staffs.objects.all();
        content_dict = {'staffs': staffs}

        return render(request, 'eval/adminstaff.html', content_dict)
    else:
        return redirect(index)


def regstaff1(request):
    if 'uid' in request.session and 'role' in request.session:
        departments = Departments.objects.all();
        content_dict = {'departments': departments}

        return render(request, 'eval/regstaff1.html', content_dict)
    else:
        return redirect(index)


def regstaff2(request):
    jscript_success = "<script>alert('Registration successful!'); window.location.href='/adminstaff/';</script>"
    jscript_failed = "<script>alert('Registration failed!'); window.location.href='/regstaff1/';</script>"
    if request.method == 'POST':
        regform = RegstaffForm(request.POST)
        if regform.is_valid():
            f_staffemail = regform.cleaned_data.get('staffemail')
            f_staffname = regform.cleaned_data.get('staffname')
            f_deptcode = regform.cleaned_data.get('deptcode')
            f_mobile = regform.cleaned_data.get('mobile')
            # photoid = datetime.today().strftime('%Y%m%d%H%M%S')
            # uploadedfilename = request.FILES['photo'].name
            # extension = os.path.splitext(uploadedfilename)[1]
            # ext_list = ('.jpeg', '.jpg', 'jpg')
            new_user_entry = Users(userid=f_staffemail, password=f_staffemail, role='staff', department=f_deptcode)
            new_staff_entry = Staffs(staffemail=f_staffemail, staffname=f_staffname, deptcode=f_deptcode,
                                     mobile=f_mobile,
                                     photo='null')

            new_user_entry.save()
            new_staff_entry.save()
            return HttpResponse(jscript_success)
        else:
            return HttpResponse(jscript_failed)


def remstaff(request):
    if request.method == 'POST':
        remform = RemstaffForm(request.POST)

        if remform.is_valid():
            f_staffemail = remform.cleaned_data.get('delid')
            uaer = Users.objects.get(userid=f_staffemail)
            staff = Staffs.objects.get(staffemail=f_staffemail)

            uaer.delete()
            staff.delete()
        return redirect(adminstaff)


def upload_new_file(myfile, filename):
    try:
        fopen = open('static/eval/images/' + myfile.name, 'wb+')
        # Iterate through the chunks.
        for chunk in myfile.chunks():
            fopen.write(chunk)
        fopen.close()

        return True
    except:
        return False


def adminstudent(request):
    if 'uid' in request.session and 'role' in request.session:
        students = Student.objects.all();
        content_dict = {'students': students}
        return render(request, 'eval/adminstudent.html', content_dict)
    else:
        return redirect(index)


def regstudent1(request):
    if 'uid' in request.session and 'role' in request.session:
        departments = Departments.objects.all();
        content_dict = {'departments': departments}
        return render(request, 'eval/regstudent1.html', content_dict)
    else:
        return redirect(index)


def regstudent2(request):
    jscript_success = "<script>alert('Registration successful!'); window.location.href='/adminstudent/';</script>"
    jscript_failed = "<script>alert('Registration failed!'); window.location.href='/regstudent1/';</script>"
    if request.method == 'POST':
        regform = RegstudentForm(request.POST)
        if regform.is_valid():
            f_studentregno = regform.cleaned_data.get('studentregno')
            f_studentname = regform.cleaned_data.get('studentname')
            f_deptcode = regform.cleaned_data.get('deptcode')
            f_level = regform.cleaned_data.get('level')
            f_mobile = regform.cleaned_data.get('mobile')
            # photoid = datetime.today().strftime('%Y%m%d%H%M%S')
            # uploadedfilename = request.FILES['photo'].name
            # extension = os.path.splitext(uploadedfilename)[1]
            # ext_list = ('.jpeg', '.jpg', 'jpg')
            new_user_entry = Users(userid=f_studentregno, password=f_studentregno, role='student',
                                   department=f_deptcode)
            new_student_entry = Student(studentregno=f_studentregno, studentname=f_studentname, deptcode=f_deptcode,
                                        mobile=f_mobile, level=f_level, photo='null')

            new_user_entry.save()
            new_student_entry.save()
            return HttpResponse(jscript_success)
        else:
            return HttpResponse(jscript_failed)


def remstaff(request):
    if request.method == 'POST':
        remform = RemstudentForm(request.POST)

        if remform.is_valid():
            f_studentregno = remform.cleaned_data.get('delid')
            uaer = Users.objects.get(userid=f_studentregno)
            student = Student.objects.get(studentregno=f_studentregno)

            uaer.delete()
            student.delete()
        return redirect(adminstudent)


def adminallocation(request):
    if 'uid' in request.session and 'role' in request.session:
        allocation = Allocations.objects.all()
        # allocchecker = Allocations.objects.all()
        allocchecker = []
        allcourses = Courses.objects.all()
        allstaffs = Staffs.objects.all()
        processed_alloc = {}

        # Recreate allocations to suit template render
        for alloc in allocation:
            aid = alloc.id

            allocid = alloc.allocid
            coursecode = alloc.coursecode
            staffemail = alloc.staffemail
            deptcode = alloc.deptcode

            course = Courses.objects.get(coursecode=coursecode)
            staff = Staffs.objects.get(staffemail=staffemail)
            department = Departments.objects.get(deptcode=deptcode)

            coursetitle = course.coursetitle
            staffname = staff.staffname
            deptname = department.deptname

            allocchecker.append(coursecode)

            sub_alloc = {'allocid': allocid, 'coursecode': coursecode, 'coursetitle': coursetitle,
                         'staffname': staffname, 'deptname': deptname}

            processed_alloc[aid] = sub_alloc

        content_dict = {'allstaffs': allstaffs, 'allcourses': allcourses, 'allocations': processed_alloc,
                        'allocchecker': allocchecker}

        return render(request, 'eval/adminallocation.html', content_dict)
    else:
        return redirect(index)


def regallocation(request):
    if request.method == 'POST':
        regform = RegallocationForm(request.POST)

        if regform.is_valid():
            f_csecode = regform.cleaned_data.get('csecode')
            f_staffemail = regform.cleaned_data.get('staffemail')
            f_allocid = 'alloc-' + datetime.today().strftime('%Y%m%d%H%M%S')

            course = Courses.objects.get(coursecode=f_csecode)
            f_dept = course.deptcode

            new_entry = Allocations(allocid=f_allocid, coursecode=f_csecode, staffemail=f_staffemail, deptcode=f_dept)
            new_entry.save()
            return redirect(adminallocation)


def remallocation(request):
    if request.method == 'POST':
        remform = RemallocationForm(request.POST)

        if remform.is_valid():
            f_allocid = remform.cleaned_data.get('delid')
            allocation = Allocations.objects.get(allocid=f_allocid)
            allocation.delete()
        return redirect(adminallocation)


def stafftest(request):
    if 'uid' in request.session and 'role' in request.session:
        course = Courses.objects.all()
        allocation = Allocations.objects.filter(staffemail=request.session['uid'])
        allocchecker = []
        for al in allocation:
            allocchecker.append(al.coursecode)

        content_dict = {'courses': course, 'allocations': allocchecker}

        return render(request, 'eval/stafftest.html', content_dict)
    else:
        return redirect(index)


def stafftest2(request):
    if request.method == 'POST':
        viewform = ViewtestForm(request.POST)

        if viewform.is_valid():
            coursecode = viewform.cleaned_data.get('cse')
            course2 = Courses.objects.get(coursecode=coursecode)
            department = Departments.objects.get(deptcode=course2.deptcode)
            deptname = department.deptname
            level = course2.level
            coursetitle = course2.coursetitle

            tests = Testquestion.objects.filter(staffemail=request.session['uid']) & \
                    Testquestion.objects.filter(coursecode=coursecode)

            course = Courses.objects.all()
            allocation = Allocations.objects.filter(staffemail=request.session['uid'])
            allocchecker = []
            for al in allocation:
                allocchecker.append(al.coursecode)

            content_dict = {'courses': course, 'coursecode': coursecode, 'coursetitle': coursetitle,
                            'deptname': deptname, 'level': level, 'allocations': allocchecker, 'tests': tests}

            return render(request, 'eval/stafftest.html', content_dict)
    return redirect(stafftest)


def regtest1(request):
    if 'uid' in request.session and 'role' in request.session:
        allocation = Allocations.objects.filter(staffemail=request.session['uid']);
        preprocessed_courses = {}
        for alloc in allocation:
            course = Courses.objects.get(coursecode=alloc.coursecode)
            sub_alloc = {'coursetitle': course.coursetitle, 'coursecode': course.coursecode}
            preprocessed_courses[alloc.id] = sub_alloc

        content_dict = {'courses': preprocessed_courses}

        return render(request, 'eval/regtest1.html', content_dict)
    else:
        return redirect(index)


def regtest2(request):
    jscript_success = "<script>alert('Operation successful!'); window.location.href='/stafftest/';</script>"
    jscript_failed = "<script>alert('Operation failed!'); window.location.href='/regtest1/';</script>"
    if request.method == 'POST':
        regform = RegtestquestionForm(request.POST)
        if regform.is_valid():
            f_testquestid = 'test-' + datetime.today().strftime('%Y%m%d%H%M%S')
            f_staffemail = request.session['uid']
            f_deptcode = request.session['dept']
            f_coursecode = regform.cleaned_data.get('course')
            f_question = regform.cleaned_data.get('question')
            f_optiona = regform.cleaned_data.get('optiona')
            f_optionb = regform.cleaned_data.get('optionb')
            f_optionc = regform.cleaned_data.get('optionc')
            f_optiond = regform.cleaned_data.get('optiond')
            f_answer = regform.cleaned_data.get('answer')

            new_entry = Testquestion(testquestid=f_testquestid, staffemail=f_staffemail, deptcode=f_deptcode,
                                     coursecode=f_coursecode, question=f_question, opta=f_optiona, optb=f_optionb,
                                     optc=f_optionc, optd=f_optiond, answer=f_answer)
            new_entry.save()

            return HttpResponse(jscript_success)
        else:
            return HttpResponse(jscript_failed)


def remtest(request):
    if request.method == 'POST':
        remform = RemtestForm(request.POST)

        if remform.is_valid():
            f_testquestid = remform.cleaned_data.get('delid')
            testquest = Testquestion.objects.get(testquestid=f_testquestid)

            testquest.delete()

        return redirect(stafftest)


def staffcourse(request):
    if 'uid' in request.session and 'role' in request.session:
        allocations = Allocations.objects.filter(staffemail=request.session['uid'])
        processed_courses = {}

        for alloc in allocations:
            course = Courses.objects.get(coursecode=alloc.coursecode);
            department = Departments.objects.get(deptcode=course.deptcode)

            sub_courses = {'coursecode': course.coursecode, 'coursetitle': course.coursetitle, 'level': course.level,
                           'deptname': department.deptname, 'allocid': alloc.allocid}

            processed_courses[alloc.allocid] = sub_courses

        content_dict = {'courses': processed_courses}

        return render(request, 'eval/staffcourse.html', content_dict)
    else:
        return redirect(index)


def staffstudent(request):
    if 'uid' in request.session and 'role' in request.session:
        courses = Courses.objects.all()
        allocations = Allocations.objects.filter(staffemail=request.session['uid'])
        alloc_list = []
        for alloc in allocations:
            alloc_list.append(alloc.coursecode)

        content_dict = {'courses': courses, 'allocations': alloc_list}

        return render(request, 'eval/staffstudent.html', content_dict)
    else:
        return redirect(index)


def staffstudent2(request):
    if request.method == 'POST':
        viewform = ViewstudentForm(request.POST)

        if viewform.is_valid():
            coursecode = viewform.cleaned_data.get('cse')
            course2 = Courses.objects.get(coursecode=coursecode)
            department = Departments.objects.get(deptcode=course2.deptcode)
            deptname = department.deptname
            level = course2.level
            coursetitle = course2.coursetitle

            # students =

            courses = Courses.objects.all()
            allocations = Allocations.objects.filter(staffemail=request.session['uid'])
            alloc_list = []
            for alloc in allocations:
                alloc_list.append(alloc.coursecode)

            content_dict = {'courses': courses, 'allocations': alloc_list, 'coursecode': coursecode,
                            'coursetitle': coursetitle, 'deptname': deptname, 'level': level, }

            return render(request, 'eval/staffcourse.html', content_dict)

    return redirect(staffstudent)


def studentcourse(request):
    if 'uid' in request.session and 'role' in request.session:
        regcses = Registercse.objects.filter(studentregno=request.session['uid'])
        processed_cse = {}

        for rc in regcses:
            coursecode = rc.coursecode
            cse = Courses.objects.get(coursecode=coursecode)
            coursetitle = cse.coursetitle
            level = cse.level

            sub_cse = {'coursecode': coursecode, 'coursetitle': coursetitle, 'level': level}
            processed_cse[rc.regcseid] = sub_cse

        courses = Courses.objects.filter(deptcode=request.session['dept'])
        registercse = Registercse.objects.filter(studentregno=request.session['uid'])
        checker = []
        for regcse in registercse:
            checker.append(regcse.coursecode)

        content_dict = {'regcourses': processed_cse, 'courses': courses, 'checker': checker}
        return render(request, 'eval/studentcourse.html', content_dict)
    else:
        return redirect(index)


def regstudcse(request):
    if request.method == 'POST':
        regform = RegstudcseForm(request.POST)

        if regform.is_valid():
            f_coursecode = regform.cleaned_data.get('course')
            f_regcseid = 'regcse-' + datetime.today().strftime('%Y%m%d%H%M%S')
            f_studentregno = request.session['uid']
            f_deptcode = request.session['dept']

            new_entry = Registercse(regcseid=f_regcseid, coursecode=f_coursecode, studentregno=f_studentregno,
                                    deptcode=f_deptcode)
            new_entry.save()

            return redirect(studentcourse)


def studenttest(request):
    if 'uid' in request.session and 'role' in request.session:
        courses = Courses.objects.filter(deptcode=request.session['dept'])
        content_dict = {'courses': courses}
        return render(request, 'eval/studenttest.html', content_dict)
    else:
        return redirect(index)


def studenttest2(request):
    if request.method == 'POST':
        viewform = TaketestForm(request.POST)

        if viewform.is_valid():
            coursecode = viewform.cleaned_data.get('cse')
            single_course = Courses.objects.get(coursecode=coursecode)
            coursetitle = single_course.coursetitle
            level = single_course.level
            single_dept = Departments.objects.get(deptcode=single_course.deptcode)
            deptcode = single_dept.deptcode
            deptname = single_dept.deptname
            testquest = Testquestion.objects.filter(coursecode=coursecode)
            alreadytaken = (Testresult.objects.filter(studentregno=request.session['uid'],
                                                      coursecode=coursecode)).exists()

            courses = Courses.objects.filter(deptcode=request.session['dept'])

            content_dict = {'courses': courses, 'testquestions': testquest, 'coursetitle': coursetitle,
                            'coursecode': coursecode, 'deptcode': deptcode, 'deptname': deptname, 'level': level,
                            'alreadytaken': alreadytaken, 'flag': True}

            return render(request, 'eval/studenttest.html', content_dict)
    return redirect(studenttest)


def submittest(request):
    if request.method == 'POST':

        # get all items in list form without using form model
        # if submitform.is_valid():

        studentregno = request.session['uid']
        testdate = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        coursecode = request.POST.get('csecode')
        deptcode = request.POST.get('deptcode')

        questionid = request.POST.getlist('questionid')
        answer_list = request.POST.getlist('answer')
        counter_index = 0
        for qid in questionid:
            testresid = 'res' + datetime.today().strftime('%Y%m%d%H%M%S') + format(counter_index)
            opt = request.POST.get(qid)[0]
            answer = answer_list[counter_index]
            score = 0
            if opt == answer:
                score += 1

            new_entry = Testresult(testresid=testresid, studentregno=studentregno, testquestid=qid,
                                   coursecode=coursecode, deptcode=deptcode, scorederivable='1',
                                   scorederived=format(score), testdatetime=testdate)
            new_entry.save()
            counter_index += 1

        # go back to normal view with success message
        msg = "<script>alert('Test taken successfully!'); window.location.href='/studenttest/';</script>"
        return HttpResponse(msg)

    return HttpResponse('Error occured please go back and try again')
