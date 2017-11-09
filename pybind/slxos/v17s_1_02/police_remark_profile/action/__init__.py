
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import set_
import map_
class action(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mqc - based on the path /police-remark-profile/action. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__classification_type','__action_type','__set_','__map_',)

  _yang_name = 'action'
  _rest_name = 'action'

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
    self.__set_ = YANGDynClass(base=set_.set_, is_container='container', presence=False, yang_name="set", rest_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    self.__classification_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'color': {'value': 0}, u'color-and-traffic-class': {'value': 3}, u'color-and-dscp': {'value': 2}, u'color-and-cos': {'value': 1}},), is_leaf=True, yang_name="classification-type", rest_name="classification-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='enumeration', is_config=True)
    self.__map_ = YANGDynClass(base=map_.map_, is_container='container', presence=False, yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    self.__action_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'conform': {'value': 1}, u'exceed': {'value': 2}},), is_leaf=True, yang_name="action-type", rest_name="action-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='enumeration', is_config=True)

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
      return [u'police-remark-profile', u'action']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'police-remark-profile', u'action']

  def _get_classification_type(self):
    """
    Getter method for classification_type, mapped from YANG variable /police_remark_profile/action/classification_type (enumeration)
    """
    return self.__classification_type
      
  def _set_classification_type(self, v, load=False):
    """
    Setter method for classification_type, mapped from YANG variable /police_remark_profile/action/classification_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_classification_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_classification_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'color': {'value': 0}, u'color-and-traffic-class': {'value': 3}, u'color-and-dscp': {'value': 2}, u'color-and-cos': {'value': 1}},), is_leaf=True, yang_name="classification-type", rest_name="classification-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """classification_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-qos-mqc:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'color': {'value': 0}, u'color-and-traffic-class': {'value': 3}, u'color-and-dscp': {'value': 2}, u'color-and-cos': {'value': 1}},), is_leaf=True, yang_name="classification-type", rest_name="classification-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='enumeration', is_config=True)""",
        })

    self.__classification_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_classification_type(self):
    self.__classification_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'color': {'value': 0}, u'color-and-traffic-class': {'value': 3}, u'color-and-dscp': {'value': 2}, u'color-and-cos': {'value': 1}},), is_leaf=True, yang_name="classification-type", rest_name="classification-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='enumeration', is_config=True)


  def _get_action_type(self):
    """
    Getter method for action_type, mapped from YANG variable /police_remark_profile/action/action_type (enumeration)
    """
    return self.__action_type
      
  def _set_action_type(self, v, load=False):
    """
    Setter method for action_type, mapped from YANG variable /police_remark_profile/action/action_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'conform': {'value': 1}, u'exceed': {'value': 2}},), is_leaf=True, yang_name="action-type", rest_name="action-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-qos-mqc:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'conform': {'value': 1}, u'exceed': {'value': 2}},), is_leaf=True, yang_name="action-type", rest_name="action-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='enumeration', is_config=True)""",
        })

    self.__action_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action_type(self):
    self.__action_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'conform': {'value': 1}, u'exceed': {'value': 2}},), is_leaf=True, yang_name="action-type", rest_name="action-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='enumeration', is_config=True)


  def _get_set_(self):
    """
    Getter method for set_, mapped from YANG variable /police_remark_profile/action/set (container)
    """
    return self.__set_
      
  def _set_set_(self, v, load=False):
    """
    Setter method for set_, mapped from YANG variable /police_remark_profile/action/set (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=set_.set_, is_container='container', presence=False, yang_name="set", rest_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_.set_, is_container='container', presence=False, yang_name="set", rest_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__set_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_(self):
    self.__set_ = YANGDynClass(base=set_.set_, is_container='container', presence=False, yang_name="set", rest_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)


  def _get_map_(self):
    """
    Getter method for map_, mapped from YANG variable /police_remark_profile/action/map (container)
    """
    return self.__map_
      
  def _set_map_(self, v, load=False):
    """
    Setter method for map_, mapped from YANG variable /police_remark_profile/action/map (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=map_.map_, is_container='container', presence=False, yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=map_.map_, is_container='container', presence=False, yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__map_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_(self):
    self.__map_ = YANGDynClass(base=map_.map_, is_container='container', presence=False, yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)

  classification_type = __builtin__.property(_get_classification_type, _set_classification_type)
  action_type = __builtin__.property(_get_action_type, _set_action_type)
  set_ = __builtin__.property(_get_set_, _set_set_)
  map_ = __builtin__.property(_get_map_, _set_map_)


  _pyangbind_elements = {'classification_type': classification_type, 'action_type': action_type, 'set_': set_, 'map_': map_, }


