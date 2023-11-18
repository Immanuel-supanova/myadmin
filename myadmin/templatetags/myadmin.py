from django import template
from django.utils import timezone

from myadmin.graphs import LogModelGraph

register = template.Library()

now = timezone.now()


@register.inclusion_tag("myadmin/tag/model.html")
def model_graph(app, model):
    return {f'year_graph': LogModelGraph(year=now.year, app=app, model=model).past_years(10),
            f'month_graph_': LogModelGraph(year=now.year, app=app, model=model).year_graph(),
            f'today_pie_chart': LogModelGraph(date=now.date(), app=app,
                                              model=model).date_pie_chart(
                day="today"), f'yesterday_pie_chart': LogModelGraph(date=now - timezone.timedelta(days=1),
                                                                    app=app, model=model).date_pie_chart(
            day="yesterday"), f'past_7_days_graph': LogModelGraph(date=now.date(), app=app,
                                                                  model=model).past_days_graph(7),
            'model': model}
