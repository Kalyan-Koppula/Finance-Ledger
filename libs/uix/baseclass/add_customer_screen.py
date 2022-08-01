import utils
from kivymd.uix.screen import MDScreen

utils.load_kv("add_customer_screen.kv")


class AddCustomerScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
