from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .ollama import ollama_response


def home(request):
    return render(request, "home/index.html")


@login_required
def generate_movie(request):
    context = {}
    if request.method == "POST":
        person_ask = request.POST.get("person_ask")
        if person_ask:
            answer = ollama_response(person_ask)
            context["answer"] = answer

    return render(request, "generate_movie/index.html", context)
