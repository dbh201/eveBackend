from flask import Blueprint
from db import dbQuery

#############
# /api/icon #
#############

_icon = Blueprint('_icon',__name__)
_prefix = '/icon'
@_icon.route('/<path:path>')
def itemAPI(path):
    v=vars(self)
    d=dir(self)
    return "Path %s not found.<br/> %s<br/> %s<br/>" % (path, v, d)

###
q_getResURLByIconID='''
SELECT iconFile
FROM eveIcons
WHERE iconID = %s ;
'''
@_icon.route('/byid/<int:iconID>', methods=['GET'])
def getResURLByIconID(iconID):
    return dbQuery( q_getResURLByIconID,(str(iconID),) )
###
