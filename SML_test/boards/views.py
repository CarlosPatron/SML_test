from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .models import Board, Topic, Post
from .forms import newTopicForm

# Create your views here.
def home(request):
    boards = Board.objects.all()

    return render(request, "home.html", {"boards": boards})

def about(request):
    print("a")
    return render(request, "about.html")

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)

    return render(request, "topics.html", {"board": board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()

    if request.method == "POST":
        form = newTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message = form.cleaned_data.get("message"),
                topic = topic,
                created_by = user

            )
            return redirect("board_topics", pk=board.pk)
    else:
        form = newTopicForm()
    
    return render(request, "new_topic.html", {"board": board, "form": form})