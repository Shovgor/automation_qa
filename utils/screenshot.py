from datetime import datetime


def save_screenshot(page, name="screenshot"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{name}_{timestamp}.png"
    page.screenshot(path=path)
