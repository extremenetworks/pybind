
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import private_vlan
class mode(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/switchport/mode. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The mode of the Layer2 interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vlan_mode','__private_vlan',)

  _yang_name = 'mode'
  _rest_name = 'mode'

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
    self.__vlan_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'access': {'value': 1}, u'trunk-no-default-native': {'value': 9}, u'trunk': {'value': 2}},), is_leaf=True, yang_name="vlan-mode", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='l2-mode-type', is_config=True)
    self.__private_vlan = YANGDynClass(base=private_vlan.private_vlan, is_container='container', yang_name="private-vlan", rest_name="private-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'switchport', u'mode']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'switchport', u'mode']

  def _get_vlan_mode(self):
    """
    Getter method for vlan_mode, mapped from YANG variable /interface/gigabitethernet/switchport/mode/vlan_mode (l2-mode-type)

    YANG Description: The access/trunk mode of this interface.
    """
    return self.__vlan_mode
      
  def _set_vlan_mode(self, v, load=False):
    """
    Setter method for vlan_mode, mapped from YANG variable /interface/gigabitethernet/switchport/mode/vlan_mode (l2-mode-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_mode() directly.

    YANG Description: The access/trunk mode of this interface.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'access': {'value': 1}, u'trunk-no-default-native': {'value': 9}, u'trunk': {'value': 2}},), is_leaf=True, yang_name="vlan-mode", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='l2-mode-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_mode must be of a type compatible with l2-mode-type""",
          'defined-type': "brocade-interface:l2-mode-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'access': {'value': 1}, u'trunk-no-default-native': {'value': 9}, u'trunk': {'value': 2}},), is_leaf=True, yang_name="vlan-mode", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='l2-mode-type', is_config=True)""",
        })

    self.__vlan_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_mode(self):
    self.__vlan_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'access': {'value': 1}, u'trunk-no-default-native': {'value': 9}, u'trunk': {'value': 2}},), is_leaf=True, yang_name="vlan-mode", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='l2-mode-type', is_config=True)


  def _get_private_vlan(self):
    """
    Getter method for private_vlan, mapped from YANG variable /interface/gigabitethernet/switchport/mode/private_vlan (container)
    """
    return self.__private_vlan
      
  def _set_private_vlan(self, v, load=False):
    """
    Setter method for private_vlan, mapped from YANG variable /interface/gigabitethernet/switchport/mode/private_vlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_private_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_private_vlan() directly.
    """
    try:
      t = YANGDynClass(v,base=private_vlan.private_vlan, is_container='container', yang_name="private-vlan", rest_name="private-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """private_vlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=private_vlan.private_vlan, is_container='container', yang_name="private-vlan", rest_name="private-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__private_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_private_vlan(self):
    self.__private_vlan = YANGDynClass(base=private_vlan.private_vlan, is_container='container', yang_name="private-vlan", rest_name="private-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

  vlan_mode = __builtin__.property(_get_vlan_mode, _set_vlan_mode)
  private_vlan = __builtin__.property(_get_private_vlan, _set_private_vlan)


  _pyangbind_elements = {'vlan_mode': vlan_mode, 'private_vlan': private_vlan, }

