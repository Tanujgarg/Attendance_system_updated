from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *
from .Files.Form_data import *
import datetime
from cse.Files.Library.Data.Database import *

form_class = None
subject = ''
is_lab = False




def index(request):
    return render(request, 'index.html')


def teachers_login(request):
    global subject
    if request.method == 'POST':
        form = Teachers_login(request.POST)
        if form.is_valid():
            print("Form valid")
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            print(name, password)
            user = Teachers.objects.filter(name=name.lower()).first()
            if user:
                if password == user.password:
                    request.session['name'] = user.name
                    request.session['subject'] = user.subject
                    subject = user.subject
                    return render(request, 'section.html',)
                else:
                    return render(request, 'teacherlogin.html', {'form': form,
                                                                 'error': 'Wrong Password'})
            else:
                return render(request, 'teacherlogin.html', {'form': form,
                                                             'error': 'No user exist with this name'})
            # print(name, password)
        else:
            print("invalid")
    elif request.method == "GET":
        form = Teachers_login()
        return render(request, 'teacherlogin.html', {'form': form})


def student_login(request):
    if request.method == 'POST':
        form = Student_login(request.POST)
        if form.is_valid():
            print("Form valid")
            roll_no = form.cleaned_data['roll_no']
            password = form.cleaned_data['password']

            user = Student.objects.filter(roll_no=roll_no).first()

            if user:
                if user.password == password:
                    wt = WT.objects.filter(roll_no=roll_no).all()
                    cd = CD.objects.filter(roll_no=roll_no).all()
                    mc = MC.objects.filter(roll_no=roll_no).all()
                    eit = EIT.objects.filter(roll_no=roll_no).all()
                    eit_lab = EITLab.objects.filter(roll_no=roll_no).all()
                    se = SE.objects.filter(roll_no=roll_no).all()
                    se_lab = SELab.objects.filter(roll_no=roll_no).all()
                    bie = BIE.objects.filter(roll_no=roll_no).all()
                    wt_lab = WTLab.objects.filter(roll_no=roll_no).all()

                    wt_total = wt.count()
                    wt_present = wt.filter(status=True).count()
                    try:
                        wt_avg = (wt_present / wt_total) * 100
                        wt_avg = round(wt_avg, 2)
                    except ZeroDivisionError:
                        wt_avg = 'N.A.'

                    cd_total = cd.count()
                    cd_present = cd.filter(status=True).count()
                    try:
                        cd_avg = (cd_present / cd_total) * 100
                        cd_avg = round(cd_avg, 2)
                    except ZeroDivisionError:
                        cd_avg = 'N.A.'

                    mc_total = mc.count()
                    mc_present = mc.filter(status=True).count()
                    try:
                        mc_avg = (mc_present / mc_total) * 100
                        mc_avg = round(mc_avg, 2)
                    except ZeroDivisionError:
                        mc_avg = 'N.A.'

                    eit_total = eit.count()
                    eit_present = eit.filter(status=True).count()
                    try:
                        eit_avg = (eit_present / eit_total) * 100
                        eit_avg = round(eit_avg, 2)
                    except ZeroDivisionError:
                        eit_avg = 'N.A.'

                    se_total = se.count()
                    se_present = se.filter(status=True).count()
                    try:
                        se_avg = (se_present / se_total) * 100
                        se_avg = round(se_avg, 2)
                    except ZeroDivisionError:
                        se_avg = 'N.A.'

                    bie_total = bie.count()
                    bie_present = bie.filter(status=True).count()
                    try:
                        bie_avg = (bie_present / wt_total) * 100
                        bie_avg = round(bie_avg, 2)
                    except ZeroDivisionError:
                        bie_avg = 'N.A.'

                    wt_lab_total = wt_lab.count()
                    wt_lab_present = wt_lab.filter(status=True).count()
                    try:
                        wt_lab_avg = (wt_lab_present / wt_lab_total) * 100
                        wt_lab_avg = round(wt_lab_avg, 2)
                    except ZeroDivisionError:
                        wt_lab_avg = 'N.A.'

                    se_lab_total = se_lab.count()
                    se_lab_present = se_lab.filter(status=True).count()
                    try:
                        se_lab_avg = (se_lab_present / se_lab_total) * 100
                        se_lab_avg = round(se_lab_avg, 2)
                    except ZeroDivisionError:
                        se_lab_avg = 'N.A.'

                    eit_lab_total = eit_lab.count()
                    eit_lab_present = eit_lab.filter(status=True).count()
                    try:
                        eit_lab_avg = (eit_lab_present / eit_lab_total) * 100
                        eit_lab_avg = round(eit_lab_avg, 2)
                    except ZeroDivisionError:
                        eit_lab_avg = 'N.A.'

                    return render(request, 'Dashboard.html', {'wt': wt,
                                                              'user': user,
                                                              'cd': cd,
                                                              'mc': mc,
                                                              'eit': eit,
                                                              'eit_lab': eit_lab,
                                                              'se': se,
                                                              'se_lab': se_lab,
                                                              'bie': bie,
                                                              'wt_lab': wt_lab,
                                                              'wt_total': wt_total,
                                                              'wt_present': wt_present,
                                                              'wt_avg': wt_avg,
                                                              'se_total': se_total,
                                                              'se_present': se_present,
                                                              'se_avg': se_avg,
                                                              'eit_total': eit_total,
                                                              'eit_present': eit_present,
                                                              'eit_avg': eit_avg,
                                                              'mc_total': mc_total,
                                                              'mc_present': mc_present,
                                                              'mc_avg': mc_avg,
                                                              'cd_total': cd_total,
                                                              'cd_present': cd_present,
                                                              'cd_avg': cd_avg,
                                                              'bie_total': bie_total,
                                                              'bie_present': bie_present,
                                                              'bie_avg': bie_avg,
                                                              'wt_lab_total': wt_lab_total,
                                                              'wt_lab_present': wt_lab_present,
                                                              'wt_lab_avg': wt_lab_avg,
                                                              'se_lab_total': se_lab_total,
                                                              'se_lab_present': se_lab_present,
                                                              'se_lab_avg': se_lab_avg,
                                                              'eit_lab_total': eit_lab_total,
                                                              'eit_lab_present': eit_lab_present,
                                                              'eit_lab_avg': eit_lab_avg})
                else:
                    return render(request, 'studentlogin.html', {'form': form,
                                                                 'error': 'Wrong password'})
            else:
                return render(request, 'studentlogin.html', {'form': form,
                                                             'error': 'Incorrect roll number'})
        else:
            print("invalid")
    elif request.method == "GET":
        form = Student_login()
        return render(request, 'studentlogin.html', {'form': form})


