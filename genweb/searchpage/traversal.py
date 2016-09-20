from plone.resource.traversal import ResourceTraverser


class GenwebSearchPageTraverser(ResourceTraverser):
    """The bootstrap resources traverser.

    Allows traversal to /++genwebsearchpage++<name> using ``plone.resource`` to fetch
    things stored either on the filesystem or in the ZODB.
    """

    name = 'genwebsearchpage'
