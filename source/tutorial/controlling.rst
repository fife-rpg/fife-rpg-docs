.. _controlling:

Accessing and controlling entities
==================================
Now that we have entities we will want to access them and control them. This
tutorial will show how that can be done.

.. note::

   From now on I will not explain how to activate Components or
   Behaviours.

Getting an entity
-----------------

Of course the first thing is to actually get the entity. This can simply be done
with the :py:meth:`get_entity() <fife_rpg.world.RPGWorld.get_entity>` method
of the world. It takes the identifier of the entity, which is set in the
identifier field of the General component. For the character from our last
tutorial it is "PlayerCharacter". So to get this entity you need to add this
line of code after the world and the entities have been created:

.. code-block:: python

   player = world.get_entity("PlayerCharacter")
   
This will store the entity in the "player" variable.

The components and fields of each component can be accessed like a member
variable.

Example:

.. code-block:: python
   
   print player.Agent.position
   
This should print "[-5, 0]" to the console.

You can also set the component fields:

.. code-block:: python
   
   player.Agent.position = [0, 7] 

Note that changing the fields does not necessarily have an immediate effect.
Also the new value will, in most cases, not be validated automatically.
If it is safe to directly modify the values depends on the actual component.

Component functions
-------------------

The component modules can have functions that work with entities that have
that component.

The fifeagent module, for example, has functions that can used to make the
agent walk or run to a location or another agent. However the entity needs
to have another component which stores the walk and run speed and animations:
The Moving component. For the object used in the tutorial we only need to set
the speeds, as the default values for the animations can be used with it.

For the tutorial we set the fields to the following values:

.. code-block:: yaml

  Moving:
      walk_speed: 1
      run_speed: 4

We will use the :py:func:`run() <fife_rpg.components.fifeagent.run>` function,
which takes two arguments, entity and location. The entity is a
:py:class:`RPGEntity <fife_rpg.entities.rpg_entity.RPGEntity>` and the location
can be a `fife.Location <http://www.fifengine.net/epydoc/fife.fife.Location-class.html>`_
or a position tuple (Like (0, 7)).

Example:

.. code-block:: python
   
   fifeagent.run(player, (0, 7))
   
The import line for fifeagent is:

.. code-block:: python

   from fife_rpg.components import fifeagent
   
If you add the example code after switching to "Level1" the entity will run to
the right.

A practical example
-------------------
To close this part of the tutorial off we will look at a practical example of
what we just learned: Using the mouse to let an entity move to a position.

For that we first need a custom Listener and Application.

Create a new module and add the following imports:

.. code-block:: python

   from fife import fife
   
   from fife_rpg import RPGApplication
   from fife_rpg.rpg_application import ApplicationListener
   from fife_rpg.components import fifeagent 
   
The first thing we need to make is the Listener. A Listener is a class that
receives events from FIFE. The default ApplicationListener offers the basic
functionality and should always the base class of a custom Listener. It will
already listen for key, command and console events. Our Listener also needs
to receive mouse events so we need to add that to the base classes.

So the definition of our Listener should be as follows:

.. code-block:: python

   class Listener(ApplicationListener, fife.IMouseListener):
       def __init__(self, engine, application):
           ApplicationListener.__init__(self, engine, application)
           fife.IMouseListener.__init__(self)
           self._eventmanager.addMouseListener(self)

self._eventmanager.addMouseListener will register our Listener as a
MouseListener.

For each FIFE listener interface we add to the base class we need to
add all possible events, otherwise you will get errors.

For the `IMouseListener <http://www.fifengine.net/epydoc/fife.fife.IMouseListener-class.html>`_
the following methods are needed:

.. code-block:: python

    def mouseEntered(self, event):
        pass
    
    def mouseExited(self, event):
        pass

    def mousePressed(self, event):
        pass
                
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
        
Now, the method we will actually need is mousePressed, with the following code:

.. code-block:: python

    def mousePressed(self, event):
        player = self._application.world.get_entity("PlayerCharacter")
        if event.getButton() == fife.MouseEvent.LEFT:
            scr_point = self._application.screen_coords_to_map_coords(
                            (event.getX(), event.getY()), "actors"
                            )
            fifeagent.run(player, scr_point)
            
First we get the entity with the identifier "PlayerCharacter".
Then we check if it was the left mouse button that was clicked with, as we only
want to react to clicks with thaz button.
Next we use the applications :py:meth:`screen_coords_to_map_coords() <fife_rpg.rpg_application.RPGApplication.screen_coords_to_map_coords>`
method which takes a `fife.ScreenPoint <http://www.fifengine.net/epydoc/fife.fife.ScreenPoint-class.html>`_
or a tuple of a position on the screen and the name of a layer and returns
the matching coordinates on given layer of the current map as a `fife.Location <http://www.fifengine.net/epydoc/fife.fife.Location-class.html>`_.
We give it the location of the mouse click.
Last we call the fifeagent.run function with the entity and the converted
coordinates.

We also need an application that uses this Listener. Like for the Listener
our application needs to derive from RPGApplication.

The code needed is much simpler than for the Listener, so here is the complete
class:

.. code-block:: python

   class Application(RPGApplication):
   
       def __init__(self, settings):
           RPGApplication.__init__(self, settings)
   
       def createListener(self):
           self._listener = Listener(self.engine, self)
           return self._listener

The important part is the createListener method. It is called by the
RPGApplication class on construction and should create a listener and return it.

As the application and listener belong together they should be placed in the
same module.

Now we need to modify the main module to use our Application instead of the
default one. Just replace "app = RPGApplication(settings)" with
"app = Application(settings)", and import the module containing the application.

If you run the code now the entity should run to the location on the map you
click on.

Here is the complete code for this tutorial:

app.py

.. code-block:: python
   :emphasize-lines: 1-

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
                               (event.getX(), event.getY()), "actors"
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
           
run.py

.. code-block:: python
   :emphasize-lines: 6, 11, 24-25

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

The next Tutorial will look at the actions system of FIFErpg.