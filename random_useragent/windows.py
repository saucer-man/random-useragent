import random

from random_useragent.chrome import Chrome


class Windows(Chrome):
    def __init__(self):
        super().__init__()
        # from https://www.wandoujia.com/apps/7672441/history
        # but is android version, to use reluctantly
        self.edge_version_list = ["106.0.1370.52", "106.0.1370.47", "105.0.1343.50", "105.0.1343.48", "105.0.1343.34",
                                  "105.0.1343.27", "104.0.1293.70", "104.0.1293.63", "104.0.1293.60", "104.0.1293.55",
                                  "104.0.1293.47", "103.0.1264.77", "103.0.1264.71", "103.0.1264.62", "103.0.1264.51",
                                  "102.0.1245.44", "102.0.1245.39", "101.0.1210.53", "101.0.1210.47", "101.0.1210.39",
                                  "100.0.1185.50", "100.0.1185.43", "100.0.1185.36", "99.0.1150.55", "99.0.1150.46",
                                  "99.0.1150.39", "99.0.1150.30", "98.0.1108.62", "98.0.1108.55", "97.0.1072.78",
                                  "97.0.1072.69", "97.0.1072.55", "96.0.1054.62", "96.0.1054.36", "95.0.1020.32"]

    def generate_windows_chrome_ua(self) -> str:
        # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
        chrome_version = self.generate_chrome_version()
        return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"

    def generate_windows_edge_ua(self) -> str:
        # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42
        chrome_version = self.generate_chrome_version()
        edge_version = random.choice(self.edge_version_list)
        return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 Edg/{edge_version}"

    def generate_windows_firefox_ua(self) -> str:
        # e.g. Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0
        # from https://www.mozilla.org/en-US/firefox/releases/
        firefox_version = f"{random.randint(70, 107)}.0"
        return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version}"

    def generate_windows_ua(self) -> str:
        d = random.choice(
            [self.generate_windows_chrome_ua, self.generate_windows_edge_ua, self.generate_windows_firefox_ua])
        return d()
