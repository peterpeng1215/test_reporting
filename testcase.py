import utils.database
import utils.web

param_dic = {
    "host": "localhost",
    "database": "itest4u",
    "user": "postgres",
    "password": "Admin@1234"
}

class testcase:
    w : utils.web.web = None

    def setup_method(self):
        self.w = utils.web.web()

    def teardown_method(self, method):
        self.w.exit()

    def query(self, query):
        utils.database.step_query_db(param_dic, query)

    def web(self):
        self.w.visit("https://www.google.com")
        self.w.screenshot()

