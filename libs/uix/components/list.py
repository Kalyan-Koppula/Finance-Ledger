from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout

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
        spacing: dp(5)
        adaptive_height: True

        MDLabel:
            text: root.text
            font_style: 'Subtitle1'
            adaptive_height: True

        MDLabel:
            text: root.secondary_text
            font_style: 'Body2'
            theme_text_color: 'Secondary'
            adaptive_height: True

    MDCheckbox:
        size_hint_x: 0.2
        pos_hint: {'center_x': .5, 'center_y': .5}
"""
)


class DailyCustomerListItem(RectangularRippleBehavior, MDBoxLayout):

    text = StringProperty()

    secondary_text = StringProperty()

    image = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

