
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class last_config_update_time_for_xpaths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vcs - based on the path /brocade_vcs_rpc/get-last-config-update-time-for-xpaths/output/last-config-update-time-for-xpaths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__xpath_string','__last_config_update_time',)

  _yang_name = 'last-config-update-time-for-xpaths'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
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
    self.__last_config_update_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-config-update-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='uint64', is_config=True)
    self.__xpath_string = YANGDynClass(base=unicode, is_leaf=True, yang_name="xpath-string", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)

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
      return [u'brocade_vcs_rpc', u'get-last-config-update-time-for-xpaths', u'output', u'last-config-update-time-for-xpaths']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'get-last-config-update-time-for-xpaths', u'output', u'last-config-update-time-for-xpaths']

  def _get_xpath_string(self):
    """
    Getter method for xpath_string, mapped from YANG variable /brocade_vcs_rpc/get_last_config_update_time_for_xpaths/output/last_config_update_time_for_xpaths/xpath_string (string)
    """
    return self.__xpath_string
      
  def _set_xpath_string(self, v, load=False):
    """
    Setter method for xpath_string, mapped from YANG variable /brocade_vcs_rpc/get_last_config_update_time_for_xpaths/output/last_config_update_time_for_xpaths/xpath_string (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_xpath_string is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_xpath_string() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="xpath-string", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """xpath_string must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="xpath-string", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)""",
        })

    self.__xpath_string = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_xpath_string(self):
    self.__xpath_string = YANGDynClass(base=unicode, is_leaf=True, yang_name="xpath-string", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)


  def _get_last_config_update_time(self):
    """
    Getter method for last_config_update_time, mapped from YANG variable /brocade_vcs_rpc/get_last_config_update_time_for_xpaths/output/last_config_update_time_for_xpaths/last_config_update_time (uint64)
    """
    return self.__last_config_update_time
      
  def _set_last_config_update_time(self, v, load=False):
    """
    Setter method for last_config_update_time, mapped from YANG variable /brocade_vcs_rpc/get_last_config_update_time_for_xpaths/output/last_config_update_time_for_xpaths/last_config_update_time (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_config_update_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_config_update_time() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-config-update-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_config_update_time must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-config-update-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='uint64', is_config=True)""",
        })

    self.__last_config_update_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_config_update_time(self):
    self.__last_config_update_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-config-update-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='uint64', is_config=True)

  xpath_string = __builtin__.property(_get_xpath_string, _set_xpath_string)
  last_config_update_time = __builtin__.property(_get_last_config_update_time, _set_last_config_update_time)


  _pyangbind_elements = {'xpath_string': xpath_string, 'last_config_update_time': last_config_update_time, }


