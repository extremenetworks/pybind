
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class syslog_facility(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ras - based on the path /logging/syslog-facility. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__local_',)

  _yang_name = 'syslog-facility'
  _rest_name = 'syslog-facility'

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
    self.__local_ = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LOG_LOCAL4': {'value': 4}, u'LOG_LOCAL5': {'value': 5}, u'LOG_LOCAL6': {'value': 6}, u'LOG_LOCAL7': {'value': 7}, u'LOG_LOCAL0': {'value': 0}, u'LOG_LOCAL1': {'value': 1}, u'LOG_LOCAL2': {'value': 2}, u'LOG_LOCAL3': {'value': 3}},), is_leaf=True, yang_name="local", rest_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='facility-enum', is_config=True)

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
      return [u'logging', u'syslog-facility']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'logging', u'syslog-facility']

  def _get_local_(self):
    """
    Getter method for local_, mapped from YANG variable /logging/syslog_facility/local (facility-enum)
    """
    return self.__local_
      
  def _set_local_(self, v, load=False):
    """
    Setter method for local_, mapped from YANG variable /logging/syslog_facility/local (facility-enum)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LOG_LOCAL4': {'value': 4}, u'LOG_LOCAL5': {'value': 5}, u'LOG_LOCAL6': {'value': 6}, u'LOG_LOCAL7': {'value': 7}, u'LOG_LOCAL0': {'value': 0}, u'LOG_LOCAL1': {'value': 1}, u'LOG_LOCAL2': {'value': 2}, u'LOG_LOCAL3': {'value': 3}},), is_leaf=True, yang_name="local", rest_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='facility-enum', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ must be of a type compatible with facility-enum""",
          'defined-type': "brocade-ras:facility-enum",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LOG_LOCAL4': {'value': 4}, u'LOG_LOCAL5': {'value': 5}, u'LOG_LOCAL6': {'value': 6}, u'LOG_LOCAL7': {'value': 7}, u'LOG_LOCAL0': {'value': 0}, u'LOG_LOCAL1': {'value': 1}, u'LOG_LOCAL2': {'value': 2}, u'LOG_LOCAL3': {'value': 3}},), is_leaf=True, yang_name="local", rest_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='facility-enum', is_config=True)""",
        })

    self.__local_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_(self):
    self.__local_ = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LOG_LOCAL4': {'value': 4}, u'LOG_LOCAL5': {'value': 5}, u'LOG_LOCAL6': {'value': 6}, u'LOG_LOCAL7': {'value': 7}, u'LOG_LOCAL0': {'value': 0}, u'LOG_LOCAL1': {'value': 1}, u'LOG_LOCAL2': {'value': 2}, u'LOG_LOCAL3': {'value': 3}},), is_leaf=True, yang_name="local", rest_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='facility-enum', is_config=True)

  local_ = __builtin__.property(_get_local_, _set_local_)


  _pyangbind_elements = {'local_': local_, }


