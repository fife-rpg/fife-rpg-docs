from fife import fife

from fife_rpg.game_scene import GameSceneListener, GameSceneController
from fife_rpg.components import fifeagent
from fife_rpg.actions import ActionManager
from fife.extensions.pychan.internal import get_manager

class Listener(GameSceneListener):
    
    def mousePressed(self, event):
        application = self.gamecontroller.application
        player = application.world.get_entity("PlayerCharacter")
        if event.getButton() == fife.MouseEvent.LEFT:
            map_point = application.screen_coords_to_map_coords(
                            (event.getX(), event.getY()), "actors"
                            )
            fifeagent.run(player, map_point)
        if event.getButton() == fife.MouseEvent.RIGHT:
            game_map = application.current_map
            if game_map:
                scr_point = fife.ScreenPoint(event.getX(), event.getY())
                actor_instances = game_map.get_instances_at(
                                                    scr_point, 
                                                    game_map.get_layer("actors"))
            if actor_instances:
                    for actor in actor_instances:
                        identifier = actor.getId()
                        if identifier == "PlayerCharacter":
                            continue
                        entity = application.world.get_entity(identifier)
                        possible_actions = ActionManager.get_possible_actions(
                                                                     player, 
                                                                     entity) 
                        actions = {}
                        for name, action in possible_actions.iteritems():
                            actions[name] = action(application, player, entity)
                            print actions[name].menu_text

                        if actions.has_key("Look"):
                            fifeagent.approach_and_execute(player, entity,
                                callback=lambda: 
                                    player.FifeAgent.instance.say(
                                            actions["Look"].execute(), 2000)
                            )
                            
class Controller(GameSceneController):
    
    def __init__(self, view, application, outliner=None, listener=None):
        listener = listener or Listener(application.engine, self)
        GameSceneController.__init__(self, view, application, outliner, listener)
        application.add_map_switch_callback(self.on_map_switched)
        
    def on_map_switched(self):
        renderer = fife.FloatingTextRenderer.getInstance(
                                        self.application.current_map.camera)
        font = get_manager().getDefaultFont()
        renderer.setFont(font)
        renderer.addActiveLayer(self.application.current_map.get_layer("actors"))
        renderer.setBackground(100, 255, 100, 165)
        renderer.setBorder(50, 255, 50)
        renderer.setEnabled(True)