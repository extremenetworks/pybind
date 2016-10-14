
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class igmp_l3_interfaces(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mc-hms-operational - based on the path /igmp-snooping-state/igmp-l3-interfaces/igmp-l3-interfaces. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Igmp L3 interface Information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_name','__is_igmp_enabled','__query_interval','__other_querier_interval','__query_reponse_time','__last_member_query_interval','__immediate_leave','__igmp_querier','__is_igmp_querier_local',)

  _yang_name = 'igmp-l3-interfaces'

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
    self.__is_igmp_enabled = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="is-igmp-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    self.__last_member_query_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-member-query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    self.__igmp_querier = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="igmp-querier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    self.__other_querier_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="other-querier-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    self.__immediate_leave = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="immediate-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    self.__is_igmp_querier_local = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="is-igmp-querier-local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    self.__query_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__query_reponse_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="query-reponse-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)

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
      return [u'igmp-snooping-state', u'igmp-l3-interfaces', u'igmp-l3-interfaces']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'igmp-snooping-state', u'igmp-l3-interfaces', u'igmp-l3-interfaces']

  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/interface_name (string)

    YANG Description: Igmp L3 interface name
    """
    return self.__interface_name
      
  def _set_interface_name(self, v, load=False):
    """
    Setter method for interface_name, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.

    YANG Description: Igmp L3 interface name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_is_igmp_enabled(self):
    """
    Getter method for is_igmp_enabled, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/is_igmp_enabled (uint8)

    YANG Description: IS IGMP Enabled on an Interface
    """
    return self.__is_igmp_enabled
      
  def _set_is_igmp_enabled(self, v, load=False):
    """
    Setter method for is_igmp_enabled, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/is_igmp_enabled (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_igmp_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_igmp_enabled() directly.

    YANG Description: IS IGMP Enabled on an Interface
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="is-igmp-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_igmp_enabled must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="is-igmp-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)""",
        })

    self.__is_igmp_enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_igmp_enabled(self):
    self.__is_igmp_enabled = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="is-igmp-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)


  def _get_query_interval(self):
    """
    Getter method for query_interval, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/query_interval (uint32)

    YANG Description: Igmp query interval
    """
    return self.__query_interval
      
  def _set_query_interval(self, v, load=False):
    """
    Setter method for query_interval, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/query_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_query_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_query_interval() directly.

    YANG Description: Igmp query interval
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """query_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__query_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_query_interval(self):
    self.__query_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_other_querier_interval(self):
    """
    Getter method for other_querier_interval, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/other_querier_interval (uint32)

    YANG Description: Igmp other querier interval
    """
    return self.__other_querier_interval
      
  def _set_other_querier_interval(self, v, load=False):
    """
    Setter method for other_querier_interval, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/other_querier_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_other_querier_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_other_querier_interval() directly.

    YANG Description: Igmp other querier interval
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="other-querier-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """other_querier_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="other-querier-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__other_querier_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_other_querier_interval(self):
    self.__other_querier_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="other-querier-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_query_reponse_time(self):
    """
    Getter method for query_reponse_time, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/query_reponse_time (uint32)

    YANG Description: Igmp query response time
    """
    return self.__query_reponse_time
      
  def _set_query_reponse_time(self, v, load=False):
    """
    Setter method for query_reponse_time, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/query_reponse_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_query_reponse_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_query_reponse_time() directly.

    YANG Description: Igmp query response time
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="query-reponse-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """query_reponse_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="query-reponse-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__query_reponse_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_query_reponse_time(self):
    self.__query_reponse_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="query-reponse-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_last_member_query_interval(self):
    """
    Getter method for last_member_query_interval, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/last_member_query_interval (uint32)

    YANG Description: Igmp last_member_query_interval
    """
    return self.__last_member_query_interval
      
  def _set_last_member_query_interval(self, v, load=False):
    """
    Setter method for last_member_query_interval, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/last_member_query_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_member_query_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_member_query_interval() directly.

    YANG Description: Igmp last_member_query_interval
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-member-query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_member_query_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-member-query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__last_member_query_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_member_query_interval(self):
    self.__last_member_query_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-member-query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_immediate_leave(self):
    """
    Getter method for immediate_leave, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/immediate_leave (uint8)

    YANG Description: Igmp Immediate Leave
    """
    return self.__immediate_leave
      
  def _set_immediate_leave(self, v, load=False):
    """
    Setter method for immediate_leave, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/immediate_leave (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_immediate_leave is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_immediate_leave() directly.

    YANG Description: Igmp Immediate Leave
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="immediate-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """immediate_leave must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="immediate-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)""",
        })

    self.__immediate_leave = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_immediate_leave(self):
    self.__immediate_leave = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="immediate-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)


  def _get_igmp_querier(self):
    """
    Getter method for igmp_querier, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/igmp_querier (uint32)

    YANG Description: Igmp querier ip address
    """
    return self.__igmp_querier
      
  def _set_igmp_querier(self, v, load=False):
    """
    Setter method for igmp_querier, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/igmp_querier (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmp_querier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmp_querier() directly.

    YANG Description: Igmp querier ip address
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="igmp-querier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmp_querier must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="igmp-querier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__igmp_querier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmp_querier(self):
    self.__igmp_querier = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="igmp-querier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_is_igmp_querier_local(self):
    """
    Getter method for is_igmp_querier_local, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/is_igmp_querier_local (uint8)

    YANG Description: Is igmp querier local
    """
    return self.__is_igmp_querier_local
      
  def _set_is_igmp_querier_local(self, v, load=False):
    """
    Setter method for is_igmp_querier_local, mapped from YANG variable /igmp_snooping_state/igmp_l3_interfaces/igmp_l3_interfaces/is_igmp_querier_local (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_igmp_querier_local is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_igmp_querier_local() directly.

    YANG Description: Is igmp querier local
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="is-igmp-querier-local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_igmp_querier_local must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="is-igmp-querier-local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)""",
        })

    self.__is_igmp_querier_local = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_igmp_querier_local(self):
    self.__is_igmp_querier_local = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="is-igmp-querier-local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)

  interface_name = __builtin__.property(_get_interface_name)
  is_igmp_enabled = __builtin__.property(_get_is_igmp_enabled)
  query_interval = __builtin__.property(_get_query_interval)
  other_querier_interval = __builtin__.property(_get_other_querier_interval)
  query_reponse_time = __builtin__.property(_get_query_reponse_time)
  last_member_query_interval = __builtin__.property(_get_last_member_query_interval)
  immediate_leave = __builtin__.property(_get_immediate_leave)
  igmp_querier = __builtin__.property(_get_igmp_querier)
  is_igmp_querier_local = __builtin__.property(_get_is_igmp_querier_local)


  _pyangbind_elements = {'interface_name': interface_name, 'is_igmp_enabled': is_igmp_enabled, 'query_interval': query_interval, 'other_querier_interval': other_querier_interval, 'query_reponse_time': query_reponse_time, 'last_member_query_interval': last_member_query_interval, 'immediate_leave': immediate_leave, 'igmp_querier': igmp_querier, 'is_igmp_querier_local': is_igmp_querier_local, }


