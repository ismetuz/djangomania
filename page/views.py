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

def about_us_view(request):
    page_title = "Hakkımızda"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam hendrerit accumsan arcu sed eleifend. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed ultrices ex orci, sit amet pellentesque libero volutpat at. Nam interdum, mi non tincidunt molestie, massa ex malesuada ante, quis egestas ligula risus non lacus. Integer eget risus nec est lacinia scelerisque sed et nibh. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque molestie felis eget turpis sagittis, et faucibus tellus congue. Nam aliquam quis nunc eu congue. Donec posuere metus nulla, vitae mattis mi ultricies et. Etiam venenatis, tortor sit amet sodales molestie, enim velit cursus nulla, sit amet finibus ante est vitae leo. Nam ullamcorper enim at velit ultrices, eget elementum purus bibendum. Curabitur egestas quam odio, non fringilla est fringilla vitae. Nullam at turpis ipsum. Sed a malesuada nisi."
    context = dict(
        page_title = page_title,
        hero_content = hero_content,
        # FAKE_DB_PROJECT = FAKE_DB_PROJECT,
    )
    return render(request, 'page/about_us.html', context)

def contact_us_view(request):
    page_title = "İletişim"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam hendrerit accumsan arcu sed eleifend. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed ultrices ex orci, sit amet pellentesque libero volutpat at. Nam interdum, mi non tincidunt molestie, massa ex malesuada ante, quis egestas ligula risus non lacus. Integer eget risus nec est lacinia scelerisque sed et nibh. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque molestie felis eget turpis sagittis, et faucibus tellus congue. Nam aliquam quis nunc eu congue. Donec posuere metus nulla, vitae mattis mi ultricies et. Etiam venenatis, tortor sit amet sodales molestie, enim velit cursus nulla, sit amet finibus ante est vitae leo. Nam ullamcorper enim at velit ultrices, eget elementum purus bibendum. Curabitur egestas quam odio, non fringilla est fringilla vitae. Nullam at turpis ipsum. Sed a malesuada nisi."
    context = dict(
        page_title = page_title,
        hero_content = hero_content,
        # FAKE_DB_PROJECT = FAKE_DB_PROJECT,
    )
    return render(request, 'page/contact_us.html', context)

def visions_view(request):
    page_title = "Vizyonumuz"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam hendrerit accumsan arcu sed eleifend. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed ultrices ex orci, sit amet pellentesque libero volutpat at. Nam interdum, mi non tincidunt molestie, massa ex malesuada ante, quis egestas ligula risus non lacus. Integer eget risus nec est lacinia scelerisque sed et nibh. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque molestie felis eget turpis sagittis, et faucibus tellus congue. Nam aliquam quis nunc eu congue. Donec posuere metus nulla, vitae mattis mi ultricies et. Etiam venenatis, tortor sit amet sodales molestie, enim velit cursus nulla, sit amet finibus ante est vitae leo. Nam ullamcorper enim at velit ultrices, eget elementum purus bibendum. Curabitur egestas quam odio, non fringilla est fringilla vitae. Nullam at turpis ipsum. Sed a malesuada nisi."
    context = dict(
        page_title = page_title,
        hero_content = hero_content,
        # FAKE_DB_PROJECT = FAKE_DB_PROJECT,
    )
    return render(request, 'page/vision.html', context)


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

