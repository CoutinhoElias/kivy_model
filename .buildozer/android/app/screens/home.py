from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import MDList, TwoLineIconListItem
from kivy.properties import StringProperty


Builder.load_string(
'''
<IconItemWidget>:
    IconLeftWidget:
        icon:root.icon

<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            id: toolbar
            title: "Aplicação de exemplo"
            elevation: 10
            left_action_items: [["menu", lambda x: app.nav_drawer.set_state('toggle')]]
        BoxLayout:
            orientation: 'vertical'
            BoxLayout:
                size_hint_y:.3
                Image:
                    source: 'company.png'
                    keep_ratio: False
                    allow_stretch: True
            BoxLayout:
                ScrollView:        
                    MDList:
                        size_hint_y: None
                        height: dp(100)
                        id: list_items

'''
)


class IconItemWidget(TwoLineIconListItem):
    name = StringProperty()

    def __init__(self, text, secondary, icon, name):
        self.text = text
        self.icon = icon
        self.secondary_text = secondary
        self.name = name
        super().__init__()


class HomeScreen(Screen):

    def on_enter(self):
        items = {
            "email": {
                "text": "Email",
                "secondary": "company@company.com",
                "name": 'email_screen'
            },
            "facebook": {
                "text": "Home",
                "secondary": "link to facebook",
                "name": 'facebook_screen'
            },
            "twitter": {
                "text": "Twitter",
                "secondary": "link to Twitter",
                "name": "twitter_screen"
            },
            "git": {
                "text": "Git",
                "secondary": "link to Git",
                "name": "git_screen"
            },
            "lock": {
                "text": "Git",
                "secondary": "link to Git",
                "name": "git_screen"
            },
            "clock": {
                "text": "Git",
                "secondary": "link to Git",
                "name": "git_screen"
            }
            
        }
        app = MDApp.get_running_app()
        list_items = app.root.ids.home_screen.ids.list_items
        for icon, data in items.items():
            item = IconItemWidget(
                text=data['text'],
                secondary=data['secondary'],
                icon=icon,
                name=data['name']
            )
            list_items.add_widget(item)
