
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class native_vlan_classification(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile - based on the path /port-profile/vlan-profile/switchport/trunk/native-vlan-classification. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__native_vlan_id','__native_vlan_ctag_id',)

  _yang_name = 'native-vlan-classification'
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
    self.__native_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4091..8191']}), is_leaf=True, yang_name="native-vlan-id", rest_name="native-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'native-vlan'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='uint32', is_config=True)
    self.__native_vlan_ctag_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4094']}), is_leaf=True, yang_name="native-vlan-ctag-id", rest_name="ctag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'ctag'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='interface:dot1q-vlan-type', is_config=True)

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
      return [u'port-profile', u'vlan-profile', u'switchport', u'trunk', u'native-vlan-classification']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'port-profile', u'vlan-profile', u'switchport', u'trunk']

  def _get_native_vlan_id(self):
    """
    Getter method for native_vlan_id, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk/native_vlan_classification/native_vlan_id (uint32)
    """
    return self.__native_vlan_id
      
  def _set_native_vlan_id(self, v, load=False):
    """
    Setter method for native_vlan_id, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk/native_vlan_classification/native_vlan_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_native_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_native_vlan_id() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4091..8191']}), is_leaf=True, yang_name="native-vlan-id", rest_name="native-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'native-vlan'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """native_vlan_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4091..8191']}), is_leaf=True, yang_name="native-vlan-id", rest_name="native-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'native-vlan'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='uint32', is_config=True)""",
        })

    self.__native_vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_native_vlan_id(self):
    self.__native_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4091..8191']}), is_leaf=True, yang_name="native-vlan-id", rest_name="native-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'native-vlan'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='uint32', is_config=True)


  def _get_native_vlan_ctag_id(self):
    """
    Getter method for native_vlan_ctag_id, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk/native_vlan_classification/native_vlan_ctag_id (interface:dot1q-vlan-type)
    """
    return self.__native_vlan_ctag_id
      
  def _set_native_vlan_ctag_id(self, v, load=False):
    """
    Setter method for native_vlan_ctag_id, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk/native_vlan_classification/native_vlan_ctag_id (interface:dot1q-vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_native_vlan_ctag_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_native_vlan_ctag_id() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4094']}), is_leaf=True, yang_name="native-vlan-ctag-id", rest_name="ctag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'ctag'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='interface:dot1q-vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """native_vlan_ctag_id must be of a type compatible with interface:dot1q-vlan-type""",
          'defined-type': "interface:dot1q-vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4094']}), is_leaf=True, yang_name="native-vlan-ctag-id", rest_name="ctag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'ctag'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='interface:dot1q-vlan-type', is_config=True)""",
        })

    self.__native_vlan_ctag_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_native_vlan_ctag_id(self):
    self.__native_vlan_ctag_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4094']}), is_leaf=True, yang_name="native-vlan-ctag-id", rest_name="ctag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'ctag'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='interface:dot1q-vlan-type', is_config=True)

  native_vlan_id = __builtin__.property(_get_native_vlan_id, _set_native_vlan_id)
  native_vlan_ctag_id = __builtin__.property(_get_native_vlan_ctag_id, _set_native_vlan_ctag_id)


  _pyangbind_elements = {'native_vlan_id': native_vlan_id, 'native_vlan_ctag_id': native_vlan_ctag_id, }


