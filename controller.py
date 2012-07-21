
""" Keyboard manager """

__author__ = "Peter Bennett"
__copyright__ = "Copyright 2012, Peter A Bennett"
__license__ = "LGPL"
__version__ = "0.1"
__maintainer__ = "Peter Bennett"
__email__ = "pab850@googlemail.com"
__contact__ = "www.bytebash.com"


from pyglet.window import key
from pyglet import clock

class Controller(object):
    def __init__(self, window, player, console):
        self.keys = key.KeyStateHandler()
        self.player = player
        
        # Console
        self.console = console        
        
        # States
        self.states = {}
        self.states['Wireframe Mode'] = False        
        
        # Key Press Events
        self.keyPressEvents = {}
        
        clock.schedule(self.update)
        
        window.push_handlers(self.on_key_press)
        window.push_handlers(self.on_key_release)
        window.push_handlers(self.keys)
        window.push_handlers(self.on_mouse_motion)
        
    def on_mouse_motion(self, x, y, dx, dy):
        self.player.orient(dx*0.08, -dy*0.08)
        
    def keyPressed(self, symbol):
        if symbol in self.keyPressEvents:
            return self.keyPressEvents[symbol]
        return False

    def update(self, dt):
        # Handle events that must occur while a key is pressed.
        if self.keyPressed(key.W):
            self.player.update(dt,True,False,False,False)
        elif self.keyPressed(key.S):
            self.player.update(dt,False,True,False,False)
            
        if self.keyPressed(key.A):
            self.player.update(dt,False,False,True,False)
        elif self.keyPressed(key.D):
            self.player.update(dt,False,False,False,True)
            
        self.player.update(dt,False,False,False,False) 
               

    def on_key_press(self, symbol, modifiers):
        # Handle events that only require one action per keypress here.
        
        # Player jump
        if symbol == key.SPACE:
            if not self.keyPressed(key.SPACE):
                self.player.jump()
        # Enable or disable flight mode.
        if symbol == key.F:
            if not self.keyPressed(key.F):
                self.player.toggleFlightMode()
        # Enable or disable wireframe mode.
        if symbol == key.T:
            if not self.keyPressed(key.T):
                self.states['Wireframe Mode'] = not self.states['Wireframe Mode']
                self.console.updateConsole('Wireframe mode: ' +
                                           str(self.states['Wireframe Mode']))
                
        self.keyPressEvents[symbol] = True
        
    def on_key_release(self, symbol, modifiers):
        self.keyPressEvents[symbol] = False