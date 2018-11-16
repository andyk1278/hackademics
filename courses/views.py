from django.shortcuts import render
from courses.models import Track, Topic, Teacher, Course


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_courses = Course.objects.all().count()

    # Number of different tracks
    num_tracks = Track.objects.all().count()

    # Courses with difficulty 'beginner'
    num_courses_beginner = Course.objects.filter(difficulty__exact='b').count()

    # the 'all()' is implied by default.
    num_teachers = Teacher.objects.count()

    context = {
        'num_courses': num_courses,
        'num_tracks': num_tracks,
        'num_courses_beginner': num_courses_beginner,
        'num_teachers': num_teachers,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)