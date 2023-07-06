from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from page.models import Page




FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/200" for id in range(24,28)
]

def index_view(request):
    page_title = "Anasayfa"
    context = dict(
        page_title = page_title,
        # FAKE_DB_PROJECT = FAKE_DB_PROJECT,
        FAKE_DB_CAROUSEL = FAKE_DB_CAROUSEL,
    )
    return render(request, "page/index.html", context)



def page_view(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    context = dict(
        page=page,
    )
    return render(request, "page/page_detail.html", context)


