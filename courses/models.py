from django.db import models
from django.urls import reverse # Used to genereate URLs by reversing the URL patterns


# Create your models here.
class Topic(models.Model):
    """Model representing the various topics the describe any course."""
    name = models.CharField(max_length=200, help_text='Enter a unique topic the describes a course.', unique=True)

    def __str__(self):
        """String for representing the Topic Model object."""
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(verbose_name='Course Description', help_text='Description of this course.')

    # Foreign key used because a course can only have one teacher, but teachers
    # may teach several courses
    # 'Teacher' as a string rather than an object because it hasn't been
    # declared yet in the file
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    topics = models.ManyToManyField(Topic, help_text='Select all relevant topics to this course.')

    LEVEL = (
        ('a', 'Advanced'),
        ('i', 'Intermediate'),
        ('b', 'Beginner'),
        ('o', 'Other'),
    )

    difficulty = models.CharField(
        max_length=1,
        choices=LEVEL,
        blank=True,
        default='o',
        help_text='The level of difficulty of the course.',
    )

    LANGUAGES = (
        ('py', 'Python'),
        ('pe', 'Perl'),
        ('ja', 'Java'),
        ('cpp', 'C++'),
        ('js', 'Javascript'),
        ('sc', 'Scala'),
        ('php', 'PHP'),
        ('csh', 'C#'),
        ('go', 'Go'),
        ('ht', 'HTML'),
        ('hsk', 'Haskell'),
    )

    track = models.CharField(
        max_length=3,
        choices=LANGUAGES,
        blank=True,
        help_text='The programming language the course is being taught in.',
    )

    def __str__(self):
        """String for representing the Course Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this course."""
        return reverse('course-detail', args=[str(self.id)])


class Teacher(models.Model):
    """Model representing a teacher."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('teacher-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Teacher Model object."""
        return f'{self.last_name}, {self.first_name}'
