from math import pi

import pandas as pd
from bokeh.embed import components
from bokeh.models import BoxZoomTool, ResetTool, WheelZoomTool, PanTool, ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge, cumsum
from django.utils import timezone

from .query import LogDate, LogMonth, LogYear

now = timezone.now()


def month_graph():
    # prepare some data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    addition_data = []
    for m in range(1, 13):
        addition_data.append(LogMonth(month=m, year=2023).addition_monthly_count())
    change_data = []
    for m in range(1, 13):
        change_data.append(LogMonth(month=m, year=2023).change_monthly_count())
    deletion_data = []
    for m in range(1, 13):
        deletion_data.append(LogMonth(month=m, year=2023).deletion_monthly_count())

    # Create a ColumnDataSource for the bar graph
    source = ColumnDataSource(
        data=dict(months=months, addition=addition_data, change=change_data, deletion=deletion_data))

    # create a new plot with a title and axis labels
    p = figure(title="Activity in 2023",
               x_range=months,
               tools=[BoxZoomTool(), WheelZoomTool(), PanTool(), ResetTool()],
               sizing_mode="stretch_width",
               height=300,
               x_axis_label="Months",
               y_axis_label="No of Logs")

    # activate toolbar autohide
    p.toolbar.autohide = True

    p.toolbar.logo = None
    p.y_range.start = 0

    # Create bar glyphs
    p.vbar(x=dodge('months', -0.25, range=p.x_range), top='addition', width=0.2, source=source,
           color="blue", legend_label="Addition")
    p.vbar(x=dodge('months', 0.0, range=p.x_range), top='change', width=0.2, source=source,
           color="green", legend_label="Change")
    p.vbar(x=dodge('months', 0.25, range=p.x_range), top='deletion', width=0.2, source=source,
           color="red", legend_label="Deletion")

    # Customize the plot
    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None

    script, div = components(p)

    return {'script': script, 'div': div}


def year_graph():
    # prepare some data
    x = ['2023']
    year = now.year

    for m in range(1, 5):
        x.append(f'{year - m}')

    x = x[::-1]

    addition = [LogYear(year=int(m)).addition_yearly_count() for m in x]
    change = [LogYear(year=int(m)).change_yearly_count() for m in x]
    deletion = [LogYear(year=int(m)).deletion_yearly_count() for m in x]

    source = ColumnDataSource(data=dict(x=x, addition=addition, change=change,
                                        deletion=deletion))

    # create a new plot with a title and axis labels
    p = figure(title="Activities in the past 5 years",
               x_range=x,
               tools=[BoxZoomTool(), WheelZoomTool(), PanTool(), ResetTool()],
               sizing_mode="stretch_width",
               height=300,
               x_axis_label="Years",
               y_axis_label="No of Logs")

    # activate toolbar autohide
    p.toolbar.autohide = True

    p.toolbar.logo = None
    p.y_range.start = 0

    # data = y[::-1]

    p.vbar(x=dodge('x', -0.25, range=p.x_range), top='addition', width=0.2, source=source,
           color="blue", legend_label="Addition")
    p.vbar(x=dodge('x', 0.0, range=p.x_range), top='change', width=0.2, source=source,
           color="green", legend_label="Change")
    p.vbar(x=dodge('x', 0.25, range=p.x_range), top='deletion', width=0.2, source=source,
           color="red", legend_label="Deletion")

    script, div = components(p)

    return {'script': script, 'div': div}


def today_pie_chart():
    x = {
        'Addition': LogDate(now.date()).addition_date_count(),
        'Change': LogDate(now.date()).change_date_count(),
        'Deletion': LogDate(now.date()).deletion_date_count(),
    }

    # Convert data to DataFrame
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'article'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi

    # Specify the colors
    colors = ['#0d6efd', '#198754', '#dc3545']

    # Add color to the DataFrame
    data['color'] = colors

    # Create the pie chart plot
    p = figure(height=300, title="Activities Today", toolbar_location=None, tools="hover",
               sizing_mode="stretch_width",
               tooltips="@article: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='article', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    # Render the plot
    script, div = components(p)

    return {'script': script, 'div': div}


def yesterday_pie_chart():
    date = now - timezone.timedelta(days=1)
    x = {
        'Addition': LogDate(date.date()).addition_date_count(),
        'Change': LogDate(date.date()).change_date_count(),
        'Deletion': LogDate(date.date()).deletion_date_count(),
    }

    # Convert data to DataFrame
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'article'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi

    # Specify the colors
    colors = ['#0d6efd', '#198754', '#dc3545']

    # Add color to the DataFrame
    data['color'] = colors

    # Create the pie chart plot
    p = figure(height=300, title="Activities Yesterday", toolbar_location=None, tools="hover",
               sizing_mode="stretch_width",
               tooltips="@article: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='article', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    # Render the plot
    script, div = components(p)

    return {'script': script, 'div': div}


def past_7_days_graph():
    week_list = [now - timezone.timedelta(days=i) for i in range(7)]
    week = []
    x = []
    y = []
    for w in week_list:
        week.append(w.strftime('%Y-%m-%d'))

    for w in week_list:
        x.append(w.strftime('%d %b'))

    for d in week:
        y.append(
            LogDate(d).date_count()
        )

    x = x[::-1]
    y = y[::-1]

    # create a new plot with a title and axis labels
    p = figure(title="Activities for the past 7 days",
               x_range=x,
               tools=[BoxZoomTool(), WheelZoomTool(), PanTool(), ResetTool()],
               sizing_mode="stretch_width",
               height=300,
               x_axis_label="days",
               y_axis_label="No of Logs")

    p.toolbar.autohide = True
    p.toolbar.logo = None

    # add a line renderer with legend and line thickness
    p.line(x, y, legend_label="Temp.", line_width=2)

    # Render the plot
    script, div = components(p)

    return {'script': script, 'div': div}
