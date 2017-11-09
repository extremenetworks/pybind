
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class access_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ip/receive/access-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ip_access_list','__ip_direction',)

  _yang_name = 'access-group'
  _rest_name = 'access-group'

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
    self.__ip_access_list = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="ip-access-list", rest_name="ip-access-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='l3-acl-policy-name', is_config=True)
    self.__ip_direction = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in': {'value': 1}},), is_leaf=True, yang_name="ip-direction", rest_name="ip-direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)

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
      return [u'rbridge-id', u'ip', u'receive', u'access-group']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ip', u'receive', u'access-group']

  def _get_ip_access_list(self):
    """
    Getter method for ip_access_list, mapped from YANG variable /rbridge_id/ip/receive/access_group/ip_access_list (l3-acl-policy-name)
    """
    return self.__ip_access_list
      
  def _set_ip_access_list(self, v, load=False):
    """
    Setter method for ip_access_list, mapped from YANG variable /rbridge_id/ip/receive/access_group/ip_access_list (l3-acl-policy-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_access_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_access_list() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="ip-access-list", rest_name="ip-access-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='l3-acl-policy-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_access_list must be of a type compatible with l3-acl-policy-name""",
          'defined-type': "brocade-ip-access-list:l3-acl-policy-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="ip-access-list", rest_name="ip-access-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='l3-acl-policy-name', is_config=True)""",
        })

    self.__ip_access_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_access_list(self):
    self.__ip_access_list = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="ip-access-list", rest_name="ip-access-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='l3-acl-policy-name', is_config=True)


  def _get_ip_direction(self):
    """
    Getter method for ip_direction, mapped from YANG variable /rbridge_id/ip/receive/access_group/ip_direction (enumeration)
    """
    return self.__ip_direction
      
  def _set_ip_direction(self, v, load=False):
    """
    Setter method for ip_direction, mapped from YANG variable /rbridge_id/ip/receive/access_group/ip_direction (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_direction is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_direction() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in': {'value': 1}},), is_leaf=True, yang_name="ip-direction", rest_name="ip-direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_direction must be of a type compatible with enumeration""",
          'defined-type': "brocade-ip-access-list:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in': {'value': 1}},), is_leaf=True, yang_name="ip-direction", rest_name="ip-direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)""",
        })

    self.__ip_direction = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_direction(self):
    self.__ip_direction = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in': {'value': 1}},), is_leaf=True, yang_name="ip-direction", rest_name="ip-direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)

  ip_access_list = __builtin__.property(_get_ip_access_list, _set_ip_access_list)
  ip_direction = __builtin__.property(_get_ip_direction, _set_ip_direction)


  _pyangbind_elements = {'ip_access_list': ip_access_list, 'ip_direction': ip_direction, }


