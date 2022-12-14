import json

import utils
from kivy.clock import Clock
from kivy.factory import Factory  # NOQA: F401
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

utils.load_kv("root.kv")


class Root(ScreenManager):
    """
    The Root (or Assembler) of the App.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.add_screens)
        Window.bind(on_keyboard = self.on_back_button)
        """
        Adding the screens to the Root (ScreenManager).
        """

    def add_screens(self, interval):
        """
        If you need to use more screens in your app,
        Create your screen files like below:
            1. Create screen_name.py in libs/uix/baseclass/
            2. Create screen_name.kv in libs/uix/kv/
            3. Add the screen details in screens.json like below:
                {
                    ...,
                    "from libs.uix.baseclass.screen_name import ScreenClassName": {
                        "screen_name": "my_screen_name",
                        "factory": "Factory.ScreenClassName()",
                    }
                }
                Note: In .JSON you must not use:
                        * Extra Commas
                        * Comments
                        * Trailing White Spaces.
        """
        with open("screens.json") as f:
            screens = json.load(f)
            for import_screen, screen_details in screens.items():
                exec(import_screen)  # excecuting imports
                screen_object = eval(screen_details["factory"])  # adding it to Factory
                screen_object.name = screen_details[
                    "screen_name"
                ]  # giving the name of the screen
                self.add_widget(
                    screen_object
                )  # finally adding it to the screen manager

    def set_screen(self, name, side="left"):
        self.transition.direction = side
        self.current = name

    def on_back_button_callback(self):
        if self.current != 'home':
            self.set_screen('home')
            return True
        return False

    def on_back_button(self,window,key,*args):
        if key == 27:
            return self.on_back_button_callback() 

