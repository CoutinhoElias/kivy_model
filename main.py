from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.factory import Factory
from menu import ItemWidget


Builder.load_string(
'''
#: import LoginScreen screens.login
#: import HomeScreen screens.home
#: import InfoScreen screens.info
#: import ContentDrawer menu

<RootWidget@Screen>:
    NavigationLayout:
        ScreenManager:
            id: screen_manager
            LoginScreen:
                id: login_screen
                name: 'login'
            HomeScreen:
                id: home_screen
                name: 'home'
            InfoScreen:
                id: information_screen
                name: 'information'
            

        MDNavigationDrawer:
            id: nav_drawer
            ContentDrawer:
                id: content_drawer
'''
)

class ExampleApp(MDApp):

    @property
    def nav_drawer(self):
        app = self.get_running_app()
        return app.root.ids.nav_drawer

    def switch_to(self, screen_name):
        app = self.get_running_app()
        app.root.screen_manager.current = screen_name


    def on_start(self):
        items = {
            "home": {
                "text": "Home",
                "screen": "home"},
            "information": {
                "text":"Informações",
                "screen": "information"},
            "close": {
                "text": "Fechar",
                "screen": ""}
        }

        for icon, data in items.items():
            item = ItemWidget(text=data['text'], screen=data['screen'], icon=icon)
            self.root.ids.content_drawer.ids.scroll_list.add_widget(
                item
            )
    def build(self):
        return Factory.RootWidget()

if __name__ == '__main__':
    ExampleApp().run()