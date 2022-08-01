import utils
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

utils.load_kv("analytics_tab.kv")


class AnalyticsTab(FloatLayout, MDTabsBase):
    pass