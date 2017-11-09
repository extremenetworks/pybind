
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class red_profile(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mls - based on the path /qos/red-profile. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__profile_id','__min_threshold','__max_threshold','__drop_probability',)

  _yang_name = 'red-profile'
  _rest_name = 'red-profile'

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
    self.__min_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="min-threshold", rest_name="min-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='int32', is_config=True)
    self.__profile_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 383']}), is_leaf=True, yang_name="profile-id", rest_name="profile-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='red-profile-id-type', is_config=True)
    self.__drop_probability = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="drop-probability", rest_name="drop-probability", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='int32', is_config=True)
    self.__max_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="max-threshold", rest_name="max-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='int32', is_config=True)

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
      return [u'qos', u'red-profile']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos', u'red-profile']

  def _get_profile_id(self):
    """
    Getter method for profile_id, mapped from YANG variable /qos/red_profile/profile_id (red-profile-id-type)
    """
    return self.__profile_id
      
  def _set_profile_id(self, v, load=False):
    """
    Setter method for profile_id, mapped from YANG variable /qos/red_profile/profile_id (red-profile-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_profile_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_profile_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 383']}), is_leaf=True, yang_name="profile-id", rest_name="profile-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='red-profile-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """profile_id must be of a type compatible with red-profile-id-type""",
          'defined-type': "brocade-qos-mls:red-profile-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 383']}), is_leaf=True, yang_name="profile-id", rest_name="profile-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='red-profile-id-type', is_config=True)""",
        })

    self.__profile_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_profile_id(self):
    self.__profile_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 383']}), is_leaf=True, yang_name="profile-id", rest_name="profile-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='red-profile-id-type', is_config=True)


  def _get_min_threshold(self):
    """
    Getter method for min_threshold, mapped from YANG variable /qos/red_profile/min_threshold (int32)
    """
    return self.__min_threshold
      
  def _set_min_threshold(self, v, load=False):
    """
    Setter method for min_threshold, mapped from YANG variable /qos/red_profile/min_threshold (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_min_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_min_threshold() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="min-threshold", rest_name="min-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """min_threshold must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="min-threshold", rest_name="min-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='int32', is_config=True)""",
        })

    self.__min_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_min_threshold(self):
    self.__min_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="min-threshold", rest_name="min-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='int32', is_config=True)


  def _get_max_threshold(self):
    """
    Getter method for max_threshold, mapped from YANG variable /qos/red_profile/max_threshold (int32)
    """
    return self.__max_threshold
      
  def _set_max_threshold(self, v, load=False):
    """
    Setter method for max_threshold, mapped from YANG variable /qos/red_profile/max_threshold (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_threshold() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="max-threshold", rest_name="max-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_threshold must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="max-threshold", rest_name="max-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='int32', is_config=True)""",
        })

    self.__max_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_threshold(self):
    self.__max_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="max-threshold", rest_name="max-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='int32', is_config=True)


  def _get_drop_probability(self):
    """
    Getter method for drop_probability, mapped from YANG variable /qos/red_profile/drop_probability (int32)
    """
    return self.__drop_probability
      
  def _set_drop_probability(self, v, load=False):
    """
    Setter method for drop_probability, mapped from YANG variable /qos/red_profile/drop_probability (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_drop_probability is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_drop_probability() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="drop-probability", rest_name="drop-probability", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """drop_probability must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="drop-probability", rest_name="drop-probability", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='int32', is_config=True)""",
        })

    self.__drop_probability = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_drop_probability(self):
    self.__drop_probability = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="drop-probability", rest_name="drop-probability", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='int32', is_config=True)

  profile_id = __builtin__.property(_get_profile_id, _set_profile_id)
  min_threshold = __builtin__.property(_get_min_threshold, _set_min_threshold)
  max_threshold = __builtin__.property(_get_max_threshold, _set_max_threshold)
  drop_probability = __builtin__.property(_get_drop_probability, _set_drop_probability)


  _pyangbind_elements = {'profile_id': profile_id, 'min_threshold': min_threshold, 'max_threshold': max_threshold, 'drop_probability': drop_probability, }


