.. _material:


.. py:currentmodule:: xara

Materials
^^^^^^^^^

A material is added to a :py:class:`xara.Model` using the ``material`` method:


.. py:method:: Model.material(object)

    Add a material to the model.

    :param object: material object
    :type object: :py:class:`xara.UniaxialMaterial` or :py:class:`xara.MultiaxialMaterial`

There are two types of materials: *uniaxial* materials and *general* materials. 
General materials can be used in any material context, and define the material behavior in all six degrees of freedom.
Uniaxial materials are used to define the material behavior in one direction.

.. toctree::
    :maxdepth: 1

    uniaxial/index
    nd
    friction/index


