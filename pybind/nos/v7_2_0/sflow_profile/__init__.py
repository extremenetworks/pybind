
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class sflow_profile(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sflow - based on the path /sflow-profile. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__profile_name','__profile_sampling_rate',)

  _yang_name = 'sflow-profile'
  _rest_name = 'sflow-profile'

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
    self.__profile_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="profile-name", rest_name="profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='profile-name-type', is_config=True)
    self.__profile_sampling_rate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'2..8388608']}), is_leaf=True, yang_name="profile-sampling-rate", rest_name="sampling-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'sampling-rate'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='uint32', is_config=True)

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
      return [u'sflow-profile']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'sflow-profile']

  def _get_profile_name(self):
    """
    Getter method for profile_name, mapped from YANG variable /sflow_profile/profile_name (profile-name-type)
    """
    return self.__profile_name
      
  def _set_profile_name(self, v, load=False):
    """
    Setter method for profile_name, mapped from YANG variable /sflow_profile/profile_name (profile-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_profile_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_profile_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="profile-name", rest_name="profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='profile-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """profile_name must be of a type compatible with profile-name-type""",
          'defined-type': "brocade-sflow:profile-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="profile-name", rest_name="profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='profile-name-type', is_config=True)""",
        })

    self.__profile_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_profile_name(self):
    self.__profile_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="profile-name", rest_name="profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='profile-name-type', is_config=True)


  def _get_profile_sampling_rate(self):
    """
    Getter method for profile_sampling_rate, mapped from YANG variable /sflow_profile/profile_sampling_rate (uint32)
    """
    return self.__profile_sampling_rate
      
  def _set_profile_sampling_rate(self, v, load=False):
    """
    Setter method for profile_sampling_rate, mapped from YANG variable /sflow_profile/profile_sampling_rate (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_profile_sampling_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_profile_sampling_rate() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'2..8388608']}), is_leaf=True, yang_name="profile-sampling-rate", rest_name="sampling-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'sampling-rate'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """profile_sampling_rate must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'2..8388608']}), is_leaf=True, yang_name="profile-sampling-rate", rest_name="sampling-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'sampling-rate'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='uint32', is_config=True)""",
        })

    self.__profile_sampling_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_profile_sampling_rate(self):
    self.__profile_sampling_rate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'2..8388608']}), is_leaf=True, yang_name="profile-sampling-rate", rest_name="sampling-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'sampling-rate'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='uint32', is_config=True)

  profile_name = __builtin__.property(_get_profile_name, _set_profile_name)
  profile_sampling_rate = __builtin__.property(_get_profile_sampling_rate, _set_profile_sampling_rate)


  _pyangbind_elements = {'profile_name': profile_name, 'profile_sampling_rate': profile_sampling_rate, }


