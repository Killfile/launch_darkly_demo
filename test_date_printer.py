from datetime import datetime

import pytest

from american_date_printer import AmericanDatePrinter
from date_printers import DatePrinter
from european_date_printer import EuropeanDatePrinter
from iso_date_printer import ISODatePrinter


def test_basic_date_printer_print_date():
    printer = DatePrinter()
    expected = "No Format Specified"
    actual = printer.print_date(datetime.now())
    assert expected == actual

def test_american_date_printer_print_date():
    printer = AmericanDatePrinter()
    expected = "12/07/1941"
    actual = printer.print_date(datetime.fromisoformat("1941-12-07"))
    assert expected == actual

def test_european_date_printer_print_date():
    printer = EuropeanDatePrinter()
    expected = "01.09.1939"
    actual = printer.print_date(datetime.fromisoformat("1939-09-01"))
    assert expected == actual

def test_iso_date_printer_print_date():
    printer = ISODatePrinter()
    expected = "1931-09-18"
    actual = printer.print_date(datetime.fromisoformat("1931-09-18"))
    assert expected == actual


