.. _material:


.. py:currentmodule:: xara

Materials
^^^^^^^^^

A material is added to a :py:class:`xara.Model` using the ``material`` method:


.. py:method:: Model.material(object)

    Add a material to the model to be used in :ref:`elements <element>` and :ref:`sections <section>`. 

    :param object: material object
    :type object: :py:class:`xara.UniaxialMaterial` or :py:class:`xara.MultiaxialMaterial`



Materials are primarily classified as *uniaxial* and *multiaxial* materials. 
Multiaxial materials can be used in any material context, and define the material behavior in all six degrees of freedom.
Uniaxial materials are used to define the material behavior in one direction.

.. toctree::
    :maxdepth: 1

    uniaxial/index
    nd
    friction/index


