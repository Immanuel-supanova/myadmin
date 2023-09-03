from bokeh.resources import INLINE
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView

from myadmin.graphs import year_graph, month_graph, today_pie_chart, yesterday_pie_chart, past_7_days_graph

js_resources = INLINE.render_js()
css_resources = INLINE.render_css()


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

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['year_graph'] = year_graph()
        context['month_graph'] = month_graph()
        context['today_pie_chart'] = today_pie_chart()
        context['yesterday_pie_chart'] = yesterday_pie_chart()
        context['past_7_days_graph'] = past_7_days_graph()

        context['css'] = css_resources
        context['js'] = js_resources
        return context
