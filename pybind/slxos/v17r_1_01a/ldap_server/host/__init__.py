
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ldap_server_options
class host(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-aaa - based on the path /ldap-server/host. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__hostname','__use_vrf','__ldap_server_options',)

  _yang_name = 'host'
  _rest_name = 'host'

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
    self.__ldap_server_options = YANGDynClass(base=ldap_server_options.ldap_server_options, is_container='container', presence=False, yang_name="ldap-server-options", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)
    self.__hostname = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'\\p{IsBasicLatin}{0,255}', 'length': [u'1..max']}), is_leaf=True, yang_name="hostname", rest_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'INETADDRESS   Domain name or IP Address of\n this LDAP server'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    self.__use_vrf = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="use-vrf", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF to choose for server connection\n(Default=mgmt-vrf)', u'cli-optional-in-sequence': None, u'key-default': u'mgmt-vrf', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='common-def:vrf-name', is_config=True)

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
      return [u'ldap-server', u'host']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ldap-server', u'host']

  def _get_hostname(self):
    """
    Getter method for hostname, mapped from YANG variable /ldap_server/host/hostname (string)
    """
    return self.__hostname
      
  def _set_hostname(self, v, load=False):
    """
    Setter method for hostname, mapped from YANG variable /ldap_server/host/hostname (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hostname is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hostname() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'\\p{IsBasicLatin}{0,255}', 'length': [u'1..max']}), is_leaf=True, yang_name="hostname", rest_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'INETADDRESS   Domain name or IP Address of\n this LDAP server'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hostname must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'\\p{IsBasicLatin}{0,255}', 'length': [u'1..max']}), is_leaf=True, yang_name="hostname", rest_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'INETADDRESS   Domain name or IP Address of\n this LDAP server'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)""",
        })

    self.__hostname = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hostname(self):
    self.__hostname = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'\\p{IsBasicLatin}{0,255}', 'length': [u'1..max']}), is_leaf=True, yang_name="hostname", rest_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'INETADDRESS   Domain name or IP Address of\n this LDAP server'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)


  def _get_use_vrf(self):
    """
    Getter method for use_vrf, mapped from YANG variable /ldap_server/host/use_vrf (common-def:vrf-name)
    """
    return self.__use_vrf
      
  def _set_use_vrf(self, v, load=False):
    """
    Setter method for use_vrf, mapped from YANG variable /ldap_server/host/use_vrf (common-def:vrf-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_use_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_use_vrf() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="use-vrf", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF to choose for server connection\n(Default=mgmt-vrf)', u'cli-optional-in-sequence': None, u'key-default': u'mgmt-vrf', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='common-def:vrf-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """use_vrf must be of a type compatible with common-def:vrf-name""",
          'defined-type': "common-def:vrf-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="use-vrf", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF to choose for server connection\n(Default=mgmt-vrf)', u'cli-optional-in-sequence': None, u'key-default': u'mgmt-vrf', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='common-def:vrf-name', is_config=True)""",
        })

    self.__use_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_use_vrf(self):
    self.__use_vrf = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="use-vrf", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF to choose for server connection\n(Default=mgmt-vrf)', u'cli-optional-in-sequence': None, u'key-default': u'mgmt-vrf', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='common-def:vrf-name', is_config=True)


  def _get_ldap_server_options(self):
    """
    Getter method for ldap_server_options, mapped from YANG variable /ldap_server/host/ldap_server_options (container)
    """
    return self.__ldap_server_options
      
  def _set_ldap_server_options(self, v, load=False):
    """
    Setter method for ldap_server_options, mapped from YANG variable /ldap_server/host/ldap_server_options (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldap_server_options is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldap_server_options() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ldap_server_options.ldap_server_options, is_container='container', presence=False, yang_name="ldap-server-options", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldap_server_options must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ldap_server_options.ldap_server_options, is_container='container', presence=False, yang_name="ldap-server-options", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)""",
        })

    self.__ldap_server_options = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldap_server_options(self):
    self.__ldap_server_options = YANGDynClass(base=ldap_server_options.ldap_server_options, is_container='container', presence=False, yang_name="ldap-server-options", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)

  hostname = __builtin__.property(_get_hostname, _set_hostname)
  use_vrf = __builtin__.property(_get_use_vrf, _set_use_vrf)
  ldap_server_options = __builtin__.property(_get_ldap_server_options, _set_ldap_server_options)


  _pyangbind_elements = {'hostname': hostname, 'use_vrf': use_vrf, 'ldap_server_options': ldap_server_options, }


