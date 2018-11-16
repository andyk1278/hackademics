from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    # path('course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    re_path(r'^course/(?P<pk>\d+)$', views.course_detail_view, name='course-detail'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
]