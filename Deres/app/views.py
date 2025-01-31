from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import User, Program, Split, Exercise, SplitExercise
from .forms import UserForm, ProgramForm, SplitForm, ExerciseForm, SplitExerciseForm
from django.db.models import Count, Avg

class HomePageView(TemplateView):
    template_name = 'app/home.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'


class ProductPageView(TemplateView):
    template_name = 'app/product.html'


# User Views
class UserListView(ListView):
    model = User
    template_name = 'app/user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    template_name = 'app/user_detail.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'app/user_form.html'
    fields = ['username', 'email', 'gender', 'height', 'weight', 'goal']
    success_url = reverse_lazy('user_list')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'app/user_update.html'
    fields = ['username', 'email', 'gender', 'height', 'weight', 'goal']
    success_url = reverse_lazy('user_list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'app/user_delete.html'
    success_url = reverse_lazy('user_list')


class ProgramUpdateView(UpdateView):
    model = Program
    fields = ['user', 'program_name', 'goal', 'duration_weeks']
    template_name = 'app/program_update.html'


class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'app/program_delete.html'
    success_url = reverse_lazy('program_list')


class ProgramDetailView(DetailView):
    model = Program
    context_object_name = 'prog'
    template_name = 'app/program_detail.html'


# Program Views
def program_list(request):
    programs = Program.objects.all()
    return render(request, 'app/program_list.html', {'programs': programs})


def program_add(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm()
    return render(request, 'app/program_form.html', {'form': form, 'title': 'Add New Program'})


def program_edit(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm(instance=program)
    return render(request, 'app/program_form.html', {'form': form, 'title': 'Edit Program'})


def program_delete(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    if request.method == 'POST':
        program.delete()
        return redirect('program_list')
    return render(request, 'app/program_confirm_delete.html', {'program': program})


def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'app/program_detail.html', {'program': program})


# Exercise Views
def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'app/exercise_list.html', {'exercises': exercises})


def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    return render(request, 'app/exercise_detail.html', {'exercise': exercise})


def exercise_create(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'app/exercise_form.html', {'form': form})


def exercise_update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == "POST":
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'app/exercise_form.html', {'form': form})


def exercise_delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == "POST":
        exercise.delete()
        return redirect('exercise_list')
    return render(request, 'app/exercise_delete.html', {'exercise': exercise})


# Split Exercise Views
def split_exercise_list(request):
    split_exercises = SplitExercise.objects.all()
    return render(request, 'app/split_exercise_list.html', {'split_exercises': split_exercises})


def split_exercise_detail(request, pk):
    split_exercise = get_object_or_404(SplitExercise, pk=pk)
    return render(request, 'app/split_exercise_detail.html', {'split_exercise': split_exercise})


def split_exercise_create(request):
    if request.method == "POST":
        form = SplitExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('split_exercise_list')
    else:
        form = SplitExerciseForm()
    return render(request, 'app/split_exercise_form.html', {'form': form})


def split_exercise_update(request, pk):
    split_exercise = get_object_or_404(SplitExercise, pk=pk)
    if request.method == "POST":
        form = SplitExerciseForm(request.POST, instance=split_exercise)
        if form.is_valid():
            form.save()
            return redirect('split_exercise_list')
    else:
        form = SplitExerciseForm(instance=split_exercise)
    return render(request, 'app/split_exercise_form.html', {'form': form})


def split_exercise_delete(request, pk):
    split_exercise = get_object_or_404(SplitExercise, pk=pk)
    if request.method == "POST":
        split_exercise.delete()
        return redirect('split_exercise_list')
    return render(request, 'app/split_exercise_delete.html', {'split_exercise': split_exercise})


# Split Views
def split_list(request):
    splits = Split.objects.all()
    return render(request, 'app/split_list.html', {'splits': splits})


def split_create(request):
    if request.method == "POST":
        form = SplitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('split_list')
    else:
        form = SplitForm()
    return render(request, 'app/split_form.html', {'form': form})


def split_update(request, pk):
    split = get_object_or_404(Split, pk=pk)
    if request.method == "POST":
        form = SplitForm(request.POST, instance=split)
        if form.is_valid():
            form.save()
            return redirect('split_list')
    else:
        form = SplitForm(instance=split)
    return render(request, 'app/split_form.html', {'form': form})


def split_delete(request, pk):
    split = get_object_or_404(Split, pk=pk)
    if request.method == "POST":
        split.delete()
        return redirect('split_list')
    return render(request, 'app/split_delete.html', {'split': split})


def split_detail(request, pk):
    split = get_object_or_404(Split, pk=pk)
    return render(request, 'app/split_detail.html', {'split': split})

def program_list(request):
    programs = Program.objects.order_by('program_name')  # Order programs alphabetically
    total_programs = programs.count()  # Count total programs
    avg_duration = programs.aggregate(Avg('duration_weeks'))  # Get average duration

    context = {
        'programs': programs,
        'total_programs': total_programs,
        'avg_duration': avg_duration['duration_weeks__avg'],
    }
    return render(request, 'app/program_list.html', context)

def exercise_list(request):
    exercises = Exercise.objects.order_by('-muscle_group')  # Order exercises by muscle group
    exercise_count = exercises.count()  # Count total exercises
    grouped_exercises = Exercise.objects.values('muscle_group').annotate(total=Count('id'))  # Group by muscle group

    context = {
        'exercises': exercises,
        'exercise_count': exercise_count,
        'grouped_exercises': grouped_exercises,
    }
    return render(request, 'app/exercise_list.html', context)

def split_exercise_list(request):
    split_exercises = SplitExercise.objects.order_by('order')  # Order by exercise order in split
    total_split_exercises = split_exercises.count()  # Count total split exercises
    avg_sets = split_exercises.aggregate(Avg('sets'))  # Get average sets
    avg_reps = split_exercises.aggregate(Avg('reps'))  # Get average reps
    avg_rest_time = split_exercises.aggregate(Avg('rest_time'))  # Get average rest time

    context = {
        'split_exercises': split_exercises,
        'total_split_exercises': total_split_exercises,
        'avg_sets': avg_sets['sets__avg'],
        'avg_reps': avg_reps['reps__avg'],
        'avg_rest_time': avg_rest_time['rest_time__avg'],
    }
    return render(request, 'app/split_exercise_list.html', context)

def split_list(request):
    splits = Split.objects.order_by('day')  # Order by day
    total_splits = splits.count()  # Count total splits
    avg_splits_per_program = Split.objects.values('program').annotate(total=Count('id')).aggregate(Avg('total'))

    context = {
        'splits': splits,
        'total_splits': total_splits,
        'avg_splits_per_program': avg_splits_per_program['total__avg'],
    }
    return render(request, 'app/split_list.html', context)