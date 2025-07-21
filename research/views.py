from django.shortcuts import render, get_object_or_404

from .models import ResearchPaper




def rehome(request):

    ResearchPapers = ResearchPaper.objects.all()

    return render(request, 'research/rehome.html',{'ResearchPapers':ResearchPapers})

