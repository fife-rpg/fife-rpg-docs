from fife_rpg import RPGApplication
from fife_rpg import GameSceneView
from fife_rpg import GameSceneController
from fife.extensions.fife_settings import Setting

settings = Setting(app_name="Tutorial 3", settings_file="settings.xml")

def main():
    app = RPGApplication(settings)
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
    app.push_mode(controller)
    app.run()
    
if __name__ == '__main__':
    main()