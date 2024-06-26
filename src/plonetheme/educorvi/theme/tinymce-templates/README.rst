TinyMCE templates
=================

To enable the TinyMCE templates feature you have to enable the plugin and
configure the templates within the TinyMCE controlpanel of your Plone site.

Activate TinyMCE Templates Plugin
---------------------------------

Go to the Plugins and Toolbar tab.
Under "Editor plugins" locate the "template" plugin and enable it.

In ``registry.xml`` in a ``GenericSetup`` profile you would do it like this:

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <registry>
      <records interface="Products.CMFPlone.interfaces.controlpanel.ITinyMCESchema"
              prefix="plone"
      >
        <value key="plugins"
              purge="false"
        >
          <element>template</element>
        </value>
    </registry>


Configure TinyMCE Templates
---------------------------

.. code-block:: json

    [
        {
          "title": "List",
          "description": "List of group items",
          "url": "++theme++educorvi-home/tinymce-templates/list.html"
        },
        {
          "title": "Card Group",
          "description": "Group of cards",
          "url": "++theme++educorvi-home/tinymce-templates/card-group.html"
        }
    ]
