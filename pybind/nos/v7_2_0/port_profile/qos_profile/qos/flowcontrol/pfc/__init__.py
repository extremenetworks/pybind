
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class pfc(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile - based on the path /port-profile/qos-profile/qos/flowcontrol/pfc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The list of priority based flow control 
elements.Each row represents the Pfc Cos, 
Pause generation and reception values
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__pfc_cos','__pfc_tx','__pfc_rx',)

  _yang_name = 'pfc'
  _rest_name = 'pfc'

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
    self.__pfc_cos = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="pfc-cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'cos'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='int32', is_config=True)
    self.__pfc_rx = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="pfc-rx", rest_name="rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'rx'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)
    self.__pfc_tx = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="pfc-tx", rest_name="tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'tx'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)

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
      return [u'port-profile', u'qos-profile', u'qos', u'flowcontrol', u'pfc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'port-profile', u'qos-profile', u'qos', u'flowcontrol', u'pfc']

  def _get_pfc_cos(self):
    """
    Getter method for pfc_cos, mapped from YANG variable /port_profile/qos_profile/qos/flowcontrol/pfc/pfc_cos (int32)

    YANG Description: This specifies the CoS value.
    """
    return self.__pfc_cos
      
  def _set_pfc_cos(self, v, load=False):
    """
    Setter method for pfc_cos, mapped from YANG variable /port_profile/qos_profile/qos/flowcontrol/pfc/pfc_cos (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pfc_cos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pfc_cos() directly.

    YANG Description: This specifies the CoS value.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="pfc-cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'cos'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pfc_cos must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="pfc-cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'cos'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='int32', is_config=True)""",
        })

    self.__pfc_cos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pfc_cos(self):
    self.__pfc_cos = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="pfc-cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'cos'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='int32', is_config=True)


  def _get_pfc_tx(self):
    """
    Getter method for pfc_tx, mapped from YANG variable /port_profile/qos_profile/qos/flowcontrol/pfc/pfc_tx (enumeration)

    YANG Description: This specifies if the Pause generation is
enabled or disabled. 'on' enables the pause
generation and 'off' disables pause 
generation.
    """
    return self.__pfc_tx
      
  def _set_pfc_tx(self, v, load=False):
    """
    Setter method for pfc_tx, mapped from YANG variable /port_profile/qos_profile/qos/flowcontrol/pfc/pfc_tx (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pfc_tx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pfc_tx() directly.

    YANG Description: This specifies if the Pause generation is
enabled or disabled. 'on' enables the pause
generation and 'off' disables pause 
generation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="pfc-tx", rest_name="tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'tx'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pfc_tx must be of a type compatible with enumeration""",
          'defined-type': "brocade-port-profile:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="pfc-tx", rest_name="tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'tx'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)""",
        })

    self.__pfc_tx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pfc_tx(self):
    self.__pfc_tx = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="pfc-tx", rest_name="tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'tx'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)


  def _get_pfc_rx(self):
    """
    Getter method for pfc_rx, mapped from YANG variable /port_profile/qos_profile/qos/flowcontrol/pfc/pfc_rx (enumeration)

    YANG Description: This specifies if the Pause reception is
enabled or disabled. 'on' enables the pause
reception and 'off' disables pause
reception.
    """
    return self.__pfc_rx
      
  def _set_pfc_rx(self, v, load=False):
    """
    Setter method for pfc_rx, mapped from YANG variable /port_profile/qos_profile/qos/flowcontrol/pfc/pfc_rx (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pfc_rx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pfc_rx() directly.

    YANG Description: This specifies if the Pause reception is
enabled or disabled. 'on' enables the pause
reception and 'off' disables pause
reception.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="pfc-rx", rest_name="rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'rx'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pfc_rx must be of a type compatible with enumeration""",
          'defined-type': "brocade-port-profile:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="pfc-rx", rest_name="rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'rx'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)""",
        })

    self.__pfc_rx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pfc_rx(self):
    self.__pfc_rx = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="pfc-rx", rest_name="rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'rx'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)

  pfc_cos = __builtin__.property(_get_pfc_cos, _set_pfc_cos)
  pfc_tx = __builtin__.property(_get_pfc_tx, _set_pfc_tx)
  pfc_rx = __builtin__.property(_get_pfc_rx, _set_pfc_rx)


  _pyangbind_elements = {'pfc_cos': pfc_cos, 'pfc_tx': pfc_tx, 'pfc_rx': pfc_rx, }


