class TwitchSearchPage:
    def __init__(self, page):
        self.page = page
        self.search_results_container = "[class='Layout-sc-1xcs6mc-0 cOFToR']"
        # self.streamer_preview = "a[data-a-target='preview-card-image-link']"

    def scroll(self, times: int = 3):
        """Scroll the search results container multiple times to load more results."""
        for _ in range(times):
            self.page.mouse.wheel(0, 1000)
            self.page.wait_for_timeout(1000)

    def wait_to_load(self, timeout: int = 10000):
        self.page.wait_for_selector(self.search_results_container, timeout=timeout)

    def choose_streamer(self):
        """Scroll and click the first available streamer preview."""
        first_streamer = self.page.locator(self.search_results_container).nth(3)
        first_streamer.wait_for(state="visible", timeout=10000)
        first_streamer.click()
        self.page.wait_for_load_state("networkidle")
