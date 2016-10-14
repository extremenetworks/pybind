
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import controller_async_list
import controller_info
class controller_detail_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/detail/controller-detail-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Controller detail
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__controller_idx','__controller_async_list','__controller_info',)

  _yang_name = 'controller-detail-list'

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
    self.__controller_info = YANGDynClass(base=controller_info.controller_info, is_container='container', yang_name="controller-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-controller-controller-info-2'}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='container', is_config=False)
    self.__controller_async_list = YANGDynClass(base=YANGListType("async_type",controller_async_list.controller_async_list, yang_name="controller-async-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='async-type', extensions={u'tailf-common': {u'callpoint': u'openflow-controller-async', u'cli-suppress-show-path': None}}), is_container='list', yang_name="controller-async-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-controller-async', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    self.__controller_idx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="controller-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)

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
      return [u'openflow-state', u'detail', u'controller-detail-list']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'openflow-state', u'detail', u'controller-detail-list']

  def _get_controller_idx(self):
    """
    Getter method for controller_idx, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_idx (uint32)

    YANG Description: Controller Index
    """
    return self.__controller_idx
      
  def _set_controller_idx(self, v, load=False):
    """
    Setter method for controller_idx, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_idx (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_controller_idx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_controller_idx() directly.

    YANG Description: Controller Index
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="controller-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """controller_idx must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="controller-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__controller_idx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_controller_idx(self):
    self.__controller_idx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="controller-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_controller_async_list(self):
    """
    Getter method for controller_async_list, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_async_list (list)
    """
    return self.__controller_async_list
      
  def _set_controller_async_list(self, v, load=False):
    """
    Setter method for controller_async_list, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_async_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_controller_async_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_controller_async_list() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("async_type",controller_async_list.controller_async_list, yang_name="controller-async-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='async-type', extensions={u'tailf-common': {u'callpoint': u'openflow-controller-async', u'cli-suppress-show-path': None}}), is_container='list', yang_name="controller-async-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-controller-async', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """controller_async_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("async_type",controller_async_list.controller_async_list, yang_name="controller-async-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='async-type', extensions={u'tailf-common': {u'callpoint': u'openflow-controller-async', u'cli-suppress-show-path': None}}), is_container='list', yang_name="controller-async-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-controller-async', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)""",
        })

    self.__controller_async_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_controller_async_list(self):
    self.__controller_async_list = YANGDynClass(base=YANGListType("async_type",controller_async_list.controller_async_list, yang_name="controller-async-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='async-type', extensions={u'tailf-common': {u'callpoint': u'openflow-controller-async', u'cli-suppress-show-path': None}}), is_container='list', yang_name="controller-async-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-controller-async', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)


  def _get_controller_info(self):
    """
    Getter method for controller_info, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info (container)
    """
    return self.__controller_info
      
  def _set_controller_info(self, v, load=False):
    """
    Setter method for controller_info, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_controller_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_controller_info() directly.
    """
    try:
      t = YANGDynClass(v,base=controller_info.controller_info, is_container='container', yang_name="controller-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-controller-controller-info-2'}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """controller_info must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=controller_info.controller_info, is_container='container', yang_name="controller-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-controller-controller-info-2'}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='container', is_config=False)""",
        })

    self.__controller_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_controller_info(self):
    self.__controller_info = YANGDynClass(base=controller_info.controller_info, is_container='container', yang_name="controller-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-controller-controller-info-2'}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='container', is_config=False)

  controller_idx = __builtin__.property(_get_controller_idx)
  controller_async_list = __builtin__.property(_get_controller_async_list)
  controller_info = __builtin__.property(_get_controller_info)


  _pyangbind_elements = {'controller_idx': controller_idx, 'controller_async_list': controller_async_list, 'controller_info': controller_info, }


