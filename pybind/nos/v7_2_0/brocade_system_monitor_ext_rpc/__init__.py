
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_system_monitor
class brocade_system_monitor_ext(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-system-monitor-ext - based on the path /brocade_system_monitor_ext_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This sub module defines show system-monitor data model
Copyright (c) 2011 by Brocade Communications Systems, Inc.
All rights reserved.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__show_system_monitor',)

  _yang_name = 'brocade-system-monitor-ext'
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
    self.__show_system_monitor = YANGDynClass(base=show_system_monitor.show_system_monitor, is_leaf=True, yang_name="show-system-monitor", rest_name="show-system-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-monitor-ext', defining_module='brocade-system-monitor-ext', yang_type='rpc', is_config=True)

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
      return [u'brocade_system_monitor_ext_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_show_system_monitor(self):
    """
    Getter method for show_system_monitor, mapped from YANG variable /brocade_system_monitor_ext_rpc/show_system_monitor (rpc)
    """
    return self.__show_system_monitor
      
  def _set_show_system_monitor(self, v, load=False):
    """
    Setter method for show_system_monitor, mapped from YANG variable /brocade_system_monitor_ext_rpc/show_system_monitor (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_system_monitor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_system_monitor() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=show_system_monitor.show_system_monitor, is_leaf=True, yang_name="show-system-monitor", rest_name="show-system-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-monitor-ext', defining_module='brocade-system-monitor-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_system_monitor must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=show_system_monitor.show_system_monitor, is_leaf=True, yang_name="show-system-monitor", rest_name="show-system-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-monitor-ext', defining_module='brocade-system-monitor-ext', yang_type='rpc', is_config=True)""",
        })

    self.__show_system_monitor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_system_monitor(self):
    self.__show_system_monitor = YANGDynClass(base=show_system_monitor.show_system_monitor, is_leaf=True, yang_name="show-system-monitor", rest_name="show-system-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-monitor-ext', defining_module='brocade-system-monitor-ext', yang_type='rpc', is_config=True)

  show_system_monitor = __builtin__.property(_get_show_system_monitor, _set_show_system_monitor)


  _pyangbind_elements = {'show_system_monitor': show_system_monitor, }


