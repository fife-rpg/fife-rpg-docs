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
component added. This is needed for the "Look" action
