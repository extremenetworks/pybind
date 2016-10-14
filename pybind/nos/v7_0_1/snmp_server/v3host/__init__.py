
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import source_interface
class v3host(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-snmp - based on the path /snmp-server/v3host. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__hostip','__username','__udp_port','__notifytype','__engineid','__severity_level','__use_vrf','__source_interface',)

  _yang_name = 'v3host'

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
    self.__username = YANGDynClass(base=unicode, is_leaf=True, yang_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Username associated with notification type.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    self.__severity_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Info': {}, u'None': {}, u'Warning': {}, u'Critical': {}, u'Error': {}, u'Debug': {}},), default=unicode("None"), is_leaf=True, yang_name="severity-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Severity level associated with traps'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='sev-level', is_config=True)
    self.__source_interface = YANGDynClass(base=source_interface.source_interface, is_container='container', yang_name="source-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface IP address to be used as a source address for Traps'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)
    self.__udp_port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(162), is_leaf=True, yang_name="udp-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port number used to send notifications.\n(Default=162)'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='host-port', is_config=True)
    self.__use_vrf = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'vrfname used to send notifications.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='use-vrf-option', is_config=True)
    self.__notifytype = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'informs': {'value': 1}, u'traps': {'value': 0}},), default=unicode("traps"), is_leaf=True, yang_name="notifytype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Type of notification sent to host.\n(Default=traps)'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='enumeration', is_config=True)
    self.__hostip = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']}),], is_leaf=True, yang_name="hostip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv4/ipv6/dns address of the notification recipient\nassociated with username. Notifications\nwill be sent to this host'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='inet:host', is_config=True)
    self.__engineid = YANGDynClass(base=unicode, default=unicode("00:00:00:00:00:00:00:00:00"), is_leaf=True, yang_name="engineid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Manager's (Remote) engine Id."}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)

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
      return [u'snmp-server', u'v3host']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'snmp-server', u'v3host']

  def _get_hostip(self):
    """
    Getter method for hostip, mapped from YANG variable /snmp_server/v3host/hostip (inet:host)
    """
    return self.__hostip
      
  def _set_hostip(self, v, load=False):
    """
    Setter method for hostip, mapped from YANG variable /snmp_server/v3host/hostip (inet:host)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hostip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hostip() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']}),], is_leaf=True, yang_name="hostip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv4/ipv6/dns address of the notification recipient\nassociated with username. Notifications\nwill be sent to this host'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='inet:host', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hostip must be of a type compatible with inet:host""",
          'defined-type': "inet:host",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']}),], is_leaf=True, yang_name="hostip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv4/ipv6/dns address of the notification recipient\nassociated with username. Notifications\nwill be sent to this host'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='inet:host', is_config=True)""",
        })

    self.__hostip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hostip(self):
    self.__hostip = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']}),], is_leaf=True, yang_name="hostip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv4/ipv6/dns address of the notification recipient\nassociated with username. Notifications\nwill be sent to this host'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='inet:host', is_config=True)


  def _get_username(self):
    """
    Getter method for username, mapped from YANG variable /snmp_server/v3host/username (string)
    """
    return self.__username
      
  def _set_username(self, v, load=False):
    """
    Setter method for username, mapped from YANG variable /snmp_server/v3host/username (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_username is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_username() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Username associated with notification type.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """username must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Username associated with notification type.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)""",
        })

    self.__username = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_username(self):
    self.__username = YANGDynClass(base=unicode, is_leaf=True, yang_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Username associated with notification type.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)


  def _get_udp_port(self):
    """
    Getter method for udp_port, mapped from YANG variable /snmp_server/v3host/udp_port (host-port)
    """
    return self.__udp_port
      
  def _set_udp_port(self, v, load=False):
    """
    Setter method for udp_port, mapped from YANG variable /snmp_server/v3host/udp_port (host-port)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_udp_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_udp_port() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(162), is_leaf=True, yang_name="udp-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port number used to send notifications.\n(Default=162)'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='host-port', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """udp_port must be of a type compatible with host-port""",
          'defined-type': "brocade-snmp:host-port",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(162), is_leaf=True, yang_name="udp-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port number used to send notifications.\n(Default=162)'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='host-port', is_config=True)""",
        })

    self.__udp_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_udp_port(self):
    self.__udp_port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(162), is_leaf=True, yang_name="udp-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port number used to send notifications.\n(Default=162)'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='host-port', is_config=True)


  def _get_notifytype(self):
    """
    Getter method for notifytype, mapped from YANG variable /snmp_server/v3host/notifytype (enumeration)
    """
    return self.__notifytype
      
  def _set_notifytype(self, v, load=False):
    """
    Setter method for notifytype, mapped from YANG variable /snmp_server/v3host/notifytype (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_notifytype is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_notifytype() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'informs': {'value': 1}, u'traps': {'value': 0}},), default=unicode("traps"), is_leaf=True, yang_name="notifytype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Type of notification sent to host.\n(Default=traps)'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """notifytype must be of a type compatible with enumeration""",
          'defined-type': "brocade-snmp:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'informs': {'value': 1}, u'traps': {'value': 0}},), default=unicode("traps"), is_leaf=True, yang_name="notifytype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Type of notification sent to host.\n(Default=traps)'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='enumeration', is_config=True)""",
        })

    self.__notifytype = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_notifytype(self):
    self.__notifytype = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'informs': {'value': 1}, u'traps': {'value': 0}},), default=unicode("traps"), is_leaf=True, yang_name="notifytype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Type of notification sent to host.\n(Default=traps)'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='enumeration', is_config=True)


  def _get_engineid(self):
    """
    Getter method for engineid, mapped from YANG variable /snmp_server/v3host/engineid (string)
    """
    return self.__engineid
      
  def _set_engineid(self, v, load=False):
    """
    Setter method for engineid, mapped from YANG variable /snmp_server/v3host/engineid (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_engineid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_engineid() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, default=unicode("00:00:00:00:00:00:00:00:00"), is_leaf=True, yang_name="engineid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Manager's (Remote) engine Id."}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """engineid must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, default=unicode("00:00:00:00:00:00:00:00:00"), is_leaf=True, yang_name="engineid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Manager's (Remote) engine Id."}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)""",
        })

    self.__engineid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_engineid(self):
    self.__engineid = YANGDynClass(base=unicode, default=unicode("00:00:00:00:00:00:00:00:00"), is_leaf=True, yang_name="engineid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Manager's (Remote) engine Id."}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)


  def _get_severity_level(self):
    """
    Getter method for severity_level, mapped from YANG variable /snmp_server/v3host/severity_level (sev-level)
    """
    return self.__severity_level
      
  def _set_severity_level(self, v, load=False):
    """
    Setter method for severity_level, mapped from YANG variable /snmp_server/v3host/severity_level (sev-level)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_severity_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_severity_level() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Info': {}, u'None': {}, u'Warning': {}, u'Critical': {}, u'Error': {}, u'Debug': {}},), default=unicode("None"), is_leaf=True, yang_name="severity-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Severity level associated with traps'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='sev-level', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """severity_level must be of a type compatible with sev-level""",
          'defined-type': "brocade-snmp:sev-level",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Info': {}, u'None': {}, u'Warning': {}, u'Critical': {}, u'Error': {}, u'Debug': {}},), default=unicode("None"), is_leaf=True, yang_name="severity-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Severity level associated with traps'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='sev-level', is_config=True)""",
        })

    self.__severity_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_severity_level(self):
    self.__severity_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Info': {}, u'None': {}, u'Warning': {}, u'Critical': {}, u'Error': {}, u'Debug': {}},), default=unicode("None"), is_leaf=True, yang_name="severity-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Severity level associated with traps'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='sev-level', is_config=True)


  def _get_use_vrf(self):
    """
    Getter method for use_vrf, mapped from YANG variable /snmp_server/v3host/use_vrf (use-vrf-option)
    """
    return self.__use_vrf
      
  def _set_use_vrf(self, v, load=False):
    """
    Setter method for use_vrf, mapped from YANG variable /snmp_server/v3host/use_vrf (use-vrf-option)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_use_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_use_vrf() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, default=unicode(""), is_leaf=True, yang_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'vrfname used to send notifications.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='use-vrf-option', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """use_vrf must be of a type compatible with use-vrf-option""",
          'defined-type': "brocade-snmp:use-vrf-option",
          'generated-type': """YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'vrfname used to send notifications.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='use-vrf-option', is_config=True)""",
        })

    self.__use_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_use_vrf(self):
    self.__use_vrf = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'vrfname used to send notifications.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='use-vrf-option', is_config=True)


  def _get_source_interface(self):
    """
    Getter method for source_interface, mapped from YANG variable /snmp_server/v3host/source_interface (container)
    """
    return self.__source_interface
      
  def _set_source_interface(self, v, load=False):
    """
    Setter method for source_interface, mapped from YANG variable /snmp_server/v3host/source_interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_interface() directly.
    """
    try:
      t = YANGDynClass(v,base=source_interface.source_interface, is_container='container', yang_name="source-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface IP address to be used as a source address for Traps'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=source_interface.source_interface, is_container='container', yang_name="source-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface IP address to be used as a source address for Traps'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)""",
        })

    self.__source_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_interface(self):
    self.__source_interface = YANGDynClass(base=source_interface.source_interface, is_container='container', yang_name="source-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface IP address to be used as a source address for Traps'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)

  hostip = __builtin__.property(_get_hostip, _set_hostip)
  username = __builtin__.property(_get_username, _set_username)
  udp_port = __builtin__.property(_get_udp_port, _set_udp_port)
  notifytype = __builtin__.property(_get_notifytype, _set_notifytype)
  engineid = __builtin__.property(_get_engineid, _set_engineid)
  severity_level = __builtin__.property(_get_severity_level, _set_severity_level)
  use_vrf = __builtin__.property(_get_use_vrf, _set_use_vrf)
  source_interface = __builtin__.property(_get_source_interface, _set_source_interface)


  _pyangbind_elements = {'hostip': hostip, 'username': username, 'udp_port': udp_port, 'notifytype': notifytype, 'engineid': engineid, 'severity_level': severity_level, 'use_vrf': use_vrf, 'source_interface': source_interface, }


