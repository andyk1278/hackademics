from django.shortcuts import render, get_object_or_404
from courses.models import Track, Topic, Teacher, Course
from django.views import generic


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


class CourseListView(generic.ListView):
    model = Course
    paginate_by = 10

# class CourseDetailView(generic.DetailView):
#     model = Course
def course_detail_view(request, primary_key):
    course = get_object_or_404(Course, primary_key)
    return render(request, 'courses/course_detail.html', context={'course': course})

class TeacherListView(generic.ListView):
    model = Teacher

class TeacherDetailView(generic.DetailView):
    model = Teacher