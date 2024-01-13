# -*- coding: utf-8 -*-
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import implementer


# from plonetheme.educorvi import _



class ILeistung(model.Schema):
    """ Marker interface and Dexterity Python Schema for Leistung
    """
 
    groups = schema.List(title = "Zielgruppen für die Leistung oder das Produkt",
                         value_type = schema.TextLine(),
                         required = False)

    topics = schema.List(title = "Stichpunkte oder Slogans zur Leistung oder zum Produkt",
                         value_type = schema.TextLine(),
                         required = False)

    cta_title = schema.TextLine(title = "Titel des Call-to-Action Buttons",
                        default = "Mehr erfahren",
                        required = True)

    cta_url = RelationChoice(title="Ziel des Call-to-Action Buttons",
                        vocabulary="plone.app.vocabularies.Catalog",
                        required=False)

    directives.widget("cta_url",
                        RelatedItemsFieldWidget,
                        pattern_options={"selectableTypes": ["Document"],},)

    image = NamedBlobImage(title = "Symbolbild oder Vorschaubild für die Leistung",
                           required = True)

    image_caption = schema.TextLine(title="Beschreibung zum Symbolbild",
                        description="Mit der Beschreibung wird der alt-Tag des Bildelements\
                                zur Gewährleistung der Barrierefreiheit befüllt.",
                        required = True)

    background_color = schema.Choice(
                        title="CSS-Klasse für den Hintergrund",
                        values=["bg-white", "bg-lightgrey"],
                        default="bg-white",
                        required=True)


@implementer(ILeistung)
class Leistung(Item):
    """ Content-type class for ILeistung
    """
