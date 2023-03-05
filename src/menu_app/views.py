from .models import Menu
from django.views.generic import TemplateView


class MenuItemView(TemplateView):
    template_name = 'menu_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_slug = kwargs.get('menu_slug')
        menu = Menu.objects.get(slug=menu_slug)
        context['items'] = menu.items.filter(parent=None)
        return context


