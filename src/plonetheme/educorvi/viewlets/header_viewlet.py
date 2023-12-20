# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import ViewletBase
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class HeaderViewlet(ViewletBase):

    def update(self):
        self.portal_url = api.portal.get().absolute_url()
        self.logo_url = self.portal_url + '/++plone++plonetheme.educorvi/educorvi-logo.svg'
        self.items = self.get_formatted_items()

    def get_formatted_items(self):
        formatted_items = []
        portalid = api.portal.get().id
        contextpath = self.context.virtual_url_path().split('/')
        if contextpath[-1] == portalid:
            formatted_items.append({'title':'Startseite', 'url':self.portal_url, 'class':'nav-link mb-1 mb-lg-0 py-2 px-3 px-xl-4 active'})
        else:
            formatted_items.append({'title':'Startseite', 'url':self.portal_url, 'class':'nav-link mb-1 mb-lg-0 py-2 px-3 px-xl-4'})

        objroot = None
        if len(contextpath) == 1: 
            if contextpath[0] != portalid:
                objroot = contextpath[0]

        if len(contextpath) > 1:
            objroot = contextpath[1]

        items = self.get_items()
        for i in items:
            if objroot and objroot in i['url']:
                i['class'] = 'nav-link mb-1 mb-lg-0 py-2 px-3 px-xl-4 active'
            else:
                i['class'] = 'nav-link mb-1 mb-lg-0 py-2 px-3 px-xl-4'
            formatted_items.append(i)
        return formatted_items

    def get_items(self):
        portalobj = api.portal.get()
        navview = api.content.get_view(name='navigation', context=portalobj, request=self.request)
        items = navview.get_items()
        return items

    def index(self):
        return super(HeaderViewlet, self).render()
