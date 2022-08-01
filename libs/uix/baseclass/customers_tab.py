import utils
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

utils.load_kv("customers_tab.kv")


class CustomersTab(FloatLayout, MDTabsBase):
    pass
