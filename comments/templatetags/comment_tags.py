from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='n_level_comments')
def n_level_comments(comments, level):
	return comments.filter(comment_level=level)