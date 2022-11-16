import random

from random_useragent.chrome import Chrome


class Linux(Chrome):
    def __init__(self):
        super().__init__()

    def generate_linux_chrome_ua(self) -> str:
        # e.g. Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
        chrome_version = self.generate_chrome_version()
        return f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"

    def generate_linux_firefox_ua(self) -> str:
        # e.g. Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0
        # e.g. Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0
        # from https://www.mozilla.org/en-US/firefox/releases/
        firefox_version = f"{random.randint(70, 107)}.0"
        system_type = random.choice(["", "Ubuntu; ", "Fedora; "])
        return f"Mozilla/5.0 (X11; {system_type}Linux x86_64; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version}"

    def generate_linux_ua(self) -> str:
        d = random.choice(
            [self.generate_linux_chrome_ua, self.generate_linux_firefox_ua])
        return d()
