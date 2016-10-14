
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import forwarding_interface
class mac_address_table(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mac-address-table - based on the path /brocade_mac_address_table_rpc/get-mac-address-table/output/mac-address-table. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__vlanid','__mac_address','__mac_type','__mac_state','__forwarding_interface',)

  _yang_name = 'mac-address-table'

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
    self.__forwarding_interface = YANGDynClass(base=YANGListType(False,forwarding_interface.forwarding_interface, yang_name="forwarding-interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="forwarding-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='list', is_config=True)
    self.__mac_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 1}, u'unknown': {'value': 4}, u'inactive': {'value': 2}, u'remote': {'value': 3}},), is_leaf=True, yang_name="mac-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    self.__mac_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'fpma': {'value': 3}, u'static': {'value': 1}, u'system': {'value': 4}},), is_leaf=True, yang_name="mac-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    self.__vlanid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}), is_leaf=True, yang_name="vlanid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='interface:vlan-type', is_config=True)
    self.__mac_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='yang:mac-address', is_config=True)

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
      return [u'brocade_mac_address_table_rpc', u'get-mac-address-table', u'output', u'mac-address-table']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'get-mac-address-table', u'output', u'mac-address-table']

  def _get_vlanid(self):
    """
    Getter method for vlanid, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/output/mac_address_table/vlanid (interface:vlan-type)

    YANG Description: vlan id
    """
    return self.__vlanid
      
  def _set_vlanid(self, v, load=False):
    """
    Setter method for vlanid, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/output/mac_address_table/vlanid (interface:vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlanid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlanid() directly.

    YANG Description: vlan id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}), is_leaf=True, yang_name="vlanid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='interface:vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlanid must be of a type compatible with interface:vlan-type""",
          'defined-type': "interface:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}), is_leaf=True, yang_name="vlanid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='interface:vlan-type', is_config=True)""",
        })

    self.__vlanid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlanid(self):
    self.__vlanid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}), is_leaf=True, yang_name="vlanid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='interface:vlan-type', is_config=True)


  def _get_mac_address(self):
    """
    Getter method for mac_address, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/output/mac_address_table/mac_address (yang:mac-address)

    YANG Description: Mac Address
    """
    return self.__mac_address
      
  def _set_mac_address(self, v, load=False):
    """
    Setter method for mac_address, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/output/mac_address_table/mac_address (yang:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_address() directly.

    YANG Description: Mac Address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='yang:mac-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_address must be of a type compatible with yang:mac-address""",
          'defined-type': "yang:mac-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='yang:mac-address', is_config=True)""",
        })

    self.__mac_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_address(self):
    self.__mac_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='yang:mac-address', is_config=True)


  def _get_mac_type(self):
    """
    Getter method for mac_type, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/output/mac_address_table/mac_type (enumeration)

    YANG Description: Mac Address type
    """
    return self.__mac_type
      
  def _set_mac_type(self, v, load=False):
    """
    Setter method for mac_type, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/output/mac_address_table/mac_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_type() directly.

    YANG Description: Mac Address type
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'fpma': {'value': 3}, u'static': {'value': 1}, u'system': {'value': 4}},), is_leaf=True, yang_name="mac-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-address-table:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'fpma': {'value': 3}, u'static': {'value': 1}, u'system': {'value': 4}},), is_leaf=True, yang_name="mac-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)""",
        })

    self.__mac_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_type(self):
    self.__mac_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'fpma': {'value': 3}, u'static': {'value': 1}, u'system': {'value': 4}},), is_leaf=True, yang_name="mac-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)


  def _get_mac_state(self):
    """
    Getter method for mac_state, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/output/mac_address_table/mac_state (enumeration)

    YANG Description: Mac Address state
    """
    return self.__mac_state
      
  def _set_mac_state(self, v, load=False):
    """
    Setter method for mac_state, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/output/mac_address_table/mac_state (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_state() directly.

    YANG Description: Mac Address state
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 1}, u'unknown': {'value': 4}, u'inactive': {'value': 2}, u'remote': {'value': 3}},), is_leaf=True, yang_name="mac-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_state must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-address-table:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 1}, u'unknown': {'value': 4}, u'inactive': {'value': 2}, u'remote': {'value': 3}},), is_leaf=True, yang_name="mac-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)""",
        })

    self.__mac_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_state(self):
    self.__mac_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 1}, u'unknown': {'value': 4}, u'inactive': {'value': 2}, u'remote': {'value': 3}},), is_leaf=True, yang_name="mac-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)


  def _get_forwarding_interface(self):
    """
    Getter method for forwarding_interface, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/output/mac_address_table/forwarding_interface (list)

    YANG Description: List of forwarding interfaces
    """
    return self.__forwarding_interface
      
  def _set_forwarding_interface(self, v, load=False):
    """
    Setter method for forwarding_interface, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/output/mac_address_table/forwarding_interface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_interface() directly.

    YANG Description: List of forwarding interfaces
    """
    try:
      t = YANGDynClass(v,base=YANGListType(False,forwarding_interface.forwarding_interface, yang_name="forwarding-interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="forwarding-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_interface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,forwarding_interface.forwarding_interface, yang_name="forwarding-interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="forwarding-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='list', is_config=True)""",
        })

    self.__forwarding_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_interface(self):
    self.__forwarding_interface = YANGDynClass(base=YANGListType(False,forwarding_interface.forwarding_interface, yang_name="forwarding-interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="forwarding-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='list', is_config=True)

  vlanid = __builtin__.property(_get_vlanid, _set_vlanid)
  mac_address = __builtin__.property(_get_mac_address, _set_mac_address)
  mac_type = __builtin__.property(_get_mac_type, _set_mac_type)
  mac_state = __builtin__.property(_get_mac_state, _set_mac_state)
  forwarding_interface = __builtin__.property(_get_forwarding_interface, _set_forwarding_interface)


  _pyangbind_elements = {'vlanid': vlanid, 'mac_address': mac_address, 'mac_type': mac_type, 'mac_state': mac_state, 'forwarding_interface': forwarding_interface, }


