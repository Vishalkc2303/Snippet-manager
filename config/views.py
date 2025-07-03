from django.contrib.auth.models import User
from core.models import Snippet, Language
from django.shortcuts import render

def home(request):
    snippets = Snippet.objects.filter(visibility='public').order_by('-created_at')
    
    public_snippet_count = snippets.count()
    user_count = User.objects.count()
    language_count = Language.objects.count()

    return render(request, 'home.html', {
        'snippets': snippets,
        'public_snippet_count': public_snippet_count,
        'user_count': user_count,
        'language_count': language_count
    })