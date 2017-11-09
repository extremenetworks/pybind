
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class port_shaper(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mls - based on the path /qos/cpu/slot/port-group/port/port-shaper. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__port_shaper_rate','__port_shaper_burst_size',)

  _yang_name = 'port-shaper'
  _rest_name = 'port-shaper'

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
    self.__port_shaper_rate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..100000']}), is_leaf=True, yang_name="port-shaper-rate", rest_name="port-shaper-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='shaper-rate', is_config=True)
    self.__port_shaper_burst_size = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="port-shaper-burst-size", rest_name="port-shaper-burst-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='burst-size', is_config=True)

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
      return [u'qos', u'cpu', u'slot', u'port-group', u'port', u'port-shaper']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos', u'cpu', u'slot', u'port-group', u'port', u'port-shaper']

  def _get_port_shaper_rate(self):
    """
    Getter method for port_shaper_rate, mapped from YANG variable /qos/cpu/slot/port_group/port/port_shaper/port_shaper_rate (shaper-rate)
    """
    return self.__port_shaper_rate
      
  def _set_port_shaper_rate(self, v, load=False):
    """
    Setter method for port_shaper_rate, mapped from YANG variable /qos/cpu/slot/port_group/port/port_shaper/port_shaper_rate (shaper-rate)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_shaper_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_shaper_rate() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..100000']}), is_leaf=True, yang_name="port-shaper-rate", rest_name="port-shaper-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='shaper-rate', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_shaper_rate must be of a type compatible with shaper-rate""",
          'defined-type': "brocade-qos-cpu:shaper-rate",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..100000']}), is_leaf=True, yang_name="port-shaper-rate", rest_name="port-shaper-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='shaper-rate', is_config=True)""",
        })

    self.__port_shaper_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_shaper_rate(self):
    self.__port_shaper_rate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..100000']}), is_leaf=True, yang_name="port-shaper-rate", rest_name="port-shaper-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='shaper-rate', is_config=True)


  def _get_port_shaper_burst_size(self):
    """
    Getter method for port_shaper_burst_size, mapped from YANG variable /qos/cpu/slot/port_group/port/port_shaper/port_shaper_burst_size (burst-size)
    """
    return self.__port_shaper_burst_size
      
  def _set_port_shaper_burst_size(self, v, load=False):
    """
    Setter method for port_shaper_burst_size, mapped from YANG variable /qos/cpu/slot/port_group/port/port_shaper/port_shaper_burst_size (burst-size)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_shaper_burst_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_shaper_burst_size() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="port-shaper-burst-size", rest_name="port-shaper-burst-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='burst-size', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_shaper_burst_size must be of a type compatible with burst-size""",
          'defined-type': "brocade-qos-cpu:burst-size",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="port-shaper-burst-size", rest_name="port-shaper-burst-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='burst-size', is_config=True)""",
        })

    self.__port_shaper_burst_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_shaper_burst_size(self):
    self.__port_shaper_burst_size = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="port-shaper-burst-size", rest_name="port-shaper-burst-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='burst-size', is_config=True)

  port_shaper_rate = __builtin__.property(_get_port_shaper_rate, _set_port_shaper_rate)
  port_shaper_burst_size = __builtin__.property(_get_port_shaper_burst_size, _set_port_shaper_burst_size)


  _pyangbind_elements = {'port_shaper_rate': port_shaper_rate, 'port_shaper_burst_size': port_shaper_burst_size, }


