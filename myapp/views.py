from django.shortcuts import render, redirect
from .models import Resume, User

# Create your views here.

def home(request):
    return render(request, 'index.html')

def logout(request):
    # Clear the session
    request.session.flush()
    # Redirect to home or login page
    return redirect('login')


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        # Check if the user already exists
        user = User.objects.filter(name=name).first()

        if user:
            # If user exists, check if the password matches
            if user.password == password:
                request.session['user_id'] = user.id  # Store user id in session
                return redirect('build_resume')
            else:
                error = 'Invalid credentials. Please try again.'
                return render(request, 'login.html', {'error': error})
        else:
            # If user doesn't exist, create a new user
            user = User.objects.create(name=name, password=password)
            request.session['user_id'] = user.id  # Store user id in session
            return redirect('build_resume')

    return render(request, 'login.html')

from django.shortcuts import render, redirect
from .models import User, Resume

def build_resume(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if not logged in

    user = User.objects.get(id=user_id)
    resume = Resume.objects.filter(user=user).first()

    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'profile': request.POST.get('profile'),
            'about': request.POST.get('about'),
            'degree': request.POST.get('degree'),
            'college': request.POST.get('college'),
            'degree_year': request.POST.get('degree_year'),
            'organization': request.POST.get('company'),
            'designation': request.POST.get('designation'),
            'exp_year': request.POST.get('exp_year'),
            'project': request.POST.get('project'),
            'desc': request.POST.get('desc'),
            'skill': request.POST.get('skill'),
            'tool': request.POST.get('tool'),
            'user': user,
        }

        if resume:
            # Update existing resume
            for key, value in data.items():
                setattr(resume, key, value)
            resume.save()
        else:
            # Create new resume
            resume = Resume.objects.create(**data)

        # Redirect to the demo resume view
        return redirect('demo_templates')

    if resume:
        data = {
            'name': resume.name,
            'email': resume.email,
            'phone': resume.phone,
            'profile': resume.profile,
            'about': resume.about,
            'degree': resume.degree,
            'college': resume.college,
            'degree_year': resume.degree_year,
            'organization': resume.organization,
            'designation': resume.designation,
            'exp_year': resume.exp_year,
            'project': resume.project,
            'desc': resume.desc,
            'skill': resume.skill,
            'tool': resume.tool,
        }
        return render(request, 'resume.html', {'data': data})
    else:
        return render(request, 'resume.html', {'data': {}})



# def demo_templates(request):
#     return render(request, 'demo_templates.html')

def demo_templates(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = User.objects.get(id=user_id)
    resume = Resume.objects.filter(user=user).first()

    if resume:
        data = {
            'name': resume.name,
            'email': resume.email,
            'phone': resume.phone,
            'profile': resume.profile,
            'about': resume.about,
            'degree': resume.degree,
            'college': resume.college,
            'degree_year': resume.degree_year,
            'organization': resume.organization,
            'designation': resume.designation,
            'exp_year': resume.exp_year,
            'project': resume.project,
            'desc': resume.desc,
            'skill': resume.skill,
            'tool': resume.tool,
        }
        return render(request, 'demo_templates.html', {'data': data})
    else:
        return redirect('build_resume')
