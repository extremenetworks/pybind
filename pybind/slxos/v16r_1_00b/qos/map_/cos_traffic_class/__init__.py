
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import cos_to_tc_dp_mappings
class cos_traffic_class(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mls - based on the path /qos/map/cos-traffic-class. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__cos_to_tc_dp_mappings',)

  _yang_name = 'cos-traffic-class'

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
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='map-name-type', is_config=True)
    self.__cos_to_tc_dp_mappings = YANGDynClass(base=YANGListType("from_cos",cos_to_tc_dp_mappings.cos_to_tc_dp_mappings, yang_name="cos-to-tc-dp-mappings", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='from-cos', extensions={u'tailf-common': {u'info': u'Map CoS value to Traffic-Class value with Drop-Precedence', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'map', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'cos_traffic_class_mapping'}}), is_container='list', yang_name="cos-to-tc-dp-mappings", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map CoS value to Traffic-Class value with Drop-Precedence', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'map', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'cos_traffic_class_mapping'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)

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
      return [u'qos', u'map', u'cos-traffic-class']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'qos', u'map', u'cos-traffic-class']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /qos/map/cos_traffic_class/name (map-name-type)
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /qos/map/cos_traffic_class/name (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with map-name-type""",
          'defined-type': "brocade-qos-mls:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='map-name-type', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='map-name-type', is_config=True)


  def _get_cos_to_tc_dp_mappings(self):
    """
    Getter method for cos_to_tc_dp_mappings, mapped from YANG variable /qos/map/cos_traffic_class/cos_to_tc_dp_mappings (list)
    """
    return self.__cos_to_tc_dp_mappings
      
  def _set_cos_to_tc_dp_mappings(self, v, load=False):
    """
    Setter method for cos_to_tc_dp_mappings, mapped from YANG variable /qos/map/cos_traffic_class/cos_to_tc_dp_mappings (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos_to_tc_dp_mappings is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos_to_tc_dp_mappings() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("from_cos",cos_to_tc_dp_mappings.cos_to_tc_dp_mappings, yang_name="cos-to-tc-dp-mappings", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='from-cos', extensions={u'tailf-common': {u'info': u'Map CoS value to Traffic-Class value with Drop-Precedence', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'map', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'cos_traffic_class_mapping'}}), is_container='list', yang_name="cos-to-tc-dp-mappings", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map CoS value to Traffic-Class value with Drop-Precedence', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'map', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'cos_traffic_class_mapping'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos_to_tc_dp_mappings must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("from_cos",cos_to_tc_dp_mappings.cos_to_tc_dp_mappings, yang_name="cos-to-tc-dp-mappings", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='from-cos', extensions={u'tailf-common': {u'info': u'Map CoS value to Traffic-Class value with Drop-Precedence', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'map', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'cos_traffic_class_mapping'}}), is_container='list', yang_name="cos-to-tc-dp-mappings", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map CoS value to Traffic-Class value with Drop-Precedence', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'map', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'cos_traffic_class_mapping'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)""",
        })

    self.__cos_to_tc_dp_mappings = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos_to_tc_dp_mappings(self):
    self.__cos_to_tc_dp_mappings = YANGDynClass(base=YANGListType("from_cos",cos_to_tc_dp_mappings.cos_to_tc_dp_mappings, yang_name="cos-to-tc-dp-mappings", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='from-cos', extensions={u'tailf-common': {u'info': u'Map CoS value to Traffic-Class value with Drop-Precedence', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'map', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'cos_traffic_class_mapping'}}), is_container='list', yang_name="cos-to-tc-dp-mappings", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map CoS value to Traffic-Class value with Drop-Precedence', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'map', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'cos_traffic_class_mapping'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  cos_to_tc_dp_mappings = __builtin__.property(_get_cos_to_tc_dp_mappings, _set_cos_to_tc_dp_mappings)


  _pyangbind_elements = {'name': name, 'cos_to_tc_dp_mappings': cos_to_tc_dp_mappings, }


