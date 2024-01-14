# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class ReferencesViewlet(ViewletBase):

    def update(self):
        self.references = self.get_references()

    def get_references(self):
        refs = []
        for entry in self.context.contentcards:
            ref = {}
            if entry.to_object:
                obj = entry.to_object
                ref['title'] = obj.title
                ref['description'] = obj.description
                ref['url'] = obj.absolute_url()
                if hasattr(obj, 'remoteUrl'):
                    ref['url'] = obj.remoteUrl
                ref['img'] = ''
                if hasattr(obj, 'image'):
                    ref['img'] = obj.absolute_url() + '/@@images/image/mini'
                refs.append(ref)
        return refs
                
    def index(self):
        if hasattr(self.context, 'contentcards'):
            if self.context.contentcards:
                return super(ReferencesViewlet, self).render()
        return ""
