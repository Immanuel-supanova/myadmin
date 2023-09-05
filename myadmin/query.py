import numpy as np
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType


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

    def deletion_yearly_count(self):
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
        count = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month)
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


class LogApp:
    """"""

    def __init__(self, app):
        self.app = app

    def app_list(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(content_type=k))

        return log

    def app_count(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(content_type=k).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count


class LogAppYear:
    """"""

    def __init__(self, year, app):
        self.year = year
        self.app = app

    def yearly_list(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, content_type=k))

        return log

    def yearly_count(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, content_type=k).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count

    """ADDITION"""

    def addition_yearly_list(self):

        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, content_type=k, action_flag=1))

        return log

    def addition_yearly_count(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, content_type=k, action_flag=1).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count

    """CHANGE"""

    def change_yearly_list(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, content_type=k, action_flag=2))

        return log

    def change_yearly_count(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, content_type=k, action_flag=2).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count

    """DELETION"""

    def deletion_yearly_list(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, content_type=k, action_flag=3))

        return log

    def deletion_yearly_count(self, ):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, content_type=k, action_flag=3).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count


class LogAppMonth:
    """"""

    def __init__(self, year, month, app):
        self.year = year
        self.month = month
        self.app = app

    def monthly_list(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year,
                                               action_time__month=self.month, content_type=k))

        return log

    def monthly_count(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year,
                                               action_time__month=self.month, content_type=k).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count

    """ADDITION"""

    def addition_monthly_list(self):

        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                               content_type=k, action_flag=1))

        return log

    def addition_monthly_count(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                               content_type=k, action_flag=1).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count

    """CHANGE"""

    def change_monthly_list(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                               content_type=k, action_flag=2))

        return log

    def change_monthly_count(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                               content_type=k, action_flag=2).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count

    """DELETION"""

    def deletion_monthly_list(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                               content_type=k, action_flag=3))

        return log

    def deletion_monthly_count(self, ):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                               content_type=k, action_flag=3).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count


class LogAppDate:
    """"""

    def __init__(self, date, app):
        self.date = date
        self.app = app

    def date_list(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__date=self.date, content_type=k))

        return log

    def date_count(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__date=self.date, content_type=k).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count

    """ADDITION"""

    def addition_date_list(self):

        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__date=self.date, content_type=k, action_flag=1))

        return log

    def addition_date_count(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__date=self.date, content_type=k, action_flag=1).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count

    """CHANGE"""

    def change_date_list(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__date=self.date, content_type=k, action_flag=2))

        return log

    def change_date_count(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__date=self.date, content_type=k, action_flag=2).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count

    """DELETION"""

    def deletion_date_list(self):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__date=self.date, content_type=k, action_flag=3))

        return log

    def deletion_date_count(self, ):
        app = ContentType.objects.filter(app_label=self.app)

        list1 = []
        for m in app:
            list1.append(m)

        log = []

        for k in list1:
            log.append(LogEntry.objects.filter(action_time__date=self.date, content_type=k, action_flag=3).count())

        arr = np.array(log)

        count = np.sum(arr)

        return count


class LogModel:
    def __init__(self, app, model):
        self.app = app
        self.model = model

    def model_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(content_type=app)

        return log

    def model_count(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(content_type=app).count()

        return count


class LogModelYear:
    """"""

    def __init__(self, year, app, model):
        self.year = year
        self.app = app
        self.model = model

    def yearly_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(action_time__year=self.year, content_type=app)

        return log

    def yearly_count(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(action_time__year=self.year, content_type=app).count()

        return count

    """ADDITION"""

    def addition_yearly_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(action_time__year=self.year, content_type=app, action_flag=1)

        return log

    def addition_yearly_count(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(action_time__year=self.year, content_type=app, action_flag=1).count()

        return count

    """CHANGE"""

    def change_yearly_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(action_time__year=self.year, content_type=app, action_flag=2)

        return log

    def change_yearly_count(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(action_time__year=self.year, content_type=app, action_flag=2).count()

        return count

    """DELETION"""

    def deletion_yearly_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(action_time__year=self.year, content_type=app, action_flag=3)

        return log

    def deletion_yearly_count(self, ):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(action_time__year=self.year, content_type=app, action_flag=3).count()

        return count


class LogModelMonth:
    """"""

    def __init__(self, year, month, app, model):
        self.year = year
        self.month = month
        self.app = app
        self.model = model

    def monthly_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month, content_type=app)

        return log

    def monthly_count(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                        content_type=app).count()

        return count

    """ADDITION"""

    def addition_monthly_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                      content_type=app, action_flag=1)

        return log

    def addition_monthly_count(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                        content_type=app, action_flag=1).count()

        return count

    """CHANGE"""

    def change_monthly_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                      content_type=app, action_flag=2)

        return log

    def change_monthly_count(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                        content_type=app, action_flag=2).count()

        return count

    """DELETION"""

    def deletion_monthly_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                      content_type=app, action_flag=3)

        return log

    def deletion_monthly_count(self, ):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                        content_type=app, action_flag=3).count()

        return count


