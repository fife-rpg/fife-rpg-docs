from fife import fife

from fife_rpg.game_scene import GameSceneListener
from fife_rpg.components import fifeagent

class Listener(GameSceneListener):
    
    def mousePressed(self, event):
        player = self.gamecontroller.application.world.get_entity("PlayerCharacter")
        if event.getButton() == fife.MouseEvent.LEFT:
            scr_point = self.gamecontroller.application.screen_coords_to_map_coords(
                            (event.getX(), event.getY()), "actors"
                            )
            fifeagent.run(player, scr_point)