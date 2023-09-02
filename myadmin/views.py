from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.

class MyadminMixin:
    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['title'] = self.title
        return context


class HomeView(LoginRequiredMixin, MyadminMixin, TemplateView):
    template_name = 'myadmin/home.html'
    title = 'myadmin|home'
