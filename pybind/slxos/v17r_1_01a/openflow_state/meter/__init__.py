
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import meter_info_list
class meter(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/meter. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Meter
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__num_of_meters','__meter_info_list',)

  _yang_name = 'meter'
  _rest_name = 'meter'

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
    self.__meter_info_list = YANGDynClass(base=YANGListType("meter_id",meter_info_list.meter_info_list, yang_name="meter-info-list", rest_name="meter-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='meter-id', extensions=None), is_container='list', yang_name="meter-info-list", rest_name="meter-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    self.__num_of_meters = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-meters", rest_name="num-of-meters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)

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
      return [u'openflow-state', u'meter']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'meter']

  def _get_num_of_meters(self):
    """
    Getter method for num_of_meters, mapped from YANG variable /openflow_state/meter/num_of_meters (uint32)

    YANG Description: Number of Meters
    """
    return self.__num_of_meters
      
  def _set_num_of_meters(self, v, load=False):
    """
    Setter method for num_of_meters, mapped from YANG variable /openflow_state/meter/num_of_meters (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_of_meters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_of_meters() directly.

    YANG Description: Number of Meters
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-meters", rest_name="num-of-meters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_of_meters must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-meters", rest_name="num-of-meters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_of_meters = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_of_meters(self):
    self.__num_of_meters = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-meters", rest_name="num-of-meters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_meter_info_list(self):
    """
    Getter method for meter_info_list, mapped from YANG variable /openflow_state/meter/meter_info_list (list)
    """
    return self.__meter_info_list
      
  def _set_meter_info_list(self, v, load=False):
    """
    Setter method for meter_info_list, mapped from YANG variable /openflow_state/meter/meter_info_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_meter_info_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_meter_info_list() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("meter_id",meter_info_list.meter_info_list, yang_name="meter-info-list", rest_name="meter-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='meter-id', extensions=None), is_container='list', yang_name="meter-info-list", rest_name="meter-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """meter_info_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("meter_id",meter_info_list.meter_info_list, yang_name="meter-info-list", rest_name="meter-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='meter-id', extensions=None), is_container='list', yang_name="meter-info-list", rest_name="meter-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)""",
        })

    self.__meter_info_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_meter_info_list(self):
    self.__meter_info_list = YANGDynClass(base=YANGListType("meter_id",meter_info_list.meter_info_list, yang_name="meter-info-list", rest_name="meter-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='meter-id', extensions=None), is_container='list', yang_name="meter-info-list", rest_name="meter-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)

  num_of_meters = __builtin__.property(_get_num_of_meters)
  meter_info_list = __builtin__.property(_get_meter_info_list)


  _pyangbind_elements = {'num_of_meters': num_of_meters, 'meter_info_list': meter_info_list, }


