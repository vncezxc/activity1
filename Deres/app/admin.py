from django.contrib import admin
from .models import User, Program, Split, Exercise, SplitExercise 


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'gender', 'height', 'weight', 'goal', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('gender', 'goal')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'user', 'goal', 'duration_weeks', 'created_at')
    search_fields = ('program_name', 'user__username', 'goal')
    list_filter = ('goal', 'duration_weeks')


@admin.register(Split)
class SplitAdmin(admin.ModelAdmin):
    list_display = ('split_name', 'program', 'day')
    search_fields = ('split_name', 'program__program_name')
    list_filter = ('day',)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise_name', 'muscle_group', 'equipment_needed', 'exercise_type')
    search_fields = ('exercise_name', 'muscle_group', 'equipment_needed')
    list_filter = ('muscle_group', 'exercise_type')


@admin.register(SplitExercise)
class SplitExerciseAdmin(admin.ModelAdmin):
    list_display = ('split', 'exercise', 'order', 'sets', 'reps', 'rest_time')
    search_fields = ('split__split_name', 'exercise__exercise_name')
    list_filter = ('split__split_name',)




