from datetime import datetime

from date_printers import DatePrinter


class AmericanDatePrinter(DatePrinter):
    def print_date(self, date: datetime):
        return date.strftime("%m/%d/%Y")