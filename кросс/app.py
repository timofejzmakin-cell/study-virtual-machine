from textual.app import App, ComposeResult
from textual.widgets import Button, TextArea
from textual import on

import asm
from asm import asm 
from interpreter import execute




DEMO = """
write_const 38 10
write_const 1 11
write_value 1 11
rshift 10 11
""".strip()

TEMPLATE = """
memory: %s
registers: %s
bytecode: %s
""".strip()


class ClockApp(App):
    CSS = """
    Screen { align: center middle; }
    Digits { width: auto; }
    """

    def compose(self) -> ComposeResult:
        yield TextArea(text=DEMO, id="input")
        yield Button(label="start", id="main")
        yield TextArea(id="output", text=" ")

    @on(Button.Pressed, "#main")
    def click(self) -> None:
        program = self.query_one("#input").text
        bytecode = asm(list(program.split('\n')))
        textcode = " ".join([hex(i) for i in bytecode])
        memory, registers=execute(bytecode)
        self.query_one("#output").text = TEMPLATE % (memory, registers, textcode)

if __name__ == "__main__":
    app = ClockApp()
    app.run()