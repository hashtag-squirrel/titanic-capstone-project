from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class E2ETest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_flow(self):
        self.browser.get(self.live_server_url + "/userform/")
        self.browser.find_element(By.ID, "id_full_name").send_keys("E2E User")
        self.browser.find_element(By.ID, "id_age").send_keys("30")
        Select(self.browser.find_element(By.ID, "id_title")).select_by_value("mr")
        Select(self.browser.find_element(By.ID, "id_gender")).select_by_value("0")
        Select(self.browser.find_element(By.ID, "id_travel_class")).select_by_value("3")
        self.browser.find_element(By.ID, "id_is_alone").click()

        self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        WebDriverWait(self.browser, 10).until(
            lambda d: ("prob" in d.page_source.lower()) or ("result" in d.page_source.lower())
        )

        body = self.browser.page_source.lower()
        self.assertTrue("prob" in body or "result" in body)