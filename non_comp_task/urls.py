from django.urls import path

from non_comp_task import views, comp_task_views

urlpatterns=[
path('',views.non_comp_task_view.as_view()),
path('/<int:id>',views.non_comp_task_view().as_view()),
path('/comptask',comp_task_views.comp_task_view().as_view())
]