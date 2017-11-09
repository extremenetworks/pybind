
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import spf_log_events
class spf_log_levels(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /spf-log-state/spf-log-levels. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: ISIS SPF LOG Level (Level-1 and level-2
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__level','__log_counts','__spf_trigger_count','__node_count','__spf_log_events',)

  _yang_name = 'spf-log-levels'
  _rest_name = 'spf-log-levels'

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
    self.__spf_log_events = YANGDynClass(base=YANGListType("spf_log_index",spf_log_events.spf_log_events, yang_name="spf-log-events", rest_name="spf-log-events", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='spf-log-index', extensions=None), is_container='list', yang_name="spf-log-events", rest_name="spf-log-events", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)
    self.__spf_trigger_count = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="spf-trigger-count", rest_name="spf-trigger-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)
    self.__node_count = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="node-count", rest_name="node-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)
    self.__log_counts = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="log-counts", rest_name="log-counts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)
    self.__level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'isis-level1-2': {'value': 0}, u'isis-level1': {'value': 1}, u'isis-level2': {'value': 2}},), is_leaf=True, yang_name="level", rest_name="level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-level', is_config=False)

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
      return [u'spf-log-state', u'spf-log-levels']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'spf-log-state', u'spf-log-levels']

  def _get_level(self):
    """
    Getter method for level, mapped from YANG variable /spf_log_state/spf_log_levels/level (isis-level)

    YANG Description: SPF LOG level type 
    """
    return self.__level
      
  def _set_level(self, v, load=False):
    """
    Setter method for level, mapped from YANG variable /spf_log_state/spf_log_levels/level (isis-level)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level() directly.

    YANG Description: SPF LOG level type 
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'isis-level1-2': {'value': 0}, u'isis-level1': {'value': 1}, u'isis-level2': {'value': 2}},), is_leaf=True, yang_name="level", rest_name="level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-level', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level must be of a type compatible with isis-level""",
          'defined-type': "brocade-isis-operational:isis-level",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'isis-level1-2': {'value': 0}, u'isis-level1': {'value': 1}, u'isis-level2': {'value': 2}},), is_leaf=True, yang_name="level", rest_name="level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-level', is_config=False)""",
        })

    self.__level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level(self):
    self.__level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'isis-level1-2': {'value': 0}, u'isis-level1': {'value': 1}, u'isis-level2': {'value': 2}},), is_leaf=True, yang_name="level", rest_name="level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-level', is_config=False)


  def _get_log_counts(self):
    """
    Getter method for log_counts, mapped from YANG variable /spf_log_state/spf_log_levels/log_counts (uint16)

    YANG Description: Number of logs
    """
    return self.__log_counts
      
  def _set_log_counts(self, v, load=False):
    """
    Setter method for log_counts, mapped from YANG variable /spf_log_state/spf_log_levels/log_counts (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_counts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_counts() directly.

    YANG Description: Number of logs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="log-counts", rest_name="log-counts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_counts must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="log-counts", rest_name="log-counts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)""",
        })

    self.__log_counts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_counts(self):
    self.__log_counts = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="log-counts", rest_name="log-counts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)


  def _get_spf_trigger_count(self):
    """
    Getter method for spf_trigger_count, mapped from YANG variable /spf_log_state/spf_log_levels/spf_trigger_count (uint16)

    YANG Description: Number of SPF triggers and run currenlty
    """
    return self.__spf_trigger_count
      
  def _set_spf_trigger_count(self, v, load=False):
    """
    Setter method for spf_trigger_count, mapped from YANG variable /spf_log_state/spf_log_levels/spf_trigger_count (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf_trigger_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf_trigger_count() directly.

    YANG Description: Number of SPF triggers and run currenlty
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="spf-trigger-count", rest_name="spf-trigger-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf_trigger_count must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="spf-trigger-count", rest_name="spf-trigger-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)""",
        })

    self.__spf_trigger_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf_trigger_count(self):
    self.__spf_trigger_count = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="spf-trigger-count", rest_name="spf-trigger-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)


  def _get_node_count(self):
    """
    Getter method for node_count, mapped from YANG variable /spf_log_state/spf_log_levels/node_count (uint16)

    YANG Description: Number of nodes SPF traversed in a given SPF run
    """
    return self.__node_count
      
  def _set_node_count(self, v, load=False):
    """
    Setter method for node_count, mapped from YANG variable /spf_log_state/spf_log_levels/node_count (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_node_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_node_count() directly.

    YANG Description: Number of nodes SPF traversed in a given SPF run
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="node-count", rest_name="node-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """node_count must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="node-count", rest_name="node-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)""",
        })

    self.__node_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_node_count(self):
    self.__node_count = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="node-count", rest_name="node-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)


  def _get_spf_log_events(self):
    """
    Getter method for spf_log_events, mapped from YANG variable /spf_log_state/spf_log_levels/spf_log_events (list)

    YANG Description: SPF Log event
    """
    return self.__spf_log_events
      
  def _set_spf_log_events(self, v, load=False):
    """
    Setter method for spf_log_events, mapped from YANG variable /spf_log_state/spf_log_levels/spf_log_events (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf_log_events is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf_log_events() directly.

    YANG Description: SPF Log event
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("spf_log_index",spf_log_events.spf_log_events, yang_name="spf-log-events", rest_name="spf-log-events", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='spf-log-index', extensions=None), is_container='list', yang_name="spf-log-events", rest_name="spf-log-events", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf_log_events must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("spf_log_index",spf_log_events.spf_log_events, yang_name="spf-log-events", rest_name="spf-log-events", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='spf-log-index', extensions=None), is_container='list', yang_name="spf-log-events", rest_name="spf-log-events", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)""",
        })

    self.__spf_log_events = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf_log_events(self):
    self.__spf_log_events = YANGDynClass(base=YANGListType("spf_log_index",spf_log_events.spf_log_events, yang_name="spf-log-events", rest_name="spf-log-events", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='spf-log-index', extensions=None), is_container='list', yang_name="spf-log-events", rest_name="spf-log-events", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)

  level = __builtin__.property(_get_level)
  log_counts = __builtin__.property(_get_log_counts)
  spf_trigger_count = __builtin__.property(_get_spf_trigger_count)
  node_count = __builtin__.property(_get_node_count)
  spf_log_events = __builtin__.property(_get_spf_log_events)


  _pyangbind_elements = {'level': level, 'log_counts': log_counts, 'spf_trigger_count': spf_trigger_count, 'node_count': node_count, 'spf_log_events': spf_log_events, }


