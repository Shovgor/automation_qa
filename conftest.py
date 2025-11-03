import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser_context():
    """Creates a Playwright browser context with Pixel 5 emulation and video recording."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Get the Pixel 5 device configuration
        pixel = p.devices["Pixel 5"]
        device_options = {
            "user_agent": pixel["user_agent"],
            "viewport": pixel["viewport"],
            "device_scale_factor": pixel["device_scale_factor"],
            "is_mobile": pixel["is_mobile"],
            "has_touch": pixel["has_touch"],
        }

        # Create a new browser context with video recording
        context = browser.new_context(
            **device_options,
            record_video_dir="videos/",
        )

        yield context
        context.close()
        browser.close()
