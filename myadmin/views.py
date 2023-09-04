from bokeh.resources import INLINE
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseServerError
from django.utils import timezone
from django.views.generic import TemplateView, DetailView

from myadmin.graphs import LogGraph, LogAppGraph, LogUserGraph, LogModelGraph
from myadmin.query import Content

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

        context['applications'] = Content.applications()
        context['models'] = Content.models()

        return context


class HomeView(LoginRequiredMixin, MyadminMixin, TemplateView):
    template_name = 'myadmin/home.html'
    title = 'myadmin|home'

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['title'] = self.title

        context['year_graph'] = LogGraph(year=now.year).past_years(10)
        context['month_graph'] = LogGraph(year=now.year).year_graph()
        context['today_pie_chart'] = LogGraph(date=now.date()).date_pie_chart(day="today")
        context['yesterday_pie_chart'] = LogGraph(date=now - timezone.timedelta(days=1)).date_pie_chart(day="yesterday")
        context['past_7_days_graph'] = LogGraph(date=now.date()).past_days_graph(7)

        context['css'] = css_resources
        context['js'] = js_resources
        return context


class AppView(LoginRequiredMixin, MyadminMixin, TemplateView):
    template_name = 'myadmin/home.html'

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        app = self.kwargs['app']

        context['title'] = f'myadmin|{app}'

        con = ContentType.objects.get(app_label=app)

        if not con:
            raise HttpResponseServerError(f"There is no app called {app}")

        context['year_graph'] = LogAppGraph(year=now.year, app=app).past_years(10)
        context['month_graph'] = LogAppGraph(year=now.year, app=app).year_graph()
        context['today_pie_chart'] = LogAppGraph(date=now.date(), app=app).date_pie_chart(day="today")
        context['yesterday_pie_chart'] = LogAppGraph(date=now - timezone.timedelta(days=1),
                                                     app=app).date_pie_chart(day="yesterday")
        context['past_7_days_graph'] = LogAppGraph(date=now.date(), app=app).past_days_graph(7)

        context['css'] = css_resources
        context['js'] = js_resources
        return context


class AppModelView(LoginRequiredMixin, MyadminMixin, TemplateView):
    template_name = 'myadmin/home.html'

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        app = self.kwargs['app']
        model = self.kwargs['model']

        context['title'] = f'myadmin|{app}|{model}'

        con = ContentType.objects.get(app_label=app, model=model)

        if not con:
            raise HttpResponseServerError(f"There is no app called {app}")

        context['year_graph'] = LogModelGraph(year=now.year, app=app, model=model).past_years(10)
        context['month_graph'] = LogModelGraph(year=now.year, app=app, model=model).year_graph()
        context['today_pie_chart'] = LogModelGraph(date=now.date(), app=app, model=model).date_pie_chart(
            day="today")
        context['yesterday_pie_chart'] = LogModelGraph(date=now - timezone.timedelta(days=1),
                                                       app=app, model=model).date_pie_chart(day="yesterday")
        context['past_7_days_graph'] = LogModelGraph(date=now.date(), app=app, model=model).past_days_graph(7)

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

        context['title'] = self.title

        context['year_graph'] = LogUserGraph(year=now.year, pk=self.object.id).past_years(10)
        context['month_graph'] = LogUserGraph(year=now.year, pk=self.object.id).year_graph()
        context['today_pie_chart'] = LogUserGraph(date=now.date(), pk=self.object.id).date_pie_chart(day="today")
        context['yesterday_pie_chart'] = LogUserGraph(date=now - timezone.timedelta(days=1),
                                                      pk=self.object.id).date_pie_chart(day="yesterday")
        context['past_7_days_graph'] = LogUserGraph(date=now.date(), pk=self.object.id).past_days_graph(7)

        context['css'] = css_resources
        context['js'] = js_resources
        return context
