# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from genweb.searchpage.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of genweb.searchpage into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if genweb.searchpage is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('genweb.searchpage'))

    def test_uninstall(self):
        """Test if genweb.searchpage is cleanly uninstalled."""
        self.installer.uninstallProducts(['genweb.searchpage'])
        self.assertFalse(self.installer.isProductInstalled('genweb.searchpage'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IGenwebSearchpageLayer is registered."""
        from genweb.searchpage.interfaces import IGenwebSearchpageLayer
        from plone.browserlayer import utils
        self.failUnless(IGenwebSearchpageLayer in utils.registered_layers())
