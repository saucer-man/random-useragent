from android import Android

class UserAgent(Android):
    def __init__(self):
        Android.__init__(self)

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
 
 
if __name__ == "__main__":
    a = UserAgent()
    print(a.android())
