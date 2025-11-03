# src/ui/pages/twitch_home_page.py
import os

from dotenv import load_dotenv

import config

load_dotenv()  # Load environment variables from .env


class TwitchHomePage:
    def __init__(self, page):
        self.page = page
        self.search_input = "input[placeholder='Search']"
        self.mobile_browse_button = "text=Browse"
        self.mobile_search_input = "input[type='search']"

    def open_twitch_home_page(self):
        """Opens Twitch homepage and returns a TwitchHomePage instance."""
        # page = browser_context.new_page()
        home = self.page.goto(config.TWITCH_URL)
        # home = TwitchHomePage(page)
        self.handle_app_popup()
        return home

    def handle_app_popup(self):
        """Close or bypass 'Open in App' popup if it appears."""
        try:
            if self.page.is_visible("text='Keep using web'", timeout=3000):
                self.page.click("text='Keep using web'")
                self.page.wait_for_timeout(1000)
            elif self.page.is_visible("button:has-text('Log In')", timeout=3000):
                # Sometimes popup has a 'Log In' instead
                self.page.keyboard.press("Escape")
        except Exception:
            pass

    def search_streamer(self, streamer_name: str):
        """Handles both desktop and mobile Twitch search."""
        try:
            # Desktop version
            if self.page.is_visible(self.search_input, timeout=3000):
                self.page.fill(self.search_input, streamer_name)
                self.page.keyboard.press("Enter")
            # Mobile version
            elif self.page.is_visible(self.mobile_browse_button, timeout=3000):
                self.page.click(self.mobile_browse_button)
                self.page.wait_for_selector(self.mobile_search_input)
                self.page.fill(self.mobile_search_input, streamer_name)
                self.page.keyboard.press("Enter")
            else:
                raise Exception("Search input not found on page.")
        except Exception as e:
            self.page.screenshot(path="search_error.png")
            raise e
