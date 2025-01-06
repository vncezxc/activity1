from django.db import models
from django.urls import reverse

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    goal = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Program(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=100)
    goal = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    duration_weeks = models.IntegerField()

    def __str__(self):
        return f"{self.program_name} ({self.user.username})"
    
    def get_absolute_url(self):
        return reverse('program_detail', kwargs={"pk": self.pk})


class Split(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    day = models.IntegerField()
    split_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.split_name} - Day {self.day} ({self.program.program_name})"


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=50)
    equipment_needed = models.CharField(max_length=50)
    exercise_type = models.CharField(max_length=50)

    def __str__(self):
        return self.exercise_name


class SplitExercise(models.Model):
    split = models.ForeignKey(Split, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.IntegerField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest_time = models.IntegerField(help_text="Rest time in seconds")

    def __str__(self):
        return f"{self.exercise.exercise_name} in {self.split.split_name}"

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    muscle_mass_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Progress on {self.date} for {self.user.username}"

