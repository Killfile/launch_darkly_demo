from datetime import datetime

from date_printers import DatePrinter


class EuropeanDatePrinter(DatePrinter):
    def print_date(self, date: datetime):
        return date.strftime("%d.%m.%Y")