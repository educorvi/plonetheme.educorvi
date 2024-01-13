# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.interface import Invalid


def check_categories(value):
    if len(value) < 3:
        raise Invalid('Es müssen mindestens 3 Servicekategorien angegeben werden.')
    return True

class IEducorviHomepage(model.Schema):
    """ Marker interface and Dexterity Python Schema for EducorviHomepage
    """

    service_categories = schema.List(title = "Kategorien an Serviceleistungen oder Produkten",
                                     description = "Die Begriffe werden um den Titel herum angeordnet. Mindestanzahl:3",
                                     value_type = schema.TextLine(),
                                     constraint = check_categories,
                                     required = True)

    alt_titles = schema.List(title = "Alternative Titel für die Homepage",
                             description = "Wenn die alternativen Titel ein @-Zeichen enthalten werden sie an dieser Position geteilt.",
                             value_type = schema.TextLine(),
                             required = False)


@implementer(IEducorviHomepage)
class EducorviHomepage(Container):
    """ Content-type class for IEducorviHomepage
    """
