from textual.app import App
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label

class ContactsApp(App):
    BINDINGS = [
        ("m", "toggle_dark", "Toggle dark mode")
    ]

    def compose(self):
        yield Header()
        yield Footer()
    
    def on_mount(self):
        self.title = "RP Contacts"
        self.sub_title = "A Contacts book with Textual & Python"

    def action_toggle_dark(self):
        self.dark = not self.dark

class QuestionDialog(Screen):
    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message

    def compose(self):
        no_button = Button("No", variant="primary", id="No")
        no_button.focus()

        yield Grid(
            Label(self.message, id = "question"),
            Button("Yes", variant="error", id="yes"),
            no_button,
            id="question-dialog"
        )
    
    def on_button_pressed(self, event):
        if event.button.id == "yes":
            self.dismiss(True)
        else:
            self.dismiss(False)