import code

class Console:
    def __init__(self, locals={}):
        self.locals = locals

    def run(self):
        code.InteractiveConsole(locals=self.locals).interact()
