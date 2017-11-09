
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class mark(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos - based on the path /qos/map/dscp-mutation/mark. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dscp_in_values','__to',)

  _yang_name = 'mark'
  _rest_name = 'mark'

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
    self.__to = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 63']}), is_leaf=True, yang_name="to", rest_name="to", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__dscp_in_values = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9])|([1-5][0-9])|(6[0-3]))(-(([0-9])|([1-5][0-9])|(6[0-3])))?((,(([0-9])|([1-5][0-9])|(6[0-3]))(-(([0-9])|([1-5][0-9])|(6[0-3])))?)?)*'}), is_leaf=True, yang_name="dscp-in-values", rest_name="dscp-in-values", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='UI32DscpMutationRange', is_config=True)

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
      return [u'qos', u'map', u'dscp-mutation', u'mark']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos', u'map', u'dscp-mutation', u'mark']

  def _get_dscp_in_values(self):
    """
    Getter method for dscp_in_values, mapped from YANG variable /qos/map/dscp_mutation/mark/dscp_in_values (UI32DscpMutationRange)
    """
    return self.__dscp_in_values
      
  def _set_dscp_in_values(self, v, load=False):
    """
    Setter method for dscp_in_values, mapped from YANG variable /qos/map/dscp_mutation/mark/dscp_in_values (UI32DscpMutationRange)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_in_values is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_in_values() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9])|([1-5][0-9])|(6[0-3]))(-(([0-9])|([1-5][0-9])|(6[0-3])))?((,(([0-9])|([1-5][0-9])|(6[0-3]))(-(([0-9])|([1-5][0-9])|(6[0-3])))?)?)*'}), is_leaf=True, yang_name="dscp-in-values", rest_name="dscp-in-values", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='UI32DscpMutationRange', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_in_values must be of a type compatible with UI32DscpMutationRange""",
          'defined-type': "brocade-qos:UI32DscpMutationRange",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9])|([1-5][0-9])|(6[0-3]))(-(([0-9])|([1-5][0-9])|(6[0-3])))?((,(([0-9])|([1-5][0-9])|(6[0-3]))(-(([0-9])|([1-5][0-9])|(6[0-3])))?)?)*'}), is_leaf=True, yang_name="dscp-in-values", rest_name="dscp-in-values", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='UI32DscpMutationRange', is_config=True)""",
        })

    self.__dscp_in_values = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_in_values(self):
    self.__dscp_in_values = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9])|([1-5][0-9])|(6[0-3]))(-(([0-9])|([1-5][0-9])|(6[0-3])))?((,(([0-9])|([1-5][0-9])|(6[0-3]))(-(([0-9])|([1-5][0-9])|(6[0-3])))?)?)*'}), is_leaf=True, yang_name="dscp-in-values", rest_name="dscp-in-values", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='UI32DscpMutationRange', is_config=True)


  def _get_to(self):
    """
    Getter method for to, mapped from YANG variable /qos/map/dscp_mutation/mark/to (int32)

    YANG Description: 0-63;;Dscp Mutation Out
    """
    return self.__to
      
  def _set_to(self, v, load=False):
    """
    Setter method for to, mapped from YANG variable /qos/map/dscp_mutation/mark/to (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_to is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_to() directly.

    YANG Description: 0-63;;Dscp Mutation Out
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 63']}), is_leaf=True, yang_name="to", rest_name="to", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """to must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 63']}), is_leaf=True, yang_name="to", rest_name="to", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__to = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_to(self):
    self.__to = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 63']}), is_leaf=True, yang_name="to", rest_name="to", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)

  dscp_in_values = __builtin__.property(_get_dscp_in_values, _set_dscp_in_values)
  to = __builtin__.property(_get_to, _set_to)


  _pyangbind_elements = {'dscp_in_values': dscp_in_values, 'to': to, }


