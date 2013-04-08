from collective.grok import gs
from iii.theme import MessageFactory as _

@gs.importstep(
    name=u'iii.theme', 
    title=_('iii.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('iii.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
