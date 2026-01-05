import re
from django import template

register = template.Library()

# YouTube video id: обычно 11 символов, но иногда бывает больше/меньше в редких кейсах,
# поэтому позволяем 6..20 и отсекаем лишние параметры.
YT_PATTERNS = [
    r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?.*v=(?P<id>[\w-]{6,20})",
    r"(?:https?:\/\/)?(?:www\.)?youtu\.be\/(?P<id>[\w-]{6,20})",
    r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/shorts\/(?P<id>[\w-]{6,20})",
    r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/(?P<id>[\w-]{6,20})",
]

@register.filter
def youtube_embed(url: str) -> str:
    if not url:
        return ""
    for pattern in YT_PATTERNS:
        m = re.search(pattern, url)
        if m:
            vid = m.group("id")
            return f"https://www.youtube-nocookie.com/embed/{vid}"
    return ""
