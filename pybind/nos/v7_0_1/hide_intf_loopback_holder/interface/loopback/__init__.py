
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vrf
import intf_loopback
class loopback(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-intf-loopback - based on the path /hide-intf-loopback-holder/interface/loopback. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__id','__vrf','__intf_loopback',)

  _yang_name = 'loopback'

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
    self.__intf_loopback = YANGDynClass(base=intf_loopback.intf_loopback, is_container='container', yang_name="intf-loopback", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='container', is_config=True)
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-custom-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='intf-loopback-port-type', is_config=True)
    self.__vrf = YANGDynClass(base=vrf.vrf, is_container='container', yang_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Assign VRF to interface', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_VRF_BIND_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='container', is_config=True)

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
      return [u'hide-intf-loopback-holder', u'interface', u'loopback']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'interface', u'Loopback']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /hide_intf_loopback_holder/interface/loopback/id (intf-loopback-port-type)
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /hide_intf_loopback_holder/interface/loopback/id (intf-loopback-port-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-custom-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='intf-loopback-port-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with intf-loopback-port-type""",
          'defined-type': "brocade-intf-loopback:intf-loopback-port-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-custom-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='intf-loopback-port-type', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-custom-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='intf-loopback-port-type', is_config=True)


  def _get_vrf(self):
    """
    Getter method for vrf, mapped from YANG variable /hide_intf_loopback_holder/interface/loopback/vrf (container)
    """
    return self.__vrf
      
  def _set_vrf(self, v, load=False):
    """
    Setter method for vrf, mapped from YANG variable /hide_intf_loopback_holder/interface/loopback/vrf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf() directly.
    """
    try:
      t = YANGDynClass(v,base=vrf.vrf, is_container='container', yang_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Assign VRF to interface', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_VRF_BIND_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vrf.vrf, is_container='container', yang_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Assign VRF to interface', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_VRF_BIND_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='container', is_config=True)""",
        })

    self.__vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf(self):
    self.__vrf = YANGDynClass(base=vrf.vrf, is_container='container', yang_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Assign VRF to interface', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_VRF_BIND_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='container', is_config=True)


  def _get_intf_loopback(self):
    """
    Getter method for intf_loopback, mapped from YANG variable /hide_intf_loopback_holder/interface/loopback/intf_loopback (container)
    """
    return self.__intf_loopback
      
  def _set_intf_loopback(self, v, load=False):
    """
    Setter method for intf_loopback, mapped from YANG variable /hide_intf_loopback_holder/interface/loopback/intf_loopback (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_intf_loopback is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_intf_loopback() directly.
    """
    try:
      t = YANGDynClass(v,base=intf_loopback.intf_loopback, is_container='container', yang_name="intf-loopback", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """intf_loopback must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=intf_loopback.intf_loopback, is_container='container', yang_name="intf-loopback", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='container', is_config=True)""",
        })

    self.__intf_loopback = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_intf_loopback(self):
    self.__intf_loopback = YANGDynClass(base=intf_loopback.intf_loopback, is_container='container', yang_name="intf-loopback", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='container', is_config=True)

  id = __builtin__.property(_get_id, _set_id)
  vrf = __builtin__.property(_get_vrf, _set_vrf)
  intf_loopback = __builtin__.property(_get_intf_loopback, _set_intf_loopback)


  _pyangbind_elements = {'id': id, 'vrf': vrf, 'intf_loopback': intf_loopback, }


