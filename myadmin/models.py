from django.contrib.admin.models import LogEntry, LogEntryManager
from django.db import models


class LogEntryQuerySet(models.QuerySet):
    """"""

    def yearly_list(self, year):
        self.filter(action_time__year=year)

    def monthly_list(self, month, year):
        self.filter(action_time__month=month, action_time__year=year)

    def date_list(self, date):
        self.filter(action_time__date=date)

    def yearly_count(self, year):
        self.filter(action_time__year=year).count()

    def monthly_count(self, month, year):
        self.filter(action_time__month=month, action_time__year=year).count()

    def date_count(self, date):
        self.filter(action_time__date=date).count()

    """ADDITION"""

    def addition_yearly_list(self, year):
        self.filter(action_time__year=year, action_flag=1)

    def addition_monthly_list(self, month, year):
        self.filter(action_time__month=month, action_time__year=year, action_flag=1)

    def addition_date_list(self, date):
        self.filter(action_time__date=date, action_flag=1)

    def addition_yearly_count(self, year):
        self.filter(action_time__year=year, action_flag=1).count()

    def addition_monthly_count(self, month, year):
        self.filter(action_time__month=month, action_time__year=year, action_flag=1).count()

    def addition_date_count(self, date):
        self.filter(action_time__date=date, action_flag=1).count()

    """CHANGE"""

    def change_yearly_list(self, year):
        self.filter(action_time__year=year, action_flag=2)

    def change_monthly_list(self, month, year):
        self.filter(action_time__month=month, action_time__year=year, action_flag=2)

    def change_date_list(self, date):
        self.filter(action_time__date=date, action_flag=2)

    def change_yearly_count(self, year):
        self.filter(action_time__year=year, action_flag=2).count()

    def change_monthly_count(self, month, year):
        self.filter(action_time__month=month, action_time__year=year, action_flag=2).count()

    def change_date_count(self, date):
        self.filter(action_time__date=date, action_flag=2).count()

    """DELETION"""

    def deletion_yearly_list(self, year):
        self.filter(action_time__year=year, action_flag=3)

    def deletion_monthly_list(self, month, year):
        self.filter(action_time__month=month, action_time__year=year, action_flag=3)

    def deletion_date_list(self, date):
        self.filter(action_time__date=date, action_flag=3)

    def deletion_yearly_count(self, year):
        self.filter(action_time__year=year, action_flag=3).count()

    def deletion_monthly_count(self, month, year):
        self.filter(action_time__month=month, action_time__year=year, action_flag=3).count()

    def deletion_date_count(self, date):
        self.filter(action_time__date=date, action_flag=3).count()


class LogManager(LogEntryManager):
    """"""

    def get_queryset(self):
        return LogEntryQuerySet(self.model, using=self._db)

    def yearly_list(self, year):
        self.get_queryset().yearly_list(year)

    def monthly_list(self, month, year):
        self.get_queryset().monthly_list(month, year)

    def date_list(self, date):
        self.get_queryset().date_list(date)

    def yearly_count(self, year):
        self.get_queryset().yearly_count(year)

    def monthly_count(self, month, year):
        self.get_queryset().monthly_count(month, year)

    def date_count(self, date):
        self.get_queryset().date_count(date)

    """ADDITION"""

    def addition_yearly_list(self, year):
        self.get_queryset().addition_yearly_list(year)

    def addition_monthly_list(self, month, year):
        self.get_queryset().addition_monthly_list(month, year)

    def addition_date_list(self, date):
        self.get_queryset().addition_date_list(date)

    def addition_yearly_count(self, year):
        self.get_queryset().addition_yearly_count(year)

    def addition_monthly_count(self, month, year):
        self.get_queryset().addition_monthly_count(month, year)

    def addition_date_count(self, date):
        self.get_queryset().addition_date_count(date)

    """CHANGE"""

    def change_yearly_list(self, year):
        self.get_queryset().change_yearly_list(year)

    def change_monthly_list(self, month, year):
        self.get_queryset().change_monthly_list(month, year)

    def change_date_list(self, date):
        self.get_queryset().change_date_list(date)

    def change_yearly_count(self, year):
        self.get_queryset().change_yearly_count(year)

    def change_monthly_count(self, month, year):
        self.get_queryset().change_monthly_count(month, year)

    def change_date_count(self, date):
        self.get_queryset().change_date_count(date)

    """DELETION"""

    def deletion_yearly_list(self, year):
        self.get_queryset().deletion_yearly_list(year)

    def deletion_monthly_list(self, month, year):
        self.get_queryset().deletion_monthly_list(month, year)

    def deletion_date_list(self, date):
        self.get_queryset().deletion_date_list(date)

    def deletion_yearly_count(self, year):
        self.get_queryset().deletion_yearly_count(year)

    def deletion_monthly_count(self, month, year):
        self.get_queryset().deletion_monthly_count(month, year)

    def deletion_date_count(self, date):
        self.get_queryset().addition_date_count(date)


class Log(LogEntry):
    """"""
    objects = LogManager()
