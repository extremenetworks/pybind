
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class set_cos_tc(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-policer - based on the path /policy-map/class/set/set_cos_tc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cos','__traffic_class',)

  _yang_name = 'set_cos_tc'
  _rest_name = ''

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
    self.__cos = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='uint8', is_config=True)
    self.__traffic_class = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='uint8', is_config=True)

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
      return [u'policy-map', u'class', u'set', u'set_cos_tc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'policy-map', u'class', u'set']

  def _get_cos(self):
    """
    Getter method for cos, mapped from YANG variable /policy_map/class/set/set_cos_tc/cos (uint8)
    """
    return self.__cos
      
  def _set_cos(self, v, load=False):
    """
    Setter method for cos, mapped from YANG variable /policy_map/class/set/set_cos_tc/cos (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='uint8', is_config=True)""",
        })

    self.__cos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos(self):
    self.__cos = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='uint8', is_config=True)


  def _get_traffic_class(self):
    """
    Getter method for traffic_class, mapped from YANG variable /policy_map/class/set/set_cos_tc/traffic_class (uint8)
    """
    return self.__traffic_class
      
  def _set_traffic_class(self, v, load=False):
    """
    Setter method for traffic_class, mapped from YANG variable /policy_map/class/set/set_cos_tc/traffic_class (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_traffic_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_traffic_class() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """traffic_class must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='uint8', is_config=True)""",
        })

    self.__traffic_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_traffic_class(self):
    self.__traffic_class = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='uint8', is_config=True)

  cos = __builtin__.property(_get_cos, _set_cos)
  traffic_class = __builtin__.property(_get_traffic_class, _set_traffic_class)


  _pyangbind_elements = {'cos': cos, 'traffic_class': traffic_class, }


