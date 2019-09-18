import allure


class TestJenkins:
    @allure.step("步骤")
    def test(self):
        allure.attach("jenkins")
        assert True
