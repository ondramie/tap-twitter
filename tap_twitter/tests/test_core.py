"""Tests standard tap features using the built-in SDK tests library."""

import datetime
import os

from singer_sdk.testing import get_tap_test_class

from tap_twitter.tap import TapTwitter

SAMPLE_CONFIG = {
    "user_ids": ["123456789"],
    "bearer_token": os.getenv("TAP_TWITTER_BEARER_TOKEN"),
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
}

# Run standard built-in tap tests from the SDK:
TestTapTwitter = get_tap_test_class(
    tap_class=TapTwitter,
    config=SAMPLE_CONFIG,
)
