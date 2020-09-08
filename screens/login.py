from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.app import App


Builder.load_string(
'''
<LetrasBrancas@MDLabel>
    size_hint_y: None
    height: self.texture_size[1]
    theme_text_color: "Custom"
    text_color: 1, 1, 1, 1

<CampoArredondado@MDTextFieldRound>
    pos_hint: {"center_x": .5}
    normal_color: 0, 1, 1, .5
    icon_left_color: 1, 1, 1, 1
    color_active: 1, 1, 1, 1

<LoginScreen>:
    email: input_email
    password: input_password

    FitImage:
        source: "guerreiros.jpg"        
    
    BoxLayout:
        id: box
        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: "24dp", "24dp", "24dp", "32dp"
        spacing: "12dp"
        size_hint_x: .75

        canvas:
            Color: 
                rgba: 0.5, 0.5, 0.5, 0.6
            Rectangle:
                pos: self.pos
                size: self.size    

        LetrasBrancas:
            text: "REGISTRO NA CONTA"
            bold: True

        Widget:
            size_hint_y: None
            bold: True
            height: "4dp"

        LetrasBrancas:
            text: "Seja bem vindo!"   
            height: "24dp"

        #Widget:
        #    size_hint_y: None
        #    height: "24dp"

        CampoArredondado:
            id: input_email
            icon_left: "mail"
            hint_text: "E-Mail"

        CampoArredondado:
            id: input_password
            icon_left: "lock"
            hint_text: "Senha" 
            password: True  

        LetrasBrancas:
            text: "Aceito os termos e condições"   
            height: "24dp"                     

        MDRaisedButton:
            text: "LOGIN"
            pos_hint: {"center_x": .5}
            md_bg_color: 0, 1, 1, .5
            on_release: root.login()
'''
)


class LoginScreen(Screen):
    email = ObjectProperty()
    password = ObjectProperty()

    def login(self):
        if self.email.text == 'admin' and self.password.text == 'admin':
            manager = App.get_running_app()
            manager.root.ids.screen_manager.current = 'home'
