import random


class Chrome:
    def __init__(self):
        # from https://en.wikipedia.org/wiki/Google_Chrome_version_history
        self.chrome_version_list = ["80.0.3987", "81.0.4044", "83.0.4103", "84.0.4147", "85.0.4183", "86.0.4240",
                                    "87.0.4280", "88.0.4324", "89.0.4389", "90.0.4430", "91.0.4472", "92.0.4515",
                                    "93.0.4577", "94.0.4606", "95.0.4638", "96.0.4664", "97.0.4692", "98.0.4758",
                                    "99.0.4844", "100.0.4896", "101.0.4951", "102.0.5005", "103.0.5060", "104.0.5112",
                                    "105.0.5195", "106.0.5249", "107.0.5304", "108.0.5359"]

    def generate_chrome_version(self) -> str:
        return '{0}.{1}'.format(random.choice(self.chrome_version_list),
                                random.randint(80, 140))
