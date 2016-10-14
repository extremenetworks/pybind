
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import igmp_snooping_mrouters_
class igmp_snooping_mrouters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mc-hms-operational - based on the path /igmp-snooping-state/igmp-snooping-mrouters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Igmp snoopig mrouter list
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__vlan_id','__igmp_snooping_mrouters',)

  _yang_name = 'igmp-snooping-mrouters'

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
    self.__igmp_snooping_mrouters = YANGDynClass(base=YANGListType("vlan_id",igmp_snooping_mrouters_.igmp_snooping_mrouters, yang_name="igmp-snooping-mrouters", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-mrouter', u'cli-suppress-show-path': None}}), is_container='list', yang_name="igmp-snooping-mrouters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-mrouter', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)

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
      return [u'igmp-snooping-state', u'igmp-snooping-mrouters']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'igmp-snooping-state', u'igmp-snooping-mrouters']

  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /igmp_snooping_state/igmp_snooping_mrouters/vlan_id (uint32)

    YANG Description: vlan id
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /igmp_snooping_state/igmp_snooping_mrouters/vlan_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: vlan id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_igmp_snooping_mrouters(self):
    """
    Getter method for igmp_snooping_mrouters, mapped from YANG variable /igmp_snooping_state/igmp_snooping_mrouters/igmp_snooping_mrouters (list)

    YANG Description: Igmp snoopig mrouter info
    """
    return self.__igmp_snooping_mrouters
      
  def _set_igmp_snooping_mrouters(self, v, load=False):
    """
    Setter method for igmp_snooping_mrouters, mapped from YANG variable /igmp_snooping_state/igmp_snooping_mrouters/igmp_snooping_mrouters (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmp_snooping_mrouters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmp_snooping_mrouters() directly.

    YANG Description: Igmp snoopig mrouter info
    """
    try:
      t = YANGDynClass(v,base=YANGListType("vlan_id",igmp_snooping_mrouters_.igmp_snooping_mrouters, yang_name="igmp-snooping-mrouters", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-mrouter', u'cli-suppress-show-path': None}}), is_container='list', yang_name="igmp-snooping-mrouters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-mrouter', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmp_snooping_mrouters must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vlan_id",igmp_snooping_mrouters_.igmp_snooping_mrouters, yang_name="igmp-snooping-mrouters", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-mrouter', u'cli-suppress-show-path': None}}), is_container='list', yang_name="igmp-snooping-mrouters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-mrouter', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)""",
        })

    self.__igmp_snooping_mrouters = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmp_snooping_mrouters(self):
    self.__igmp_snooping_mrouters = YANGDynClass(base=YANGListType("vlan_id",igmp_snooping_mrouters_.igmp_snooping_mrouters, yang_name="igmp-snooping-mrouters", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-mrouter', u'cli-suppress-show-path': None}}), is_container='list', yang_name="igmp-snooping-mrouters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-mrouter', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)

  vlan_id = __builtin__.property(_get_vlan_id)
  igmp_snooping_mrouters = __builtin__.property(_get_igmp_snooping_mrouters)


  _pyangbind_elements = {'vlan_id': vlan_id, 'igmp_snooping_mrouters': igmp_snooping_mrouters, }


