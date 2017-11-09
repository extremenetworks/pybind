
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import nh_info
class ipv4_route_entry(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/ipv4-routes/ipv4-route-entry. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: ISIS IPv4 Route Entry
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__level','__cost','__tag','__flags','__is_l1_summarized','__is_l2_summarized','__is_summary','__ipv4_dest_addr','__ipv4_subnet_mask','__ipv4_prefix_len','__nh_info',)

  _yang_name = 'ipv4-route-entry'
  _rest_name = 'ipv4-route-entry'

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
    self.__ipv4_dest_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipv4-dest-addr", rest_name="ipv4-dest-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__ipv4_prefix_len = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="ipv4-prefix-len", rest_name="ipv4-prefix-len", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='int8', is_config=False)
    self.__level = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="level", rest_name="level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint8', is_config=False)
    self.__tag = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__ipv4_subnet_mask = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipv4-subnet-mask", rest_name="ipv4-subnet-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__nh_info = YANGDynClass(base=YANGListType("outgoing_intf_type outgoing_intf_number",nh_info.nh_info, yang_name="nh-info", rest_name="nh-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='outgoing-intf-type outgoing-intf-number', extensions=None), is_container='list', yang_name="nh-info", rest_name="nh-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)
    self.__cost = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cost", rest_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__flags = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="flags", rest_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)
    self.__is_l2_summarized = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-l2-summarized", rest_name="is-l2-summarized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)
    self.__is_l1_summarized = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-l1-summarized", rest_name="is-l1-summarized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)
    self.__is_summary = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-summary", rest_name="is-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)

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
      return [u'isis-state', u'ipv4-routes', u'ipv4-route-entry']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isis-state', u'ipv4-routes', u'ipv4-route-entry']

  def _get_level(self):
    """
    Getter method for level, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/level (uint8)

    YANG Description: IS-IS Level
    """
    return self.__level
      
  def _set_level(self, v, load=False):
    """
    Setter method for level, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/level (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level() directly.

    YANG Description: IS-IS Level
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="level", rest_name="level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="level", rest_name="level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint8', is_config=False)""",
        })

    self.__level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level(self):
    self.__level = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="level", rest_name="level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint8', is_config=False)


  def _get_cost(self):
    """
    Getter method for cost, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/cost (uint32)

    YANG Description: IS-IS Interface Cost
    """
    return self.__cost
      
  def _set_cost(self, v, load=False):
    """
    Setter method for cost, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/cost (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cost is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cost() directly.

    YANG Description: IS-IS Interface Cost
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cost", rest_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cost must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cost", rest_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__cost = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cost(self):
    self.__cost = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cost", rest_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_tag(self):
    """
    Getter method for tag, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/tag (uint32)

    YANG Description: IS-IS Route Tag
    """
    return self.__tag
      
  def _set_tag(self, v, load=False):
    """
    Setter method for tag, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/tag (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tag() directly.

    YANG Description: IS-IS Route Tag
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tag must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tag(self):
    self.__tag = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_flags(self):
    """
    Getter method for flags, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/flags (uint16)

    YANG Description: Route Flags
    """
    return self.__flags
      
  def _set_flags(self, v, load=False):
    """
    Setter method for flags, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/flags (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flags() directly.

    YANG Description: Route Flags
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="flags", rest_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flags must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="flags", rest_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)""",
        })

    self.__flags = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flags(self):
    self.__flags = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="flags", rest_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint16', is_config=False)


  def _get_is_l1_summarized(self):
    """
    Getter method for is_l1_summarized, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/is_l1_summarized (boolean)

    YANG Description: L1 Summarized
    """
    return self.__is_l1_summarized
      
  def _set_is_l1_summarized(self, v, load=False):
    """
    Setter method for is_l1_summarized, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/is_l1_summarized (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_l1_summarized is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_l1_summarized() directly.

    YANG Description: L1 Summarized
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="is-l1-summarized", rest_name="is-l1-summarized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_l1_summarized must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-l1-summarized", rest_name="is-l1-summarized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)""",
        })

    self.__is_l1_summarized = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_l1_summarized(self):
    self.__is_l1_summarized = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-l1-summarized", rest_name="is-l1-summarized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)


  def _get_is_l2_summarized(self):
    """
    Getter method for is_l2_summarized, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/is_l2_summarized (boolean)

    YANG Description: L2 Summarized
    """
    return self.__is_l2_summarized
      
  def _set_is_l2_summarized(self, v, load=False):
    """
    Setter method for is_l2_summarized, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/is_l2_summarized (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_l2_summarized is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_l2_summarized() directly.

    YANG Description: L2 Summarized
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="is-l2-summarized", rest_name="is-l2-summarized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_l2_summarized must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-l2-summarized", rest_name="is-l2-summarized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)""",
        })

    self.__is_l2_summarized = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_l2_summarized(self):
    self.__is_l2_summarized = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-l2-summarized", rest_name="is-l2-summarized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)


  def _get_is_summary(self):
    """
    Getter method for is_summary, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/is_summary (boolean)

    YANG Description: Summary
    """
    return self.__is_summary
      
  def _set_is_summary(self, v, load=False):
    """
    Setter method for is_summary, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/is_summary (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_summary is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_summary() directly.

    YANG Description: Summary
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="is-summary", rest_name="is-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_summary must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-summary", rest_name="is-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)""",
        })

    self.__is_summary = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_summary(self):
    self.__is_summary = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-summary", rest_name="is-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)


  def _get_ipv4_dest_addr(self):
    """
    Getter method for ipv4_dest_addr, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/ipv4_dest_addr (inet:ipv4-address)

    YANG Description: Destination IPv4 Address 
    """
    return self.__ipv4_dest_addr
      
  def _set_ipv4_dest_addr(self, v, load=False):
    """
    Setter method for ipv4_dest_addr, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/ipv4_dest_addr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_dest_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_dest_addr() directly.

    YANG Description: Destination IPv4 Address 
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipv4-dest-addr", rest_name="ipv4-dest-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_dest_addr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipv4-dest-addr", rest_name="ipv4-dest-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__ipv4_dest_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_dest_addr(self):
    self.__ipv4_dest_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipv4-dest-addr", rest_name="ipv4-dest-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_ipv4_subnet_mask(self):
    """
    Getter method for ipv4_subnet_mask, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/ipv4_subnet_mask (inet:ipv4-address)

    YANG Description: Destination IPv4 Subnet Mask 
    """
    return self.__ipv4_subnet_mask
      
  def _set_ipv4_subnet_mask(self, v, load=False):
    """
    Setter method for ipv4_subnet_mask, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/ipv4_subnet_mask (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_subnet_mask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_subnet_mask() directly.

    YANG Description: Destination IPv4 Subnet Mask 
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipv4-subnet-mask", rest_name="ipv4-subnet-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_subnet_mask must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipv4-subnet-mask", rest_name="ipv4-subnet-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__ipv4_subnet_mask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_subnet_mask(self):
    self.__ipv4_subnet_mask = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipv4-subnet-mask", rest_name="ipv4-subnet-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_ipv4_prefix_len(self):
    """
    Getter method for ipv4_prefix_len, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/ipv4_prefix_len (int8)

    YANG Description: Destination IPv4 Prefix Length 
    """
    return self.__ipv4_prefix_len
      
  def _set_ipv4_prefix_len(self, v, load=False):
    """
    Setter method for ipv4_prefix_len, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/ipv4_prefix_len (int8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_prefix_len is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_prefix_len() directly.

    YANG Description: Destination IPv4 Prefix Length 
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="ipv4-prefix-len", rest_name="ipv4-prefix-len", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='int8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_prefix_len must be of a type compatible with int8""",
          'defined-type': "int8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="ipv4-prefix-len", rest_name="ipv4-prefix-len", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='int8', is_config=False)""",
        })

    self.__ipv4_prefix_len = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_prefix_len(self):
    self.__ipv4_prefix_len = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="ipv4-prefix-len", rest_name="ipv4-prefix-len", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='int8', is_config=False)


  def _get_nh_info(self):
    """
    Getter method for nh_info, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/nh_info (list)

    YANG Description: is-is route nexthop information
    """
    return self.__nh_info
      
  def _set_nh_info(self, v, load=False):
    """
    Setter method for nh_info, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/nh_info (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nh_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nh_info() directly.

    YANG Description: is-is route nexthop information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("outgoing_intf_type outgoing_intf_number",nh_info.nh_info, yang_name="nh-info", rest_name="nh-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='outgoing-intf-type outgoing-intf-number', extensions=None), is_container='list', yang_name="nh-info", rest_name="nh-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nh_info must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("outgoing_intf_type outgoing_intf_number",nh_info.nh_info, yang_name="nh-info", rest_name="nh-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='outgoing-intf-type outgoing-intf-number', extensions=None), is_container='list', yang_name="nh-info", rest_name="nh-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)""",
        })

    self.__nh_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nh_info(self):
    self.__nh_info = YANGDynClass(base=YANGListType("outgoing_intf_type outgoing_intf_number",nh_info.nh_info, yang_name="nh-info", rest_name="nh-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='outgoing-intf-type outgoing-intf-number', extensions=None), is_container='list', yang_name="nh-info", rest_name="nh-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)

  level = __builtin__.property(_get_level)
  cost = __builtin__.property(_get_cost)
  tag = __builtin__.property(_get_tag)
  flags = __builtin__.property(_get_flags)
  is_l1_summarized = __builtin__.property(_get_is_l1_summarized)
  is_l2_summarized = __builtin__.property(_get_is_l2_summarized)
  is_summary = __builtin__.property(_get_is_summary)
  ipv4_dest_addr = __builtin__.property(_get_ipv4_dest_addr)
  ipv4_subnet_mask = __builtin__.property(_get_ipv4_subnet_mask)
  ipv4_prefix_len = __builtin__.property(_get_ipv4_prefix_len)
  nh_info = __builtin__.property(_get_nh_info)


  _pyangbind_elements = {'level': level, 'cost': cost, 'tag': tag, 'flags': flags, 'is_l1_summarized': is_l1_summarized, 'is_l2_summarized': is_l2_summarized, 'is_summary': is_summary, 'ipv4_dest_addr': ipv4_dest_addr, 'ipv4_subnet_mask': ipv4_subnet_mask, 'ipv4_prefix_len': ipv4_prefix_len, 'nh_info': nh_info, }


