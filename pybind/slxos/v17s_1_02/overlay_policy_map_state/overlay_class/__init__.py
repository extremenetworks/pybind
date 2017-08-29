
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class overlay_class(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ssm-operational - based on the path /overlay-policy-map-state/overlay-class. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Overlay Class
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__seq_id','__overlay_class_name','__mac_acl_name','__ip_acl_name','__ipv6_acl_name','__service_policy_name',)

  _yang_name = 'overlay-class'
  _rest_name = 'overlay-class'

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
    self.__ip_acl_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-acl-name", rest_name="ip-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    self.__seq_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="seq-id", rest_name="seq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint32', is_config=False)
    self.__service_policy_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="service-policy-name", rest_name="service-policy-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    self.__overlay_class_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="overlay-class-name", rest_name="overlay-class-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    self.__ipv6_acl_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="ipv6-acl-name", rest_name="ipv6-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    self.__mac_acl_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-acl-name", rest_name="mac-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)

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
      return [u'overlay-policy-map-state', u'overlay-class']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-policy-map-state', u'overlay-class']

  def _get_seq_id(self):
    """
    Getter method for seq_id, mapped from YANG variable /overlay_policy_map_state/overlay_class/seq_id (uint32)

    YANG Description: Sequence Id
    """
    return self.__seq_id
      
  def _set_seq_id(self, v, load=False):
    """
    Setter method for seq_id, mapped from YANG variable /overlay_policy_map_state/overlay_class/seq_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_seq_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_seq_id() directly.

    YANG Description: Sequence Id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="seq-id", rest_name="seq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """seq_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="seq-id", rest_name="seq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__seq_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_seq_id(self):
    self.__seq_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="seq-id", rest_name="seq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint32', is_config=False)


  def _get_overlay_class_name(self):
    """
    Getter method for overlay_class_name, mapped from YANG variable /overlay_policy_map_state/overlay_class/overlay_class_name (string)

    YANG Description: Overlay Class name
    """
    return self.__overlay_class_name
      
  def _set_overlay_class_name(self, v, load=False):
    """
    Setter method for overlay_class_name, mapped from YANG variable /overlay_policy_map_state/overlay_class/overlay_class_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_overlay_class_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_overlay_class_name() directly.

    YANG Description: Overlay Class name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="overlay-class-name", rest_name="overlay-class-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """overlay_class_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="overlay-class-name", rest_name="overlay-class-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)""",
        })

    self.__overlay_class_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_overlay_class_name(self):
    self.__overlay_class_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="overlay-class-name", rest_name="overlay-class-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)


  def _get_mac_acl_name(self):
    """
    Getter method for mac_acl_name, mapped from YANG variable /overlay_policy_map_state/overlay_class/mac_acl_name (string)

    YANG Description: Mac Access List name
    """
    return self.__mac_acl_name
      
  def _set_mac_acl_name(self, v, load=False):
    """
    Setter method for mac_acl_name, mapped from YANG variable /overlay_policy_map_state/overlay_class/mac_acl_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_acl_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_acl_name() directly.

    YANG Description: Mac Access List name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mac-acl-name", rest_name="mac-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_acl_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-acl-name", rest_name="mac-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)""",
        })

    self.__mac_acl_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_acl_name(self):
    self.__mac_acl_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-acl-name", rest_name="mac-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)


  def _get_ip_acl_name(self):
    """
    Getter method for ip_acl_name, mapped from YANG variable /overlay_policy_map_state/overlay_class/ip_acl_name (string)

    YANG Description: IP Access List name
    """
    return self.__ip_acl_name
      
  def _set_ip_acl_name(self, v, load=False):
    """
    Setter method for ip_acl_name, mapped from YANG variable /overlay_policy_map_state/overlay_class/ip_acl_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_acl_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_acl_name() directly.

    YANG Description: IP Access List name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ip-acl-name", rest_name="ip-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_acl_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-acl-name", rest_name="ip-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)""",
        })

    self.__ip_acl_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_acl_name(self):
    self.__ip_acl_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-acl-name", rest_name="ip-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)


  def _get_ipv6_acl_name(self):
    """
    Getter method for ipv6_acl_name, mapped from YANG variable /overlay_policy_map_state/overlay_class/ipv6_acl_name (string)

    YANG Description: IPv6 Access List name
    """
    return self.__ipv6_acl_name
      
  def _set_ipv6_acl_name(self, v, load=False):
    """
    Setter method for ipv6_acl_name, mapped from YANG variable /overlay_policy_map_state/overlay_class/ipv6_acl_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_acl_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_acl_name() directly.

    YANG Description: IPv6 Access List name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ipv6-acl-name", rest_name="ipv6-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_acl_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ipv6-acl-name", rest_name="ipv6-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)""",
        })

    self.__ipv6_acl_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_acl_name(self):
    self.__ipv6_acl_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="ipv6-acl-name", rest_name="ipv6-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)


  def _get_service_policy_name(self):
    """
    Getter method for service_policy_name, mapped from YANG variable /overlay_policy_map_state/overlay_class/service_policy_name (string)

    YANG Description: Service Policy name
    """
    return self.__service_policy_name
      
  def _set_service_policy_name(self, v, load=False):
    """
    Setter method for service_policy_name, mapped from YANG variable /overlay_policy_map_state/overlay_class/service_policy_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_service_policy_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_service_policy_name() directly.

    YANG Description: Service Policy name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="service-policy-name", rest_name="service-policy-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """service_policy_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="service-policy-name", rest_name="service-policy-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)""",
        })

    self.__service_policy_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_service_policy_name(self):
    self.__service_policy_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="service-policy-name", rest_name="service-policy-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)

  seq_id = __builtin__.property(_get_seq_id)
  overlay_class_name = __builtin__.property(_get_overlay_class_name)
  mac_acl_name = __builtin__.property(_get_mac_acl_name)
  ip_acl_name = __builtin__.property(_get_ip_acl_name)
  ipv6_acl_name = __builtin__.property(_get_ipv6_acl_name)
  service_policy_name = __builtin__.property(_get_service_policy_name)


  _pyangbind_elements = {'seq_id': seq_id, 'overlay_class_name': overlay_class_name, 'mac_acl_name': mac_acl_name, 'ip_acl_name': ip_acl_name, 'ipv6_acl_name': ipv6_acl_name, 'service_policy_name': service_policy_name, }


