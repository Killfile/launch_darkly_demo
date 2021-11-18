from datetime import datetime

from dateprinterfactory import DatePrinterFactory
from launch_darkly_client import SingletonLaunchDarklyClient
from user_feature_flags import UserFeatureFlags


def print_the_date():
    test_sdk_key = "[insert_key_here]"

    user = {
        "key": "example-user-key",
        "name": "Sandy"
    }

    client = SingletonLaunchDarklyClient(test_sdk_key)
    value_store = UserFeatureFlags(client, user)
    factory = DatePrinterFactory(value_store)
    printer = factory.get_printer()

    print(f"The current date is {printer.print_date(datetime.now())}")

    client.get_close()


if __name__ == '__main__':
    print_the_date()
