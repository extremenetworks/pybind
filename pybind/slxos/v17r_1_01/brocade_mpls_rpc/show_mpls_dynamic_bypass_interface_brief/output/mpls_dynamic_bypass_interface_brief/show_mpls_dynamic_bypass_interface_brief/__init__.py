
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class show_mpls_dynamic_bypass_interface_brief(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-dynamic-bypass-interface-brief/output/mpls-dynamic-bypass-interface-brief/show-mpls-dynamic-bypass-interface-brief. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dbyp_interface_name','__dbyp_interface_active_status','__dbyp_interface_admin_type','__dbyp_interface_admin_status','__dbyp_interface_count','__dbyp_interface_merge_point',)

  _yang_name = 'show-mpls-dynamic-bypass-interface-brief'
  _rest_name = 'show-mpls-dynamic-bypass-interface-brief'

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
    self.__dbyp_interface_admin_status = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="dbyp-interface-admin-status", rest_name="dbyp-interface-admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    self.__dbyp_interface_merge_point = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dbyp-interface-merge-point", rest_name="dbyp-interface-merge-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__dbyp_interface_count = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dbyp-interface-count", rest_name="dbyp-interface-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint16', is_config=True)
    self.__dbyp_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="dbyp-interface-name", rest_name="dbyp-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__dbyp_interface_admin_type = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="dbyp-interface-admin-type", rest_name="dbyp-interface-admin-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    self.__dbyp_interface_active_status = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="dbyp-interface-active-status", rest_name="dbyp-interface-active-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-dynamic-bypass-interface-brief', u'output', u'mpls-dynamic-bypass-interface-brief', u'show-mpls-dynamic-bypass-interface-brief']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-dynamic-bypass-interface-brief', u'output', u'mpls-dynamic-bypass-interface-brief', u'show-mpls-dynamic-bypass-interface-brief']

  def _get_dbyp_interface_name(self):
    """
    Getter method for dbyp_interface_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_dynamic_bypass_interface_brief/output/mpls_dynamic_bypass_interface_brief/show_mpls_dynamic_bypass_interface_brief/dbyp_interface_name (string)

    YANG Description: Dynamic Bypass Interface name
    """
    return self.__dbyp_interface_name
      
  def _set_dbyp_interface_name(self, v, load=False):
    """
    Setter method for dbyp_interface_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_dynamic_bypass_interface_brief/output/mpls_dynamic_bypass_interface_brief/show_mpls_dynamic_bypass_interface_brief/dbyp_interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dbyp_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dbyp_interface_name() directly.

    YANG Description: Dynamic Bypass Interface name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="dbyp-interface-name", rest_name="dbyp-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dbyp_interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="dbyp-interface-name", rest_name="dbyp-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__dbyp_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dbyp_interface_name(self):
    self.__dbyp_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="dbyp-interface-name", rest_name="dbyp-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_dbyp_interface_active_status(self):
    """
    Getter method for dbyp_interface_active_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_dynamic_bypass_interface_brief/output/mpls_dynamic_bypass_interface_brief/show_mpls_dynamic_bypass_interface_brief/dbyp_interface_active_status (uint8)

    YANG Description: Active status for the dynamic bypass interface
    """
    return self.__dbyp_interface_active_status
      
  def _set_dbyp_interface_active_status(self, v, load=False):
    """
    Setter method for dbyp_interface_active_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_dynamic_bypass_interface_brief/output/mpls_dynamic_bypass_interface_brief/show_mpls_dynamic_bypass_interface_brief/dbyp_interface_active_status (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dbyp_interface_active_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dbyp_interface_active_status() directly.

    YANG Description: Active status for the dynamic bypass interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="dbyp-interface-active-status", rest_name="dbyp-interface-active-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dbyp_interface_active_status must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="dbyp-interface-active-status", rest_name="dbyp-interface-active-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)""",
        })

    self.__dbyp_interface_active_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dbyp_interface_active_status(self):
    self.__dbyp_interface_active_status = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="dbyp-interface-active-status", rest_name="dbyp-interface-active-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)


  def _get_dbyp_interface_admin_type(self):
    """
    Getter method for dbyp_interface_admin_type, mapped from YANG variable /brocade_mpls_rpc/show_mpls_dynamic_bypass_interface_brief/output/mpls_dynamic_bypass_interface_brief/show_mpls_dynamic_bypass_interface_brief/dbyp_interface_admin_type (uint8)

    YANG Description: Admin type of the dynamic bypass interface
    """
    return self.__dbyp_interface_admin_type
      
  def _set_dbyp_interface_admin_type(self, v, load=False):
    """
    Setter method for dbyp_interface_admin_type, mapped from YANG variable /brocade_mpls_rpc/show_mpls_dynamic_bypass_interface_brief/output/mpls_dynamic_bypass_interface_brief/show_mpls_dynamic_bypass_interface_brief/dbyp_interface_admin_type (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dbyp_interface_admin_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dbyp_interface_admin_type() directly.

    YANG Description: Admin type of the dynamic bypass interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="dbyp-interface-admin-type", rest_name="dbyp-interface-admin-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dbyp_interface_admin_type must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="dbyp-interface-admin-type", rest_name="dbyp-interface-admin-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)""",
        })

    self.__dbyp_interface_admin_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dbyp_interface_admin_type(self):
    self.__dbyp_interface_admin_type = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="dbyp-interface-admin-type", rest_name="dbyp-interface-admin-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)


  def _get_dbyp_interface_admin_status(self):
    """
    Getter method for dbyp_interface_admin_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_dynamic_bypass_interface_brief/output/mpls_dynamic_bypass_interface_brief/show_mpls_dynamic_bypass_interface_brief/dbyp_interface_admin_status (uint8)

    YANG Description: Admin status of the dynamic bypass interface
    """
    return self.__dbyp_interface_admin_status
      
  def _set_dbyp_interface_admin_status(self, v, load=False):
    """
    Setter method for dbyp_interface_admin_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_dynamic_bypass_interface_brief/output/mpls_dynamic_bypass_interface_brief/show_mpls_dynamic_bypass_interface_brief/dbyp_interface_admin_status (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dbyp_interface_admin_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dbyp_interface_admin_status() directly.

    YANG Description: Admin status of the dynamic bypass interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="dbyp-interface-admin-status", rest_name="dbyp-interface-admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dbyp_interface_admin_status must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="dbyp-interface-admin-status", rest_name="dbyp-interface-admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)""",
        })

    self.__dbyp_interface_admin_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dbyp_interface_admin_status(self):
    self.__dbyp_interface_admin_status = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="dbyp-interface-admin-status", rest_name="dbyp-interface-admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)


  def _get_dbyp_interface_count(self):
    """
    Getter method for dbyp_interface_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_dynamic_bypass_interface_brief/output/mpls_dynamic_bypass_interface_brief/show_mpls_dynamic_bypass_interface_brief/dbyp_interface_count (uint16)

    YANG Description: Dynamic bypass count of the interface
    """
    return self.__dbyp_interface_count
      
  def _set_dbyp_interface_count(self, v, load=False):
    """
    Setter method for dbyp_interface_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_dynamic_bypass_interface_brief/output/mpls_dynamic_bypass_interface_brief/show_mpls_dynamic_bypass_interface_brief/dbyp_interface_count (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dbyp_interface_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dbyp_interface_count() directly.

    YANG Description: Dynamic bypass count of the interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dbyp-interface-count", rest_name="dbyp-interface-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dbyp_interface_count must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dbyp-interface-count", rest_name="dbyp-interface-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint16', is_config=True)""",
        })

    self.__dbyp_interface_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dbyp_interface_count(self):
    self.__dbyp_interface_count = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dbyp-interface-count", rest_name="dbyp-interface-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint16', is_config=True)


  def _get_dbyp_interface_merge_point(self):
    """
    Getter method for dbyp_interface_merge_point, mapped from YANG variable /brocade_mpls_rpc/show_mpls_dynamic_bypass_interface_brief/output/mpls_dynamic_bypass_interface_brief/show_mpls_dynamic_bypass_interface_brief/dbyp_interface_merge_point (uint32)

    YANG Description: Dynamic Bypass merge point count of the interface
    """
    return self.__dbyp_interface_merge_point
      
  def _set_dbyp_interface_merge_point(self, v, load=False):
    """
    Setter method for dbyp_interface_merge_point, mapped from YANG variable /brocade_mpls_rpc/show_mpls_dynamic_bypass_interface_brief/output/mpls_dynamic_bypass_interface_brief/show_mpls_dynamic_bypass_interface_brief/dbyp_interface_merge_point (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dbyp_interface_merge_point is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dbyp_interface_merge_point() directly.

    YANG Description: Dynamic Bypass merge point count of the interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dbyp-interface-merge-point", rest_name="dbyp-interface-merge-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dbyp_interface_merge_point must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dbyp-interface-merge-point", rest_name="dbyp-interface-merge-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__dbyp_interface_merge_point = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dbyp_interface_merge_point(self):
    self.__dbyp_interface_merge_point = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dbyp-interface-merge-point", rest_name="dbyp-interface-merge-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  dbyp_interface_name = __builtin__.property(_get_dbyp_interface_name, _set_dbyp_interface_name)
  dbyp_interface_active_status = __builtin__.property(_get_dbyp_interface_active_status, _set_dbyp_interface_active_status)
  dbyp_interface_admin_type = __builtin__.property(_get_dbyp_interface_admin_type, _set_dbyp_interface_admin_type)
  dbyp_interface_admin_status = __builtin__.property(_get_dbyp_interface_admin_status, _set_dbyp_interface_admin_status)
  dbyp_interface_count = __builtin__.property(_get_dbyp_interface_count, _set_dbyp_interface_count)
  dbyp_interface_merge_point = __builtin__.property(_get_dbyp_interface_merge_point, _set_dbyp_interface_merge_point)


  _pyangbind_elements = {'dbyp_interface_name': dbyp_interface_name, 'dbyp_interface_active_status': dbyp_interface_active_status, 'dbyp_interface_admin_type': dbyp_interface_admin_type, 'dbyp_interface_admin_status': dbyp_interface_admin_status, 'dbyp_interface_count': dbyp_interface_count, 'dbyp_interface_merge_point': dbyp_interface_merge_point, }

