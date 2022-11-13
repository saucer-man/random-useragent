from android import Android

class UserAgent(Android):
    def __init__(self):
        Android.__init__(self)

    def android(self, app="webview"):
        """
        :param app: type, eg. app/webview/uc/baidu/qq/wechat
        :return:
        """
        if app =="webview":
            return self.generate_webview_ua()


if __name__ == "__main__":
    a = UserAgent()
    print(a.android(app="webview"))
