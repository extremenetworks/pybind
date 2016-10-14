
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class l1_circ_metrics(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/interface-detail/isis-intf/l1-circ-metrics. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__auth_check','__auth_mode','__auth_key','__circ_metric','__ip6_circ_metric','__circ_priority','__hello_int','__hello_mult','__dis','__dis_ch','__next_hello','__active_adj',)

  _yang_name = 'l1-circ-metrics'

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
    self.__hello_int = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-int", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__ip6_circ_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ip6-circ-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__auth_key = YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    self.__circ_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="circ-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__dis_ch = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dis-ch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__active_adj = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="active-adj", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__auth_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'cleartext': {'value': 1}, u'md5': {'value': 2}},), is_leaf=True, yang_name="auth-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='auth-mode', is_config=False)
    self.__circ_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="circ-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint8', is_config=False)
    self.__dis = YANGDynClass(base=unicode, is_leaf=True, yang_name="dis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    self.__next_hello = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="next-hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__auth_check = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="auth-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    self.__hello_mult = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-mult", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)

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
      return [u'isis-state', u'interface-detail', u'isis-intf', u'l1-circ-metrics']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'isis-state', u'interface-detail', u'isis-intf', u'l1-circ-metrics']

  def _get_auth_check(self):
    """
    Getter method for auth_check, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/auth_check (isis-status)

    YANG Description: If authentication enabled on incoming IS-IS PDUs
    """
    return self.__auth_check
      
  def _set_auth_check(self, v, load=False):
    """
    Setter method for auth_check, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/auth_check (isis-status)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_check is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_check() directly.

    YANG Description: If authentication enabled on incoming IS-IS PDUs
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="auth-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_check must be of a type compatible with isis-status""",
          'defined-type': "brocade-isis-operational:isis-status",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="auth-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)""",
        })

    self.__auth_check = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_check(self):
    self.__auth_check = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="auth-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)


  def _get_auth_mode(self):
    """
    Getter method for auth_mode, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/auth_mode (auth-mode)

    YANG Description: IS-IS authentication mode
    """
    return self.__auth_mode
      
  def _set_auth_mode(self, v, load=False):
    """
    Setter method for auth_mode, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/auth_mode (auth-mode)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_mode() directly.

    YANG Description: IS-IS authentication mode
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'cleartext': {'value': 1}, u'md5': {'value': 2}},), is_leaf=True, yang_name="auth-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='auth-mode', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_mode must be of a type compatible with auth-mode""",
          'defined-type': "brocade-isis-operational:auth-mode",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'cleartext': {'value': 1}, u'md5': {'value': 2}},), is_leaf=True, yang_name="auth-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='auth-mode', is_config=False)""",
        })

    self.__auth_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_mode(self):
    self.__auth_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'cleartext': {'value': 1}, u'md5': {'value': 2}},), is_leaf=True, yang_name="auth-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='auth-mode', is_config=False)


  def _get_auth_key(self):
    """
    Getter method for auth_key, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/auth_key (string)

    YANG Description: IS-IS authentication key
    """
    return self.__auth_key
      
  def _set_auth_key(self, v, load=False):
    """
    Setter method for auth_key, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/auth_key (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_key() directly.

    YANG Description: IS-IS authentication key
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="auth-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_key must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)""",
        })

    self.__auth_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_key(self):
    self.__auth_key = YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)


  def _get_circ_metric(self):
    """
    Getter method for circ_metric, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/circ_metric (uint32)

    YANG Description: ISIS circuit Metric
    """
    return self.__circ_metric
      
  def _set_circ_metric(self, v, load=False):
    """
    Setter method for circ_metric, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/circ_metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_circ_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_circ_metric() directly.

    YANG Description: ISIS circuit Metric
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="circ-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """circ_metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="circ-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__circ_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_circ_metric(self):
    self.__circ_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="circ-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_ip6_circ_metric(self):
    """
    Getter method for ip6_circ_metric, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/ip6_circ_metric (uint32)

    YANG Description: ISISv6 circuit Metric
    """
    return self.__ip6_circ_metric
      
  def _set_ip6_circ_metric(self, v, load=False):
    """
    Setter method for ip6_circ_metric, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/ip6_circ_metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip6_circ_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip6_circ_metric() directly.

    YANG Description: ISISv6 circuit Metric
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ip6-circ-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip6_circ_metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ip6-circ-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__ip6_circ_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip6_circ_metric(self):
    self.__ip6_circ_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ip6-circ-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_circ_priority(self):
    """
    Getter method for circ_priority, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/circ_priority (uint8)

    YANG Description: Circuit Priority
    """
    return self.__circ_priority
      
  def _set_circ_priority(self, v, load=False):
    """
    Setter method for circ_priority, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/circ_priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_circ_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_circ_priority() directly.

    YANG Description: Circuit Priority
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="circ-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """circ_priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="circ-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint8', is_config=False)""",
        })

    self.__circ_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_circ_priority(self):
    self.__circ_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="circ-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint8', is_config=False)


  def _get_hello_int(self):
    """
    Getter method for hello_int, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/hello_int (uint32)

    YANG Description: Hello interval
    """
    return self.__hello_int
      
  def _set_hello_int(self, v, load=False):
    """
    Setter method for hello_int, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/hello_int (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_int is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_int() directly.

    YANG Description: Hello interval
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-int", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_int must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-int", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__hello_int = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_int(self):
    self.__hello_int = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-int", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_hello_mult(self):
    """
    Getter method for hello_mult, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/hello_mult (uint32)

    YANG Description: Hello multiplier
    """
    return self.__hello_mult
      
  def _set_hello_mult(self, v, load=False):
    """
    Setter method for hello_mult, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/hello_mult (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_mult is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_mult() directly.

    YANG Description: Hello multiplier
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-mult", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_mult must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-mult", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__hello_mult = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_mult(self):
    self.__hello_mult = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-mult", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_dis(self):
    """
    Getter method for dis, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/dis (string)

    YANG Description: Designated IS
    """
    return self.__dis
      
  def _set_dis(self, v, load=False):
    """
    Setter method for dis, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/dis (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dis is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dis() directly.

    YANG Description: Designated IS
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="dis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dis must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="dis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)""",
        })

    self.__dis = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dis(self):
    self.__dis = YANGDynClass(base=unicode, is_leaf=True, yang_name="dis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)


  def _get_dis_ch(self):
    """
    Getter method for dis_ch, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/dis_ch (uint32)

    YANG Description: DIS changes
    """
    return self.__dis_ch
      
  def _set_dis_ch(self, v, load=False):
    """
    Setter method for dis_ch, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/dis_ch (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dis_ch is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dis_ch() directly.

    YANG Description: DIS changes
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dis-ch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dis_ch must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dis-ch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__dis_ch = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dis_ch(self):
    self.__dis_ch = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="dis-ch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_next_hello(self):
    """
    Getter method for next_hello, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/next_hello (uint32)

    YANG Description: Time remaining until next hello
    """
    return self.__next_hello
      
  def _set_next_hello(self, v, load=False):
    """
    Setter method for next_hello, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/next_hello (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hello is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hello() directly.

    YANG Description: Time remaining until next hello
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="next-hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hello must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="next-hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__next_hello = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hello(self):
    self.__next_hello = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="next-hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_active_adj(self):
    """
    Getter method for active_adj, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/active_adj (uint32)

    YANG Description: Number of active adjacencies
    """
    return self.__active_adj
      
  def _set_active_adj(self, v, load=False):
    """
    Setter method for active_adj, mapped from YANG variable /isis_state/interface_detail/isis_intf/l1_circ_metrics/active_adj (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_active_adj is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_active_adj() directly.

    YANG Description: Number of active adjacencies
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="active-adj", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """active_adj must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="active-adj", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__active_adj = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_active_adj(self):
    self.__active_adj = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="active-adj", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)

  auth_check = __builtin__.property(_get_auth_check)
  auth_mode = __builtin__.property(_get_auth_mode)
  auth_key = __builtin__.property(_get_auth_key)
  circ_metric = __builtin__.property(_get_circ_metric)
  ip6_circ_metric = __builtin__.property(_get_ip6_circ_metric)
  circ_priority = __builtin__.property(_get_circ_priority)
  hello_int = __builtin__.property(_get_hello_int)
  hello_mult = __builtin__.property(_get_hello_mult)
  dis = __builtin__.property(_get_dis)
  dis_ch = __builtin__.property(_get_dis_ch)
  next_hello = __builtin__.property(_get_next_hello)
  active_adj = __builtin__.property(_get_active_adj)


  _pyangbind_elements = {'auth_check': auth_check, 'auth_mode': auth_mode, 'auth_key': auth_key, 'circ_metric': circ_metric, 'ip6_circ_metric': ip6_circ_metric, 'circ_priority': circ_priority, 'hello_int': hello_int, 'hello_mult': hello_mult, 'dis': dis, 'dis_ch': dis_ch, 'next_hello': next_hello, 'active_adj': active_adj, }


