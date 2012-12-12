from fife_rpg import GameSceneView
from fife_rpg import GameSceneController
from fife.extensions.fife_settings import Setting
from fife_rpg.components import fifeagent

from app import Application

settings = Setting(app_name="Tutorial 4", settings_file="settings.xml")

def main():
    app = Application(settings)
    app.load_components("combined.yaml")
    app.load_behaviours("combined.yaml")
    app.register_components()
    app.register_behaviours()
    view = GameSceneView(app)
    controller = GameSceneController(view, app)
    app.create_world()
    app.load_maps()
    world = app.world
    world.import_agent_objects()
    world.load_and_create_entities()
    app.switch_map("Level1")
    player = world.get_entity("PlayerCharacter")
    fifeagent.run(player, (0, 7))
    app.push_mode(controller)
    app.run()
    
if __name__ == '__main__':
    main()