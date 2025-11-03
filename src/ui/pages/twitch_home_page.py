# src/ui/pages/twitch_home_page.py
import os

from dotenv import load_dotenv

import config

load_dotenv()  # Load environment variables from .env


class TwitchHomePage:
    def __init__(self, page):
        self.page = page
        self.search_input = "input[placeholder='Search']"

    @staticmethod
    def open_twitch_home_page(browser_context):
        """Opens Twitch homepage and returns a TwitchHomePage instance."""
        page = browser_context.new_page()
        page.goto(config.TWITCH_URL)
        return TwitchHomePage(page)

    def search_streamer(self, streamer_name: str):
        """Searches for a streamer using the search bar."""
        self.page.fill(self.search_input, streamer_name)
        self.page.keyboard.press("Enter")
