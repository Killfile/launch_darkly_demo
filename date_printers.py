import abc
from datetime import datetime


class DatePrinter:
    @abc.abstractmethod
    def print_date(self, date: datetime):
        return "No Format Specified"
