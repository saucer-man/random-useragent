import random

from random_useragent.android import Android
from random_useragent.linux import Linux
from random_useragent.mac import Mac
from random_useragent.windows import Windows


class UserAgent(Android, Windows, Mac, Linux):
    def __init__(self):
        Android.__init__(self)
        Windows.__init__(self)
        Mac.__init__(self)
        Linux.__init__(self)

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
        if app == "firefox":
            return self.generate_windows_firefox_ua()
        if app == "edge":
            return self.generate_windows_edge_ua()

    def mac(self, app="default"):
        if app == "default":
            return self.generate_mac_ua()
        if app == "chrome":
            return self.generate_mac_chrome_ua()
        if app == "firefox":
            return self.generate_mac_firefox_ua()
        if app == "safiri":
            return self.generate_mac_safiri_ua()

    def linux(self, app="default"):
        if app == "default":
            return self.generate_linux_ua()
        if app == "chrome":
            return self.generate_linux_chrome_ua()
        if app == "firefox":
            return self.generate_linux_firefox_ua()

    def pc(self):
        d = random.choice(
            [self.windows, self.mac, self.linux])
        return d()

    def random(self):
        d = random.choice(
            [self.android, self.windows, self.mac, self.linux])
        return d()


if __name__ == "__main__":
    a = UserAgent()
    print(a.random())
    print(a.android())
    print(a.windows())
    print(a.linux())
    print(a.mac())
    print(a.pc())
