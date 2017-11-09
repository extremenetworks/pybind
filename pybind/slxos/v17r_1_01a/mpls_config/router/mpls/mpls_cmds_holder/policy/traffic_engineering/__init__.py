
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import traffic_eng_ospf
class traffic_engineering(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/policy/traffic-engineering. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__isis_set_level','__traffic_eng_ospf',)

  _yang_name = 'traffic-engineering'
  _rest_name = 'traffic-engineering'

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
    self.__isis_set_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="isis-set-level", rest_name="isis-set-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)
    self.__traffic_eng_ospf = YANGDynClass(base=traffic_eng_ospf.traffic_eng_ospf, is_container='container', presence=False, yang_name="traffic-eng-ospf", rest_name="traffic-eng-ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'policy', u'traffic-engineering']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'policy', u'traffic-engineering']

  def _get_isis_set_level(self):
    """
    Getter method for isis_set_level, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/traffic_engineering/isis_set_level (enumeration)
    """
    return self.__isis_set_level
      
  def _set_isis_set_level(self, v, load=False):
    """
    Setter method for isis_set_level, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/traffic_engineering/isis_set_level (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis_set_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis_set_level() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="isis-set-level", rest_name="isis-set-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis_set_level must be of a type compatible with enumeration""",
          'defined-type': "brocade-mpls:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="isis-set-level", rest_name="isis-set-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)""",
        })

    self.__isis_set_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis_set_level(self):
    self.__isis_set_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="isis-set-level", rest_name="isis-set-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)


  def _get_traffic_eng_ospf(self):
    """
    Getter method for traffic_eng_ospf, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/traffic_engineering/traffic_eng_ospf (container)
    """
    return self.__traffic_eng_ospf
      
  def _set_traffic_eng_ospf(self, v, load=False):
    """
    Setter method for traffic_eng_ospf, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/traffic_engineering/traffic_eng_ospf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_traffic_eng_ospf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_traffic_eng_ospf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=traffic_eng_ospf.traffic_eng_ospf, is_container='container', presence=False, yang_name="traffic-eng-ospf", rest_name="traffic-eng-ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """traffic_eng_ospf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=traffic_eng_ospf.traffic_eng_ospf, is_container='container', presence=False, yang_name="traffic-eng-ospf", rest_name="traffic-eng-ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__traffic_eng_ospf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_traffic_eng_ospf(self):
    self.__traffic_eng_ospf = YANGDynClass(base=traffic_eng_ospf.traffic_eng_ospf, is_container='container', presence=False, yang_name="traffic-eng-ospf", rest_name="traffic-eng-ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

  isis_set_level = __builtin__.property(_get_isis_set_level, _set_isis_set_level)
  traffic_eng_ospf = __builtin__.property(_get_traffic_eng_ospf, _set_traffic_eng_ospf)


  _pyangbind_elements = {'isis_set_level': isis_set_level, 'traffic_eng_ospf': traffic_eng_ospf, }


