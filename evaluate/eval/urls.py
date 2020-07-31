from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    re_path(r'^dashboard/$', views.dashboard, name='dashboard'),
    re_path(r'^signin_form/$', views.signinform),
    re_path(r'^signout/$', views.signout),
    re_path(r'^admindepartment/', views.admindepartment),
    re_path(r'^regdepartment/$', views.regdepartment),
    re_path(r'^remdepartment/$', views.remdepartment),
    re_path(r'^admincourse/$', views.admincourse),
    re_path(r'^regcourse/$', views.regcourse),
    re_path(r'^remcourse/$', views.remcourse),
    re_path(r'^adminstaff/$', views.adminstaff),
    re_path(r'^regstaff1/$', views.regstaff1),
    re_path(r'^regstaff2/$', views.regstaff2),
    re_path(r'^remstaff/$', views.remstaff),
    re_path(r'^adminstudent/$', views.adminstudent),
    re_path(r'^regstudent1/$', views.regstudent1),
    re_path(r'^regstudent2/$', views.regstudent2),
    re_path(r'^remstudent/$', views.remstaff),
    re_path(r'^adminallocation/$', views.adminallocation),
    re_path(r'^regallocation/$', views.regallocation),
    re_path(r'^remallocation/$', views.remallocation),
    re_path(r'^stafftest/$', views.stafftest),
    re_path(r'^stafftest2/$', views.stafftest2),
    re_path(r'^regtest1/$', views.regtest1),
    re_path(r'^regtest2/$', views.regtest2),
    re_path(r'^remtest/$', views.remtest),
    re_path(r'^staffcourse/$', views.staffcourse),
    re_path(r'^staffstudent/$', views.staffstudent),
    re_path(r'^staffstudent2/$', views.staffstudent2),
    re_path(r'^studentcourse/$', views.studentcourse),
    re_path(r'^regstudcse/$', views.regstudcse),
    re_path(r'^studenttest/$', views.studenttest),
    re_path(r'^studenttest2/$', views.studenttest2),
    re_path(r'^submittest/$', views.submittest),

]