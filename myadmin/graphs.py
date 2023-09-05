from math import pi

import pandas as pd
from bokeh.embed import components
from bokeh.models import BoxZoomTool, ResetTool, WheelZoomTool, PanTool, ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge, cumsum
from django.contrib.auth import get_user_model
from django.utils import timezone

from .query import LogDate, LogMonth, LogYear, LogAppYear, LogAppMonth, LogAppDate, LogModelYear, LogModelMonth, \
    LogModelDate, LogUserYear, LogUserMonth, LogUserDate

now = timezone.now()
User = get_user_model()


class LogGraph:
    """"""

    def __init__(self, year=None, date=None):
        """
        from django.utils import timezone
        now = timezone.now()
        now.date()
        """

        self.year = year
        self.date = date

    def past_years(self, no_of_years):
        # prepare some data
        x = [f'{str(self.year)}']

        for m in range(1, no_of_years):
            x.append(f'{self.year - m}')

        x = x[::-1]

        addition = [LogYear(year=int(m)).addition_yearly_count() for m in x]
        change = [LogYear(year=int(m)).change_yearly_count() for m in x]
        deletion = [LogYear(year=int(m)).deletion_yearly_count() for m in x]

        source = ColumnDataSource(data=dict(x=x, addition=addition, change=change,
                                            deletion=deletion))

        # create a new plot with a title and axis labels
        p = figure(title=f"Activities in the past {no_of_years} years",
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

        p.vbar(x=dodge('x', -0.25, range=p.x_range), top='addition', width=0.2, source=source,
               color="blue", legend_label="Addition")
        p.vbar(x=dodge('x', 0.0, range=p.x_range), top='change', width=0.2, source=source,
               color="green", legend_label="Change")
        p.vbar(x=dodge('x', 0.25, range=p.x_range), top='deletion', width=0.2, source=source,
               color="red", legend_label="Deletion")

        script, div = components(p)

        return {'script': script, 'div': div}

    def year_graph(self):
        # prepare some data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        addition_data = []
        for m in range(1, 13):
            addition_data.append(LogMonth(month=m, year=self.year).addition_monthly_count())
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
        p = figure(title=f"Activity in {self.year}",
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

    def date_pie_chart(self, day=None):

        x = {
            'Addition': LogDate(self.date).addition_date_count(),
            'Change': LogDate(self.date).change_date_count(),
            'Deletion': LogDate(self.date).deletion_date_count(),
        }

        # Convert data to DataFrame
        data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'article'})
        data['angle'] = data['value'] / data['value'].sum() * 2 * pi

        # Specify the colors
        colors = ['#0d6efd', '#198754', '#dc3545']

        # Add color to the DataFrame
        data['color'] = colors

        if day is None:
            day_name = str(self.date)
        else:
            day_name = day

        # Create the pie chart plot
        p = figure(height=300, title=f"Activities {day_name}", toolbar_location=None, tools="hover",
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

    def past_days_graph(self, no_of_days):
        week_list = [self.date - timezone.timedelta(days=i) for i in range(int(no_of_days))]
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
        p = figure(title=f"Activities for the past {no_of_days} days",
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


class LogAppGraph:
    """"""

    def __init__(self, app, year=None, date=None):
        """
        from django.utils import timezone
        now = timezone.now()
        now.date()
        """

        self.year = year
        self.date = date
        self.app = app

    def past_years(self, no_of_years):
        # prepare some data
        x = [f'{str(self.year)}']

        for m in range(1, no_of_years):
            x.append(f'{self.year - m}')

        x = x[::-1]

        addition = [LogAppYear(year=int(m), app=self.app).addition_yearly_count() for m in x]
        change = [LogAppYear(year=int(m), app=self.app).change_yearly_count() for m in x]
        deletion = [LogAppYear(year=int(m), app=self.app).deletion_yearly_count() for m in x]

        source = ColumnDataSource(data=dict(x=x, addition=addition, change=change,
                                            deletion=deletion))

        # create a new plot with a title and axis labels
        p = figure(title=f"{self.app} logs in the past {no_of_years} years",
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

        p.vbar(x=dodge('x', -0.25, range=p.x_range), top='addition', width=0.2, source=source,
               color="blue", legend_label="Addition")
        p.vbar(x=dodge('x', 0.0, range=p.x_range), top='change', width=0.2, source=source,
               color="green", legend_label="Change")
        p.vbar(x=dodge('x', 0.25, range=p.x_range), top='deletion', width=0.2, source=source,
               color="red", legend_label="Deletion")

        script, div = components(p)

        return {'script': script, 'div': div}

    def year_graph(self):
        # prepare some data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        addition_data = []
        for m in range(1, 13):
            addition_data.append(LogAppMonth(month=m, year=self.year, app=self.app).addition_monthly_count())
        change_data = []
        for m in range(1, 13):
            change_data.append(LogAppMonth(month=m, year=2023, app=self.app).change_monthly_count())
        deletion_data = []
        for m in range(1, 13):
            deletion_data.append(LogAppMonth(month=m, year=2023, app=self.app).deletion_monthly_count())

        # Create a ColumnDataSource for the bar graph
        source = ColumnDataSource(
            data=dict(months=months, addition=addition_data, change=change_data, deletion=deletion_data))

        # create a new plot with a title and axis labels
        p = figure(title=f"{self.app} logs in {self.year}",
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

    def date_pie_chart(self, day=None):

        x = {
            'Addition': LogAppDate(self.date, app=self.app).addition_date_count(),
            'Change': LogAppDate(self.date, app=self.app).change_date_count(),
            'Deletion': LogAppDate(self.date, app=self.app).deletion_date_count(),
        }

        # Convert data to DataFrame
        data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'article'})
        data['angle'] = data['value'] / data['value'].sum() * 2 * pi

        # Specify the colors
        colors = ['#0d6efd', '#198754', '#dc3545']

        # Add color to the DataFrame
        data['color'] = colors

        if day is None:
            day_name = str(self.date)
        else:
            day_name = day

        # Create the pie chart plot
        p = figure(height=300, title=f"{self.app} logs {day_name}", toolbar_location=None, tools="hover",
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

    def past_days_graph(self, no_of_days):
        week_list = [self.date - timezone.timedelta(days=i) for i in range(int(no_of_days))]
        week = []
        x = []
        y = []
        for w in week_list:
            week.append(w.strftime('%Y-%m-%d'))

        for w in week_list:
            x.append(w.strftime('%d %b'))

        for d in week:
            y.append(
                LogAppDate(d, app=self.app).date_count()
            )

        x = x[::-1]
        y = y[::-1]

        # create a new plot with a title and axis labels
        p = figure(title=f"{self.app} logs for the past {no_of_days} days",
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


class LogModelGraph:
    """"""

    def __init__(self, model, app, year=None, date=None):
        """
        from django.utils import timezone
        now = timezone.now()
        now.date()
        """

        self.year = year
        self.date = date
        self.model = model
        self.app = app

    def past_years(self, no_of_years):
        # prepare some data
        x = [f'{str(self.year)}']

        for m in range(1, no_of_years):
            x.append(f'{self.year - m}')

        x = x[::-1]

        addition = [LogModelYear(year=int(m), app=self.app, model=self.model).addition_yearly_count() for m in x]
        change = [LogModelYear(year=int(m), app=self.app, model=self.model).change_yearly_count() for m in x]
        deletion = [LogModelYear(year=int(m), app=self.app, model=self.model).deletion_yearly_count() for m in x]

        source = ColumnDataSource(data=dict(x=x, addition=addition, change=change,
                                            deletion=deletion))

        # create a new plot with a title and axis labels
        p = figure(title=f"{self.app}|{self.model} logs in the past {no_of_years} years",
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

        p.vbar(x=dodge('x', -0.25, range=p.x_range), top='addition', width=0.2, source=source,
               color="blue", legend_label="Addition")
        p.vbar(x=dodge('x', 0.0, range=p.x_range), top='change', width=0.2, source=source,
               color="green", legend_label="Change")
        p.vbar(x=dodge('x', 0.25, range=p.x_range), top='deletion', width=0.2, source=source,
               color="red", legend_label="Deletion")

        script, div = components(p)

        return {'script': script, 'div': div}

    def year_graph(self):
        # prepare some data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        addition_data = []
        for m in range(1, 13):
            addition_data.append(LogModelMonth(month=m, year=self.year,
                                               app=self.app, model=self.model).addition_monthly_count())
        change_data = []
        for m in range(1, 13):
            change_data.append(LogModelMonth(month=m, year=2023,
                                             app=self.app, model=self.model).change_monthly_count())
        deletion_data = []
        for m in range(1, 13):
            deletion_data.append(LogModelMonth(month=m, year=2023,
                                               app=self.app, model=self.model).deletion_monthly_count())

        # Create a ColumnDataSource for the bar graph
        source = ColumnDataSource(
            data=dict(months=months, addition=addition_data, change=change_data, deletion=deletion_data))

        # create a new plot with a title and axis labels
        p = figure(title=f"{self.app}|{self.model} logs in {self.year}",
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

    def date_pie_chart(self, day=None):

        x = {
            'Addition': LogModelDate(self.date, app=self.app, model=self.model).addition_date_count(),
            'Change': LogModelDate(self.date, app=self.app, model=self.model).change_date_count(),
            'Deletion': LogModelDate(self.date, app=self.app, model=self.model).deletion_date_count(),
        }

        # Convert data to DataFrame
        data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'article'})
        data['angle'] = data['value'] / data['value'].sum() * 2 * pi

        # Specify the colors
        colors = ['#0d6efd', '#198754', '#dc3545']

        # Add color to the DataFrame
        data['color'] = colors

        if day is None:
            day_name = str(self.date)
        else:
            day_name = day

        # Create the pie chart plot
        p = figure(height=300, title=f"{self.app}|{self.model} logs {day_name}", toolbar_location=None, tools="hover",
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

    def past_days_graph(self, no_of_days):
        week_list = [self.date - timezone.timedelta(days=i) for i in range(int(no_of_days))]
        week = []
        x = []
        y = []
        for w in week_list:
            week.append(w.strftime('%Y-%m-%d'))

        for w in week_list:
            x.append(w.strftime('%d %b'))

        for d in week:
            y.append(
                LogModelDate(d, app=self.app, model=self.model).date_count()
            )

        x = x[::-1]
        y = y[::-1]

        # create a new plot with a title and axis labels
        p = figure(title=f"{self.app}|{self.model} logs for the past {no_of_days} days",
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


class LogUserGraph:
    """"""

    def __init__(self, pk, year=None, date=None):
        """
        from django.utils import timezone
        now = timezone.now()
        now.date()
        """

        self.year = year
        self.date = date
        self.id = pk
        self.user = User.objects.get(id=self.id)

    def past_years(self, no_of_years):
        # prepare some data
        x = [f'{str(self.year)}']

        for m in range(1, no_of_years):
            x.append(f'{self.year - m}')

        x = x[::-1]

        addition = [LogUserYear(year=int(m), user=self.user).addition_yearly_count() for m in x]
        change = [LogUserYear(year=int(m), user=self.user).change_yearly_count() for m in x]
        deletion = [LogUserYear(year=int(m), user=self.user).deletion_yearly_count() for m in x]

        source = ColumnDataSource(data=dict(x=x, addition=addition, change=change,
                                            deletion=deletion))

        # create a new plot with a title and axis labels
        p = figure(title=f"{self.user.username} logs in the past {no_of_years} years",
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

        p.vbar(x=dodge('x', -0.25, range=p.x_range), top='addition', width=0.2, source=source,
               color="blue", legend_label="Addition")
        p.vbar(x=dodge('x', 0.0, range=p.x_range), top='change', width=0.2, source=source,
               color="green", legend_label="Change")
        p.vbar(x=dodge('x', 0.25, range=p.x_range), top='deletion', width=0.2, source=source,
               color="red", legend_label="Deletion")

        script, div = components(p)

        return {'script': script, 'div': div}

    def year_graph(self):
        # prepare some data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        addition_data = []
        for m in range(1, 13):
            addition_data.append(LogUserMonth(month=m, year=self.year, user=self.user).addition_monthly_count())
        change_data = []
        for m in range(1, 13):
            change_data.append(LogUserMonth(month=m, year=2023, user=self.user).change_monthly_count())
        deletion_data = []
        for m in range(1, 13):
            deletion_data.append(LogUserMonth(month=m, year=2023, user=self.user).deletion_monthly_count())

        # Create a ColumnDataSource for the bar graph
        source = ColumnDataSource(
            data=dict(months=months, addition=addition_data, change=change_data, deletion=deletion_data))

        # create a new plot with a title and axis labels
        p = figure(title=f"{self.user.username} logs in {self.year}",
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

    def date_pie_chart(self, day=None):

        x = {
            'Addition': LogUserDate(self.date, user=self.user).addition_date_count(),
            'Change': LogUserDate(self.date, user=self.user).change_date_count(),
            'Deletion': LogUserDate(self.date, user=self.user).deletion_date_count(),
        }

        # Convert data to DataFrame
        data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'article'})
        data['angle'] = data['value'] / data['value'].sum() * 2 * pi

        # Specify the colors
        colors = ['#0d6efd', '#198754', '#dc3545']

        # Add color to the DataFrame
        data['color'] = colors

        if day is None:
            day_name = str(self.date)
        else:
            day_name = day

        # Create the pie chart plot
        p = figure(height=300, title=f"{self.user.username}'s logs {day_name}", toolbar_location=None, tools="hover",
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

    def past_days_graph(self, no_of_days):
        week_list = [self.date - timezone.timedelta(days=i) for i in range(int(no_of_days))]
        week = []
        x = []
        y = []
        for w in week_list:
            week.append(w.strftime('%Y-%m-%d'))

        for w in week_list:
            x.append(w.strftime('%d %b'))

        for d in week:
            y.append(
                LogUserDate(d, user=self.user).date_count()
            )

        x = x[::-1]
        y = y[::-1]

        # create a new plot with a title and axis labels
        p = figure(title=f"{self.user.username}'s logs for the past {no_of_days} days",
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
