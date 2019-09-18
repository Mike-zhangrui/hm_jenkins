import allure


class TestJenkins:
    @allure.step(title="步骤")
    def test(self):
        allure.attach("用户名", "jenkins")
        assert True
