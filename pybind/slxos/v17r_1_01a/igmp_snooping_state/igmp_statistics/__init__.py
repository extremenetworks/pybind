
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import igmp_statistics_
class igmp_statistics(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mc-hms-operational - based on the path /igmp-snooping-state/igmp-statistics. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Igmp snooping statistics
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__igmp_statistics',)

  _yang_name = 'igmp-statistics'
  _rest_name = 'igmp-statistics'

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
    self.__igmp_statistics = YANGDynClass(base=YANGListType("interface_name",igmp_statistics_.igmp_statistics, yang_name="igmp-statistics", rest_name="igmp-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-name', extensions=None), is_container='list', yang_name="igmp-statistics", rest_name="igmp-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)

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
      return [u'igmp-snooping-state', u'igmp-statistics']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'igmp-snooping-state', u'igmp-statistics']

  def _get_igmp_statistics(self):
    """
    Getter method for igmp_statistics, mapped from YANG variable /igmp_snooping_state/igmp_statistics/igmp_statistics (list)
    """
    return self.__igmp_statistics
      
  def _set_igmp_statistics(self, v, load=False):
    """
    Setter method for igmp_statistics, mapped from YANG variable /igmp_snooping_state/igmp_statistics/igmp_statistics (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmp_statistics is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmp_statistics() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("interface_name",igmp_statistics_.igmp_statistics, yang_name="igmp-statistics", rest_name="igmp-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-name', extensions=None), is_container='list', yang_name="igmp-statistics", rest_name="igmp-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmp_statistics must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("interface_name",igmp_statistics_.igmp_statistics, yang_name="igmp-statistics", rest_name="igmp-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-name', extensions=None), is_container='list', yang_name="igmp-statistics", rest_name="igmp-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)""",
        })

    self.__igmp_statistics = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmp_statistics(self):
    self.__igmp_statistics = YANGDynClass(base=YANGListType("interface_name",igmp_statistics_.igmp_statistics, yang_name="igmp-statistics", rest_name="igmp-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-name', extensions=None), is_container='list', yang_name="igmp-statistics", rest_name="igmp-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)

  igmp_statistics = __builtin__.property(_get_igmp_statistics)


  _pyangbind_elements = {'igmp_statistics': igmp_statistics, }


