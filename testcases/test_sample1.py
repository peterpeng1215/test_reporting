from testcase import testcase
import allure
import pytest


@allure.feature('mytest feature')  # feature definition function
class TestShoppingTrolley(testcase):
    @allure.story('first story')  # toryDefine user scenes
    @pytest.mark.parametrize('text', ['text', 'test2'], ids=['id explaining value 1', 'id explaining value 2'])
    def test_success(self, text):
        with allure.step('query database'):
            self.query("select * from users")

        with allure.step('visit google'):
            self.w.visit("https://www.google.com")
            self.w.screenshot()

        with allure.step('input search str'):
            self.w.page.type('form[role=search] input[type=text]',text)
            self.w.screenshot()
            self.w.page.click('input[type=submit][value="Google Search"]')
            self.w.page.waitForSelector('#rso')
            assert len(self.w.page.querySelectorAll('table[role=presentation] td'))==12

            self.w.screenshot()


# @allure.feature('mytest')
# @allure.title("hello world")
# @allure.description("my testcase description")
# def test_success():
#     """this test succeeds"""
#     assert True
#     utils.database.step_query_db(param_dic, f"select * from users")
