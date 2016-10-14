
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import priority
class traffic_class_exp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mpls - based on the path /qos-mpls/map/traffic-class-exp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__traffic_class_exp_map_name','__priority',)

  _yang_name = 'traffic-class-exp'

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
    self.__priority = YANGDynClass(base=YANGListType("priority_in_values",priority.priority, yang_name="priority", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority-in-values', extensions={u'tailf-common': {u'info': u'Map Traffic class value to Exp value', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'QosMplsTrafficClassExpCallpoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'traffic-class'}}), is_container='list', yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map Traffic class value to Exp value', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'QosMplsTrafficClassExpCallpoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'traffic-class'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)
    self.__traffic_class_exp_map_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="traffic-class-exp-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='map-name-type', is_config=True)

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
      return [u'qos-mpls', u'map', u'traffic-class-exp']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'qos-mpls', u'map', u'traffic-class-exp']

  def _get_traffic_class_exp_map_name(self):
    """
    Getter method for traffic_class_exp_map_name, mapped from YANG variable /qos_mpls/map/traffic_class_exp/traffic_class_exp_map_name (map-name-type)
    """
    return self.__traffic_class_exp_map_name
      
  def _set_traffic_class_exp_map_name(self, v, load=False):
    """
    Setter method for traffic_class_exp_map_name, mapped from YANG variable /qos_mpls/map/traffic_class_exp/traffic_class_exp_map_name (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_traffic_class_exp_map_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_traffic_class_exp_map_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="traffic-class-exp-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """traffic_class_exp_map_name must be of a type compatible with map-name-type""",
          'defined-type': "brocade-qos-mpls:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="traffic-class-exp-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='map-name-type', is_config=True)""",
        })

    self.__traffic_class_exp_map_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_traffic_class_exp_map_name(self):
    self.__traffic_class_exp_map_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="traffic-class-exp-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='map-name-type', is_config=True)


  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /qos_mpls/map/traffic_class_exp/priority (list)
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /qos_mpls/map/traffic_class_exp/priority (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("priority_in_values",priority.priority, yang_name="priority", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority-in-values', extensions={u'tailf-common': {u'info': u'Map Traffic class value to Exp value', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'QosMplsTrafficClassExpCallpoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'traffic-class'}}), is_container='list', yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map Traffic class value to Exp value', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'QosMplsTrafficClassExpCallpoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'traffic-class'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("priority_in_values",priority.priority, yang_name="priority", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority-in-values', extensions={u'tailf-common': {u'info': u'Map Traffic class value to Exp value', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'QosMplsTrafficClassExpCallpoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'traffic-class'}}), is_container='list', yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map Traffic class value to Exp value', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'QosMplsTrafficClassExpCallpoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'traffic-class'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=YANGListType("priority_in_values",priority.priority, yang_name="priority", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority-in-values', extensions={u'tailf-common': {u'info': u'Map Traffic class value to Exp value', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'QosMplsTrafficClassExpCallpoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'traffic-class'}}), is_container='list', yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map Traffic class value to Exp value', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'QosMplsTrafficClassExpCallpoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'traffic-class'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)

  traffic_class_exp_map_name = __builtin__.property(_get_traffic_class_exp_map_name, _set_traffic_class_exp_map_name)
  priority = __builtin__.property(_get_priority, _set_priority)


  _pyangbind_elements = {'traffic_class_exp_map_name': traffic_class_exp_map_name, 'priority': priority, }


