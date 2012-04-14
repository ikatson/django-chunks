from django import forms
from django.contrib import admin

from models import Chunk

from ckeditor_extras.widgets import CKEditorToggleWidget


class CKEditorContentAdminForm(forms.ModelForm):
  content = forms.CharField(widget=CKEditorToggleWidget())


class ChunkAdmin(admin.ModelAdmin):
  list_display = ('key','description',)
  search_fields = ('key', 'content')
  form = CKEditorContentAdminForm

admin.site.register(Chunk, ChunkAdmin)
