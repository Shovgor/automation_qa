# src/ui/pages/twitch_streamer_page.py
class TwitchStreamerPage:
    def __init__(self, page):
        self.page = page

    def handle_cookies(self):
        # Example cookie handler
        if self.page.locator("button:has-text('Accept Cookies')").is_visible():
            self.page.click("button:has-text('Accept Cookies')")
