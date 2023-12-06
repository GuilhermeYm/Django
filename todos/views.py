from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo

# Create your views here.


class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "dead_line"]
    success_url=reverse_lazy("home")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "dead_line"]
    success_url = reverse_lazy("home")
class TodoDeleteView(DeleteView):
    model = Todo