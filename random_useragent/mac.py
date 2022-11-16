import random

from random_useragent.chrome import Chrome


class Mac(Chrome):
    def __init__(self):
        super().__init__()

        # from https://zh.m.wikipedia.org/zh-hans/MacOS
        self.macos_version_list = ["13.0", "12.6",
                                   "11.7", "10.15.7", "10.14.6", "10.13.6"]

        # from https://en.wikipedia.org/wiki/Safari_version_history
        self.safiri_version_list = [
            "16.1", "15.6.1", "14.1.2", "13.1.2", "12.1.2"]

    def generate_mac_chrome_ua(self) -> str:
        # e.g. Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
        chrome_version = self.generate_chrome_version()
        macos_vesion = random.choice(self.macos_version_list).replace(".", "_")
        return f"Mozilla/5.0 (Macintosh; Intel Mac OS X {macos_vesion}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"

    def generate_mac_firefox_ua(self) -> str:
        # e.g. Mozilla/5.0 (Macintosh; Intel Mac OS X 13.0; rv:107.0) Gecko/20100101 Firefox/107.0
        # from https://www.mozilla.org/en-US/firefox/releases/
        firefox_version = f"{random.randint(70, 107)}.0"
        macos_vesion = random.choice(self.macos_version_list)
        return f"Mozilla/5.0 (Macintosh; Intel Mac OS X {macos_vesion}; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version}"

    def generate_mac_safiri_ua(self) -> str:
        # e.g. Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15
        safari_version = random.choice(self.safiri_version_list)
        macos_vesion = random.choice(self.macos_version_list).replace(".", "_")
        return f"Mozilla/5.0 (Macintosh; Intel Mac OS X {macos_vesion}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{safari_version} Safari/605.1.15"

    def generate_mac_ua(self) -> str:
        d = random.choice(
            [self.generate_mac_chrome_ua, self.generate_mac_firefox_ua, self.generate_mac_safiri_ua])
        return d()
