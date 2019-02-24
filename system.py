from flask impot Blueprint
from db import dbQuery

#####################
# /api/solarsystem/ #
#####################

_system = BluePrint('_solarSystem',__name__)
_prefix = '/api/solarsystem'

###
q_getSolarSystemIDBySolarSystemName='''
SELECT solarSystemID
FROM mapSolarSystems
WHERE solarSystemName LIKE %s ;
'''
@_system.route('/id/byname/<string:solarSystemName>', methods=['GET'])
def getSolarSystemIDBySolarSystemName(solarSystemName):
    return dbQuery( q_getSystemIDBySystemName, (solarSystemName,) )
###


###
q_getSolarSystemNameBySolarSystemID='''
SELECT solarSystemName
FROM mapSolarSystems
WHERE solarSystemID = %s ;
'''
@_system.route('', methods=['GET'])
def getSolarSystemNameBySolarSystemID():
    return dbQuery( q_getSystemNameBySystemID, (str(solarSystemID),) )
###
