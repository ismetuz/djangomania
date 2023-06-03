from django.shortcuts import render
from django.http import HttpResponse, Http404
from .fake_db.pages import FAKE_DB_PAGES



# Create your views here.

# FAKE_DB_PROJECT = [
#     f"https://picsum.photos/id/{id}/400/250" for id in range(71,79)
#     ] 

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



def page_view(request, slug):
    result = list(filter(lambda x: (x['url'] == slug), FAKE_DB_PAGES))
    context = dict()
        # FAKE_DB_PROJECT = FAKE_DB_PROJECT,
    if result:
        context = dict(
            page_title = result[0]["title"],
            # FAKE_DB_PROJECT = FAKE_DB_PROJECT,
            detail = result[0]["detail"]
            )
        return render(request, "page/page_detail.html", context)
    raise Http404("Sayfa Bulunamadı")

