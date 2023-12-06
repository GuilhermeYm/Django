from django.views.generic import ListView, CreateView
from .models import Todo

# Create your views here.


class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo