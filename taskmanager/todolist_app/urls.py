from todolist_app import views

urlpatterns = [
    path('/', views.todolist, name='todolist'),
]
