from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import BaseDialog

Builder.load_string(
    """
#: import gch kivy.utils.get_color_from_hex

<ProfilePreview>
    auto_dismiss: True
    orientation: 'vertical'
    adaptive_size: True
    size_hint: 0.7,0.5
    pos_hint: {'top':0.9}

    MDToolbar:
        title: root.title
        font_style: 'Body2'
        specific_text_color: 1, 1, 1, 1
        right_action_items: [["check", lambda x: root.save_details()]]

    MDBoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_y": .5,"center_x": .5}
        spacing: dp(10)
        padding: [0,dp(20),0,dp(20)]
        adaptive_height: True

        canvas.before:
            Color:
                rgba: 1,1,1,1
            Rectangle:
                size: self.size
                pos: self.pos

        MDBoxLayout:
            orientation: 'horizontal'
            pos_hint: {'center_y': .5}
            spacing: dp(5)
            adaptive_height: True
            
            MDLabel:
                text: root.f_no
                halign: "center"
                pos_hint: {"center_y": .5,"center_x": .5}
                font_style: 'Subtitle1'
                theme_text_color: 'Secondary'
                padding: [dp(5), dp(5)]
                adaptive_height: True
            
            MDLabel:
                text: root.amount
                halign: "center"
                font_style: 'Subtitle1'
                theme_text_color: 'Secondary'
                padding: [dp(5), dp(5)]
                adaptive_height: True

        MDTextField:
            hint_text: "Installment"
            text: root.installment
            input_filter: 'int'
            font_style: 'Body1'
            theme_text_color: 'Secondary'
            pos_hint: {"center_y": .5,"center_x": .5}
            mode: "rectangle"
            size_hint_x: 0.5   





"""
)


class ProfilePreview(MDBoxLayout, BaseDialog):

    title = StringProperty()

    amount = StringProperty()

    f_no = '#23'

    installment = '100'

    def fire(self, title, f_no, amount):
        self.title = title
        self.f_no = f_no
        self.amount = amount
        self.open()

    def save_details(self):
        self.dismiss()
