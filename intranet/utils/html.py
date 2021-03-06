# -*- coding: utf-8 -*-

import bleach

ALLOWED_TAGS = ['a', 'abbr', 'acronym', 'b', 'br', 'blockquote', 'code', 'em', 'hr', 'i', 'li', 'ol', 'strong', 'ul', 'iframe', 'img', 'div', 'p']
ALLOWED_ATTRIBUTES = {
    'acronym': ['title'],
    'a': ['href', 'title'],
    'abbr': ['title'],
    'iframe': ['src', 'height', 'width', 'allowfullscreen', 'frameborder'],
    'img': ['src', 'alt', 'title']
}


def safe_html(txt):
    return bleach.linkify(bleach.clean(txt, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES))
