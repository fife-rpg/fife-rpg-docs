from fife_rpg import RPGApplication
from fife_rpg import GameSceneView
from fife_rpg import GameSceneController
from fife.extensions.fife_settings import Setting

settings = Setting(app_name="Tutorial 1", settings_file="settings.xml")

def main():
    app = RPGApplication(settings)
    view = GameSceneView(app)
    controller = GameSceneController(view, app)
    app.create_world()
    app.push_mode(controller)
    app.run()

if __name__ == '__main__':
    main()