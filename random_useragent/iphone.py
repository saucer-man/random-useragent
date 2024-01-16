import random
from random_useragent.chrome import Chrome


class Iphone(Chrome):
    def generate_ios_version(self) -> str:
        return f"{random.randint(14, 17)}.{random.randint(0, 8)}.{random.randint(0, 8)}"

    def generate_AppleWebKit_version(self) -> str:
        return f"{random.randint(600, 605)}.1.{random.randint(1, 20)}"

    def generate_safari_version(self) -> str:
        return f"{random.randint(601, 604)}.1"

    def generate_iphone_safari_ua(self) -> str:
        # e.g. Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1
        ios_version = self.generate_ios_version()
        AppleWebKit_version = self.generate_AppleWebKit_version()
        safari_version = self.generate_safari_version()
        return f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version.replace('.', '_')} like Mac OS X) AppleWebKit/{AppleWebKit_version} (KHTML, like Gecko) Version/{'.'.join(ios_version.split('.')[:-1])} Mobile/15E148 Safari/{safari_version}"

    def generate_iphone_chrome_ua(self) -> str:
        # e.g. Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.119 Mobile/15E148 Safari/604.1
        ios_version = self.generate_ios_version()
        safari_version = self.generate_safari_version()
        AppleWebKit_version = self.generate_AppleWebKit_version()
        chrome_version = self.generate_chrome_version()
        return f"Mozilla/5.0 (iPhone; CPU iPhone OS {'.'.join(ios_version.split('.')[:-1]).replace('.', '_')} like Mac OS X) AppleWebKit/{AppleWebKit_version} (KHTML, like Gecko) CriOS/{chrome_version} Mobile/15E148 Safari/{safari_version}"

    def generate_iphone_ua(self):
        d = random.choice(
            [self.generate_iphone_chrome_ua, self.generate_iphone_safari_ua])
        return d()


if __name__ == "__main__":
    i = Iphone()
    for _ in range(10):
        print(i.generate_iphone_ua())
