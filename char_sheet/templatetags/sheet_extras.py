from django import template

register = template.Library()

@register.filter
def get(mapping, key):
  return mapping.get(key, '')

@register.filter
def bold_first(value):
  s = str(value)
  s = s.split()
  if s:
    s[0] = "<b>%s</b>" % s[0]
    s = ' '.join(s)
    return s
  else:
    return ''
