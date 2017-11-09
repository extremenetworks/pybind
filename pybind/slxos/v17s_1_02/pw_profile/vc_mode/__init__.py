
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vc_mode(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-pw-profile - based on the path /pw-profile/vc-mode. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Psuedo Wire type
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vc_mode',)

  _yang_name = 'vc-mode'
  _rest_name = 'vc-mode'

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
    self.__vc_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raw-passthrough': {'value': 3}, u'raw': {'value': 2}, u'tag': {'value': 1}},), default=unicode("raw"), is_leaf=True, yang_name="vc-mode", rest_name="vc-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pw-profile', defining_module='brocade-pw-profile', yang_type='enumeration', is_config=True)

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
      return [u'pw-profile', u'vc-mode']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'pw-profile', u'vc-mode']

  def _get_vc_mode(self):
    """
    Getter method for vc_mode, mapped from YANG variable /pw_profile/vc_mode/vc_mode (enumeration)

    YANG Description: The mode will be used during Psuedo Wire setup signalling process
    """
    return self.__vc_mode
      
  def _set_vc_mode(self, v, load=False):
    """
    Setter method for vc_mode, mapped from YANG variable /pw_profile/vc_mode/vc_mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vc_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vc_mode() directly.

    YANG Description: The mode will be used during Psuedo Wire setup signalling process
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raw-passthrough': {'value': 3}, u'raw': {'value': 2}, u'tag': {'value': 1}},), default=unicode("raw"), is_leaf=True, yang_name="vc-mode", rest_name="vc-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pw-profile', defining_module='brocade-pw-profile', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vc_mode must be of a type compatible with enumeration""",
          'defined-type': "brocade-pw-profile:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raw-passthrough': {'value': 3}, u'raw': {'value': 2}, u'tag': {'value': 1}},), default=unicode("raw"), is_leaf=True, yang_name="vc-mode", rest_name="vc-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pw-profile', defining_module='brocade-pw-profile', yang_type='enumeration', is_config=True)""",
        })

    self.__vc_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vc_mode(self):
    self.__vc_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raw-passthrough': {'value': 3}, u'raw': {'value': 2}, u'tag': {'value': 1}},), default=unicode("raw"), is_leaf=True, yang_name="vc-mode", rest_name="vc-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pw-profile', defining_module='brocade-pw-profile', yang_type='enumeration', is_config=True)

  vc_mode = __builtin__.property(_get_vc_mode, _set_vc_mode)


  _pyangbind_elements = {'vc_mode': vc_mode, }


