from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3

age = 0 
pulse = 0
pulse2 = 0
pulse3 = 0

def check_int(strnum):
    try:
        return int(strnum)
    except:
        return False


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_Layout = BoxLayout(orientation='vertical', padding=8, spacing=8)
        name_Layout = BoxLayout(orientation='horizontal',size_hint=(0.8, None), height='30sp')
        age_Layout = BoxLayout(orientation='horizontal',size_hint=(0.8, None), height='30sp')

        instructionText = Label(text = txt_instruction)
        nameLabel = Label(text = 'Enter your name:', halign='right')
        nameInput = TextInput(multiline = False)
        name_Layout.add_widget(nameLabel)
        name_Layout.add_widget(nameInput)

        ageLabel = Label(text = 'Enter your age:', halign='right')
        self.ageInput = TextInput(multiline = False)
        age_Layout.add_widget(ageLabel)
        age_Layout.add_widget(self.ageInput)

        startBtn = Button(text = 'start', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

        startBtn.on_press = self.next
     

        main_Layout.add_widget(instructionText)
        main_Layout.add_widget(name_Layout)
        main_Layout.add_widget(age_Layout)
        main_Layout.add_widget(startBtn)
        self.add_widget(main_Layout)



    def next(self):

        global age
        age = check_int(self.ageInput.text)
        if age < 7:
            self.ageInput.text=""
        
        else:
            self.manager.transition.direction = 'up'
            self.manager.current = 'second'



class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

        main_Layout = BoxLayout(orientation='vertical', padding=8, spacing=8)
        pulse_Layout = BoxLayout(orientation='horizontal',size_hint=(0.8, None), height='30sp')

        instructionText = Label(text = txt_test1)
        pulseLabel = Label(text = 'Enter the result:', halign='right')
        self.pulseInput = TextInput(multiline = False)
        pulse_Layout.add_widget(pulseLabel)
        pulse_Layout.add_widget(self.pulseInput)


        nextbtn = Button(text = 'next', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

        nextbtn.on_press = self.next
     
        main_Layout.add_widget(instructionText)
        main_Layout.add_widget(pulse_Layout)
        main_Layout.add_widget(nextbtn)
        self.add_widget(main_Layout)
    
    
    def next(self):

        global pulse

        pulse = check_int(self.pulseInput.text)
        if pulse < 0:
            self.pulseInput.text=""
        
        else:
            self.manager.transition.direction = 'up'
            self.manager.current = 'third'


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_Layout = BoxLayout(orientation='vertical', padding=8, spacing=8)


        instructionText = Label(text = txt_test2)
        mainLabel = Label(text = 'Enter the result:', halign='right')
        mainInput = TextInput(multiline = False)
       



        nextbtn = Button(text = 'next', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

        nextbtn.on_press = self.next


        main_Layout.add_widget(instructionText)
        main_Layout.add_widget(nextbtn)
        self.add_widget(main_Layout)


    def next(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'fourth'




class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_Layout = BoxLayout(orientation='vertical', padding=8, spacing=8)
        result_Layout = BoxLayout(orientation='horizontal',size_hint=(0.8, None), height='30sp')
        restresult_Layout = BoxLayout(orientation='horizontal',size_hint=(0.8, None), height='30sp')

        instructionText = Label(text = txt_test3)
        restresultLabel = Label(text = 'Result after rest:', halign='right')
        self.restresultInput = TextInput(multiline = False)
        restresult_Layout.add_widget(restresultLabel)
        restresult_Layout.add_widget(self.restresultInput)

        resultLabel = Label(text = 'Result:', halign='right')
        self.resultInput = TextInput(multiline = False)
        result_Layout.add_widget(resultLabel)
        result_Layout.add_widget(self.resultInput)

        finalizeBtn = Button(text = 'finalize', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

        finalizeBtn.on_press = self.next
     

        main_Layout.add_widget(instructionText)
        main_Layout.add_widget(restresult_Layout)
        main_Layout.add_widget(result_Layout)
        main_Layout.add_widget(finalizeBtn)
        self.add_widget(main_Layout)

    def next(self):

        global pulse2
        global pulse3

        pulse2 = check_int(self.restresultInput.text)
        pulse3 = check_int(self.resultInput.text)
        if pulse2 < 0 or pulse3 < 0:

            self.restresultInput.text=""
            self.resultInput.text=""
        else:
            self.manager.transition.direction = 'up'
            self.manager.current = 'fifth'


class FifthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_Layout = BoxLayout(orientation='vertical', padding=8, spacing=8)


        label = Label(text = 'Great job your pulse is above average!', halign='right')

        main_Layout.add_widget(label)
        self.add_widget(main_Layout)

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