class LogModelDate:
    """"""

    def __init__(self, date, app, model):
        self.date = date
        self.app = app
        self.model = model

    def date_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(action_time__date=self.date, content_type=app)

        return log

    def date_count(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(action_time__date=self.date, content_type=app).count()

        return count

    """ADDITION"""

    def addition_date_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(action_time__date=self.date, content_type=app, action_flag=1)

        return log

    def addition_date_count(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(action_time__date=self.date, content_type=app, action_flag=1).count()

        return count

    """CHANGE"""

    def change_date_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(action_time__date=self.date, content_type=app, action_flag=2)

        return log

    def change_date_count(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(action_time__date=self.date, content_type=app, action_flag=2).count()

        return count

    """DELETION"""

    def deletion_date_list(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        log = LogEntry.objects.filter(action_time__date=self.date, content_type=app, action_flag=3)

        return log

    def deletion_date_count(self):
        app = ContentType.objects.get(app_label=self.app, model=self.model)

        count = LogEntry.objects.filter(action_time__date=self.date, content_type=app, action_flag=3).count()

        return count


class LogUser:
    """"""

    def __init__(self, user):
        self.user = user

    def user_list(self):
        log = LogEntry.objects.filter(user=self.user)
        return log

    def user_count(self):
        count = LogEntry.objects.filter(user=self.user).count()
        return count


class LogUserYear:
    """"""

    def __init__(self, year, user):
        self.year = year
        self.user = user

    def yearly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, user=self.user)
        return log

    def yearly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year, user=self.user).count()
        return count

    """ADDITION"""

    def addition_yearly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, user=self.user, action_flag=1)
        return log

    def addition_yearly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year, user=self.user, action_flag=1).count()
        return count

    """CHANGE"""

    def change_yearly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, user=self.user, action_flag=2)
        return log

    def change_yearly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year, user=self.user, action_flag=2).count()
        return count

    """DELETION"""

    def deletion_yearly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, user=self.user, action_flag=3)
        return log

    def deletion_yearly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year, user=self.user, action_flag=3).count()
        return count


class LogUserMonth:
    """"""

    def __init__(self, year, month, user):
        self.year = year
        self.month = month
        self.user = user

    def monthly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month, user=self.user)
        return log

    def monthly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month, user=self.user)
        return count

    """ADDITION"""

    def addition_monthly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month,
                                      user=self.user, action_flag=1)
        return log

    def addition_monthly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month, user=self.user,
                                        action_flag=1).count()
        return count

    """CHANGE"""

    def change_monthly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month, user=self.user,
                                      action_flag=2)
        return log

    def change_monthly_count(self):
        count = LogEntry.objects.filter(action_time__year=self.year,
                                        action_time__month=self.month, user=self.user, action_flag=2).count()
        return count

    """DELETION"""

    def deletion_monthly_list(self):
        log = LogEntry.objects.filter(action_time__year=self.year, action_time__month=self.month, user=self.user,
                                      action_flag=3)
        return log

    def deletion_monthly_count(self, ):
        count = LogEntry.objects.filter(action_time__year=self.year,
                                        action_time__month=self.month, user=self.user, action_flag=3).count()
        return count


class LogUserDate:
    """"""

    def __init__(self, date, user):
        self.date = date
        self.user = user

    def date_list(self):
        log = LogEntry.objects.filter(action_time__date=self.date, user=self.user)
        return log

    def date_count(self):
        count = LogEntry.objects.filter(action_time__date=self.date, user=self.user).count()
        return count

    """ADDITION"""

    def addition_date_list(self):
        log = LogEntry.objects.filter(action_time__date=self.date, user=self.user, action_flag=1)
        return log

    def addition_date_count(self):
        count = LogEntry.objects.filter(action_time__date=self.date, user=self.user, action_flag=1).count()
        return count

    """CHANGE"""

    def change_date_list(self):
        log = LogEntry.objects.filter(action_time__date=self.date, user=self.user, action_flag=2)
        return log

    def change_date_count(self):
        count = LogEntry.objects.filter(action_time__date=self.date, user=self.user, action_flag=2).count()
        return count

    """DELETION"""

    def deletion_date_list(self):
        log = LogEntry.objects.filter(action_time__date=self.date, user=self.user, action_flag=3)
        return log

    def deletion_date_count(self):
        count = LogEntry.objects.filter(action_time__date=self.date, user=self.user, action_flag=3).count()
        return count


class Content:

    @staticmethod
    def applications():
        content = ContentType.objects.exclude(app_label='admin').exclude(app_label='sessions').exclude(
            app_label='contenttypes')
        app = []
        apps = []

        for con in content:
            app.append(con.app_label)

        for con in app:
            if con not in apps:
                apps.append(con)

        return apps

    @staticmethod
    def models():
        content = ContentType.objects.exclude(app_label='admin').exclude(app_label='sessions').exclude(
            app_label='contenttypes')
        app = []

        for con in content:
            app.append({str(con.app_label): str(con.model)})

        return app
