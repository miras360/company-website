import re
from django import template

register = template.Library()

YOUTUBE_REGEX = [
    r'youtu\.be/(?P<id>[\w-]{6,})',
    r'youtube\.com/watch\?v=(?P<id>[\w-]{6,})',
    r'youtube\.com/embed/(?P<id>[\w-]{6,})',
    r'youtube\.com/shorts/(?P<id>[\w-]{6,})',
]

@register.filter
def youtube_embed(url):
    if not url:
        return ""
    for pattern in YOUTUBE_REGEX:
        m = re.search(pattern, url)
        if m:
            vid = m.group('id')
            return f"https://www.youtube-nocookie.com/embed/{vid}"
    return ""