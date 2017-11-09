
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class adjustment_threshold(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/autobw-template/adjustment-threshold. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__threshold_percentage','__use_threshold_table',)

  _yang_name = 'adjustment-threshold'
  _rest_name = 'adjustment-threshold'

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
    self.__threshold_percentage = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="threshold-percentage", rest_name="threshold-percentage", parent=self, choice=(u'threshold-options', u'threshold-case-percentage'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__use_threshold_table = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="use-threshold-table", rest_name="use-threshold-table", parent=self, choice=(u'threshold-options', u'threshold-case-table'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'autobw-template', u'adjustment-threshold']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'autobw-template', u'adjustment-threshold']

  def _get_threshold_percentage(self):
    """
    Getter method for threshold_percentage, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/adjustment_threshold/threshold_percentage (uint32)
    """
    return self.__threshold_percentage
      
  def _set_threshold_percentage(self, v, load=False):
    """
    Setter method for threshold_percentage, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/adjustment_threshold/threshold_percentage (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_threshold_percentage is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_threshold_percentage() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="threshold-percentage", rest_name="threshold-percentage", parent=self, choice=(u'threshold-options', u'threshold-case-percentage'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """threshold_percentage must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="threshold-percentage", rest_name="threshold-percentage", parent=self, choice=(u'threshold-options', u'threshold-case-percentage'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__threshold_percentage = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_threshold_percentage(self):
    self.__threshold_percentage = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..100']}), is_leaf=True, yang_name="threshold-percentage", rest_name="threshold-percentage", parent=self, choice=(u'threshold-options', u'threshold-case-percentage'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_use_threshold_table(self):
    """
    Getter method for use_threshold_table, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/adjustment_threshold/use_threshold_table (empty)
    """
    return self.__use_threshold_table
      
  def _set_use_threshold_table(self, v, load=False):
    """
    Setter method for use_threshold_table, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/adjustment_threshold/use_threshold_table (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_use_threshold_table is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_use_threshold_table() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="use-threshold-table", rest_name="use-threshold-table", parent=self, choice=(u'threshold-options', u'threshold-case-table'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """use_threshold_table must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="use-threshold-table", rest_name="use-threshold-table", parent=self, choice=(u'threshold-options', u'threshold-case-table'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__use_threshold_table = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_use_threshold_table(self):
    self.__use_threshold_table = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="use-threshold-table", rest_name="use-threshold-table", parent=self, choice=(u'threshold-options', u'threshold-case-table'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

  threshold_percentage = __builtin__.property(_get_threshold_percentage, _set_threshold_percentage)
  use_threshold_table = __builtin__.property(_get_use_threshold_table, _set_use_threshold_table)

  __choices__ = {u'threshold-options': {u'threshold-case-percentage': [u'threshold_percentage'], u'threshold-case-table': [u'use_threshold_table']}}
  _pyangbind_elements = {'threshold_percentage': threshold_percentage, 'use_threshold_table': use_threshold_table, }


