
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vc_proto_tnnl(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-pwm-operational - based on the path /bd-vc-peer-state/bd-vc-peer-data/vc-proto-tnnl. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: VC proto tnnl
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__vc_proto_name','__vc_ldp_tunnel_id','__vc_ldp_name','__vc_lsp_name','__vc_peer_lsp_cos_enabled','__vc_peer_lsp_cos_value',)

  _yang_name = 'vc-proto-tnnl'

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
    self.__vc_peer_lsp_cos_enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vc-peer-lsp-cos-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='boolean', is_config=False)
    self.__vc_ldp_tunnel_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vc-ldp-tunnel-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint32', is_config=False)
    self.__vc_lsp_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vc-lsp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)
    self.__vc_peer_lsp_cos_value = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="vc-peer-lsp-cos-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint8', is_config=False)
    self.__vc_proto_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vc-proto-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)
    self.__vc_ldp_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vc-ldp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)

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
      return [u'bd-vc-peer-state', u'bd-vc-peer-data', u'vc-proto-tnnl']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'bd-vc-peer-state', u'bd-vc-peer-data', u'vc-proto-tnnl']

  def _get_vc_proto_name(self):
    """
    Getter method for vc_proto_name, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_proto_tnnl/vc_proto_name (string)

    YANG Description: protocol name
    """
    return self.__vc_proto_name
      
  def _set_vc_proto_name(self, v, load=False):
    """
    Setter method for vc_proto_name, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_proto_tnnl/vc_proto_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vc_proto_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vc_proto_name() directly.

    YANG Description: protocol name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vc-proto-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vc_proto_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vc-proto-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)""",
        })

    self.__vc_proto_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vc_proto_name(self):
    self.__vc_proto_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vc-proto-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)


  def _get_vc_ldp_tunnel_id(self):
    """
    Getter method for vc_ldp_tunnel_id, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_proto_tnnl/vc_ldp_tunnel_id (uint32)

    YANG Description: protocol ldp tunnel id
    """
    return self.__vc_ldp_tunnel_id
      
  def _set_vc_ldp_tunnel_id(self, v, load=False):
    """
    Setter method for vc_ldp_tunnel_id, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_proto_tnnl/vc_ldp_tunnel_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vc_ldp_tunnel_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vc_ldp_tunnel_id() directly.

    YANG Description: protocol ldp tunnel id
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vc-ldp-tunnel-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vc_ldp_tunnel_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vc-ldp-tunnel-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__vc_ldp_tunnel_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vc_ldp_tunnel_id(self):
    self.__vc_ldp_tunnel_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vc-ldp-tunnel-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint32', is_config=False)


  def _get_vc_ldp_name(self):
    """
    Getter method for vc_ldp_name, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_proto_tnnl/vc_ldp_name (string)

    YANG Description: ldp name
    """
    return self.__vc_ldp_name
      
  def _set_vc_ldp_name(self, v, load=False):
    """
    Setter method for vc_ldp_name, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_proto_tnnl/vc_ldp_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vc_ldp_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vc_ldp_name() directly.

    YANG Description: ldp name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vc-ldp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vc_ldp_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vc-ldp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)""",
        })

    self.__vc_ldp_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vc_ldp_name(self):
    self.__vc_ldp_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vc-ldp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)


  def _get_vc_lsp_name(self):
    """
    Getter method for vc_lsp_name, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_proto_tnnl/vc_lsp_name (string)

    YANG Description: lsp name
    """
    return self.__vc_lsp_name
      
  def _set_vc_lsp_name(self, v, load=False):
    """
    Setter method for vc_lsp_name, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_proto_tnnl/vc_lsp_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vc_lsp_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vc_lsp_name() directly.

    YANG Description: lsp name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vc-lsp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vc_lsp_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vc-lsp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)""",
        })

    self.__vc_lsp_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vc_lsp_name(self):
    self.__vc_lsp_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vc-lsp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)


  def _get_vc_peer_lsp_cos_enabled(self):
    """
    Getter method for vc_peer_lsp_cos_enabled, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_proto_tnnl/vc_peer_lsp_cos_enabled (boolean)

    YANG Description: peer cos enabled
    """
    return self.__vc_peer_lsp_cos_enabled
      
  def _set_vc_peer_lsp_cos_enabled(self, v, load=False):
    """
    Setter method for vc_peer_lsp_cos_enabled, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_proto_tnnl/vc_peer_lsp_cos_enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vc_peer_lsp_cos_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vc_peer_lsp_cos_enabled() directly.

    YANG Description: peer cos enabled
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="vc-peer-lsp-cos-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vc_peer_lsp_cos_enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vc-peer-lsp-cos-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='boolean', is_config=False)""",
        })

    self.__vc_peer_lsp_cos_enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vc_peer_lsp_cos_enabled(self):
    self.__vc_peer_lsp_cos_enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vc-peer-lsp-cos-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='boolean', is_config=False)


  def _get_vc_peer_lsp_cos_value(self):
    """
    Getter method for vc_peer_lsp_cos_value, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_proto_tnnl/vc_peer_lsp_cos_value (uint8)

    YANG Description: peer cos value
    """
    return self.__vc_peer_lsp_cos_value
      
  def _set_vc_peer_lsp_cos_value(self, v, load=False):
    """
    Setter method for vc_peer_lsp_cos_value, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_proto_tnnl/vc_peer_lsp_cos_value (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vc_peer_lsp_cos_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vc_peer_lsp_cos_value() directly.

    YANG Description: peer cos value
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="vc-peer-lsp-cos-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vc_peer_lsp_cos_value must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="vc-peer-lsp-cos-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint8', is_config=False)""",
        })

    self.__vc_peer_lsp_cos_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vc_peer_lsp_cos_value(self):
    self.__vc_peer_lsp_cos_value = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="vc-peer-lsp-cos-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint8', is_config=False)

  vc_proto_name = __builtin__.property(_get_vc_proto_name)
  vc_ldp_tunnel_id = __builtin__.property(_get_vc_ldp_tunnel_id)
  vc_ldp_name = __builtin__.property(_get_vc_ldp_name)
  vc_lsp_name = __builtin__.property(_get_vc_lsp_name)
  vc_peer_lsp_cos_enabled = __builtin__.property(_get_vc_peer_lsp_cos_enabled)
  vc_peer_lsp_cos_value = __builtin__.property(_get_vc_peer_lsp_cos_value)


  _pyangbind_elements = {'vc_proto_name': vc_proto_name, 'vc_ldp_tunnel_id': vc_ldp_tunnel_id, 'vc_ldp_name': vc_ldp_name, 'vc_lsp_name': vc_lsp_name, 'vc_peer_lsp_cos_enabled': vc_peer_lsp_cos_enabled, 'vc_peer_lsp_cos_value': vc_peer_lsp_cos_value, }


