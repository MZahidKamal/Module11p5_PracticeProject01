from django.urls import path
from .views import home, task, meals, submission

urlpatterns = [
    path('', home),
    path('home/', home),
    path('task/', task),
    path('meals/', meals),
    path('submission/', submission),
]
