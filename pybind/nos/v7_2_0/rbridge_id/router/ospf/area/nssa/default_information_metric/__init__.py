
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class default_information_metric(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/ospf/area/nssa/default-information-metric. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This parameter generates a default route into an NSSA. If no-summary option is enabled then a type-3 default LSA will be generated into NSSA else a type-7 LSA will begenerated into NSSA. By default the default-information-origiante parameter is not set.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__default_information_metric_value','__default_information_metric_type',)

  _yang_name = 'default-information-metric'
  _rest_name = 'default-information-metric'

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
    self.__default_information_metric_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="default-information-metric-value", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    self.__default_information_metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type1': {'value': 1}, u'type2': {'value': 2}},), is_leaf=True, yang_name="default-information-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf:metric-type', is_config=True)

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
      return [u'rbridge-id', u'router', u'ospf', u'area', u'nssa', u'default-information-metric']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'ospf', u'area', u'nssa', u'default-information-metric']

  def _get_default_information_metric_value(self):
    """
    Getter method for default_information_metric_value, mapped from YANG variable /rbridge_id/router/ospf/area/nssa/default_information_metric/default_information_metric_value (uint32)

    YANG Description: This parameter specifies the cost of the default LSA originated into the NSSA area.The range is 1 to 16777215. There is no default.
    """
    return self.__default_information_metric_value
      
  def _set_default_information_metric_value(self, v, load=False):
    """
    Setter method for default_information_metric_value, mapped from YANG variable /rbridge_id/router/ospf/area/nssa/default_information_metric/default_information_metric_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_information_metric_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_information_metric_value() directly.

    YANG Description: This parameter specifies the cost of the default LSA originated into the NSSA area.The range is 1 to 16777215. There is no default.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="default-information-metric-value", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_information_metric_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="default-information-metric-value", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)""",
        })

    self.__default_information_metric_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_information_metric_value(self):
    self.__default_information_metric_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="default-information-metric-value", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)


  def _get_default_information_metric_type(self):
    """
    Getter method for default_information_metric_type, mapped from YANG variable /rbridge_id/router/ospf/area/nssa/default_information_metric/default_information_metric_type (ospf:metric-type)

    YANG Description: The metric-type parameter specifies the type of the default external LSA originated into the NSSA area. It can be either type-1 or type-2. The default is type-1.
    """
    return self.__default_information_metric_type
      
  def _set_default_information_metric_type(self, v, load=False):
    """
    Setter method for default_information_metric_type, mapped from YANG variable /rbridge_id/router/ospf/area/nssa/default_information_metric/default_information_metric_type (ospf:metric-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_information_metric_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_information_metric_type() directly.

    YANG Description: The metric-type parameter specifies the type of the default external LSA originated into the NSSA area. It can be either type-1 or type-2. The default is type-1.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type1': {'value': 1}, u'type2': {'value': 2}},), is_leaf=True, yang_name="default-information-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf:metric-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_information_metric_type must be of a type compatible with ospf:metric-type""",
          'defined-type': "ospf:metric-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type1': {'value': 1}, u'type2': {'value': 2}},), is_leaf=True, yang_name="default-information-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf:metric-type', is_config=True)""",
        })

    self.__default_information_metric_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_information_metric_type(self):
    self.__default_information_metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type1': {'value': 1}, u'type2': {'value': 2}},), is_leaf=True, yang_name="default-information-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf:metric-type', is_config=True)

  default_information_metric_value = __builtin__.property(_get_default_information_metric_value, _set_default_information_metric_value)
  default_information_metric_type = __builtin__.property(_get_default_information_metric_type, _set_default_information_metric_type)


  _pyangbind_elements = {'default_information_metric_value': default_information_metric_value, 'default_information_metric_type': default_information_metric_type, }


