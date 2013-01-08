.. _actions:

Context based actions
=====================
In this tutorial I will explain the actions system of FIFErpg, which
automatically creates a list of actions that one entity can perform with
another. Such a list could be used, for example, to populate a context menu -
which is, however, not part of this tutorial.

Preparations
------------
First we need to add a new component and an action to the settings.
The name of the component is "Description".
The actions are set in the "Actions" setting which works the same as
"Components" and "Behaviours" do. The only action we need is the "Look" action.

You can review the changes in the
:download:`settings <actions/settings-dist.xml>` file.

We are also going to add another entity, on which we can perform the action.
In "entities.yaml" add a new yaml document with the following content:

.. code :: yaml

   !Entity
   Components:
     General:
         identifier: David
     Agent:
         gfx: player
         map: Level1
         layer: actors
         position: [-1, 0]
         rotation: 180
         behaviour_type: Base
     Moving:
         walk_speed: 1
         run_speed: 4
     Description:
         real_name: David
         view_name: David
         desc: This is David.
         
Compare the result with the :download:`entities <actions/objects/entities.yaml>`
file.
The entity is mostly exact like the PlayerCharacter with an "Description"
component added. This is needed for the "Look" action.

Code changes
------------
Activating the actions is done the same way as for components and behaviours:

.. code :: python

   app.load_actions("combined.yaml")
   app.register_actions()

The Look action returns a string when it is executed, thus we need a way to
display that. We are going to use the "say" method of the fife instance. For
that we first need to activate the "FloatingTextRenderer" for the layer the
instance is on.
A good way to do this is to activate it for all layers, that entities can be
on, when the map is switched.

For this we are going to make a custom GameSceneController.
In the same line where GameSceneListener is imported add GameSceneController
as well, so the line should look like this:

.. code :: python

   from fife_rpg.game_scene import GameSceneListener, GameSceneController
   
Also add the following import, I will explain what it is used for later:

.. code :: python

   from fife.extensions.pychan.internal import get_manager
   
The basic code for the Controller is as follows:

.. code :: python

   class Controller(GameSceneController):
       
       def __init__(self, view, application, outliner=None, listener=None):
           listener = listener or Listener(application.engine, self)
           GameSceneController.__init__(self, view, application, outliner, listener)

The first line in the constructor will set the listener to our custom Listener
unless a listener was passed. This mimics the GameSceneController.

Next thing we need to add is a method that gets called when the map is
switched:

.. code :: python

    def on_map_switched(self):
        renderer = fife.FloatingTextRenderer.getInstance(self.application.current_map.camera)
        font = get_manager().getDefaultFont()
        renderer.setFont(font)
        renderer.addActiveLayer(self.application.current_map.get_layer("actors"))
        renderer.setBackground(100, 255, 100, 165)
        renderer.setBorder(50, 255, 50)
        renderer.setEnabled(True)

The name of the method does not really matter, as it will be used as a
callback function.

First we get the instance of the FloatingTextRender of the camera of the
current map. Then we will use the get_manager method to get the pychan
manager which is used to get the default font of pychan.

Next we set the renderer to use this font and add the "actors" layer to its
active layers. We also set the background and border colour of the text window
and enable the renderer.

Now we just need to add this as a callback when the map has switched. This is
done by adding this line to the constructor of the controller:

.. cocde :: python

   application.add_map_switch_callback(self.on_map_switched)