def mark_attendance(request):
    global form_class
    global is_lab
    if request.method == "GET":
        if request.session.has_key('name'):
            print(request.session['name'])
            section = request.GET.get('class')
            # print(section, request.GET.get('key'))
            if section == 'cse1':
                form_class = 'cse1'
                print(section, form_class)
                form = Cse1(request.POST)
                return render(request, 'Mark_attendance.html', {'form': form,
                                                                'data': Cse1_data,
                                                                'teacher': request.session['name'].upper(),
                                                                'subject': subject.upper(),
                                                                'date': datetime.datetime.now().date()})
            if section == 'cse1a':

                form_class = 'cse1a'
                form = Cse1a(request.POST)
                return render(request, 'Mark_attendance.html', {'form': form,
                                                                'data': A1_data,
                                                                'teacher': request.session['name'].upper(),
                                                                'subject': subject.upper(),
                                                                'date': datetime.datetime.now().date()})
            elif section == 'cse1b':

                form_class = 'cse1b'
                form = Cse1b(request.POST)
                return render(request, 'Mark_attendance.html', {'form': form,
                                                                'data': A2_data,
                                                                'teacher': request.session['name'].upper(),
                                                                'subject': subject.upper(),
                                                                'date': datetime.datetime.now().date()})
            elif section == 'cse1la':
                is_lab = True
                form_class = 'cse1la'
                form = Cse1a(request.POST)
                return render(request, 'Mark_attendance.html', {'form': form,
                                                                'data': A1_data,
                                                                'teacher': request.session['name'].upper(),
                                                                'subject': subject.upper(),
                                                                'date': datetime.datetime.now().date()})
            elif section == 'cse1lb':
                is_lab = True
                form_class = 'cse1lb'
                form = Cse1b(request.POST)
                return render(request, 'Mark_attendance.html', {'form': form,
                                                                'data': A2_data,
                                                                'teacher': request.session['name'].upper(),
                                                                'subject': subject.upper(),
                                                                'date': datetime.datetime.now().date()})

            else:
                return redirect("/home")
        return render(request, 'Error.html', {'login_error': True})
    elif request.method == "POST":
        if form_class == 'cse1':
            form = Cse1(request.POST)
            print("Post")
            if form.is_valid():
                print("form valid")
                print(form_class)
                for i, j in zip(Cse1_roll, Cse1_key):
                    status = form.cleaned_data[j]
                    print(i, status)
                    if subject == 'wt' and not is_lab:
                        attendance = WT(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'eit' and not is_lab:
                        attendance = EIT(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'bie':
                        attendance = BIE(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'se' and not is_lab:
                        attendance = SE(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'mc':
                        attendance = MC(roll_no=i, status=status)
                        attendance.save()
                        print("mc saved")
                    elif subject == 'cd':
                        attendance = CD(roll_no=i, status=status)
                        attendance.save()
                    else:
                        request.session.flush()
                        return render(request, 'Error.html', {'error': True})
                    # print(i, status)
        if form_class == 'cse1a':
            form = Cse1a(request.POST)
            print("Post")
            if form.is_valid():
                print("form valid")
                for i, j in zip(A1_roll, A_key):
                    status = form.cleaned_data[j]
                    if subject == 'wt' and not is_lab:
                        attendance = WT(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'eit' and not is_lab:
                        attendance = EIT(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'bie':
                        attendance = BIE(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'se' and not is_lab:
                        attendance = SE(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'mc':
                        attendance = MC(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'cd':
                        attendance = CD(roll_no=i, status=status)
                        attendance.save()
                    else:
                        request.session.flush()
                        return render(request, 'Error.html', {'error': True})
        if form_class == 'cse1b':
            form = Cse1b(request.POST)
            print("Post")
            if form.is_valid():
                print("form valid")
                for i, j in zip(A2_roll, A_key):
                    status = form.cleaned_data[j]
                    if subject == 'wt' and not is_lab:
                        attendance = WT(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'eit' and not is_lab:
                        attendance = EIT(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'bie':
                        attendance = BIE(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'se' and not is_lab:
                        attendance = SE(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'mc':
                        attendance = MC(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'cd':
                        attendance = CD(roll_no=i, status=status)
                        attendance.save()
                    else:
                        request.session.flush()
                        return render(request, 'Error.html', {'error': True})
        if form_class == 'cse1la':
            form = Cse1a(request.POST)
            print("Post")
            if form.is_valid():
                print("form valid")
                for i, j in zip(A1_roll, A_key):
                    status = form.cleaned_data[j]
                    if subject == 'wt' and is_lab:
                        attendance = WTLab(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'se' and is_lab:
                        attendance = SELab(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'eit' and is_lab:
                        attendance = EITLab(roll_no=i, status=status)
                        attendance.save()
                    else:
                        request.session.flush()
                        return render(request, 'Error.html', {'lab_error': True})
        if form_class == 'cse1lb':
            form = Cse1b(request.POST)
            print("Post")
            if form.is_valid():
                print("form valid")
                for i, j in zip(A2_roll, A_key):
                    status = form.cleaned_data[j]
                    if subject == 'wt' and is_lab:
                        attendance = WTLab(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'se' and is_lab:
                        attendance = SELab(roll_no=i, status=status)
                        attendance.save()
                    elif subject == 'eit' and is_lab:
                        attendance = EITLab(roll_no=i, status=status)
                        attendance.save()
                    else:
                        request.session.flush()
                        return render(request, 'Error.html', {'lab_error': True})
        request.session.flush()
        return render(request, 'Error.html', {'success': True})


def student_register(request):
    if request.method == "POST":
        print("Post")
        form = Student_Signup(request.POST)
        if form.is_valid():
            print("valid")
            name = form.cleaned_data['name']
            roll_no = form.cleaned_data['roll_no']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(name, password, email, roll_no)
            student = Student(name=name, roll_no=roll_no, email=email, password=password)
            student.save()
            print("saved")
            return render(request, 'Error.html', {'signup': True})
    elif request.method == "GET":
        print("Get")
        # return render(request, 'Signup.html')
    return render(request, 'Signup.html')


def Change_password(request):
    if request.method == "GET":
        teacher = request.GET.get('name')
        password = request.GET.get('pswrd')
        print(teacher, password)
        user = Teachers.objects.filter(name=teacher).first()
        user.password = password

        user.save()
        print("saved")
        print(user.password)
    return HttpResponse("Password Changed")


# def dept(request):
#     if request.method == "GET":
#         if not request.session.has_key('dept'):
#             request.session.flush()
#             wt1 = []
#             se1 = []
#             mc1 = []
#             cd1 = []
#             bie1 = []
#             eit1 = []
#             wt_lab1 = []
#             se_lab1 = []
#             eit_lab1 = []
#             wt_avg1 = []
#             se_avg1 = []
#             mc_avg1 = []
#             cd_avg1 = []
#             bie_avg1 = []
#             eit_avg1 = []
#             wt_lab_avg1 = []
#             se_lab_avg1 = []
#             eit_lab_avg1 = []
#             for i in A1_roll:
#                 obj1 = DataByRollNo(i)
#                 wt1.append(obj1.wt_present)
#                 se1.append(obj1.se_present)
#                 mc1.append(obj1.mc_present)
#                 cd1.append(obj1.cd_present)
#                 bie1.append(obj1.bie_present)
#                 eit1.append(obj1.eit_present)
#                 wt_lab1.append(obj1.wt_lab_present)
#                 se_lab1.append(obj1.se_lab_present)
#                 eit_lab1.append(obj1.eit_lab_present)
#                 wt_avg1.append(obj1.wt_avg)
#                 se_avg1.append(obj1.se_avg)
#                 mc_avg1.append(obj1.mc_avg)
#                 cd_avg1.append(obj1.cd_avg)
#                 bie_avg1.append(obj1.bie_avg)
#                 eit_avg1.append(obj1.eit_avg)
#                 wt_lab_avg1.append(obj1.wt_lab_avg)
#                 se_lab_avg1.append(obj1.se_lab_avg)
#                 eit_lab_avg1.append(obj1.eit_lab_avg)
#                 # print(wt)
#             data1 = list(zip(A1_roll, wt1, wt_avg1, se1, se_avg1, mc1, mc_avg1, bie1, bie_avg1, eit1, eit_avg1, cd1,
#                              cd_avg1, wt_lab1, wt_lab_avg1, se_lab1, se_lab_avg1, eit_lab1, eit_lab_avg1))
#
#             wt2 = []
#             se2 = []
#             mc2 = []
#             cd2 = []
#             bie2 = []
#             eit2 = []
#             wt_lab2 = []
#             se_lab2 = []
#             eit_lab2 = []
#             wt_avg2 = []
#             se_avg2 = []
#             mc_avg2 = []
#             cd_avg2 = []
#             bie_avg2 = []
#             eit_avg2 = []
#             wt_lab_avg2 = []
#             se_lab_avg2 = []
#             eit_lab_avg2 = []
#             for i in A2_roll:
#                 obj2 = DataByRollNo(i)
#                 wt2.append(obj2.wt_present)
#                 se2.append(obj2.se_present)
#                 mc2.append(obj2.mc_present)
#                 cd2.append(obj2.cd_present)
#                 bie2.append(obj2.bie_present)
#                 eit2.append(obj2.eit_present)
#                 wt_lab2.append(obj2.wt_lab_present)
#                 se_lab2.append(obj2.se_lab_present)
#                 eit_lab2.append(obj2.eit_lab_present)
#                 wt_avg2.append(obj2.wt_avg)
#                 se_avg2.append(obj2.se_avg)
#                 mc_avg2.append(obj2.mc_avg)
#                 cd_avg2.append(obj2.cd_avg)
#                 bie_avg2.append(obj2.bie_avg)
#                 eit_avg2.append(obj2.eit_avg)
#                 wt_lab_avg2.append(obj2.wt_lab_avg)
#                 se_lab_avg2.append(obj2.se_lab_avg)
#                 eit_lab_avg2.append(obj2.eit_lab_avg)
#                 # print(wt)
#             data2 = list(zip(A2_roll, wt2, wt_avg2, se2, se_avg2, mc2, mc_avg2, bie2, bie_avg2, eit2, eit_avg2, cd2,
#                              cd_avg2, wt_lab2, wt_lab_avg2, se_lab2, se_lab_avg2, eit_lab2, eit_lab_avg2))
#             return render(request, 'Students_attendance_data.html', {'data1': data1,
#                                                                      'data2': data2,
#                                                                      'wt_total1': wt_total1,
#                                                                      'wt_req1': wt_req1,
#                                                                      'wt_lab_total1': wt_lab_total1,
#                                                                      'wt_lab_req1': wt_lab_req1,
#                                                                      'se_total1': se_total1,
#                                                                      'se_req1': se_req1,
#                                                                      'se_lab_total1': se_lab_total1,
#                                                                      'se_lab_req1': se_lab_req1,
#                                                                      'eit_total1': eit_total1,
#                                                                      'eit_req1': eit_req1,
#                                                                      'eit_lab_total1': eit_lab_total1,
#                                                                      'eit_lab_req1': eit_lab_req1,
#                                                                      'cd_total1': cd_total1,
#                                                                      'cd_req1': cd_req1,
#                                                                      'mc_total1': mc_total1,
#                                                                      'mc_req1': mc_req1,
#                                                                      'bie_total1': bie_total1,
#                                                                      'bie_req1': bie_req1,
#                                                                      'date': auth_date,
#                                                                      'se_lab_total2': se_lab_total2})
#         return render(request, 'Error.html', {'login_error': True})
#     else:
#         return HttpResponse("Bad Request")


def dept_login(request):
    if request.method == "POST":
        form = Teachers_login(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            print(name,password)

            user = Auth.objects.filter(name=name.lower()).first()
            if user:
                if user.password == password:
                    request.session['dept'] = name
                    return redirect('/dept')
                else:
                    return render(request, 'authlogin.html', {'error': 'Incorrect password'})
            else:
                return render(request, 'authlogin.html', {'error': 'User not found'})
    elif request.method == "GET":
        return render(request, 'authlogin.html', {})


def feedback(request):
    if request.method == "POST":
        form = Feedback_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            roll_no = form.cleaned_data['roll_no']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(message)
            feed = Query(name=name, roll_no=roll_no, email=email, message=message)
            try:
                feed.save()
            except:
                return render(request, 'Error.html', {'error': True})
            print('saved')
            return render(request, 'Error.html', {'feed': True})
    elif request.method == "GET":
        return render(request, 'Feedback.html', {})


def error(request):
    return redirect('/')


def dept(request):
    print("dept")
    if request.method == "GET":
        print("get")
        if request.session.has_key('dept'):
            del request.session['dept']
            auth_date = datetime.datetime.now().replace(microsecond=0)
            a1_lecture_data = present_and_avg(A1_roll)
            a2_lecture_data = present_and_avg(A2_roll)
            a1_req = req_lectures(6315010)
            a2_req = req_lectures(6315037)
            a1_total = total_lectures(6315010)
            a2_total = total_lectures(6315037)
            return render(request, 'Students_attendance_data.html', {'a1_total': a1_total,
                                                                     'a2_total': a2_total,
                                                                     'a1_req': a1_req,
                                                                     'a2_req': a2_req,
                                                                     'a1_data': a1_lecture_data,
                                                                     'a2_data': a2_lecture_data,
                                                                     'date': auth_date})
        else:
            return render(request, 'Error.html', {'login_error': True})
    else:
        return HttpResponse("Bad Request")
