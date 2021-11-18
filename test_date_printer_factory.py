import pytest

from american_date_printer import AmericanDatePrinter
from date_printers import DatePrinter
from dateprinterfactory import DatePrinterFactory
from unittest.mock import MagicMock, patch

from european_date_printer import EuropeanDatePrinter
from iso_date_printer import ISODatePrinter
from user_feature_flags import UserFeatureFlags


def test_constructor():
    factory = DatePrinterFactory(None)
    assert isinstance(factory, DatePrinterFactory)


printerdata = {
    "USA": ("USA", AmericanDatePrinter),
    "Euro": ("Europe", EuropeanDatePrinter),
    "ISO": ("ISO", ISODatePrinter),
    "Other": ("FooBar", DatePrinter)
}

@pytest.mark.parametrize("flag_value, expected", printerdata.values(), ids=printerdata.keys())
def test_get_printer(flag_value: str, expected):
    flags = UserFeatureFlags(None, None)
    with patch.dict(flags, {"date-format": flag_value}, clear=True):
        factory = DatePrinterFactory(flags)
        printer = factory.get_printer()
    assert isinstance(printer, expected)
