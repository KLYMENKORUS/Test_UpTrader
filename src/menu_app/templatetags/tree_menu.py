from django import template
from menu_app.models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_slug):
    menu = Menu.objects.get(slug=menu_slug)
    items = menu.items.filter(parent=None)
    request = context['request']
    return render_menu_items(items, request)


def render_menu_items(items, request):
    result = ''
    for item in items:
        active_class = 'active' if item.url == request.path else ''
        children = item.children.all()
        has_children_class = 'has-children' if children else ''
        result += f'<li class="{has_children_class}">'
        result += f'<a href="{item.url}" class="{active_class}">{item.name}</a>'
        if children:
            result += '<ul>'
            result += render_menu_items(children, request)
            result += '</ul>'
        result += '</li>'
    return result
