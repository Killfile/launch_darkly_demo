from datetime import datetime

from date_printers import DatePrinter


class ISODatePrinter(DatePrinter):
    def print_date(self, date: datetime):
        return date.strftime("%Y-%m-%d")