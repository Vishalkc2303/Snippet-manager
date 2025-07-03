from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Snippet
from django.contrib.auth.decorators import login_required
from .models import Snippet, Language, Tag

@login_required(login_url='login')
def add_snippet(request):
    languages = Language.objects.all()
    tags = Tag.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        language_name = request.POST.get('language')  # e.g. "rust"
        code = request.POST.get('code')
        description = request.POST.get('description')
        visibility = request.POST.get('visibility')
        tag_list = request.POST.getlist('tags')  # Assuming JS/comma-separated handling

        # Get or create Language
        try:
            language_obj = Language.objects.get(name=language_name)
        except Language.DoesNotExist:
            language_obj = None  # Or handle gracefully
           
        print("up")
        if title and language_obj and code and visibility:
            snippet = Snippet.objects.create(
                user=request.user,
                title=title,
                language=language_obj,
                code=code,
                description=description,
                visibility=visibility
            )
            print("hii")

            # Tags: split comma-separated string and get/create
            for tag_name in tag_list:
                tag_obj, _ = Tag.objects.get_or_create(name=tag_name.strip())
                snippet.tags.add(tag_obj)

            return redirect('home')  # Or your snippet list page
        else:
            error = "All fields (except description) are required."
            return render(request, 'pages/add_snippet.html', {
                'languages': languages,
                'tags': tags,
                'error': error
            })

    return render(request, 'pages/add_snippet.html', {
        'languages': languages,
        'tags': tags
    })

def snippet_detail(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    return render(request, 'pages/snippet_detail.html', {'snippet': snippet})


@login_required(login_url='login')
def my_snippet(request):
    user_snippets = Snippet.objects.filter(user=request.user).order_by('-created_at')

    total_snippets = user_snippets.count()
    public_snippets = user_snippets.filter(visibility='public').count()
    private_snippets = user_snippets.filter(visibility='private').count()

    return render(request, 'pages/my_snippet.html', {
        'snippets': user_snippets,
        'total_snippets': total_snippets,
        'public_snippets': public_snippets,
        'private_snippets': private_snippets
    })


@login_required(login_url='login') 
def saved_snippet(request):
    saved = request.user.saved_snippets.all()
    return render(request, 'pages/saved_snippet.html', {'snippets': saved})

@login_required
def toggle_save_snippet(request, id):
    snippet = get_object_or_404(Snippet, id=id)

    if request.user in snippet.saved_by.all():
        snippet.saved_by.remove(request.user)  # Unsave
    else:
        snippet.saved_by.add(request.user)     # Save

    # return redirect('snippet_detail', id=id)
    return redirect('home')


# @login_required(login_url='login') 
# def add_snippet(request):
#     languages = [
#         'javascript', 'python', 'java', 'cpp', 'c', 'csharp', 'php',
#         'ruby', 'go', 'rust', 'typescript', 'html', 'css', 'sql',
#         'bash', 'other'
#     ]
#     tags = ['sorting', 'array', 'recursion', 'dynamic programming']

#     if request.method == 'POST':
#         title = request.POST.get('title')
#         language = request.POST.get('language')
#         code = request.POST.get('code')
#         description = request.POST.get('description')
#         tag_string = request.POST.get('tags')  # comma-separated tags
#         visibility = request.POST.get('visibility')

#         if title and language and code and description and visibility:
#             Snippet.objects.create(
#                 user=request.user,
#                 title=title,
#                 language=language,
#                 code=code,
#                 description=description,
#                 tags=tag_string,
#                 visibility=visibility
#             )
#             return redirect('home')  # Change to your actual view name
#         else:
#             error = "Please fill all required fields."
#             return render(request, 'add_snippet.html', {
#                 'languages': languages,
#                 'tags': tags,
#                 'error': error
#             })

#     return render(request, 'snippets/add_snippet.html', {
#         'languages': languages,
#         'tags': tags
#     })


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully.")
        return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')


# from django.contrib.auth.decorators import login_required

# @login_required
# def home(request):
#     return render(request, 'snippets/home.html', {'username': request.user.username})
