
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class pim_ecmp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-pim-operational - based on the path /pim-ecmp-state/pim-ecmp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Pim Load Sharing
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vrf_name','__src_ip','__rp_addr','__upstream_nbr','__interface_name','__interface_count',)

  _yang_name = 'pim-ecmp'
  _rest_name = 'pim-ecmp'

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
    self.__upstream_nbr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="upstream-nbr", rest_name="upstream-nbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__interface_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="interface-count", rest_name="interface-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='uint32', is_config=False)
    self.__rp_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="rp-addr", rest_name="rp-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__src_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-ip", rest_name="src-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__vrf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)

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
      return [u'pim-ecmp-state', u'pim-ecmp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'pim-ecmp-state', u'pim-ecmp']

  def _get_vrf_name(self):
    """
    Getter method for vrf_name, mapped from YANG variable /pim_ecmp_state/pim_ecmp/vrf_name (string)

    YANG Description: vrf name
    """
    return self.__vrf_name
      
  def _set_vrf_name(self, v, load=False):
    """
    Setter method for vrf_name, mapped from YANG variable /pim_ecmp_state/pim_ecmp/vrf_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf_name() directly.

    YANG Description: vrf name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)""",
        })

    self.__vrf_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf_name(self):
    self.__vrf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)


  def _get_src_ip(self):
    """
    Getter method for src_ip, mapped from YANG variable /pim_ecmp_state/pim_ecmp/src_ip (inet:ipv4-address)

    YANG Description: source ip address
    """
    return self.__src_ip
      
  def _set_src_ip(self, v, load=False):
    """
    Setter method for src_ip, mapped from YANG variable /pim_ecmp_state/pim_ecmp/src_ip (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_ip() directly.

    YANG Description: source ip address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-ip", rest_name="src-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_ip must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-ip", rest_name="src-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__src_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_ip(self):
    self.__src_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-ip", rest_name="src-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_rp_addr(self):
    """
    Getter method for rp_addr, mapped from YANG variable /pim_ecmp_state/pim_ecmp/rp_addr (inet:ipv4-address)

    YANG Description: Rp ip address
    """
    return self.__rp_addr
      
  def _set_rp_addr(self, v, load=False):
    """
    Setter method for rp_addr, mapped from YANG variable /pim_ecmp_state/pim_ecmp/rp_addr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rp_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rp_addr() directly.

    YANG Description: Rp ip address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="rp-addr", rest_name="rp-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rp_addr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="rp-addr", rest_name="rp-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__rp_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rp_addr(self):
    self.__rp_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="rp-addr", rest_name="rp-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_upstream_nbr(self):
    """
    Getter method for upstream_nbr, mapped from YANG variable /pim_ecmp_state/pim_ecmp/upstream_nbr (inet:ipv4-address)

    YANG Description: upstream neighbour ip adderess
    """
    return self.__upstream_nbr
      
  def _set_upstream_nbr(self, v, load=False):
    """
    Setter method for upstream_nbr, mapped from YANG variable /pim_ecmp_state/pim_ecmp/upstream_nbr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_upstream_nbr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_upstream_nbr() directly.

    YANG Description: upstream neighbour ip adderess
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="upstream-nbr", rest_name="upstream-nbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """upstream_nbr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="upstream-nbr", rest_name="upstream-nbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__upstream_nbr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_upstream_nbr(self):
    self.__upstream_nbr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="upstream-nbr", rest_name="upstream-nbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /pim_ecmp_state/pim_ecmp/interface_name (string)

    YANG Description: interface name
    """
    return self.__interface_name
      
  def _set_interface_name(self, v, load=False):
    """
    Setter method for interface_name, mapped from YANG variable /pim_ecmp_state/pim_ecmp/interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.

    YANG Description: interface name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)


  def _get_interface_count(self):
    """
    Getter method for interface_count, mapped from YANG variable /pim_ecmp_state/pim_ecmp/interface_count (uint32)

    YANG Description: Interface Count
    """
    return self.__interface_count
      
  def _set_interface_count(self, v, load=False):
    """
    Setter method for interface_count, mapped from YANG variable /pim_ecmp_state/pim_ecmp/interface_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_count() directly.

    YANG Description: Interface Count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="interface-count", rest_name="interface-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="interface-count", rest_name="interface-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='uint32', is_config=False)""",
        })

    self.__interface_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_count(self):
    self.__interface_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="interface-count", rest_name="interface-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='uint32', is_config=False)

  vrf_name = __builtin__.property(_get_vrf_name)
  src_ip = __builtin__.property(_get_src_ip)
  rp_addr = __builtin__.property(_get_rp_addr)
  upstream_nbr = __builtin__.property(_get_upstream_nbr)
  interface_name = __builtin__.property(_get_interface_name)
  interface_count = __builtin__.property(_get_interface_count)


  _pyangbind_elements = {'vrf_name': vrf_name, 'src_ip': src_ip, 'rp_addr': rp_addr, 'upstream_nbr': upstream_nbr, 'interface_name': interface_name, 'interface_count': interface_count, }

