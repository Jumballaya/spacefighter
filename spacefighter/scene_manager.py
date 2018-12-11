'''
Scene Manager
'''

class SceneManager(object):

    def __init__(self, title, key='title'):
        self.scenes = {}
        self.scenes[key] = title
        self.current = self.scenes[key]
        self.title = key

    def add_scene(self, key, scene):
        self.scenes[key] = scene

    def use_joystick(self, joystick):
        self.current.set_joystick(joystick)

    def set_scene(self, key):
        self.current = self.scenes[key]

    def pause(self):
        self.current.pause()

    def unpause(self):
        self.current.unpause()

    def handle_event(self, e):
        self.current.handle_event(e)

    def update(self):
        self.current.update()
