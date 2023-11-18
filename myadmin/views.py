from bokeh.resources import INLINE
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.http import HttpResponseServerError
from django.utils import timezone
from django.views.generic import TemplateView, DetailView, UpdateView

from myadmin.forms import ProfileForm
from myadmin.graphs import LogGraph, LogAppGraph, LogUserGraph
from myadmin.models import Profile
from myadmin.query import Content, LogUser, LogApp

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


class ProfileUpdateMixin(UserPassesTestMixin):
    def form_valid(self, form):
        response = super().form_valid(form)
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.pk,
            object_repr=self.object.user.username,
            action_flag=CHANGE)
        return response


class HomeView(LoginRequiredMixin, MyadminMixin, TemplateView):
    template_name = 'myadmin/home.html'
    title = 'myadmin'

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        context['title'] = self.title

        context['year_graph'] = LogGraph(year=now.year).past_years(10)
        context['month_graph'] = LogGraph(year=now.year).year_graph()
        context['today_pie_chart'] = LogGraph(date=now.date()).date_pie_chart(day="today")
        context['yesterday_pie_chart'] = LogGraph(date=now - timezone.timedelta(days=1)).date_pie_chart(day="yesterday")
        context['past_7_days_graph'] = LogGraph(date=now.date()).past_days_graph(7)

        logentry = LogEntry.objects.all()

        paginator = Paginator(logentry, 10)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['logentry'] = page_obj

        context['css'] = css_resources
        context['js'] = js_resources
        return context


class AppView(LoginRequiredMixin, MyadminMixin, TemplateView):
    template_name = 'myadmin/app_model.html'

    def get_context_data(self, **kwargs):
        # ___________________________________________________________

        context = super().get_context_data(**kwargs)

        app = self.kwargs['app']

        context['title'] = f'myadmin|{app}'

        con = ContentType.objects.filter(app_label=app)

        if not con:
            raise HttpResponseServerError(f"There is no app called {app}")

        context['app'] = app
        context['content'] = con

        context['year_graph'] = LogAppGraph(year=now.year, app=app).past_years(10)
        context['month_graph'] = LogAppGraph(year=now.year, app=app).year_graph()
        context['today_pie_chart'] = LogAppGraph(date=now.date(), app=app).date_pie_chart(day="today")
        context['yesterday_pie_chart'] = LogAppGraph(date=now - timezone.timedelta(days=1),
                                                     app=app).date_pie_chart(day="yesterday")
        context['past_7_days_graph'] = LogAppGraph(date=now.date(), app=app).past_days_graph(7)

        app_logs = LogApp(app=app).app_list()
        paginator = Paginator(app_logs, 10)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['app_logs'] = page_obj

        context['css'] = css_resources
        context['js'] = js_resources
        return context


class UserModelDetailView(LoginRequiredMixin, MyadminMixin, DetailView):
    template_name = 'myadmin/user_model.html'
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

        user_logs = LogUser(user=self.object).user_list()

        paginator = Paginator(user_logs, 10)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['user_logs'] = page_obj

        profile = Profile.objects.get(user=self.object.id)

        context['profile'] = profile

        context['css'] = css_resources
        context['js'] = js_resources
        return context


class ProfileUpdateView(MyadminMixin, ProfileUpdateMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'myadmin/profile_change.html'
