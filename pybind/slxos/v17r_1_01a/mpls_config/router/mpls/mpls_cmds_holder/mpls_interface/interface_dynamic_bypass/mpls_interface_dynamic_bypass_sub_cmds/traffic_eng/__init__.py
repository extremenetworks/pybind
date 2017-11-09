
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class traffic_eng(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/mpls-interface/interface-dynamic-bypass/mpls-interface-dynamic-bypass-sub-cmds/traffic-eng. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interface_dynamic_bypass_traffic_eng_max_burst','__interface_dynamic_bypass_traffic_eng_max_rate','__interface_dynamic_bypass_traffic_eng_mean_rate',)

  _yang_name = 'traffic-eng'
  _rest_name = 'traffic-eng'

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
    self.__interface_dynamic_bypass_traffic_eng_max_rate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..214748364']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interface-dynamic-bypass-traffic-eng-max-rate", rest_name="interface-dynamic-bypass-traffic-eng-max-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__interface_dynamic_bypass_traffic_eng_mean_rate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..214748364']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interface-dynamic-bypass-traffic-eng-mean-rate", rest_name="interface-dynamic-bypass-traffic-eng-mean-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__interface_dynamic_bypass_traffic_eng_max_burst = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..214748364']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interface-dynamic-bypass-traffic-eng-max-burst", rest_name="interface-dynamic-bypass-traffic-eng-max-burst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'mpls-interface', u'interface-dynamic-bypass', u'mpls-interface-dynamic-bypass-sub-cmds', u'traffic-eng']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'mpls-interface', u'interface-dynamic-bypass', u'mpls-interface-dynamic-bypass-sub-cmds', u'traffic-eng']

  def _get_interface_dynamic_bypass_traffic_eng_max_burst(self):
    """
    Getter method for interface_dynamic_bypass_traffic_eng_max_burst, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_dynamic_bypass/mpls_interface_dynamic_bypass_sub_cmds/traffic_eng/interface_dynamic_bypass_traffic_eng_max_burst (uint32)
    """
    return self.__interface_dynamic_bypass_traffic_eng_max_burst
      
  def _set_interface_dynamic_bypass_traffic_eng_max_burst(self, v, load=False):
    """
    Setter method for interface_dynamic_bypass_traffic_eng_max_burst, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_dynamic_bypass/mpls_interface_dynamic_bypass_sub_cmds/traffic_eng/interface_dynamic_bypass_traffic_eng_max_burst (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_dynamic_bypass_traffic_eng_max_burst is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_dynamic_bypass_traffic_eng_max_burst() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..214748364']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interface-dynamic-bypass-traffic-eng-max-burst", rest_name="interface-dynamic-bypass-traffic-eng-max-burst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_dynamic_bypass_traffic_eng_max_burst must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..214748364']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interface-dynamic-bypass-traffic-eng-max-burst", rest_name="interface-dynamic-bypass-traffic-eng-max-burst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__interface_dynamic_bypass_traffic_eng_max_burst = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_dynamic_bypass_traffic_eng_max_burst(self):
    self.__interface_dynamic_bypass_traffic_eng_max_burst = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..214748364']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interface-dynamic-bypass-traffic-eng-max-burst", rest_name="interface-dynamic-bypass-traffic-eng-max-burst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_interface_dynamic_bypass_traffic_eng_max_rate(self):
    """
    Getter method for interface_dynamic_bypass_traffic_eng_max_rate, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_dynamic_bypass/mpls_interface_dynamic_bypass_sub_cmds/traffic_eng/interface_dynamic_bypass_traffic_eng_max_rate (uint32)
    """
    return self.__interface_dynamic_bypass_traffic_eng_max_rate
      
  def _set_interface_dynamic_bypass_traffic_eng_max_rate(self, v, load=False):
    """
    Setter method for interface_dynamic_bypass_traffic_eng_max_rate, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_dynamic_bypass/mpls_interface_dynamic_bypass_sub_cmds/traffic_eng/interface_dynamic_bypass_traffic_eng_max_rate (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_dynamic_bypass_traffic_eng_max_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_dynamic_bypass_traffic_eng_max_rate() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..214748364']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interface-dynamic-bypass-traffic-eng-max-rate", rest_name="interface-dynamic-bypass-traffic-eng-max-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_dynamic_bypass_traffic_eng_max_rate must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..214748364']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interface-dynamic-bypass-traffic-eng-max-rate", rest_name="interface-dynamic-bypass-traffic-eng-max-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__interface_dynamic_bypass_traffic_eng_max_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_dynamic_bypass_traffic_eng_max_rate(self):
    self.__interface_dynamic_bypass_traffic_eng_max_rate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..214748364']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interface-dynamic-bypass-traffic-eng-max-rate", rest_name="interface-dynamic-bypass-traffic-eng-max-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_interface_dynamic_bypass_traffic_eng_mean_rate(self):
    """
    Getter method for interface_dynamic_bypass_traffic_eng_mean_rate, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_dynamic_bypass/mpls_interface_dynamic_bypass_sub_cmds/traffic_eng/interface_dynamic_bypass_traffic_eng_mean_rate (uint32)
    """
    return self.__interface_dynamic_bypass_traffic_eng_mean_rate
      
  def _set_interface_dynamic_bypass_traffic_eng_mean_rate(self, v, load=False):
    """
    Setter method for interface_dynamic_bypass_traffic_eng_mean_rate, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_dynamic_bypass/mpls_interface_dynamic_bypass_sub_cmds/traffic_eng/interface_dynamic_bypass_traffic_eng_mean_rate (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_dynamic_bypass_traffic_eng_mean_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_dynamic_bypass_traffic_eng_mean_rate() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..214748364']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interface-dynamic-bypass-traffic-eng-mean-rate", rest_name="interface-dynamic-bypass-traffic-eng-mean-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_dynamic_bypass_traffic_eng_mean_rate must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..214748364']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interface-dynamic-bypass-traffic-eng-mean-rate", rest_name="interface-dynamic-bypass-traffic-eng-mean-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__interface_dynamic_bypass_traffic_eng_mean_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_dynamic_bypass_traffic_eng_mean_rate(self):
    self.__interface_dynamic_bypass_traffic_eng_mean_rate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..214748364']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interface-dynamic-bypass-traffic-eng-mean-rate", rest_name="interface-dynamic-bypass-traffic-eng-mean-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  interface_dynamic_bypass_traffic_eng_max_burst = __builtin__.property(_get_interface_dynamic_bypass_traffic_eng_max_burst, _set_interface_dynamic_bypass_traffic_eng_max_burst)
  interface_dynamic_bypass_traffic_eng_max_rate = __builtin__.property(_get_interface_dynamic_bypass_traffic_eng_max_rate, _set_interface_dynamic_bypass_traffic_eng_max_rate)
  interface_dynamic_bypass_traffic_eng_mean_rate = __builtin__.property(_get_interface_dynamic_bypass_traffic_eng_mean_rate, _set_interface_dynamic_bypass_traffic_eng_mean_rate)


  _pyangbind_elements = {'interface_dynamic_bypass_traffic_eng_max_burst': interface_dynamic_bypass_traffic_eng_max_burst, 'interface_dynamic_bypass_traffic_eng_max_rate': interface_dynamic_bypass_traffic_eng_max_rate, 'interface_dynamic_bypass_traffic_eng_mean_rate': interface_dynamic_bypass_traffic_eng_mean_rate, }


