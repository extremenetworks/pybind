
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import isis_intf
class interface_detail(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/interface-detail. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: ISIS Interface info detail
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__isis_intf',)

  _yang_name = 'interface-detail'

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
    self.__isis_intf = YANGDynClass(base=YANGListType("intf_name",isis_intf.isis_intf, yang_name="isis-intf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='intf-name', extensions={u'tailf-common': {u'callpoint': u'isis-port-isis-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="isis-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-port-isis-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)

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
      return [u'isis-state', u'interface-detail']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'isis-state', u'interface-detail']

  def _get_isis_intf(self):
    """
    Getter method for isis_intf, mapped from YANG variable /isis_state/interface_detail/isis_intf (list)

    YANG Description: ISIS Interface configuration
    """
    return self.__isis_intf
      
  def _set_isis_intf(self, v, load=False):
    """
    Setter method for isis_intf, mapped from YANG variable /isis_state/interface_detail/isis_intf (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis_intf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis_intf() directly.

    YANG Description: ISIS Interface configuration
    """
    try:
      t = YANGDynClass(v,base=YANGListType("intf_name",isis_intf.isis_intf, yang_name="isis-intf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='intf-name', extensions={u'tailf-common': {u'callpoint': u'isis-port-isis-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="isis-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-port-isis-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis_intf must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("intf_name",isis_intf.isis_intf, yang_name="isis-intf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='intf-name', extensions={u'tailf-common': {u'callpoint': u'isis-port-isis-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="isis-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-port-isis-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)""",
        })

    self.__isis_intf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis_intf(self):
    self.__isis_intf = YANGDynClass(base=YANGListType("intf_name",isis_intf.isis_intf, yang_name="isis-intf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='intf-name', extensions={u'tailf-common': {u'callpoint': u'isis-port-isis-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="isis-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-port-isis-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)

  isis_intf = __builtin__.property(_get_isis_intf)


  _pyangbind_elements = {'isis_intf': isis_intf, }


