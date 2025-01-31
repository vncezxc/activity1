from django import forms
from .models import User, Program, Split, Exercise, SplitExercise

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'gender', 'height', 'weight', 'goal']

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['user', 'program_name', 'goal', 'duration_weeks']

class SplitForm(forms.ModelForm):
    class Meta:
        model = Split
        fields = ['program', 'day', 'split_name']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise_name', 'muscle_group', 'equipment_needed', 'exercise_type']

class SplitExerciseForm(forms.ModelForm):
    class Meta:
        model = SplitExercise
        fields = ['split', 'exercise', 'order', 'sets', 'reps', 'rest_time']
