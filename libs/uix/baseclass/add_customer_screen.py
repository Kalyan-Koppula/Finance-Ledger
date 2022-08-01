import utils
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker
from datetime import datetime

utils.load_kv("add_customer_screen.kv")


class AddCustomerScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_date_save(self,instance,date_obj,range):
        value = date_obj.strftime("%d/%m/%Y")
        self.ids.text_date.text = value
        
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.open()
        date_dialog.bind(on_save = self.on_date_save)
    
    def save_details(self):
        print(self.ids.text_name.text)
        print(self.ids.aadhar_box.state)        
