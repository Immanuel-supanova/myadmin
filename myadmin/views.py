from bokeh.resources import INLINE
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from django.views.generic import TemplateView, DetailView

from myadmin.graphs import LogGraph, LogAppGraph, LogUserGraph, LogModelGraph

js_resources = INLINE.render_js()
css_resources = INLINE.render_css()

now = timezone.now()

User = get_user_model()


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

        context['year_graph'] = LogGraph(year=now.year).past_years(10)
        context['month_graph'] = LogGraph(year=now.year).year_graph()
        context['today_pie_chart'] = LogGraph(date=now.date()).date_pie_chart(day="today")
        context['yesterday_pie_chart'] = LogGraph(date=now - timezone.timedelta(days=1)).date_pie_chart(day="yesterday")
        context['past_7_days_graph'] = LogGraph(date=now.date()).past_days_graph(7)

        context['css'] = css_resources
        context['js'] = js_resources
        return context


class AccountAppView(LoginRequiredMixin, MyadminMixin, TemplateView):
    template_name = 'myadmin/home.html'
    title = 'myadmin|Account'

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['year_graph'] = LogAppGraph(year=now.year, app="accounts").past_years(10)
        context['month_graph'] = LogAppGraph(year=now.year, app="accounts").year_graph()
        context['today_pie_chart'] = LogAppGraph(date=now.date(), app="accounts").date_pie_chart(day="today")
        context['yesterday_pie_chart'] = LogAppGraph(date=now - timezone.timedelta(days=1),
                                                     app="accounts").date_pie_chart(day="yesterday")
        context['past_7_days_graph'] = LogAppGraph(date=now.date(), app="accounts").past_days_graph(7)

        context['css'] = css_resources
        context['js'] = js_resources
        return context


class UserModelView(LoginRequiredMixin, MyadminMixin, TemplateView):
    template_name = 'myadmin/home.html'
    title = 'myadmin|Account|User'

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['year_graph'] = LogModelGraph(year=now.year, app="accounts", model='user').past_years(10)
        context['month_graph'] = LogModelGraph(year=now.year, app="accounts", model='user').year_graph()
        context['today_pie_chart'] = LogModelGraph(date=now.date(), app="accounts", model='user').date_pie_chart(
            day="today")
        context['yesterday_pie_chart'] = LogModelGraph(date=now - timezone.timedelta(days=1),
                                                       app="accounts", model='user').date_pie_chart(day="yesterday")
        context['past_7_days_graph'] = LogModelGraph(date=now.date(), app="accounts", model='user').past_days_graph(7)

        context['css'] = css_resources
        context['js'] = js_resources
        return context


class UserModelDetailView(LoginRequiredMixin, MyadminMixin, DetailView):
    template_name = 'myadmin/home.html'
    title = 'myadmin|User'
    model = User

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['year_graph'] = LogUserGraph(year=now.year, pk=self.object.id).past_years(10)
        context['month_graph'] = LogUserGraph(year=now.year, pk=self.object.id).year_graph()
        context['today_pie_chart'] = LogUserGraph(date=now.date(), pk=self.object.id).date_pie_chart(day="today")
        context['yesterday_pie_chart'] = LogUserGraph(date=now - timezone.timedelta(days=1),
                                                      pk=self.object.id).date_pie_chart(day="yesterday")
        context['past_7_days_graph'] = LogUserGraph(date=now.date(), pk=self.object.id).past_days_graph(7)

        context['css'] = css_resources
        context['js'] = js_resources
        return context
