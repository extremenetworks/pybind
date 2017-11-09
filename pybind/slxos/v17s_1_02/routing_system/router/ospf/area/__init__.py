
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import nssa
import stub
import range
import prefix_list
import virtual_link
class area(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/ospf/area. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__area_id','__normal','__nssa','__stub','__range','__prefix_list','__virtual_link',)

  _yang_name = 'area'
  _rest_name = 'area'

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
    self.__area_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(([0-9])|([1-9]([0-9]{1,8}))|([1]([0-9]{1,9}))|([2][0]([0-9]{1,8}))|([2][1][0-3]([0-9]{1,7}))|([2][1][4][0-6]([0-9]{1,6}))|([2][1][4][7][0-3]([0-9]{1,5}))|([2][1][4][7][4][0-7]([0-9]{1,4}))|([2][1][4][7][4][8][0-2]([0-9]{1,3}))|([2][1][4][7][4][8][3][0-5]([0-9]{1,2}))|([2][1][4][7][4][8][3][6][0-3][0-9])|([2][1][4][7][4][8][3][6][4][0-7]))'}), is_leaf=True, yang_name="area-id", rest_name="area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-area-id', is_config=True)
    self.__normal = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="normal", rest_name="normal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    self.__nssa = YANGDynClass(base=nssa.nssa, is_container='container', presence=False, yang_name="nssa", rest_name="nssa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__stub = YANGDynClass(base=stub.stub, is_container='container', presence=False, yang_name="stub", rest_name="stub", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__range = YANGDynClass(base=YANGListType("range_address range_mask",range.range, yang_name="range", rest_name="range", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range-address range-mask', extensions=None), is_container='list', yang_name="range", rest_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)
    self.__virtual_link = YANGDynClass(base=YANGListType("virt_link_neighbor",virtual_link.virtual_link, yang_name="virtual-link", rest_name="virtual-link", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='virt-link-neighbor', extensions=None), is_container='list', yang_name="virtual-link", rest_name="virtual-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)
    self.__prefix_list = YANGDynClass(base=prefix_list.prefix_list, is_container='container', presence=False, yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'ospf', u'area']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'routing-system', u'router', u'ospf', u'area']

  def _get_area_id(self):
    """
    Getter method for area_id, mapped from YANG variable /routing_system/router/ospf/area/area_id (ospf-area-id)
    """
    return self.__area_id
      
  def _set_area_id(self, v, load=False):
    """
    Setter method for area_id, mapped from YANG variable /routing_system/router/ospf/area/area_id (ospf-area-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_area_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_area_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(([0-9])|([1-9]([0-9]{1,8}))|([1]([0-9]{1,9}))|([2][0]([0-9]{1,8}))|([2][1][0-3]([0-9]{1,7}))|([2][1][4][0-6]([0-9]{1,6}))|([2][1][4][7][0-3]([0-9]{1,5}))|([2][1][4][7][4][0-7]([0-9]{1,4}))|([2][1][4][7][4][8][0-2]([0-9]{1,3}))|([2][1][4][7][4][8][3][0-5]([0-9]{1,2}))|([2][1][4][7][4][8][3][6][0-3][0-9])|([2][1][4][7][4][8][3][6][4][0-7]))'}), is_leaf=True, yang_name="area-id", rest_name="area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-area-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """area_id must be of a type compatible with ospf-area-id""",
          'defined-type': "brocade-ospf:ospf-area-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(([0-9])|([1-9]([0-9]{1,8}))|([1]([0-9]{1,9}))|([2][0]([0-9]{1,8}))|([2][1][0-3]([0-9]{1,7}))|([2][1][4][0-6]([0-9]{1,6}))|([2][1][4][7][0-3]([0-9]{1,5}))|([2][1][4][7][4][0-7]([0-9]{1,4}))|([2][1][4][7][4][8][0-2]([0-9]{1,3}))|([2][1][4][7][4][8][3][0-5]([0-9]{1,2}))|([2][1][4][7][4][8][3][6][0-3][0-9])|([2][1][4][7][4][8][3][6][4][0-7]))'}), is_leaf=True, yang_name="area-id", rest_name="area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-area-id', is_config=True)""",
        })

    self.__area_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_area_id(self):
    self.__area_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(([0-9])|([1-9]([0-9]{1,8}))|([1]([0-9]{1,9}))|([2][0]([0-9]{1,8}))|([2][1][0-3]([0-9]{1,7}))|([2][1][4][0-6]([0-9]{1,6}))|([2][1][4][7][0-3]([0-9]{1,5}))|([2][1][4][7][4][0-7]([0-9]{1,4}))|([2][1][4][7][4][8][0-2]([0-9]{1,3}))|([2][1][4][7][4][8][3][0-5]([0-9]{1,2}))|([2][1][4][7][4][8][3][6][0-3][0-9])|([2][1][4][7][4][8][3][6][4][0-7]))'}), is_leaf=True, yang_name="area-id", rest_name="area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-area-id', is_config=True)


  def _get_normal(self):
    """
    Getter method for normal, mapped from YANG variable /routing_system/router/ospf/area/normal (empty)
    """
    return self.__normal
      
  def _set_normal(self, v, load=False):
    """
    Setter method for normal, mapped from YANG variable /routing_system/router/ospf/area/normal (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_normal is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_normal() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="normal", rest_name="normal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """normal must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="normal", rest_name="normal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__normal = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_normal(self):
    self.__normal = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="normal", rest_name="normal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)


  def _get_nssa(self):
    """
    Getter method for nssa, mapped from YANG variable /routing_system/router/ospf/area/nssa (container)
    """
    return self.__nssa
      
  def _set_nssa(self, v, load=False):
    """
    Setter method for nssa, mapped from YANG variable /routing_system/router/ospf/area/nssa (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nssa is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nssa() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=nssa.nssa, is_container='container', presence=False, yang_name="nssa", rest_name="nssa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nssa must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=nssa.nssa, is_container='container', presence=False, yang_name="nssa", rest_name="nssa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__nssa = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nssa(self):
    self.__nssa = YANGDynClass(base=nssa.nssa, is_container='container', presence=False, yang_name="nssa", rest_name="nssa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_stub(self):
    """
    Getter method for stub, mapped from YANG variable /routing_system/router/ospf/area/stub (container)
    """
    return self.__stub
      
  def _set_stub(self, v, load=False):
    """
    Setter method for stub, mapped from YANG variable /routing_system/router/ospf/area/stub (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_stub is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_stub() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=stub.stub, is_container='container', presence=False, yang_name="stub", rest_name="stub", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """stub must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=stub.stub, is_container='container', presence=False, yang_name="stub", rest_name="stub", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__stub = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_stub(self):
    self.__stub = YANGDynClass(base=stub.stub, is_container='container', presence=False, yang_name="stub", rest_name="stub", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_range(self):
    """
    Getter method for range, mapped from YANG variable /routing_system/router/ospf/area/range (list)
    """
    return self.__range
      
  def _set_range(self, v, load=False):
    """
    Setter method for range, mapped from YANG variable /routing_system/router/ospf/area/range (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_range is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_range() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("range_address range_mask",range.range, yang_name="range", rest_name="range", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range-address range-mask', extensions=None), is_container='list', yang_name="range", rest_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """range must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("range_address range_mask",range.range, yang_name="range", rest_name="range", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range-address range-mask', extensions=None), is_container='list', yang_name="range", rest_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)""",
        })

    self.__range = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_range(self):
    self.__range = YANGDynClass(base=YANGListType("range_address range_mask",range.range, yang_name="range", rest_name="range", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range-address range-mask', extensions=None), is_container='list', yang_name="range", rest_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)


  def _get_prefix_list(self):
    """
    Getter method for prefix_list, mapped from YANG variable /routing_system/router/ospf/area/prefix_list (container)

    YANG Description: either prefix list or distribution-list
    """
    return self.__prefix_list
      
  def _set_prefix_list(self, v, load=False):
    """
    Setter method for prefix_list, mapped from YANG variable /routing_system/router/ospf/area/prefix_list (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_list() directly.

    YANG Description: either prefix list or distribution-list
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=prefix_list.prefix_list, is_container='container', presence=False, yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_list must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=prefix_list.prefix_list, is_container='container', presence=False, yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__prefix_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_list(self):
    self.__prefix_list = YANGDynClass(base=prefix_list.prefix_list, is_container='container', presence=False, yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_virtual_link(self):
    """
    Getter method for virtual_link, mapped from YANG variable /routing_system/router/ospf/area/virtual_link (list)
    """
    return self.__virtual_link
      
  def _set_virtual_link(self, v, load=False):
    """
    Setter method for virtual_link, mapped from YANG variable /routing_system/router/ospf/area/virtual_link (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_link is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_link() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("virt_link_neighbor",virtual_link.virtual_link, yang_name="virtual-link", rest_name="virtual-link", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='virt-link-neighbor', extensions=None), is_container='list', yang_name="virtual-link", rest_name="virtual-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_link must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("virt_link_neighbor",virtual_link.virtual_link, yang_name="virtual-link", rest_name="virtual-link", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='virt-link-neighbor', extensions=None), is_container='list', yang_name="virtual-link", rest_name="virtual-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)""",
        })

    self.__virtual_link = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_link(self):
    self.__virtual_link = YANGDynClass(base=YANGListType("virt_link_neighbor",virtual_link.virtual_link, yang_name="virtual-link", rest_name="virtual-link", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='virt-link-neighbor', extensions=None), is_container='list', yang_name="virtual-link", rest_name="virtual-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)

  area_id = __builtin__.property(_get_area_id, _set_area_id)
  normal = __builtin__.property(_get_normal, _set_normal)
  nssa = __builtin__.property(_get_nssa, _set_nssa)
  stub = __builtin__.property(_get_stub, _set_stub)
  range = __builtin__.property(_get_range, _set_range)
  prefix_list = __builtin__.property(_get_prefix_list, _set_prefix_list)
  virtual_link = __builtin__.property(_get_virtual_link, _set_virtual_link)


  _pyangbind_elements = {'area_id': area_id, 'normal': normal, 'nssa': nssa, 'stub': stub, 'range': range, 'prefix_list': prefix_list, 'virtual_link': virtual_link, }


