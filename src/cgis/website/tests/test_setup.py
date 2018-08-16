# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from cgis.website.testing import CGIS_WEBSITE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that cgis.website is properly installed."""

    layer = CGIS_WEBSITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if cgis.website is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'cgis.website'))

    def test_browserlayer(self):
        """Test that ICgisWebsiteLayer is registered."""
        from cgis.website.interfaces import (
            ICgisWebsiteLayer)
        from plone.browserlayer import utils
        self.assertIn(ICgisWebsiteLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CGIS_WEBSITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(username=TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['cgis.website'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if cgis.website is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'cgis.website'))

    def test_browserlayer_removed(self):
        """Test that ICgisWebsiteLayer is removed."""
        from cgis.website.interfaces import \
            ICgisWebsiteLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICgisWebsiteLayer,
            utils.registered_layers(),
        )
