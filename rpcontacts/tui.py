from textual.app import App
from textual.widgets import Header, Footer

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
