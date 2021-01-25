from django import template

register = template.Library()


@register.filter
def get_dic_element(dictionary, key):
    if hasattr('dictionary', 'get'):
        return dictionary.get(key, None)
    else:
        try:
            return dictionary[key]
        except KeyError:
            return None
