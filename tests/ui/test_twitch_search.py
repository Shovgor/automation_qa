from src.ui.pages.twitch_home_page import TwitchHomePage
from src.ui.pages.twitch_streamer_page import TwitchStreamerPage
from utils.screenshot import save_screenshot


def test_search_stream(browser_context):
    home = TwitchHomePage.open_twitch_home_page(browser_context)
    home.search_streamer("StarCraft II")

    page = home.page
    page.wait_for_timeout(3000)
    page.locator("a[data-a-target='preview-card-image-link']").nth(0).click()
    page.wait_for_load_state("networkidle")

    streamer = TwitchStreamerPage(page)
    streamer.handle_cookies()
    streamer.scroll()

    save_screenshot(page, "twitch_streamer.png")
