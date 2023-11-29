from django.urls import path
from .views import home, task, submission

urlpatterns = [
    path('', home),
    path('home/', home),
    path('task/', task),
    path('submission/', submission),
]
