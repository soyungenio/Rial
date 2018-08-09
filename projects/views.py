from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from projects.models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_content(request):
    r = request.POST
    try:
        if int(r['type']) == 1:
            f = r["filter"]
            if int(r["all"]) == 0:
                projects_filter = ProjectType.objects.get(name=f).projects_set.all()[:4]
            else:
                projects_filter = ProjectType.objects.get(name=f).projects_set.all()
            return HttpResponse(render(request, 'main/project_items.html', locals()), content_type='text/plain')
        if int(r['type']) == 2:
            f = r["filter"]
            t = r["t"]
            projects_filter = None
            if f == 'all':
                if int(r["all"]) == 0:
                    projects_filter = ProjectType.objects.get(name=t).projects_set.all()[:4]
                else:
                    projects_filter = ProjectType.objects.get(name=t).projects_set.all()
            elif f == 'design':
                if int(r["all"]) == 0:
                    projects_filter = ProjectType.objects.get(name=t).projects_set.all().filter(design=True)[:4]
                else:
                    projects_filter = ProjectType.objects.get(name=t).projects_set.all().filter(design=True)
            elif f == 'no-design':
                if int(r["all"]) == 0:
                    projects_filter = ProjectType.objects.get(name=t).projects_set.all().filter(design=False)[:4]
                else:
                    projects_filter = ProjectType.objects.get(name=t).projects_set.all().filter(design=False)
            return HttpResponse(render(request, 'main/project_items.html', locals()), content_type='text/plain')

    except:
        return JsonResponse(r)


