import utils
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

utils.load_kv("daily_tab.kv")


class DailyTab(FloatLayout, MDTabsBase):
    pass
