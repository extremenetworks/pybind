
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class fcoe_fip_advertisement(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fcoe - based on the path /fcoe/fcoe-fabric-map/fcoe-fip-advertisement. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This provides the grouping of all FIP configuration
elements.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__fcoe_fip_advertisement_interval',)

  _yang_name = 'fcoe-fip-advertisement'

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
    self.__fcoe_fip_advertisement_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'250..90000']}), is_leaf=True, yang_name="fcoe-fip-advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure the FIP Advertisement interval', u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='int32', is_config=True)

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
      return [u'fcoe', u'fcoe-fabric-map', u'fcoe-fip-advertisement']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'fcoe', u'fabric-map', u'advertisement']

  def _get_fcoe_fip_advertisement_interval(self):
    """
    Getter method for fcoe_fip_advertisement_interval, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fip_advertisement/fcoe_fip_advertisement_interval (int32)

    YANG Description: This specifies the FCoE advertisement interval.
    """
    return self.__fcoe_fip_advertisement_interval
      
  def _set_fcoe_fip_advertisement_interval(self, v, load=False):
    """
    Setter method for fcoe_fip_advertisement_interval, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fip_advertisement/fcoe_fip_advertisement_interval (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_fip_advertisement_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_fip_advertisement_interval() directly.

    YANG Description: This specifies the FCoE advertisement interval.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'250..90000']}), is_leaf=True, yang_name="fcoe-fip-advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure the FIP Advertisement interval', u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_fip_advertisement_interval must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'250..90000']}), is_leaf=True, yang_name="fcoe-fip-advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure the FIP Advertisement interval', u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='int32', is_config=True)""",
        })

    self.__fcoe_fip_advertisement_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_fip_advertisement_interval(self):
    self.__fcoe_fip_advertisement_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'250..90000']}), is_leaf=True, yang_name="fcoe-fip-advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure the FIP Advertisement interval', u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='int32', is_config=True)

  fcoe_fip_advertisement_interval = __builtin__.property(_get_fcoe_fip_advertisement_interval, _set_fcoe_fip_advertisement_interval)


  _pyangbind_elements = {'fcoe_fip_advertisement_interval': fcoe_fip_advertisement_interval, }


