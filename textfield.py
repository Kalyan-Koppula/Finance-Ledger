from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    padding: "10dp"
    spacing: "10dp"
    orientation: "vertical"

    MDBoxLayout:
        orientation: "horizontal"
        padding: "10dp"
        
        MDIcon:
            icon: "account"
            size_hint_x: .25
            pos_hint: {"center_y": .5,"center_x":1}

        MDTextField:
            id: text_field_error
            hint_text: "Name"
            pos_hint: {"center_y": .5}
            mode: "rectangle"
            size_hint_x: 0.75
            padding_right: "20dp"
    
    MDBoxLayout:
        orientation: "horizontal"
        padding: "10dp"
        
        MDIcon:
            icon: "cash-multiple"

        MDTextField:
            id: text_field_error
            hint_text: "Amount"
            pos_hint: {"center_y": .5}
            mode: "rectangle"
'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        self.screen.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        return self.screen

    def set_error_message(self, instance_textfield):
        self.screen.ids.text_field_error.error = True


Test().run()