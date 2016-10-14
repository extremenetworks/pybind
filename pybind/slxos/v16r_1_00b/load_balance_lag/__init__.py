
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import load_balance
import lag
class load_balance_lag(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge-lag - based on the path /load-balance-lag. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__load_balance','__lag',)

  _yang_name = 'load-balance-lag'

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
    self.__load_balance = YANGDynClass(base=load_balance.load_balance, is_container='container', yang_name="load-balance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'load-balance'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    self.__lag = YANGDynClass(base=lag.lag, is_container='container', yang_name="lag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'lag'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)

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
      return [u'load-balance-lag']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return []

  def _get_load_balance(self):
    """
    Getter method for load_balance, mapped from YANG variable /load_balance_lag/load_balance (container)
    """
    return self.__load_balance
      
  def _set_load_balance(self, v, load=False):
    """
    Setter method for load_balance, mapped from YANG variable /load_balance_lag/load_balance (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_load_balance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_load_balance() directly.
    """
    try:
      t = YANGDynClass(v,base=load_balance.load_balance, is_container='container', yang_name="load-balance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'load-balance'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """load_balance must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=load_balance.load_balance, is_container='container', yang_name="load-balance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'load-balance'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)""",
        })

    self.__load_balance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_load_balance(self):
    self.__load_balance = YANGDynClass(base=load_balance.load_balance, is_container='container', yang_name="load-balance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'load-balance'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)


  def _get_lag(self):
    """
    Getter method for lag, mapped from YANG variable /load_balance_lag/lag (container)
    """
    return self.__lag
      
  def _set_lag(self, v, load=False):
    """
    Setter method for lag, mapped from YANG variable /load_balance_lag/lag (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lag() directly.
    """
    try:
      t = YANGDynClass(v,base=lag.lag, is_container='container', yang_name="lag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'lag'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lag must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=lag.lag, is_container='container', yang_name="lag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'lag'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)""",
        })

    self.__lag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lag(self):
    self.__lag = YANGDynClass(base=lag.lag, is_container='container', yang_name="lag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'lag'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)

  load_balance = __builtin__.property(_get_load_balance, _set_load_balance)
  lag = __builtin__.property(_get_lag, _set_lag)


  _pyangbind_elements = {'load_balance': load_balance, 'lag': lag, }


