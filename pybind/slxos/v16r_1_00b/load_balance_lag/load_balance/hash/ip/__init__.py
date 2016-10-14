
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge-lag - based on the path /load-balance-lag/load-balance/hash/ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__src_l4_port','__dst_l4_port','__src_ip','__dst_ip','__protocol',)

  _yang_name = 'ip'

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
    self.__src_ip = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="src-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'src-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip src-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__dst_ip = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dst-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'dst-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip dst-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__protocol = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'protocol', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip protocol\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__dst_l4_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dst-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'dst-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip dst-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__src_l4_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="src-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'src-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip src-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)

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
      return [u'load-balance-lag', u'load-balance', u'hash', u'ip']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'load-balance', u'hash', u'ip']

  def _get_src_l4_port(self):
    """
    Getter method for src_l4_port, mapped from YANG variable /load_balance_lag/load_balance/hash/ip/src_l4_port (empty)
    """
    return self.__src_l4_port
      
  def _set_src_l4_port(self, v, load=False):
    """
    Setter method for src_l4_port, mapped from YANG variable /load_balance_lag/load_balance/hash/ip/src_l4_port (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_l4_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_l4_port() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="src-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'src-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip src-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_l4_port must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="src-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'src-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip src-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__src_l4_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_l4_port(self):
    self.__src_l4_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="src-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'src-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip src-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_dst_l4_port(self):
    """
    Getter method for dst_l4_port, mapped from YANG variable /load_balance_lag/load_balance/hash/ip/dst_l4_port (empty)
    """
    return self.__dst_l4_port
      
  def _set_dst_l4_port(self, v, load=False):
    """
    Setter method for dst_l4_port, mapped from YANG variable /load_balance_lag/load_balance/hash/ip/dst_l4_port (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dst_l4_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dst_l4_port() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dst-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'dst-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip dst-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dst_l4_port must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dst-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'dst-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip dst-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__dst_l4_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dst_l4_port(self):
    self.__dst_l4_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dst-l4-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'dst-l4-port', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip dst-l4-port\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_src_ip(self):
    """
    Getter method for src_ip, mapped from YANG variable /load_balance_lag/load_balance/hash/ip/src_ip (empty)
    """
    return self.__src_ip
      
  def _set_src_ip(self, v, load=False):
    """
    Setter method for src_ip, mapped from YANG variable /load_balance_lag/load_balance/hash/ip/src_ip (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_ip() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="src-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'src-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip src-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_ip must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="src-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'src-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip src-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__src_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_ip(self):
    self.__src_ip = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="src-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'src-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip src-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_dst_ip(self):
    """
    Getter method for dst_ip, mapped from YANG variable /load_balance_lag/load_balance/hash/ip/dst_ip (empty)
    """
    return self.__dst_ip
      
  def _set_dst_ip(self, v, load=False):
    """
    Setter method for dst_ip, mapped from YANG variable /load_balance_lag/load_balance/hash/ip/dst_ip (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dst_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dst_ip() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dst-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'dst-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip dst-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dst_ip must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dst-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'dst-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip dst-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__dst_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dst_ip(self):
    self.__dst_ip = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dst-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'dst-ip', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip dst-ip\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_protocol(self):
    """
    Getter method for protocol, mapped from YANG variable /load_balance_lag/load_balance/hash/ip/protocol (empty)
    """
    return self.__protocol
      
  def _set_protocol(self, v, load=False):
    """
    Setter method for protocol, mapped from YANG variable /load_balance_lag/load_balance/hash/ip/protocol (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'protocol', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip protocol\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'protocol', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip protocol\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol(self):
    self.__protocol = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'protocol', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ip protocol\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)

  src_l4_port = __builtin__.property(_get_src_l4_port, _set_src_l4_port)
  dst_l4_port = __builtin__.property(_get_dst_l4_port, _set_dst_l4_port)
  src_ip = __builtin__.property(_get_src_ip, _set_src_ip)
  dst_ip = __builtin__.property(_get_dst_ip, _set_dst_ip)
  protocol = __builtin__.property(_get_protocol, _set_protocol)


  _pyangbind_elements = {'src_l4_port': src_l4_port, 'dst_l4_port': dst_l4_port, 'src_ip': src_ip, 'dst_ip': dst_ip, 'protocol': protocol, }


