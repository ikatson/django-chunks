from django.views.decorators.http import require_POST

from django.shortcuts import get_object_or_404, redirect
from shared.admin import get_admin_url
from chunks.models import Chunk

def edit_link(request, slug):
    """Get a URL to edit chunk."""
    chunk = get_object_or_404(Chunk, key=slug)
    url = get_admin_url(chunk)
    return redirect(url)
