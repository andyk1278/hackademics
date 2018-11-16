from django.contrib import admin
from courses.models import Track, Topic, Course, Teacher

# Registering models
# admin.site.register(Topic)
# admin.site.register(Course)
# admin.site.register(Teacher)

# Define the admin class
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'email')
    fields = ['first_name', 'last_name', ('date_of_birth', 'email')]
# Register the admin class with the associated model
admin.site.register(Teacher, TeacherAdmin)

# tabular inline course editing for courses on the same track
class CourseInline(admin.TabularInline):
    model = Course

# Register the admin class for Track using the decorator
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'language')
    inlines = [CourseInline]


# Register the Admin classes for Topic using the decorator
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    sortable_by = ['name']

# Register the Admin classes for Course using the decorator
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # list_display = ('title', 'teacher', 'display_topic', 'track', 'difficulty')
    list_filter = ('track', 'difficulty')
    fieldsets = (
        (None, {
            'fields': ('title', 'topics', 'teacher')
        }),
        ('Track', {
            'fields': ('track', 'difficulty')
        }),
    )
    # fields = ['title', 'teacher', 'display_topic', ('track', 'difficulty')]