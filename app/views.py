from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import User, Program, Split, Exercise, SplitExercise
from .forms import UserForm, ProgramForm, SplitForm, ExerciseForm, SplitExerciseForm

class HomePageView (TemplateView):
    template_name = 'app/home.html'

class AboutPageView (TemplateView):
    template_name = 'app/about.html'

class ProductPageView (TemplateView):
    template_name = 'app/product.html'




# List View for Home Page
class HomePageView(TemplateView):
    template_name = 'app/home.html'


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
    fields = [ 'user', 'program_name', 'goal', 'duration_weeks']
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


def program_detail(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    return render(request,  'app/program_detail.html', {'program': program})

 