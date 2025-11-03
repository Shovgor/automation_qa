# src/ui/pages/twitch_streamer_page.py
class TwitchStreamerPage:
    def __init__(self, page):
        self.page = page

    def handle_cookies(self):
        # Example cookie handler
        if self.page.locator("button:has-text('Accept Cookies')").is_visible():
            self.page.click("button:has-text('Accept Cookies')")

    def scroll(self, scroll_times=2, scroll_amount=2000):
        """Scroll down the streamer page."""
        for _ in range(scroll_times):
            self.page.mouse.wheel(0, scroll_amount)
            self.page.wait_for_timeout(1000)
