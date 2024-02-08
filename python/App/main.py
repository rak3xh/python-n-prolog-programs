from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class Main(App):
    def build(self):
        layout = GridLayout(cols=2, spacing=20, padding=50)
        born = Label(text="Enter born year")
        self.current = TextInput()
        current = Label(text="Enter current year")
        self.born = TextInput()
        btn = Button(text="submit", on_press=self.hit)
        self.lab = Label(text="")
        layout.add_widget(born)
        layout.add_widget(self.born)
        layout.add_widget(current)
        layout.add_widget(self.current)
        layout.add_widget(btn)
        layout.add_widget(self.lab)
        return layout

    def hit(self, obj):
        res = int(self.current.text) - int(self.born.text)
        self.lab.text = f"age is:{res}"


if __name__ == "__main__":
    Main().run()
