from playwright.sync_api import Playwright


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://cloud.ru")
    page.get_by_role("navigation").get_by_text("Сервисы").click()
    page.locator("//*[@class='Products_menuItem__OZqKu']").get_by_text("Инфраструктура").click()
    page.get_by_role("link", name="Product Icon API Gateway Высокопроизводительный, полностью управляемый хостинг API").first.click()
    h1_title = page.wait_for_selector("h1[class='Hero_title__0eNxo']").inner_text()
    assert h1_title == "API Gateway", "Требуемая страница не открылась"
    page.close()
    context.close()
    browser.close()
