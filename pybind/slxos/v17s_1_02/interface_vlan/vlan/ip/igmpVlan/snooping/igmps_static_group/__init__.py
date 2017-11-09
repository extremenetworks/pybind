
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class igmps_static_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface-vlan/vlan/ip/igmpVlan/snooping/igmps_static-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__igmps_mcast_address','__igmps_interface','__igmps_if_type','__igmps_value',)

  _yang_name = 'igmps_static-group'
  _rest_name = 'igmps_static-group'

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
    self.__igmps_interface = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface': {}},), is_leaf=True, yang_name="igmps-interface", rest_name="igmps-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)
    self.__igmps_if_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 8}, u'port-channel': {'value': 3}},), is_leaf=True, yang_name="igmps-if-type", rest_name="igmps-if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)
    self.__igmps_value = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']}), is_leaf=True, yang_name="igmps-value", rest_name="igmps-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='string-type', is_config=True)
    self.__igmps_mcast_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="igmps-mcast-address", rest_name="igmps-mcast-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='inet:ipv4-address', is_config=True)

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
      return [u'interface-vlan', u'vlan', u'ip', u'igmpVlan', u'snooping', u'igmps_static-group']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface-vlan', u'vlan', u'ip', u'igmpVlan', u'snooping', u'igmps_static-group']

  def _get_igmps_mcast_address(self):
    """
    Getter method for igmps_mcast_address, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_static_group/igmps_mcast_address (inet:ipv4-address)
    """
    return self.__igmps_mcast_address
      
  def _set_igmps_mcast_address(self, v, load=False):
    """
    Setter method for igmps_mcast_address, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_static_group/igmps_mcast_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_mcast_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_mcast_address() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="igmps-mcast-address", rest_name="igmps-mcast-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_mcast_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="igmps-mcast-address", rest_name="igmps-mcast-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__igmps_mcast_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_mcast_address(self):
    self.__igmps_mcast_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="igmps-mcast-address", rest_name="igmps-mcast-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='inet:ipv4-address', is_config=True)


  def _get_igmps_interface(self):
    """
    Getter method for igmps_interface, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_static_group/igmps_interface (enumeration)
    """
    return self.__igmps_interface
      
  def _set_igmps_interface(self, v, load=False):
    """
    Setter method for igmps_interface, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_static_group/igmps_interface (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_interface() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface': {}},), is_leaf=True, yang_name="igmps-interface", rest_name="igmps-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_interface must be of a type compatible with enumeration""",
          'defined-type': "brocade-igmp-snooping:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface': {}},), is_leaf=True, yang_name="igmps-interface", rest_name="igmps-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)""",
        })

    self.__igmps_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_interface(self):
    self.__igmps_interface = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface': {}},), is_leaf=True, yang_name="igmps-interface", rest_name="igmps-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)


  def _get_igmps_if_type(self):
    """
    Getter method for igmps_if_type, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_static_group/igmps_if_type (enumeration)
    """
    return self.__igmps_if_type
      
  def _set_igmps_if_type(self, v, load=False):
    """
    Setter method for igmps_if_type, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_static_group/igmps_if_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_if_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_if_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 8}, u'port-channel': {'value': 3}},), is_leaf=True, yang_name="igmps-if-type", rest_name="igmps-if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_if_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-igmp-snooping:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 8}, u'port-channel': {'value': 3}},), is_leaf=True, yang_name="igmps-if-type", rest_name="igmps-if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)""",
        })

    self.__igmps_if_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_if_type(self):
    self.__igmps_if_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 8}, u'port-channel': {'value': 3}},), is_leaf=True, yang_name="igmps-if-type", rest_name="igmps-if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)


  def _get_igmps_value(self):
    """
    Getter method for igmps_value, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_static_group/igmps_value (string-type)
    """
    return self.__igmps_value
      
  def _set_igmps_value(self, v, load=False):
    """
    Setter method for igmps_value, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_static_group/igmps_value (string-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_value() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']}), is_leaf=True, yang_name="igmps-value", rest_name="igmps-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='string-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_value must be of a type compatible with string-type""",
          'defined-type': "brocade-igmp-snooping:string-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']}), is_leaf=True, yang_name="igmps-value", rest_name="igmps-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='string-type', is_config=True)""",
        })

    self.__igmps_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_value(self):
    self.__igmps_value = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']}), is_leaf=True, yang_name="igmps-value", rest_name="igmps-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='string-type', is_config=True)

  igmps_mcast_address = __builtin__.property(_get_igmps_mcast_address, _set_igmps_mcast_address)
  igmps_interface = __builtin__.property(_get_igmps_interface, _set_igmps_interface)
  igmps_if_type = __builtin__.property(_get_igmps_if_type, _set_igmps_if_type)
  igmps_value = __builtin__.property(_get_igmps_value, _set_igmps_value)


  _pyangbind_elements = {'igmps_mcast_address': igmps_mcast_address, 'igmps_interface': igmps_interface, 'igmps_if_type': igmps_if_type, 'igmps_value': igmps_value, }


