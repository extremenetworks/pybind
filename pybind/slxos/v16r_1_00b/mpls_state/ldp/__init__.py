
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ldp_out
import interface
import ldp_neighbors
import ldp_session_summary
import fec
import tunnels
import statistics
import ldp_database
import targeted_peer
import path
import ldp_session
class ldp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: LDP Operational Information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ldp_out','__interface','__ldp_neighbors','__ldp_session_summary','__fec','__tunnels','__statistics','__ldp_database','__targeted_peer','__path','__ldp_session',)

  _yang_name = 'ldp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
    else:
      self._path_helper = False

    extmethods = kwargs.pop("extmethods", None)
    if extmethods is False:
      self._extmethods = False
    elif extmethods is not None and isinstance(extmethods, dict):
      self._extmethods = extmethods
    elif hasattr(self, "_parent"):
      extmethods = getattr(self._parent, "_extmethods", None)
      self._extmethods = extmethods
    else:
      self._extmethods = False
    self.__statistics = YANGDynClass(base=statistics.statistics, is_container='container', yang_name="statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-global-ldp-stats', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__fec = YANGDynClass(base=fec.fec, is_container='container', yang_name="fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__ldp_out = YANGDynClass(base=ldp_out.ldp_out, is_container='container', yang_name="ldp-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-out', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__ldp_database = YANGDynClass(base=YANGListType("ldp_database_peer_ip",ldp_database.ldp_database, yang_name="ldp-database", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-database-peer-ip', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ldp-database", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__ldp_neighbors = YANGDynClass(base=ldp_neighbors.ldp_neighbors, is_container='container', yang_name="ldp-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-neighbors', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__ldp_session = YANGDynClass(base=YANGListType("peer_ldp_id",ldp_session.ldp_session, yang_name="ldp-session", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='peer-ldp-id', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-session', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ldp-session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-session', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__targeted_peer = YANGDynClass(base=YANGListType("mpls_ldp_targeted_peer_id",targeted_peer.targeted_peer, yang_name="targeted-peer", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-ldp-targeted-peer-id', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-targeted-peer', u'cli-suppress-show-path': None}}), is_container='list', yang_name="targeted-peer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-targeted-peer', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-interface', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__path = YANGDynClass(base=YANGListType("destination_route",path.path, yang_name="path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='destination-route', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-path', u'cli-suppress-show-path': None}}), is_container='list', yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-path', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__ldp_session_summary = YANGDynClass(base=ldp_session_summary.ldp_session_summary, is_container='container', yang_name="ldp-session-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-session-summary', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-tunnels', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'mpls-state', u'ldp']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'mpls-state', u'ldp']

  def _get_ldp_out(self):
    """
    Getter method for ldp_out, mapped from YANG variable /mpls_state/ldp/ldp_out (container)
    """
    return self.__ldp_out
      
  def _set_ldp_out(self, v, load=False):
    """
    Setter method for ldp_out, mapped from YANG variable /mpls_state/ldp/ldp_out (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_out is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_out() directly.
    """
    try:
      t = YANGDynClass(v,base=ldp_out.ldp_out, is_container='container', yang_name="ldp-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-out', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_out must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ldp_out.ldp_out, is_container='container', yang_name="ldp-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-out', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__ldp_out = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_out(self):
    self.__ldp_out = YANGDynClass(base=ldp_out.ldp_out, is_container='container', yang_name="ldp-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-out', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /mpls_state/ldp/interface (container)

    YANG Description:  LDP interface information
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /mpls_state/ldp/interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description:  LDP interface information
    """
    try:
      t = YANGDynClass(v,base=interface.interface, is_container='container', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-interface', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-interface', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-interface', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_ldp_neighbors(self):
    """
    Getter method for ldp_neighbors, mapped from YANG variable /mpls_state/ldp/ldp_neighbors (container)

    YANG Description: LDP neighbors information
    """
    return self.__ldp_neighbors
      
  def _set_ldp_neighbors(self, v, load=False):
    """
    Setter method for ldp_neighbors, mapped from YANG variable /mpls_state/ldp/ldp_neighbors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_neighbors() directly.

    YANG Description: LDP neighbors information
    """
    try:
      t = YANGDynClass(v,base=ldp_neighbors.ldp_neighbors, is_container='container', yang_name="ldp-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-neighbors', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_neighbors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ldp_neighbors.ldp_neighbors, is_container='container', yang_name="ldp-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-neighbors', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__ldp_neighbors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_neighbors(self):
    self.__ldp_neighbors = YANGDynClass(base=ldp_neighbors.ldp_neighbors, is_container='container', yang_name="ldp-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-neighbors', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_ldp_session_summary(self):
    """
    Getter method for ldp_session_summary, mapped from YANG variable /mpls_state/ldp/ldp_session_summary (container)
    """
    return self.__ldp_session_summary
      
  def _set_ldp_session_summary(self, v, load=False):
    """
    Setter method for ldp_session_summary, mapped from YANG variable /mpls_state/ldp/ldp_session_summary (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_session_summary is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_session_summary() directly.
    """
    try:
      t = YANGDynClass(v,base=ldp_session_summary.ldp_session_summary, is_container='container', yang_name="ldp-session-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-session-summary', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_session_summary must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ldp_session_summary.ldp_session_summary, is_container='container', yang_name="ldp-session-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-session-summary', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__ldp_session_summary = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_session_summary(self):
    self.__ldp_session_summary = YANGDynClass(base=ldp_session_summary.ldp_session_summary, is_container='container', yang_name="ldp-session-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-session-summary', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_fec(self):
    """
    Getter method for fec, mapped from YANG variable /mpls_state/ldp/fec (container)
    """
    return self.__fec
      
  def _set_fec(self, v, load=False):
    """
    Setter method for fec, mapped from YANG variable /mpls_state/ldp/fec (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fec is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fec() directly.
    """
    try:
      t = YANGDynClass(v,base=fec.fec, is_container='container', yang_name="fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fec must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fec.fec, is_container='container', yang_name="fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__fec = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fec(self):
    self.__fec = YANGDynClass(base=fec.fec, is_container='container', yang_name="fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_tunnels(self):
    """
    Getter method for tunnels, mapped from YANG variable /mpls_state/ldp/tunnels (container)

    YANG Description: LDP Tunnels
    """
    return self.__tunnels
      
  def _set_tunnels(self, v, load=False):
    """
    Setter method for tunnels, mapped from YANG variable /mpls_state/ldp/tunnels (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnels is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnels() directly.

    YANG Description: LDP Tunnels
    """
    try:
      t = YANGDynClass(v,base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-tunnels', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnels must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-tunnels', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__tunnels = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnels(self):
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-tunnels', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_statistics(self):
    """
    Getter method for statistics, mapped from YANG variable /mpls_state/ldp/statistics (container)

    YANG Description: Global LDP stats
    """
    return self.__statistics
      
  def _set_statistics(self, v, load=False):
    """
    Setter method for statistics, mapped from YANG variable /mpls_state/ldp/statistics (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_statistics is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_statistics() directly.

    YANG Description: Global LDP stats
    """
    try:
      t = YANGDynClass(v,base=statistics.statistics, is_container='container', yang_name="statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-global-ldp-stats', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """statistics must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=statistics.statistics, is_container='container', yang_name="statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-global-ldp-stats', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__statistics = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_statistics(self):
    self.__statistics = YANGDynClass(base=statistics.statistics, is_container='container', yang_name="statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-global-ldp-stats', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_ldp_database(self):
    """
    Getter method for ldp_database, mapped from YANG variable /mpls_state/ldp/ldp_database (list)

    YANG Description: LDP database operational Information
    """
    return self.__ldp_database
      
  def _set_ldp_database(self, v, load=False):
    """
    Setter method for ldp_database, mapped from YANG variable /mpls_state/ldp/ldp_database (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_database is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_database() directly.

    YANG Description: LDP database operational Information
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ldp_database_peer_ip",ldp_database.ldp_database, yang_name="ldp-database", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-database-peer-ip', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ldp-database", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_database must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ldp_database_peer_ip",ldp_database.ldp_database, yang_name="ldp-database", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-database-peer-ip', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ldp-database", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__ldp_database = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_database(self):
    self.__ldp_database = YANGDynClass(base=YANGListType("ldp_database_peer_ip",ldp_database.ldp_database, yang_name="ldp-database", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-database-peer-ip', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ldp-database", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)


  def _get_targeted_peer(self):
    """
    Getter method for targeted_peer, mapped from YANG variable /mpls_state/ldp/targeted_peer (list)

    YANG Description:  LDP Targeted Peer
    """
    return self.__targeted_peer
      
  def _set_targeted_peer(self, v, load=False):
    """
    Setter method for targeted_peer, mapped from YANG variable /mpls_state/ldp/targeted_peer (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_targeted_peer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_targeted_peer() directly.

    YANG Description:  LDP Targeted Peer
    """
    try:
      t = YANGDynClass(v,base=YANGListType("mpls_ldp_targeted_peer_id",targeted_peer.targeted_peer, yang_name="targeted-peer", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-ldp-targeted-peer-id', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-targeted-peer', u'cli-suppress-show-path': None}}), is_container='list', yang_name="targeted-peer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-targeted-peer', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """targeted_peer must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mpls_ldp_targeted_peer_id",targeted_peer.targeted_peer, yang_name="targeted-peer", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-ldp-targeted-peer-id', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-targeted-peer', u'cli-suppress-show-path': None}}), is_container='list', yang_name="targeted-peer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-targeted-peer', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__targeted_peer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_targeted_peer(self):
    self.__targeted_peer = YANGDynClass(base=YANGListType("mpls_ldp_targeted_peer_id",targeted_peer.targeted_peer, yang_name="targeted-peer", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-ldp-targeted-peer-id', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-targeted-peer', u'cli-suppress-show-path': None}}), is_container='list', yang_name="targeted-peer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-targeted-peer', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)


  def _get_path(self):
    """
    Getter method for path, mapped from YANG variable /mpls_state/ldp/path (list)

    YANG Description:  LDP Path information
    """
    return self.__path
      
  def _set_path(self, v, load=False):
    """
    Setter method for path, mapped from YANG variable /mpls_state/ldp/path (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path() directly.

    YANG Description:  LDP Path information
    """
    try:
      t = YANGDynClass(v,base=YANGListType("destination_route",path.path, yang_name="path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='destination-route', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-path', u'cli-suppress-show-path': None}}), is_container='list', yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-path', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("destination_route",path.path, yang_name="path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='destination-route', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-path', u'cli-suppress-show-path': None}}), is_container='list', yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-path', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path(self):
    self.__path = YANGDynClass(base=YANGListType("destination_route",path.path, yang_name="path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='destination-route', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-path', u'cli-suppress-show-path': None}}), is_container='list', yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-path', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)


  def _get_ldp_session(self):
    """
    Getter method for ldp_session, mapped from YANG variable /mpls_state/ldp/ldp_session (list)
    """
    return self.__ldp_session
      
  def _set_ldp_session(self, v, load=False):
    """
    Setter method for ldp_session, mapped from YANG variable /mpls_state/ldp/ldp_session (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_session is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_session() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("peer_ldp_id",ldp_session.ldp_session, yang_name="ldp-session", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='peer-ldp-id', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-session', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ldp-session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-session', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_session must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("peer_ldp_id",ldp_session.ldp_session, yang_name="ldp-session", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='peer-ldp-id', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-session', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ldp-session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-session', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__ldp_session = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_session(self):
    self.__ldp_session = YANGDynClass(base=YANGListType("peer_ldp_id",ldp_session.ldp_session, yang_name="ldp-session", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='peer-ldp-id', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-session', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ldp-session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-session', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  ldp_out = __builtin__.property(_get_ldp_out)
  interface = __builtin__.property(_get_interface)
  ldp_neighbors = __builtin__.property(_get_ldp_neighbors)
  ldp_session_summary = __builtin__.property(_get_ldp_session_summary)
  fec = __builtin__.property(_get_fec)
  tunnels = __builtin__.property(_get_tunnels)
  statistics = __builtin__.property(_get_statistics)
  ldp_database = __builtin__.property(_get_ldp_database)
  targeted_peer = __builtin__.property(_get_targeted_peer)
  path = __builtin__.property(_get_path)
  ldp_session = __builtin__.property(_get_ldp_session)


  _pyangbind_elements = {'ldp_out': ldp_out, 'interface': interface, 'ldp_neighbors': ldp_neighbors, 'ldp_session_summary': ldp_session_summary, 'fec': fec, 'tunnels': tunnels, 'statistics': statistics, 'ldp_database': ldp_database, 'targeted_peer': targeted_peer, 'path': path, 'ldp_session': ldp_session, }


