from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import MDList, ThreeLineIconListItem
from kivy.properties import StringProperty

import requests
import json

Builder.load_string('''
<InfoScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            id: toolbar
            pos_hint: {"top": 1}
            title: "Aplicação de exemplo"
            elevation: 10
            left_action_items: [["menu", lambda x: app.nav_drawer.set_state('toggle')]]
            
        BoxLayout:
            ScrollView:
                MDList:
                    id: list_states
    Widget:

''')


class InfoScreen(Screen):

    def on_enter(self):
        url = 'https://covid19-brazil-api.now.sh/api/report/v1'
    
        response = requests.get(url)
        status_code = response.status_code
        content_json = response.json()
        #print(json.dumps(content_json['data'], indent=4))
    
        i=0
        app = MDApp.get_running_app()
        print(app.root.ids, '<<<<<========')
        list_states = app.root.ids.information_screen.ids.list_states
    
        for state in content_json['data']:
            items = ThreeLineIconListItem(text=content_json['data'][i]['state'], 
                                          secondary_text='Casos de COVID-19: ' + str(content_json['data'][i]['cases']), 
                                          tertiary_text='Casos suspeitos: ' + str(content_json['data'][i]['suspects']))
            list_states.add_widget(items)
    
            i+=1
    pass        

