
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class Cpu(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-threshold-monitor - based on the path /threshold-monitor-hidden/threshold-monitor/Cpu. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__poll','__retry','__limit','__actions',)

  _yang_name = 'Cpu'
  _rest_name = 'Cpu'

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
    self.__poll = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'10 .. 3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="poll", rest_name="poll", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:10-3600 Polling interval'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='uint32', is_config=True)
    self.__limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 80']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(75), is_leaf=True, yang_name="limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'PERCENT:0-80 Percent threshold usage for component:CPU'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='uint32', is_config=True)
    self.__retry = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 100']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="retry", rest_name="retry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:1-100 Number of retries'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='uint32', is_config=True)
    self.__actions = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loginfo': {'value': 129}, u'none': {'value': 1}, u'raslog': {'value': 2}},), default=unicode("none"), is_leaf=True, yang_name="actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action to be taken when usage exceeds limit'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='enumeration', is_config=True)

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
      return [u'threshold-monitor-hidden', u'threshold-monitor', u'Cpu']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'threshold-monitor', u'Cpu']

  def _get_poll(self):
    """
    Getter method for poll, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/Cpu/poll (uint32)
    """
    return self.__poll
      
  def _set_poll(self, v, load=False):
    """
    Setter method for poll, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/Cpu/poll (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_poll is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_poll() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'10 .. 3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="poll", rest_name="poll", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:10-3600 Polling interval'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """poll must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'10 .. 3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="poll", rest_name="poll", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:10-3600 Polling interval'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='uint32', is_config=True)""",
        })

    self.__poll = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_poll(self):
    self.__poll = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'10 .. 3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="poll", rest_name="poll", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:10-3600 Polling interval'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='uint32', is_config=True)


  def _get_retry(self):
    """
    Getter method for retry, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/Cpu/retry (uint32)
    """
    return self.__retry
      
  def _set_retry(self, v, load=False):
    """
    Setter method for retry, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/Cpu/retry (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_retry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_retry() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 100']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="retry", rest_name="retry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:1-100 Number of retries'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """retry must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 100']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="retry", rest_name="retry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:1-100 Number of retries'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='uint32', is_config=True)""",
        })

    self.__retry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_retry(self):
    self.__retry = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 100']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="retry", rest_name="retry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:1-100 Number of retries'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='uint32', is_config=True)


  def _get_limit(self):
    """
    Getter method for limit, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/Cpu/limit (uint32)
    """
    return self.__limit
      
  def _set_limit(self, v, load=False):
    """
    Setter method for limit, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/Cpu/limit (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_limit() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 80']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(75), is_leaf=True, yang_name="limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'PERCENT:0-80 Percent threshold usage for component:CPU'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """limit must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 80']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(75), is_leaf=True, yang_name="limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'PERCENT:0-80 Percent threshold usage for component:CPU'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='uint32', is_config=True)""",
        })

    self.__limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_limit(self):
    self.__limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 80']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(75), is_leaf=True, yang_name="limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'PERCENT:0-80 Percent threshold usage for component:CPU'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='uint32', is_config=True)


  def _get_actions(self):
    """
    Getter method for actions, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/Cpu/actions (enumeration)
    """
    return self.__actions
      
  def _set_actions(self, v, load=False):
    """
    Setter method for actions, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/Cpu/actions (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_actions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_actions() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loginfo': {'value': 129}, u'none': {'value': 1}, u'raslog': {'value': 2}},), default=unicode("none"), is_leaf=True, yang_name="actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action to be taken when usage exceeds limit'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """actions must be of a type compatible with enumeration""",
          'defined-type': "brocade-threshold-monitor:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loginfo': {'value': 129}, u'none': {'value': 1}, u'raslog': {'value': 2}},), default=unicode("none"), is_leaf=True, yang_name="actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action to be taken when usage exceeds limit'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='enumeration', is_config=True)""",
        })

    self.__actions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_actions(self):
    self.__actions = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loginfo': {'value': 129}, u'none': {'value': 1}, u'raslog': {'value': 2}},), default=unicode("none"), is_leaf=True, yang_name="actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action to be taken when usage exceeds limit'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='enumeration', is_config=True)

  poll = __builtin__.property(_get_poll, _set_poll)
  retry = __builtin__.property(_get_retry, _set_retry)
  limit = __builtin__.property(_get_limit, _set_limit)
  actions = __builtin__.property(_get_actions, _set_actions)


  _pyangbind_elements = {'poll': poll, 'retry': retry, 'limit': limit, 'actions': actions, }

