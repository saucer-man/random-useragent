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

        # from https://www.wandoujia.com/apps/36557/history?spm=aligames_platform_ug.wdj_seo.0.0.57205b3ebiRRii
        self.uc_version_list = ["15.1.5.1205", "15.1.4.1204", "15.1.2.1202", "15.1.1.1201", "15.0.9.1199",
                                "15.0.7.1197", "15.0.6.1196", "15.0.5.1195", "15.0.4.1194", "15.0.3.1193",
                                "15.0.2.1192", "15.0.1.1191", "15.0.0.1190", "14.1.0.1185", "14.0.0.1181",
                                "13.9.9.1180", "13.9.8.1179", "13.9.7.1178", "13.9.6.1177", "13.9.5.1176",
                                "13.9.4.1175", "13.9.3.1174", "13.9.2.1173", "13.9.1.1172", "13.9.0.1171",
                                "13.8.9.1170", "13.8.8.1169", "13.8.7.1168", "13.8.6.1167", "13.8.5.1166",
                                "13.8.4.1165", "13.8.3.1164", "13.8.2.1163", "13.8.1.1162", "13.8.0.1161",
                                "13.7.9.1160", "13.7.8.1159", "13.7.7.1158", "13.7.6.1157", "13.7.4.1155",
                                "13.7.3.1154", "13.7.1.1152", "13.7.0.1151", "13.6.9.1150", "13.6.8.1149",
                                "13.6.7.1148", "13.6.6.1146", "13.6.5.1145", "13.6.3.1143", "13.6.2.1142",
                                "13.6.1.1141", "13.6.0.1140", "13.5.9.1139", "13.5.8.1138", "13.5.7.1137",
                                "13.5.6.1136", "13.5.5.1135", "13.5.4.1134", "13.5.3.1133", "13.5.2.1132",
                                "13.5.1.1131", "13.5.0.1130", "13.4.9.1129", "13.4.8.1128", "13.4.7.1127",
                                "13.4.5.1125", "13.4.4.1124", "13.4.2.1122", "13.4.1.1121", "13.4.0.1120",
                                "13.3.9.1119", "13.3.8.1118", "13.3.7.1117", "13.3.6.1116", "13.3.5.1115",
                                "13.3.4.1114", "13.3.3.1113", "13.3.2.1112", "13.3.1.1111", "13.2.9.1109",
                                "13.2.8.1108", "13.2.7.1107", "13.2.6.1106", "13.2.5.1105", "13.2.3.1103",
                                "13.2.2.1102", "13.2.1.1101", "13.2.0.1100", "13.1.9.1099", "13.1.8.1098",
                                "13.1.7.1097", "13.1.6.1096", "13.1.5.1095", "13.1.4.1094", "13.1.3.1093",
                                "13.1.2.1092", "13.1.0.1090", "13.0.8.1088", "13.0.7.1087", "13.0.6.1086",
                                "13.0.5.1085", "13.0.4.1084", "13.0.3.1083", "13.0.2.1082", "13.0.1.1081",
                                "13.0.0.1080", "12.9.9.1079", "12.9.8.1078", "12.9.7.1077", "12.9.6.1076",
                                "12.9.5.1075", "12.9.4.1074", "12.9.2.1072", "12.9.1.1071", "12.9.0.1070",
                                "12.8.9.1069", "12.8.8.1068", "12.8.7.1067", "12.8.6.1066", "12.8.5.1065",
                                "12.8.4.1064", "12.8.2.1062", "12.8.0.1060", "12.7.9.1059", "12.7.8.1058",
                                "12.7.6.1056", "12.7.4.1054", "12.7.2.1052", "12.7.0.1050", "12.6.8.1048",
                                "12.6.6.1046", "12.6.2.1042", "12.6.1.1041", "12.6.0.1040", "12.5.9.1039",
                                "12.5.6.1036", "12.5.5.1035", "12.5.4.1034", "12.5.2.1032", "12.5.0.1030",
                                "12.4.8.1028", "12.4.6.1026", "12.4.4.1024", "12.4.3.1023", "12.4.2.1022",
                                "12.4.0.1020", "12.3.8.1018", "12.3.6.1016", "12.3.0.1010", "12.2.8.1008",
                                "12.2.6.1006", "12.2.4.1004", "12.2.2.1002"]

    def generate_android_webview_ua(self) -> str:
        # generate webview useragent
        # in android is `WebView.getSettings().getUserAgentString()`
        # eg. "Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36"
        # 这里不加U
        android_version = self.generate_android_version()
        android_model = self.generate_android_model()
        chrome_version = self.generate_chrome_version()
        ua = f"Mozilla/5.0 (Linux; Android {android_version}; {android_model}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36"
        return ua

    def generate_android_app_ua(self) -> str:
        # generate app useragent
        # in android is `System.getProperty("http.agent");`
        # eg. "Dalvik/2.1.0 (Linux; U; Android 10; Pixel 3a Build/QQ2A.200305.002)"
        # 这里一般要U
        android_version = self.generate_android_version()
        android_model = self.generate_android_model()
        ua = f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {android_model})"
        return ua

    def generate_android_uc_ua(self) -> str:
        # generate ucbrowser useragent
        # Mozilla/5.0 (Linux; U; Android 9; zh-CN; LON-AL00 Build/HUAWEILON-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.0.1070 Mobile Safari/537.36
        android_version = self.generate_android_version()
        android_model = self.generate_android_model()
        chrome_version = self.generate_chrome_version()
        uc_version = self.generate_uc_version()
        ua = f"Mozilla/5.0 (Linux; Android {android_version}; zh-CN; {android_model}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} UCBrowser/{uc_version} Mobile Safari/537.36"
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

    def generate_uc_version(self) -> str:
        return random.choice(self.uc_version_list)


if __name__ == "__main__":
    a = Android()
    print(a.generate_webview_ua())
