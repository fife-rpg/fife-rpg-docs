.. _components:

Components
==========

This tutorial will explain the component system FIFErpg uses and show
how to create your own components.

bGrease
-------
FIFErpg uses bGrease, which is a fork of the the
`Grease Framework <http://packages.python.org/grease/index.html>`_.
Grease components are simple classes that only contain information about
what fields a component has.
Adding a grease component is as simple as putting this code inside the
configure method of a grease world:

.. code :: python

   self.components.health = component.Component(
       health=int, max_health=int)


FIFErpg
-------

While this would also perfectly work with FIFErpg this does not use the auto
registering functions. For that you would need to make your own component
class, that inherits from the :py:class:`~fife_rpg.components.base.Base`
component class.

First we will need to import the Base class.

.. code :: python

   from fife_rpg.components.base import Base

Then make a class that derives from that.

.. code :: python

   class Health(Base):

To define the fields you will need to call the Base class constructor with
their information:

.. code :: python

   def __init(self):
      Base.__init__(health=int, max_health=int)

The possible types for the fields can be found in the components
`documentation <http://beliaar.github.com/bGrease/mod/component.html#bGrease.component.Component>`_.

If you want to set the default value for a field you need to add this in the
constructor:

.. code :: python

   self.fields["health"].default = lambda: 100
   self.fields["max_health"].default = lambda: 100
   
You can also set the default to a type that can be constructed with no
arguments, you won't need the lambda then.

Now, the next important part is the "register" class method, which needs to be
overwritten. The following code is all that is needed for that:

.. code :: python

    @classmethod
    def register(cls, name="Health", auto_register=True):
        return (super(Health, cls).register(name, auto_register))

Dependencies and inheriting from another component
--------------------------------------------------
If you want to have the component automatically register other components,
or any of the other FIFErpg classes the support auto registering. You can
set the dependencies class member. It is a list of classes. When registering
a component the register method will look through all the classes in that
list and calls their register method if the class is not already registered.
This is done before registering the component itself.

Also, if the component derives from a component that is not the Base component,
the register method will, by default, make it so that the class that the
component derives from will appear as registered but points to the component
that derives from it. This can be used to make components that replace other
components. This can be disabled by setting the "auto_register" argument
of the register method to False.
components that replace other components.