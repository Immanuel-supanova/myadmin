from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView


# Create your views here.

class MyadminMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['title'] = self.title
        return context


class HomeView(LoginRequiredMixin, MyadminMixin, TemplateView):
    template_name = 'myadmin/home.html'
    title = 'myadmin|home'
