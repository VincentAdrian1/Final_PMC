from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Contractor, Project, Experience, Skill

def paginate_items(request, items, items_per_page):
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    paginated_items = paginator.get_page(page_number)
    return paginated_items

def home(request):
    return render(request, 'home.html', {})

def contractor_view(request):
    all_contractors = Contractor.objects.all()
    contractor_list = paginate_items(request, all_contractors, 5)
    return render(request, 'contractor.html', {'contractors': contractor_list})

def project_view(request):
    all_projects = Project.objects.all()
    project_list = paginate_items(request, all_projects, 4)
    return render(request, 'project.html', {'projects': project_list})

def experience_view(request):
    all_experiences = Experience.objects.all()
    experience_list = paginate_items(request, all_experiences, 4)
    return render(request, 'experience.html', {'experiences': experience_list})

def skill_view(request):
    all_skills = Skill.objects.all()
    skill_list = paginate_items(request, all_skills, 5)
    return render(request, 'skill.html', {'skills': skill_list})
