from django.contrib.admin.models import LogEntry


class LogYear:
    """"""

    def __init__(self, year):
        self.year = year

    def yearly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year)
        return log

    def yearly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year).count()
        return count

    """ADDITION"""

    def addition_yearly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, action_flag=1)
        return log

    def addition_yearly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year, action_flag=1).count()
        return count

    """CHANGE"""

    def change_yearly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, action_flag=2)
        return log

    def change_yearly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year, action_flag=2).count()
        return count

    """DELETION"""

    def deletion_yearly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, action_flag=3)
        return log

    def deletion_yearly_count(self, ):
        count = LogEntry.objects.filter(action_time__year=self.year, action_flag=3).count()
        return count


class LogMonth:
    """"""

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def monthly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month)
        return log

    def monthly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year)
        return count

    """ADDITION"""

    def addition_monthly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month, action_flag=1)
        return log

    def addition_monthly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                        action_flag=1).count()
        return count

    """CHANGE"""

    def change_monthly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month, action_flag=2)
        return log

    def change_monthly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year,
                                        action_time__month=self.month, action_flag=2).count()
        return count

    """DELETION"""

    def deletion_monthly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month, action_flag=3)
        return log

    def deletion_monthly_count(self, ):
        count = LogEntry.objects.filter(action_time__year=self.year,
                                        action_time__month=self.month, action_flag=3).count()
        return count


class LogDate:
    """"""

    def __init__(self, date):
        self.date = date

    def date_list(self):
        log = LogEntry.objects.filter(action_time__date=self.date)
        return log

    def date_count(self):
        count = LogEntry.objects.filter(action_time__date=self.date).count()
        return count

    """ADDITION"""

    def addition_date_list(self):
        log = LogEntry.objects.filter(action_time__date=self.date, action_flag=1)
        return log

    def addition_date_count(self):
        count = LogEntry.objects.filter(action_time__date=self.date, action_flag=1).count()
        return count

    """CHANGE"""

    def change_date_list(self):
        log = LogEntry.objects.filter(action_time__date=self.date, action_flag=2)
        return log

    def change_date_count(self):
        count = LogEntry.objects.filter(action_time__date=self.date, action_flag=2).count()
        return count

    """DELETION"""

    def deletion_date_list(self):
        log = LogEntry.objects.filter(action_time__date=self.date, action_flag=3)
        return log

    def deletion_date_count(self):
        count = LogEntry.objects.filter(action_time__date=self.date, action_flag=3).count()
        return count
