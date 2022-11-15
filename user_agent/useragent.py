from android import Android
from windows import Windows
import random

class UserAgent(Android, Windows):
    def __init__(self):
        Android.__init__(self)
        Windows.__init__(self)

    def android(self, app="default"):
        """
        :param app: type, eg. app/webview/uc/baidu/qq/wechat
        :return:
        """
        if app == "default":
            return self.generate_android_ua()
        if app == "webview":
            return self.generate_android_webview_ua()
        if app == "app":
            return self.generate_android_app_ua()
        if app == "uc":
            return self.generate_android_uc_ua()
        if app == "qq":
            return self.generate_android_qq_ua()
        if app == "baidu":
            return self.generate_android_baidu_ua()
        if app == "wechat":
            return self.generate_android_wechat_ua()

    def windows(self, app="default"):
        if app == "default":
            return self.generate_windows_ua()
        if app == "chrome":
            return self.generate_windows_chrome_ua()
        if app == "edge":
            return self.generate_windows_edge_ua()

    def random(self):
        d = random.choice(
            [self.android, self.windows])
        return d()

if __name__ == "__main__":
    a = UserAgent()
    print(a.random())
