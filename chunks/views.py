from django.shortcuts import get_object_or_404, redirect
from shared.admin import get_admin_url
from chunks.models import Chunk

def edit_link(request, slug):
    chunk = get_object_or_404(Chunk, key=slug)
    url = get_admin_url(chunk)
    return redirect(url)