
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class bsr_cand_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/pim/bsr-candidate/bsr-cand-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bsr_cand_intf_type','__bsr_cand_intf_id','__hash_mask_length','__bsr_cand_priority',)

  _yang_name = 'bsr-cand-interface'
  _rest_name = 'interface'

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
    self.__hash_mask_length = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..32']}), is_leaf=True, yang_name="hash-mask-length", rest_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BSR hash mask', u'alt-name': u'mask', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='uint16', is_config=True)
    self.__bsr_cand_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..255']}), is_leaf=True, yang_name="bsr-cand-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BSR priority', u'alt-name': u'priority', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='uint32', is_config=True)
    self.__bsr_cand_intf_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="bsr-cand-intf-id", rest_name="bsr-cand-intf-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name in slot/port format for ethernet or port-channel/ve/loopback interface number', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='string', is_config=True)
    self.__bsr_cand_intf_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {}, u'port-channel': {}, u've': {}, u'loopback': {}},), is_leaf=True, yang_name="bsr-cand-intf-type", rest_name="bsr-cand-intf-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='pim-intf-types', is_config=True)

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
      return [u'routing-system', u'router', u'pim', u'bsr-candidate', u'bsr-cand-interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'pim', u'bsr-candidate', u'interface']

  def _get_bsr_cand_intf_type(self):
    """
    Getter method for bsr_cand_intf_type, mapped from YANG variable /routing_system/router/pim/bsr_candidate/bsr_cand_interface/bsr_cand_intf_type (pim-intf-types)
    """
    return self.__bsr_cand_intf_type
      
  def _set_bsr_cand_intf_type(self, v, load=False):
    """
    Setter method for bsr_cand_intf_type, mapped from YANG variable /routing_system/router/pim/bsr_candidate/bsr_cand_interface/bsr_cand_intf_type (pim-intf-types)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bsr_cand_intf_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bsr_cand_intf_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {}, u'port-channel': {}, u've': {}, u'loopback': {}},), is_leaf=True, yang_name="bsr-cand-intf-type", rest_name="bsr-cand-intf-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='pim-intf-types', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bsr_cand_intf_type must be of a type compatible with pim-intf-types""",
          'defined-type': "brocade-pim:pim-intf-types",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {}, u'port-channel': {}, u've': {}, u'loopback': {}},), is_leaf=True, yang_name="bsr-cand-intf-type", rest_name="bsr-cand-intf-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='pim-intf-types', is_config=True)""",
        })

    self.__bsr_cand_intf_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bsr_cand_intf_type(self):
    self.__bsr_cand_intf_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {}, u'port-channel': {}, u've': {}, u'loopback': {}},), is_leaf=True, yang_name="bsr-cand-intf-type", rest_name="bsr-cand-intf-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='pim-intf-types', is_config=True)


  def _get_bsr_cand_intf_id(self):
    """
    Getter method for bsr_cand_intf_id, mapped from YANG variable /routing_system/router/pim/bsr_candidate/bsr_cand_interface/bsr_cand_intf_id (string)
    """
    return self.__bsr_cand_intf_id
      
  def _set_bsr_cand_intf_id(self, v, load=False):
    """
    Setter method for bsr_cand_intf_id, mapped from YANG variable /routing_system/router/pim/bsr_candidate/bsr_cand_interface/bsr_cand_intf_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bsr_cand_intf_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bsr_cand_intf_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="bsr-cand-intf-id", rest_name="bsr-cand-intf-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name in slot/port format for ethernet or port-channel/ve/loopback interface number', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bsr_cand_intf_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="bsr-cand-intf-id", rest_name="bsr-cand-intf-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name in slot/port format for ethernet or port-channel/ve/loopback interface number', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='string', is_config=True)""",
        })

    self.__bsr_cand_intf_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bsr_cand_intf_id(self):
    self.__bsr_cand_intf_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="bsr-cand-intf-id", rest_name="bsr-cand-intf-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name in slot/port format for ethernet or port-channel/ve/loopback interface number', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='string', is_config=True)


  def _get_hash_mask_length(self):
    """
    Getter method for hash_mask_length, mapped from YANG variable /routing_system/router/pim/bsr_candidate/bsr_cand_interface/hash_mask_length (uint16)
    """
    return self.__hash_mask_length
      
  def _set_hash_mask_length(self, v, load=False):
    """
    Setter method for hash_mask_length, mapped from YANG variable /routing_system/router/pim/bsr_candidate/bsr_cand_interface/hash_mask_length (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hash_mask_length is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hash_mask_length() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..32']}), is_leaf=True, yang_name="hash-mask-length", rest_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BSR hash mask', u'alt-name': u'mask', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hash_mask_length must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..32']}), is_leaf=True, yang_name="hash-mask-length", rest_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BSR hash mask', u'alt-name': u'mask', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='uint16', is_config=True)""",
        })

    self.__hash_mask_length = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hash_mask_length(self):
    self.__hash_mask_length = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..32']}), is_leaf=True, yang_name="hash-mask-length", rest_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BSR hash mask', u'alt-name': u'mask', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='uint16', is_config=True)


  def _get_bsr_cand_priority(self):
    """
    Getter method for bsr_cand_priority, mapped from YANG variable /routing_system/router/pim/bsr_candidate/bsr_cand_interface/bsr_cand_priority (uint32)
    """
    return self.__bsr_cand_priority
      
  def _set_bsr_cand_priority(self, v, load=False):
    """
    Setter method for bsr_cand_priority, mapped from YANG variable /routing_system/router/pim/bsr_candidate/bsr_cand_interface/bsr_cand_priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bsr_cand_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bsr_cand_priority() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..255']}), is_leaf=True, yang_name="bsr-cand-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BSR priority', u'alt-name': u'priority', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bsr_cand_priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..255']}), is_leaf=True, yang_name="bsr-cand-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BSR priority', u'alt-name': u'priority', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='uint32', is_config=True)""",
        })

    self.__bsr_cand_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bsr_cand_priority(self):
    self.__bsr_cand_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..255']}), is_leaf=True, yang_name="bsr-cand-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BSR priority', u'alt-name': u'priority', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='uint32', is_config=True)

  bsr_cand_intf_type = __builtin__.property(_get_bsr_cand_intf_type, _set_bsr_cand_intf_type)
  bsr_cand_intf_id = __builtin__.property(_get_bsr_cand_intf_id, _set_bsr_cand_intf_id)
  hash_mask_length = __builtin__.property(_get_hash_mask_length, _set_hash_mask_length)
  bsr_cand_priority = __builtin__.property(_get_bsr_cand_priority, _set_bsr_cand_priority)


  _pyangbind_elements = {'bsr_cand_intf_type': bsr_cand_intf_type, 'bsr_cand_intf_id': bsr_cand_intf_id, 'hash_mask_length': hash_mask_length, 'bsr_cand_priority': bsr_cand_priority, }


