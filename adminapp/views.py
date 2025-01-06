from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')


@login_required_decorator
def home_page(request):
    faculties = services.get_faculties()
    kafedras = services.get_kafedra()
    subjects = services.get_subject()
    teachers = services.get_teacher()
    groups = services.get_group()
    students = services.get_students()
    ctx = {
        'counts': {
            'faculties': len(faculties),
            'kafedras': len(kafedras),
            'subjects': len(subjects),
            'teachers': len(teachers),
            'groups': len(groups),
            'students': len(students),
        }
    }
    return render(request, 'index.html', ctx)


@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        "form": form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return redirect('faculty_list')


@login_required_decorator
def faculty_list(request):
    faculties = services.get_faculties()
    print(faculties)
    ctx = {
        "faculties": faculties
    }
    return render(request, 'faculty/list.html', ctx)


# KAFEDRA
@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        "form": form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_edit(request, pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_delete(request, pk):
    model = Kafedra.objects.get(pk=pk)
    model.delete()
    return redirect('kafedra_list')


@login_required_decorator
def kafedra_list(request):
    kafedras = services.get_kafedra()
    ctx = {
        "kafedras": kafedras
    }
    return render(request, 'kafedra/list.html', ctx)

# SUBJECT
@login_required_decorator
def subject_create(request):
    model = Subject()
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {
        "form": form
    }
    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_edit(request, pk):
    model = Subject.objects.get(pk=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_delete(request, pk):
    model = Subject.objects.get(pk=pk)
    model.delete()
    return redirect('subject_list')


@login_required_decorator
def subject_list(request):
    subjects = services.get_subject()
    ctx = {
        "subjects": subjects
    }
    return render(request, 'subject/list.html', ctx)

# TEACHERS

@login_required_decorator
def teacher_create(request):
    model = Teacher()
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teachers_list')
    ctx = {
        "form": form
    }
    return render(request, 'teachers/form.html', ctx)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teacher.objects.get(pk=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teachers_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'teachers/form.html', ctx)


@login_required_decorator
def teacher_delete(request, pk):
    model = Teacher.objects.get(pk=pk)
    model.delete()
    return redirect('teachers_list')


@login_required_decorator
def teachers_list(request):
    teachers = services.get_teacher()
    ctx = {
        "teachers": teachers
    }
    return render(request, 'teachers/list.html', ctx)

# GROUP

@login_required_decorator
def group_create(request):
    model = Group()
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('groups_list')
    ctx = {
        "form": form
    }
    return render(request, 'groups/form.html', ctx)


@login_required_decorator
def group_edit(request, pk):
    model = Group.objects.get(pk=pk)
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('groups_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'groups/form.html', ctx)


@login_required_decorator
def group_delete(request, pk):
    model = Group.objects.get(pk=pk)
    model.delete()
    return redirect('groups_list')


@login_required_decorator
def groups_list(request):
    groups = services.get_group()
    print(groups)
    ctx = {
        "groups": groups
    }
    return render(request, 'groups/list.html', ctx)

# STUDENTS

@login_required_decorator
def student_create(request):
    model = Student()
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('students_list')
    ctx = {
        "form": form
    }
    return render(request, 'students/form.html', ctx)


@login_required_decorator
def student_edit(request, pk):
    model = Student.objects.get(pk=pk)
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('students_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'students/form.html', ctx)


@login_required_decorator
def student_delete(request, pk):
    model = Student.objects.get(pk=pk)
    model.delete()
    return redirect('students_list')


@login_required_decorator
def students_list(request):
    students = services.get_students()
    ctx = {
        "students": students
    }
    return render(request, 'students/list.html', ctx)
