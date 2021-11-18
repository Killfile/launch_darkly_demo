from american_date_printer import AmericanDatePrinter
from date_printers import DatePrinter
from european_date_printer import EuropeanDatePrinter
from iso_date_printer import ISODatePrinter
from user_feature_flags import UserFeatureFlags


class DatePrinterFactory:
    def __init__(self, flags: UserFeatureFlags):
        self._flags = flags

    def get_printer(self) -> DatePrinter:
        printer = DatePrinter()
        if self._flags["date-format"] == "USA":
            printer = AmericanDatePrinter()
        elif self._flags["date-format"] == "Europe":
            printer = EuropeanDatePrinter()
        elif self._flags["date-format"] == "ISO":
            printer = ISODatePrinter()

        return printer
