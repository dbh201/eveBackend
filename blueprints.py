import marketgroup as mg
import item as it
import market as mk
import region as rg
import solarsystem as ss
import analysis as an

_prefix='/api'
def register_all(_api):
    _api.register_blueprint(mg._marketGroup,url_prefix=_prefix+mg._prefix)
    _api.register_blueprint(it._item,url_prefix=_prefix+it._prefix)
    _api.register_blueprint(mk._market,url_prefix=_prefix+mk._prefix)
    _api.register_blueprint(rg._region,url_prefix=_prefix+rg._prefix)
    _api.register_blueprint(ss._solarsystem,url_prefix=_prefix+ss._prefix)
    _api.register_blueprint(an._analysis,url_prefix=_prefix+an._prefix)
