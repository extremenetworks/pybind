
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class bfd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/ipv6/router/ospf/bfd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: BFD provides rapid detection of the failure of a forwarding path by checking that the next-hop device is alive. Without BFD enabled, it can take some time to detect that a neighboring device is not operational causing packet loss due to incorrect routing information at a level unacceptable for real-time applications such as VOIP and video over IP. Using BFD, you can detect a forwarding path failure rapidly depending on the configuration.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bfd_enable','__bfd_holdover_interval',)

  _yang_name = 'bfd'
  _rest_name = 'bfd'

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
    self.__bfd_holdover_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..20']}), is_leaf=True, yang_name="bfd-holdover-interval", rest_name="bfd-holdover-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)
    self.__bfd_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-enable", rest_name="bfd-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'ipv6', u'router', u'ospf', u'bfd']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'routing-system', u'ipv6', u'router', u'ospf', u'bfd']

  def _get_bfd_enable(self):
    """
    Getter method for bfd_enable, mapped from YANG variable /routing_system/ipv6/router/ospf/bfd/bfd_enable (empty)
    """
    return self.__bfd_enable
      
  def _set_bfd_enable(self, v, load=False):
    """
    Setter method for bfd_enable, mapped from YANG variable /routing_system/ipv6/router/ospf/bfd/bfd_enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_enable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bfd-enable", rest_name="bfd-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-enable", rest_name="bfd-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)""",
        })

    self.__bfd_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_enable(self):
    self.__bfd_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-enable", rest_name="bfd-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)


  def _get_bfd_holdover_interval(self):
    """
    Getter method for bfd_holdover_interval, mapped from YANG variable /routing_system/ipv6/router/ospf/bfd/bfd_holdover_interval (common-def:time-interval-sec)

    YANG Description: Holdover-interval is the time by which the BFD session DOWN notification to Ospf is delayed.If within that holdover time, the BFD session is UP then Ospf is not notified of the BFD session flap.
    """
    return self.__bfd_holdover_interval
      
  def _set_bfd_holdover_interval(self, v, load=False):
    """
    Setter method for bfd_holdover_interval, mapped from YANG variable /routing_system/ipv6/router/ospf/bfd/bfd_holdover_interval (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_holdover_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_holdover_interval() directly.

    YANG Description: Holdover-interval is the time by which the BFD session DOWN notification to Ospf is delayed.If within that holdover time, the BFD session is UP then Ospf is not notified of the BFD session flap.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..20']}), is_leaf=True, yang_name="bfd-holdover-interval", rest_name="bfd-holdover-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_holdover_interval must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..20']}), is_leaf=True, yang_name="bfd-holdover-interval", rest_name="bfd-holdover-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__bfd_holdover_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_holdover_interval(self):
    self.__bfd_holdover_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..20']}), is_leaf=True, yang_name="bfd-holdover-interval", rest_name="bfd-holdover-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)

  bfd_enable = __builtin__.property(_get_bfd_enable, _set_bfd_enable)
  bfd_holdover_interval = __builtin__.property(_get_bfd_holdover_interval, _set_bfd_holdover_interval)


  _pyangbind_elements = {'bfd_enable': bfd_enable, 'bfd_holdover_interval': bfd_holdover_interval, }


