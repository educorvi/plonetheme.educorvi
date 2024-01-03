# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from plonetheme.educorvi.content.leistung import ILeistung  # NOQA E501
from plonetheme.educorvi.testing import PLONETHEME_EDUCORVI_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class LeistungIntegrationTest(unittest.TestCase):

    layer = PLONETHEME_EDUCORVI_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'educorvi Homepage',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_leistung_schema(self):
        fti = queryUtility(IDexterityFTI, name='Leistung')
        schema = fti.lookupSchema()
        self.assertEqual(ILeistung, schema)

    def test_ct_leistung_fti(self):
        fti = queryUtility(IDexterityFTI, name='Leistung')
        self.assertTrue(fti)

    def test_ct_leistung_factory(self):
        fti = queryUtility(IDexterityFTI, name='Leistung')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ILeistung.providedBy(obj),
            u'ILeistung not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_leistung_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Leistung',
            id='leistung',
        )

        self.assertTrue(
            ILeistung.providedBy(obj),
            u'ILeistung not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('leistung', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('leistung', parent.objectIds())

    def test_ct_leistung_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Leistung')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
