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

    MDBoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_x': .5}
        spacing: dp(5)
        adaptive_height: True
        
        canvas.before:
            Color:
                rgba: 1,1,1,1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [10,10]

        MDLabel:
            id: title
            text: root.title
            font_style: 'Subtitle1'
            padding: [dp(5), dp(5)]
            adaptive_height: True

            canvas.before:
                Color:
                    rgba: self.theme_cls.accent_color
                RoundedRectangle:
                    size: self.size
                    pos: self.pos

        MDBoxLayout:
            orientation: 'horizontal'
            pos_hint: {'center_y': .5}
            spacing: dp(5)
            adaptive_height: True
            
            MDLabel:
                text: root.f_no
                padding: [dp(5), dp(5)]
                adaptive_height: True
            
            MDLabel:
                text: root.amount
                padding: [dp(5), dp(5)]
                adaptive_height: True

        MDTextField:
            hint_text: "Installment"
            input_filter: 'int'
            pos_hint: {"center_y": .5,"center_x": .5}
            mode: "rectangle"
            size_hint_x: 0.5




    MDBoxLayout:
        id: btn_box
        adaptive_height: True
        size_hint_x: None
        width: self.minimum_size[0] + dp(40)

        Widget:

        DialogIconButton:
            icon: 'android-messages'

        DialogIconButton:
            icon: 'phone'

        DialogIconButton:
            icon: 'video'

        DialogIconButton:
            icon: 'information-outline'

        Widget:

<DialogIconButton@MDIconButton>
    theme_text_color: 'Custom'
    text_color: self.theme_cls.accent_color
"""
)


class ProfilePreview(MDBoxLayout, BaseDialog):

    title = StringProperty()

    amount = StringProperty()

    f_no = '123'

    def fire(self, title, f_no, amount):
        self.title = title
        self.f_no = f_no
        self.amount = amount
        self.open()
