
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ipv6_global_cont(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/management/ipv6/ipv6-address-cont/ipv6-global-cont. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv6_global_address','__ipv6_global_address_eui64',)

  _yang_name = 'ipv6-global-cont'
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
    self.__ipv6_global_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-global-address", rest_name="ipv6-global-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='common-def:ipv6-address-prefix', is_config=True)
    self.__ipv6_global_address_eui64 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-global-address-eui64", rest_name="eui-64", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'eui-64'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)

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
      return [u'interface', u'management', u'ipv6', u'ipv6-address-cont', u'ipv6-global-cont']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Management', u'ipv6', u'address']

  def _get_ipv6_global_address(self):
    """
    Getter method for ipv6_global_address, mapped from YANG variable /interface/management/ipv6/ipv6_address_cont/ipv6_global_cont/ipv6_global_address (common-def:ipv6-address-prefix)

    YANG Description: IPv6 global address for this management 
interface.
    """
    return self.__ipv6_global_address
      
  def _set_ipv6_global_address(self, v, load=False):
    """
    Setter method for ipv6_global_address, mapped from YANG variable /interface/management/ipv6/ipv6_address_cont/ipv6_global_cont/ipv6_global_address (common-def:ipv6-address-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_global_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_global_address() directly.

    YANG Description: IPv6 global address for this management 
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-global-address", rest_name="ipv6-global-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='common-def:ipv6-address-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_global_address must be of a type compatible with common-def:ipv6-address-prefix""",
          'defined-type': "common-def:ipv6-address-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-global-address", rest_name="ipv6-global-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='common-def:ipv6-address-prefix', is_config=True)""",
        })

    self.__ipv6_global_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_global_address(self):
    self.__ipv6_global_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-global-address", rest_name="ipv6-global-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='common-def:ipv6-address-prefix', is_config=True)


  def _get_ipv6_global_address_eui64(self):
    """
    Getter method for ipv6_global_address_eui64, mapped from YANG variable /interface/management/ipv6/ipv6_address_cont/ipv6_global_cont/ipv6_global_address_eui64 (empty)
    """
    return self.__ipv6_global_address_eui64
      
  def _set_ipv6_global_address_eui64(self, v, load=False):
    """
    Setter method for ipv6_global_address_eui64, mapped from YANG variable /interface/management/ipv6/ipv6_address_cont/ipv6_global_cont/ipv6_global_address_eui64 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_global_address_eui64 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_global_address_eui64() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ipv6-global-address-eui64", rest_name="eui-64", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'eui-64'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_global_address_eui64 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-global-address-eui64", rest_name="eui-64", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'eui-64'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__ipv6_global_address_eui64 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_global_address_eui64(self):
    self.__ipv6_global_address_eui64 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6-global-address-eui64", rest_name="eui-64", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'eui-64'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)

  ipv6_global_address = __builtin__.property(_get_ipv6_global_address, _set_ipv6_global_address)
  ipv6_global_address_eui64 = __builtin__.property(_get_ipv6_global_address_eui64, _set_ipv6_global_address_eui64)


  _pyangbind_elements = {'ipv6_global_address': ipv6_global_address, 'ipv6_global_address_eui64': ipv6_global_address_eui64, }


