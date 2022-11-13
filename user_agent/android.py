import random
import json


class Android:
    def __init__(self):
        with open("android_data.json", encoding="utf-8") as f:
            self.android_model = json.load(f)

        # from https://en.wikipedia.org/wiki/Google_Chrome_version_history
        self.chrome_version_list = ["80.0.3987", "81.0.4044", "83.0.4103", "84.0.4147", "85.0.4183", "86.0.4240",
                                    "87.0.4280", "88.0.4324", "89.0.4389", "90.0.4430", "91.0.4472", "92.0.4515",
                                    "93.0.4577", "94.0.4606", "95.0.4638", "96.0.4664", "97.0.4692", "98.0.4758",
                                    "99.0.4844", "100.0.4896", "101.0.4951", "102.0.5005", "103.0.5060", "104.0.5112",
                                    "105.0.5195", "106.0.5249", "107.0.5304", "108.0.5359"]

    def generate_webview_ua(self) -> str:
        # generate webview useragent
        # in android is `WebView.getSettings().getUserAgentString()`
        # eg. "Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36"
        # 这里不加U
        android_version = self.generate_android_version()
        android_model = self.generate_android_model()
        chrome_version = self.generate_chrome_version()
        ua = f"Mozilla/5.0 (Linux; Android {android_version}; {android_model}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36"
        return ua

    @staticmethod
    def generate_android_version() -> str:
        # from ro.build.version.release 系统版本
        l = ["12", "11", "10", "9", "8.1.0", "8", "7.1.2", "7.1.1", "7.1.0", "7"]
        return random.choice(l)

    def generate_android_model(self) -> str:
        # ro.product.model  手机代号
        # ro.build.id 修订版本列表
        # "Pixel 3 XL Build/PPRL.190801.002"
        model = random.choice(self.android_model)
        return model["model"] + " Build/" + model["id"]

    def generate_chrome_version(self) -> str:
        return '{0}.{1}'.format(random.choice(self.chrome_version_list),
                                random.randint(80, 140))


if __name__ == "__main__":
    a = Android()
    print(a.generate_webview_ua())
