from fife import fife

from fife_rpg import RPGApplication
from fife_rpg.rpg_application import ApplicationListener
from fife_rpg.components import fifeagent

class Listener(ApplicationListener, fife.IMouseListener):
    def __init__(self, engine, application):
        ApplicationListener.__init__(self, engine, application)
        fife.IMouseListener.__init__(self)
        self._eventmanager.addMouseListener(self)

    def mouseEntered(self, event):
        pass
    
    def mouseExited(self, event):
        pass

    def mousePressed(self, event):
        player = self._application.world.get_entity("PlayerCharacter")
        if event.getButton() == fife.MouseEvent.LEFT:
            scr_point = self._application.screen_coords_to_map_coords(
                            (event.getX(), event.getY())
                            )
            fifeagent.run(player, scr_point)
                
    def mouseReleased(self, event):
        pass

    def mouseClicked(self, event):
        pass

    def mouseMoved(self, event):
        pass
    
    def mouseDragged(self, event):
        pass    
    
    def mouseWheelMovedDown(self, event):
        pass

    def mouseWheelMovedUp(self, event):
        pass

class Application(RPGApplication):
    
    def __init__(self, settings):
        RPGApplication.__init__(self, settings)
        
    def createListener(self):
        self._listener = Listener(self.engine, self)
        return self._listener        