from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from libs.uix.components.profile_preview_dialog import ProfilePreview

Builder.load_string(
    """
<DailyCustomerListItem>
    adaptive_height: True
    padding: dp(15)
    spacing: dp(20)

    FitImage:
        id: img
        source: root.image
        size_hint: None, None
        size: dp(50), dp(50)
        radius: [self.width/2,]
        pos_hint: {'center_y': .5}

    MDBoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_y': .5}
        spacing: dp(10)
        adaptive_height: True
        on_touch_down:
            if self.collide_point(*args[1].pos): root.open_dialog()

        MDLabel:
            id: name
            text: root.name
            font_style: 'Subtitle1'
            adaptive_height: True
        
        MDBoxLayout:
            orientation: 'horizontal'
            pos_hint: {'center_y': .5}
            spacing: dp(5)
            adaptive_height: True
        
            MDLabel:
                text: root.f_no
                font_style: 'Body2'
                theme_text_color: 'Secondary'
                adaptive_height: True
                size_hint_x: 0.25

            MDLabel:
                text: root.amount
                font_style: 'Body2'
                theme_text_color: 'Secondary'
                adaptive_height: True
                size_hint_x: 0.75
            
"""
)


class DailyCustomerListItem(RectangularRippleBehavior, MDBoxLayout):

    name = StringProperty()

    amount = StringProperty()

    image = StringProperty()

    installment = StringProperty()

    f_no = '123'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def open_dialog(self):
        ProfilePreview().fire(title=self.name, image=self.image)

