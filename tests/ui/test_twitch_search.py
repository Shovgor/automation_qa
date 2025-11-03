from src.ui.pages.twitch_home_page import TwitchHomePage
from src.ui.pages.twitch_search_page import TwitchSearchPage
from src.ui.pages.twitch_streamer_page import TwitchStreamerPage
from utils.screenshot import save_screenshot


def test_search_stream(browser_context):
    page = browser_context.new_page()
    home = TwitchHomePage(page)
    home.open_twitch_home_page()
    home.search_streamer("StarCraft II")

    search_page = TwitchSearchPage(home.page)
    search_page.wait_to_load()
    search_page.scroll(times=2)
    search_page.choose_streamer()

    streamer = TwitchStreamerPage(search_page.page)
    streamer.handle_cookies()

    save_screenshot(streamer.page, "twitch_streamer.png")
    streamer.page.wait_for_timeout(1000)
