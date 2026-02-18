import re
import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.django_db(transaction=True)
def test_user_can_submit_form_and_see_result_and_history(live_server):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        page = browser.new_page()
        print("LIVE SERVER URL:", live_server.url)

        # 1. Home
        page.goto(live_server.url + "/")
        page.wait_for_load_state("domcontentloaded")

        # 2. Go to Form
        page.goto(live_server.url + "/userform/")
        page.wait_for_load_state("domcontentloaded")

        # 3. Fill form
        page.fill("#id_full_name", "E2E Test User")
        page.fill("#id_age", "30")
        page.select_option("#id_title", "mr")
        page.select_option("#id_gender", "0")
        page.select_option("#id_travel_class", "3")
        page.check("#id_is_alone")

        # 4. Submit
        page.click('button[type="submit"]')
        page.wait_for_load_state("domcontentloaded")

        # 5. Assert we see results page content
        html = page.content()
        assert "prob" in html.lower() or "result" in html.lower()

        # 6. Go to history and comfirm something exits
        page.goto(live_server.url + "/history/")
        page.wait_for_load_state("domcontentloaded")
        assert "E2E Test User" in page.content()

        page.pause()
        browser.close()