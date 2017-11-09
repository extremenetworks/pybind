
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import tcp
import ip
import ipv6
import vrf
import line_speed
class management(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/management. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The list of management interfaces in the managed 
device. Each row represents a management interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__tcp','__ip','__ipv6','__vrf','__speed','__line_speed','__shutdown_management','__shutdown_management_oper',)

  _yang_name = 'management'
  _rest_name = 'Management'

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
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/([0-9]|[1-9][0-9])', 'length': [u'3..16']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='man-interface-type', is_config=True)
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__tcp = YANGDynClass(base=tcp.tcp, is_container='container', presence=False, yang_name="tcp", rest_name="tcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__line_speed = YANGDynClass(base=line_speed.line_speed, is_container='container', presence=False, yang_name="line-speed", rest_name="line-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__vrf = YANGDynClass(base=vrf.vrf, is_container='container', presence=False, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__shutdown_management_oper = YANGDynClass(base=unicode, is_leaf=True, yang_name="shutdown_management_oper", rest_name="oper-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'oper-status'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)
    self.__speed = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 0}, u'100': {'value': 2}, u'10': {'value': 1}},), default=unicode("auto"), is_leaf=True, yang_name="speed", rest_name="speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='enumeration', is_config=True)
    self.__shutdown_management = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown_management", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)

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
      return [u'interface', u'management']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Management']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /interface/management/name (man-interface-type)

    YANG Description: The name of the management interface.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /interface/management/name (man-interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: The name of the management interface.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/([0-9]|[1-9][0-9])', 'length': [u'3..16']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='man-interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with man-interface-type""",
          'defined-type': "brocade-interface:man-interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/([0-9]|[1-9][0-9])', 'length': [u'3..16']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='man-interface-type', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/([0-9]|[1-9][0-9])', 'length': [u'3..16']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='man-interface-type', is_config=True)


  def _get_tcp(self):
    """
    Getter method for tcp, mapped from YANG variable /interface/management/tcp (container)

    YANG Description: The TCP burstrate.
    """
    return self.__tcp
      
  def _set_tcp(self, v, load=False):
    """
    Setter method for tcp, mapped from YANG variable /interface/management/tcp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tcp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tcp() directly.

    YANG Description: The TCP burstrate.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tcp.tcp, is_container='container', presence=False, yang_name="tcp", rest_name="tcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tcp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tcp.tcp, is_container='container', presence=False, yang_name="tcp", rest_name="tcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__tcp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tcp(self):
    self.__tcp = YANGDynClass(base=tcp.tcp, is_container='container', presence=False, yang_name="tcp", rest_name="tcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /interface/management/ip (container)

    YANG Description: The IPv4 configurations for this management 
interface.
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /interface/management/ip (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: The IPv4 configurations for this management 
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_ipv6(self):
    """
    Getter method for ipv6, mapped from YANG variable /interface/management/ipv6 (container)

    YANG Description: The IPv6 configurations for this management 
interface.
    """
    return self.__ipv6
      
  def _set_ipv6(self, v, load=False):
    """
    Setter method for ipv6, mapped from YANG variable /interface/management/ipv6 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6() directly.

    YANG Description: The IPv6 configurations for this management 
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6(self):
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_vrf(self):
    """
    Getter method for vrf, mapped from YANG variable /interface/management/vrf (container)
    """
    return self.__vrf
      
  def _set_vrf(self, v, load=False):
    """
    Setter method for vrf, mapped from YANG variable /interface/management/vrf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vrf.vrf, is_container='container', presence=False, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vrf.vrf, is_container='container', presence=False, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf(self):
    self.__vrf = YANGDynClass(base=vrf.vrf, is_container='container', presence=False, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_speed(self):
    """
    Getter method for speed, mapped from YANG variable /interface/management/speed (enumeration)

    YANG Description: This specifies the administratively configured
bandwidth for this management interface.
    """
    return self.__speed
      
  def _set_speed(self, v, load=False):
    """
    Setter method for speed, mapped from YANG variable /interface/management/speed (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_speed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_speed() directly.

    YANG Description: This specifies the administratively configured
bandwidth for this management interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 0}, u'100': {'value': 2}, u'10': {'value': 1}},), default=unicode("auto"), is_leaf=True, yang_name="speed", rest_name="speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """speed must be of a type compatible with enumeration""",
          'defined-type': "brocade-interface:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 0}, u'100': {'value': 2}, u'10': {'value': 1}},), default=unicode("auto"), is_leaf=True, yang_name="speed", rest_name="speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='enumeration', is_config=True)""",
        })

    self.__speed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_speed(self):
    self.__speed = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 0}, u'100': {'value': 2}, u'10': {'value': 1}},), default=unicode("auto"), is_leaf=True, yang_name="speed", rest_name="speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='enumeration', is_config=True)


  def _get_line_speed(self):
    """
    Getter method for line_speed, mapped from YANG variable /interface/management/line_speed (container)

    YANG Description: The line-speed characteristics for this management 
interface.
    """
    return self.__line_speed
      
  def _set_line_speed(self, v, load=False):
    """
    Setter method for line_speed, mapped from YANG variable /interface/management/line_speed (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_line_speed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_line_speed() directly.

    YANG Description: The line-speed characteristics for this management 
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=line_speed.line_speed, is_container='container', presence=False, yang_name="line-speed", rest_name="line-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """line_speed must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=line_speed.line_speed, is_container='container', presence=False, yang_name="line-speed", rest_name="line-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__line_speed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_line_speed(self):
    self.__line_speed = YANGDynClass(base=line_speed.line_speed, is_container='container', presence=False, yang_name="line-speed", rest_name="line-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_shutdown_management(self):
    """
    Getter method for shutdown_management, mapped from YANG variable /interface/management/shutdown_management (empty)

    YANG Description: Shutdown this management interface.
    """
    return self.__shutdown_management
      
  def _set_shutdown_management(self, v, load=False):
    """
    Setter method for shutdown_management, mapped from YANG variable /interface/management/shutdown_management (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shutdown_management is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shutdown_management() directly.

    YANG Description: Shutdown this management interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="shutdown_management", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shutdown_management must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown_management", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__shutdown_management = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shutdown_management(self):
    self.__shutdown_management = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown_management", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_shutdown_management_oper(self):
    """
    Getter method for shutdown_management_oper, mapped from YANG variable /interface/management/shutdown_management_oper (string)

    YANG Description: Show the status of this management interface.
    """
    return self.__shutdown_management_oper
      
  def _set_shutdown_management_oper(self, v, load=False):
    """
    Setter method for shutdown_management_oper, mapped from YANG variable /interface/management/shutdown_management_oper (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shutdown_management_oper is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shutdown_management_oper() directly.

    YANG Description: Show the status of this management interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="shutdown_management_oper", rest_name="oper-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'oper-status'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shutdown_management_oper must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="shutdown_management_oper", rest_name="oper-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'oper-status'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)""",
        })

    self.__shutdown_management_oper = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shutdown_management_oper(self):
    self.__shutdown_management_oper = YANGDynClass(base=unicode, is_leaf=True, yang_name="shutdown_management_oper", rest_name="oper-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'oper-status'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)

  name = __builtin__.property(_get_name, _set_name)
  tcp = __builtin__.property(_get_tcp, _set_tcp)
  ip = __builtin__.property(_get_ip, _set_ip)
  ipv6 = __builtin__.property(_get_ipv6, _set_ipv6)
  vrf = __builtin__.property(_get_vrf, _set_vrf)
  speed = __builtin__.property(_get_speed, _set_speed)
  line_speed = __builtin__.property(_get_line_speed, _set_line_speed)
  shutdown_management = __builtin__.property(_get_shutdown_management, _set_shutdown_management)
  shutdown_management_oper = __builtin__.property(_get_shutdown_management_oper)


  _pyangbind_elements = {'name': name, 'tcp': tcp, 'ip': ip, 'ipv6': ipv6, 'vrf': vrf, 'speed': speed, 'line_speed': line_speed, 'shutdown_management': shutdown_management, 'shutdown_management_oper': shutdown_management_oper, }


