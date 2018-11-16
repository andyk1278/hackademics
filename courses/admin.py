from django.contrib import admin
from courses.models import Topic, Course, Teacher

# Registering models
admin.site.register(Topic)
admin.site.register(Course)
admin.site.register(Teacher)
