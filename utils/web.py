from playwright import sync_playwright
#
# with sync_playwright() as p:
#     for browser_type in [p.chromium]:
#         browser = browser_type.launch(executablePath=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
#         page = browser.newPage()
#         page.goto('https://playwright.dev/#version=v1.5.2&path=docs%2Fapi.md&q=pagescreenshotoptions')
#         import time
#         time.sleep(3)
#         page.screenshot(path=f'example-{browser_type.name}.png', fullPage=True)
#         browser.close()
#
# def get_browser():
#     return p.chromium.launch(executablePath=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

import allure

class web():
    browser = None
    page = None
    pw_context = None


    def __init__(self, exec_path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"):
        # playwright = sync_playwright().start()
        # self.browser = playwright.chromium.launch(executablePath=exec_path, headless=False)
        self.pw_context = sync_playwright()
        pw = self.pw_context.__enter__()

        self.browser = pw.chromium.launch(executablePath=exec_path, headless=False)
        pass

    def visit(self, url, newPage= True):
        if newPage or self.page is None:
            self.page = self.browser.newPage()
        self.page.goto(url)

    def screenshot(self):
        byte_array = self.page.screenshot(type="png")
        allure.attach(byte_array, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            # .file('./data/totally_open_source_kitten.png', attachment_type=allure.attachment_type.PNG)

    def exit(self):
        self.browser.close()
        self.pw_context.__exit__()

    def __del__(self):
        print("exit")
        # self.browser.close()
        # self.pw_context.__exit__()



# w = web()
# w.visit("https://www.google.com")
# w.screenshot()