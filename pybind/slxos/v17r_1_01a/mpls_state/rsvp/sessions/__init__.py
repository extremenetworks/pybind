
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import psbs
class sessions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/rsvp/sessions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MPLS RSVP Sessions
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dest_ip_addr','__src_ip_addr','__tunnel_id','__session_role','__session_operational_status','__psbs',)

  _yang_name = 'sessions'
  _rest_name = 'sessions'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    path_helper_ = kwargs.pop("path_helper", None)
    if path_helper_ is False:
      self._path_helper = False
    elif path_helper_ is not None and isinstance(path_helper_, xpathhelper.YANGPathHelper):
      self._path_helper = path_helper_
    elif hasattr(self, "_parent"):
      path_helper_ = getattr(self._parent, "_path_helper", False)
      self._path_helper = path_helper_
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
    self.__session_operational_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="session-operational-status", rest_name="session-operational-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__dest_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dest-ip-addr", rest_name="dest-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__session_role = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'session-role-ingress': {'value': 1}, u'session-role-transit': {'value': 3}, u'session-role-unspecified': {'value': 0}, u'session-role-egress': {'value': 2}},), is_leaf=True, yang_name="session-role", rest_name="session-role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='session-role', is_config=False)
    self.__tunnel_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tunnel-id", rest_name="tunnel-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint16', is_config=False)
    self.__psbs = YANGDynClass(base=YANGListType("path_index",psbs.psbs, yang_name="psbs", rest_name="psbs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path-index', extensions=None), is_container='list', yang_name="psbs", rest_name="psbs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__src_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-ip-addr", rest_name="src-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)

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
      return [u'mpls-state', u'rsvp', u'sessions']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'rsvp', u'sessions']

  def _get_dest_ip_addr(self):
    """
    Getter method for dest_ip_addr, mapped from YANG variable /mpls_state/rsvp/sessions/dest_ip_addr (inet:ipv4-address)

    YANG Description: Destination ip address
    """
    return self.__dest_ip_addr
      
  def _set_dest_ip_addr(self, v, load=False):
    """
    Setter method for dest_ip_addr, mapped from YANG variable /mpls_state/rsvp/sessions/dest_ip_addr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dest_ip_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dest_ip_addr() directly.

    YANG Description: Destination ip address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dest-ip-addr", rest_name="dest-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dest_ip_addr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dest-ip-addr", rest_name="dest-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__dest_ip_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dest_ip_addr(self):
    self.__dest_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dest-ip-addr", rest_name="dest-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_src_ip_addr(self):
    """
    Getter method for src_ip_addr, mapped from YANG variable /mpls_state/rsvp/sessions/src_ip_addr (inet:ipv4-address)

    YANG Description: Srouce ip address
    """
    return self.__src_ip_addr
      
  def _set_src_ip_addr(self, v, load=False):
    """
    Setter method for src_ip_addr, mapped from YANG variable /mpls_state/rsvp/sessions/src_ip_addr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_ip_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_ip_addr() directly.

    YANG Description: Srouce ip address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-ip-addr", rest_name="src-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_ip_addr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-ip-addr", rest_name="src-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__src_ip_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_ip_addr(self):
    self.__src_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-ip-addr", rest_name="src-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_tunnel_id(self):
    """
    Getter method for tunnel_id, mapped from YANG variable /mpls_state/rsvp/sessions/tunnel_id (uint16)

    YANG Description: Tunnel ID
    """
    return self.__tunnel_id
      
  def _set_tunnel_id(self, v, load=False):
    """
    Setter method for tunnel_id, mapped from YANG variable /mpls_state/rsvp/sessions/tunnel_id (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel_id() directly.

    YANG Description: Tunnel ID
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tunnel-id", rest_name="tunnel-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel_id must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tunnel-id", rest_name="tunnel-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint16', is_config=False)""",
        })

    self.__tunnel_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel_id(self):
    self.__tunnel_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tunnel-id", rest_name="tunnel-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint16', is_config=False)


  def _get_session_role(self):
    """
    Getter method for session_role, mapped from YANG variable /mpls_state/rsvp/sessions/session_role (session-role)

    YANG Description: If this session role is ingress, egress or transit
    """
    return self.__session_role
      
  def _set_session_role(self, v, load=False):
    """
    Setter method for session_role, mapped from YANG variable /mpls_state/rsvp/sessions/session_role (session-role)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_session_role is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_session_role() directly.

    YANG Description: If this session role is ingress, egress or transit
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'session-role-ingress': {'value': 1}, u'session-role-transit': {'value': 3}, u'session-role-unspecified': {'value': 0}, u'session-role-egress': {'value': 2}},), is_leaf=True, yang_name="session-role", rest_name="session-role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='session-role', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """session_role must be of a type compatible with session-role""",
          'defined-type': "brocade-mpls-operational:session-role",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'session-role-ingress': {'value': 1}, u'session-role-transit': {'value': 3}, u'session-role-unspecified': {'value': 0}, u'session-role-egress': {'value': 2}},), is_leaf=True, yang_name="session-role", rest_name="session-role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='session-role', is_config=False)""",
        })

    self.__session_role = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_session_role(self):
    self.__session_role = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'session-role-ingress': {'value': 1}, u'session-role-transit': {'value': 3}, u'session-role-unspecified': {'value': 0}, u'session-role-egress': {'value': 2}},), is_leaf=True, yang_name="session-role", rest_name="session-role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='session-role', is_config=False)


  def _get_session_operational_status(self):
    """
    Getter method for session_operational_status, mapped from YANG variable /mpls_state/rsvp/sessions/session_operational_status (boolean)

    YANG Description: If the session up or not
    """
    return self.__session_operational_status
      
  def _set_session_operational_status(self, v, load=False):
    """
    Setter method for session_operational_status, mapped from YANG variable /mpls_state/rsvp/sessions/session_operational_status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_session_operational_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_session_operational_status() directly.

    YANG Description: If the session up or not
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="session-operational-status", rest_name="session-operational-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """session_operational_status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="session-operational-status", rest_name="session-operational-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__session_operational_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_session_operational_status(self):
    self.__session_operational_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="session-operational-status", rest_name="session-operational-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_psbs(self):
    """
    Getter method for psbs, mapped from YANG variable /mpls_state/rsvp/sessions/psbs (list)

    YANG Description: MPLS RSVP session path state
    """
    return self.__psbs
      
  def _set_psbs(self, v, load=False):
    """
    Setter method for psbs, mapped from YANG variable /mpls_state/rsvp/sessions/psbs (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_psbs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_psbs() directly.

    YANG Description: MPLS RSVP session path state
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("path_index",psbs.psbs, yang_name="psbs", rest_name="psbs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path-index', extensions=None), is_container='list', yang_name="psbs", rest_name="psbs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """psbs must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("path_index",psbs.psbs, yang_name="psbs", rest_name="psbs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path-index', extensions=None), is_container='list', yang_name="psbs", rest_name="psbs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__psbs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_psbs(self):
    self.__psbs = YANGDynClass(base=YANGListType("path_index",psbs.psbs, yang_name="psbs", rest_name="psbs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path-index', extensions=None), is_container='list', yang_name="psbs", rest_name="psbs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  dest_ip_addr = __builtin__.property(_get_dest_ip_addr)
  src_ip_addr = __builtin__.property(_get_src_ip_addr)
  tunnel_id = __builtin__.property(_get_tunnel_id)
  session_role = __builtin__.property(_get_session_role)
  session_operational_status = __builtin__.property(_get_session_operational_status)
  psbs = __builtin__.property(_get_psbs)


  _pyangbind_elements = {'dest_ip_addr': dest_ip_addr, 'src_ip_addr': src_ip_addr, 'tunnel_id': tunnel_id, 'session_role': session_role, 'session_operational_status': session_operational_status, 'psbs': psbs, }


