import utils
from kivy.animation import Animation
from kivy.metrics import dp
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen

utils.load_kv("home_screen.kv")


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_tab = "home" 

    def on_tab_switch(self, *args):
        if args[1].icon == "home":
            self.ids.float_btn.icon = "refresh"
            self.current_tab = "home"
        elif args[1].icon == "account-group":
            self.ids.float_btn.icon = "plus"
            self.current_tab = "customers"
        elif args[1].icon == "finance":
            self.ids.float_btn.icon = "calendar"
            self.current_tab = "analytics"
    
    def on_press(self):
        if self.current_tab == 'customers':
            self.add_new_customer()
        elif self.current_tab == 'home':
            self.refresh_home()
        elif self.current_tab == 'analytics':
            self.update_analytics()

    def add_new_customer(self):
        self.manager.set_screen("add_customer")

    def refresh_home(self):
        pass

    def update_analytics(self):
        pass
            
        

class CustomFloatingActionButton(MDFloatingActionButton):
    def set_size(self, interval):
        self.width = "40dp"
        self.height = "40dp"

