from fife_rpg import RPGApplication
from fife_rpg import GameSceneView
from fife_rpg import GameSceneController
from fife.extensions.fife_settings import Setting

settings = Setting(app_name="Tutorial 2", settings_file="settings.xml")

def main():
    app = RPGApplication(settings)
    app.load_components("combined.yaml")
    app.register_components()
    view = GameSceneView(app)
    controller = GameSceneController(view, app)
    app.create_world()
    app.load_maps()
    app.switch_map("Level1")
    app.push_mode(controller)    
    app.run()
    
if __name__ == '__main__':
    main()