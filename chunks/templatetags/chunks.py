from django import template
from django.db import models

register = template.Library()

Chunk = models.get_model('chunks', 'chunk')
CACHE_PREFIX = "chunk_"



def do_get_chunk(parser, token):
    # split_contents() knows not to split quoted strings.
    """
    Usage:
      {% chunk "chunk_name" %} print chunk contents
      {% chunk "chunk_name" as var_name %} places chunk object to "var_name" context variable.
    """
    tokens = token.split_contents()
    if len(tokens) not in (2, 4):
        raise template.TemplateSyntaxError, "%r tag should have either 2 or 4 arguments" % (tokens[0],)
    tag_name, key = tokens[:2]
    if len(tokens) == 4:
        if tokens[2] != 'as':
            raise template.TemplateSyntaxError, "invalid syntax of %r tag" % tokens[0]
        var_name = tokens[3]
    else:
        var_name = None
    def check_quotes(value):
        """Check to see if the value is properly double/single quoted"""
        if not (value[0] == value[-1] and value[0] in ('"', "'")):
            raise ValueError
        return value[1:-1]
    try:
        key = check_quotes(key)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    return ChunkNode(key, var_name)

    
class ChunkNode(template.Node):

    def __init__(self, key, var_name):
       self.key = key
       self.var_name = var_name
    
    def render(self, context):
        chunk = Chunk.objects.get_or_create(key=self.key)[0]
        if self.var_name:
            context[self.var_name] = chunk
            return ''
        else:
            return chunk.content if chunk else ''
        
register.tag('chunk', do_get_chunk)
