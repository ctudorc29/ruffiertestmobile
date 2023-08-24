from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instructions import txt_instruction


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_Layout = BoxLayout(orientation='vertical')
        name_Layout = BoxLayout(orientation='horizontal')
        age_Layout = BoxLayout(orientation='horizontal')

        instructionText = Label(text = txt_instruction)
        nameLabel = Label(text = 'Enter your name:')
        nameInput = TextInput(multiline = False)
        name_Layout.add_widget(nameLabel)
        name_Layout.add_widget(nameInput)

        ageLabel = Label(text = 'Enter your name:')
        ageInput = TextInput(multiline = False)
        age_Layout.add_widget(ageLabel)
        age_Layout.add_widget(ageInput)
        
        startBtn = Button(text = 'start')

        main_Layout.add_widget(instructionText)
        main_Layout.add_widget(name_Layout)
        main_Layout.add_widget(age_Layout)
        main_Layout.add_widget(startBtn)
        self.add_widget(main_Layout)



class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class FifthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name = 'first'))
        sm.add_widget(SecondScreen(name = 'second'))
        sm.add_widget(ThirdScreen(name = 'third'))
        sm.add_widget(FourthScreen(name = 'fourth'))
        sm.add_widget(FifthScreen(name = 'fifth'))

        return sm
MyApp().run()