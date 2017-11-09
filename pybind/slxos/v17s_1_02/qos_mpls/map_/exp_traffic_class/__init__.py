
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import exp
class exp_traffic_class(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mpls - based on the path /qos-mpls/map/exp-traffic-class. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__exp_traffic_class_map_name','__exp',)

  _yang_name = 'exp-traffic-class'
  _rest_name = 'exp-traffic-class'

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
    self.__exp_traffic_class_map_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="exp-traffic-class-map-name", rest_name="exp-traffic-class-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='map-name-type', is_config=True)
    self.__exp = YANGDynClass(base=YANGListType("exp_in_values",exp.exp, yang_name="exp", rest_name="exp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp-in-values', extensions=None), is_container='list', yang_name="exp", rest_name="exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)

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
      return [u'qos-mpls', u'map', u'exp-traffic-class']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos-mpls', u'map', u'exp-traffic-class']

  def _get_exp_traffic_class_map_name(self):
    """
    Getter method for exp_traffic_class_map_name, mapped from YANG variable /qos_mpls/map/exp_traffic_class/exp_traffic_class_map_name (map-name-type)
    """
    return self.__exp_traffic_class_map_name
      
  def _set_exp_traffic_class_map_name(self, v, load=False):
    """
    Setter method for exp_traffic_class_map_name, mapped from YANG variable /qos_mpls/map/exp_traffic_class/exp_traffic_class_map_name (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exp_traffic_class_map_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exp_traffic_class_map_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="exp-traffic-class-map-name", rest_name="exp-traffic-class-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exp_traffic_class_map_name must be of a type compatible with map-name-type""",
          'defined-type': "brocade-qos-mpls:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="exp-traffic-class-map-name", rest_name="exp-traffic-class-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='map-name-type', is_config=True)""",
        })

    self.__exp_traffic_class_map_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exp_traffic_class_map_name(self):
    self.__exp_traffic_class_map_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="exp-traffic-class-map-name", rest_name="exp-traffic-class-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='map-name-type', is_config=True)


  def _get_exp(self):
    """
    Getter method for exp, mapped from YANG variable /qos_mpls/map/exp_traffic_class/exp (list)
    """
    return self.__exp
      
  def _set_exp(self, v, load=False):
    """
    Setter method for exp, mapped from YANG variable /qos_mpls/map/exp_traffic_class/exp (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("exp_in_values",exp.exp, yang_name="exp", rest_name="exp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp-in-values', extensions=None), is_container='list', yang_name="exp", rest_name="exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exp must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("exp_in_values",exp.exp, yang_name="exp", rest_name="exp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp-in-values', extensions=None), is_container='list', yang_name="exp", rest_name="exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)""",
        })

    self.__exp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exp(self):
    self.__exp = YANGDynClass(base=YANGListType("exp_in_values",exp.exp, yang_name="exp", rest_name="exp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp-in-values', extensions=None), is_container='list', yang_name="exp", rest_name="exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)

  exp_traffic_class_map_name = __builtin__.property(_get_exp_traffic_class_map_name, _set_exp_traffic_class_map_name)
  exp = __builtin__.property(_get_exp, _set_exp)


  _pyangbind_elements = {'exp_traffic_class_map_name': exp_traffic_class_map_name, 'exp': exp, }


