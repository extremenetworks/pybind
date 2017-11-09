
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class rp_cand_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/hide-pim-holder/pim/rp-candidate/rp-cand-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rp_cand_intf_type','__rp_cand_intf_id','__rp_cand_priority',)

  _yang_name = 'rp-cand-interface'
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
    self.__rp_cand_intf_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="rp-cand-intf-id", rest_name="rp-cand-intf-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='string', is_config=True)
    self.__rp_cand_intf_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'gigabitethernet': {}, u've': {}, u'loopback': {}, u'fortygigabitethernet': {}, u'port-channel': {}, u'tengigabitethernet': {}, u'hundredgigabitethernet': {}},), is_leaf=True, yang_name="rp-cand-intf-type", rest_name="rp-cand-intf-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='pim-intf-types', is_config=True)
    self.__rp_cand_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(192), is_leaf=True, yang_name="rp-cand-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='uint32', is_config=True)

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
      return [u'rbridge-id', u'router', u'hide-pim-holder', u'pim', u'rp-candidate', u'rp-cand-interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'pim', u'rp-candidate', u'interface']

  def _get_rp_cand_intf_type(self):
    """
    Getter method for rp_cand_intf_type, mapped from YANG variable /rbridge_id/router/hide_pim_holder/pim/rp_candidate/rp_cand_interface/rp_cand_intf_type (pim-intf-types)
    """
    return self.__rp_cand_intf_type
      
  def _set_rp_cand_intf_type(self, v, load=False):
    """
    Setter method for rp_cand_intf_type, mapped from YANG variable /rbridge_id/router/hide_pim_holder/pim/rp_candidate/rp_cand_interface/rp_cand_intf_type (pim-intf-types)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rp_cand_intf_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rp_cand_intf_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'gigabitethernet': {}, u've': {}, u'loopback': {}, u'fortygigabitethernet': {}, u'port-channel': {}, u'tengigabitethernet': {}, u'hundredgigabitethernet': {}},), is_leaf=True, yang_name="rp-cand-intf-type", rest_name="rp-cand-intf-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='pim-intf-types', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rp_cand_intf_type must be of a type compatible with pim-intf-types""",
          'defined-type': "brocade-pim:pim-intf-types",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'gigabitethernet': {}, u've': {}, u'loopback': {}, u'fortygigabitethernet': {}, u'port-channel': {}, u'tengigabitethernet': {}, u'hundredgigabitethernet': {}},), is_leaf=True, yang_name="rp-cand-intf-type", rest_name="rp-cand-intf-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='pim-intf-types', is_config=True)""",
        })

    self.__rp_cand_intf_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rp_cand_intf_type(self):
    self.__rp_cand_intf_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'gigabitethernet': {}, u've': {}, u'loopback': {}, u'fortygigabitethernet': {}, u'port-channel': {}, u'tengigabitethernet': {}, u'hundredgigabitethernet': {}},), is_leaf=True, yang_name="rp-cand-intf-type", rest_name="rp-cand-intf-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='pim-intf-types', is_config=True)


  def _get_rp_cand_intf_id(self):
    """
    Getter method for rp_cand_intf_id, mapped from YANG variable /rbridge_id/router/hide_pim_holder/pim/rp_candidate/rp_cand_interface/rp_cand_intf_id (string)
    """
    return self.__rp_cand_intf_id
      
  def _set_rp_cand_intf_id(self, v, load=False):
    """
    Setter method for rp_cand_intf_id, mapped from YANG variable /rbridge_id/router/hide_pim_holder/pim/rp_candidate/rp_cand_interface/rp_cand_intf_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rp_cand_intf_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rp_cand_intf_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="rp-cand-intf-id", rest_name="rp-cand-intf-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rp_cand_intf_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="rp-cand-intf-id", rest_name="rp-cand-intf-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='string', is_config=True)""",
        })

    self.__rp_cand_intf_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rp_cand_intf_id(self):
    self.__rp_cand_intf_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="rp-cand-intf-id", rest_name="rp-cand-intf-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='string', is_config=True)


  def _get_rp_cand_priority(self):
    """
    Getter method for rp_cand_priority, mapped from YANG variable /rbridge_id/router/hide_pim_holder/pim/rp_candidate/rp_cand_interface/rp_cand_priority (uint32)
    """
    return self.__rp_cand_priority
      
  def _set_rp_cand_priority(self, v, load=False):
    """
    Setter method for rp_cand_priority, mapped from YANG variable /rbridge_id/router/hide_pim_holder/pim/rp_candidate/rp_cand_interface/rp_cand_priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rp_cand_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rp_cand_priority() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(192), is_leaf=True, yang_name="rp-cand-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rp_cand_priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(192), is_leaf=True, yang_name="rp-cand-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='uint32', is_config=True)""",
        })

    self.__rp_cand_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rp_cand_priority(self):
    self.__rp_cand_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(192), is_leaf=True, yang_name="rp-cand-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='uint32', is_config=True)

  rp_cand_intf_type = __builtin__.property(_get_rp_cand_intf_type, _set_rp_cand_intf_type)
  rp_cand_intf_id = __builtin__.property(_get_rp_cand_intf_id, _set_rp_cand_intf_id)
  rp_cand_priority = __builtin__.property(_get_rp_cand_priority, _set_rp_cand_priority)


  _pyangbind_elements = {'rp_cand_intf_type': rp_cand_intf_type, 'rp_cand_intf_id': rp_cand_intf_id, 'rp_cand_priority': rp_cand_priority, }


