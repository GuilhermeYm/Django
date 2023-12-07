from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .models import Todo
from django.shortcuts import get_object_or_404, redirect
from datetime import date
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
    success_url = reverse_lazy("home")
class TodoCompleteView(View): 
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.finshed_at = date.today()
        todo.save()
        return redirect("home")