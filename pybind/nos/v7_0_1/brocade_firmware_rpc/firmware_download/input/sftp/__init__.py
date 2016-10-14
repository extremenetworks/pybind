
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class sftp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-firmware - based on the path /brocade_firmware_rpc/firmware-download/input/sftp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__user','__password','__host','__directory','__file','__port','__host_key_check',)

  _yang_name = 'sftp'

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
    self.__host = YANGDynClass(base=unicode, is_leaf=True, yang_name="host", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Host ipv4/ipv6 address'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__user = YANGDynClass(base=unicode, is_leaf=True, yang_name="user", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Username'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__file = YANGDynClass(base=unicode, is_leaf=True, yang_name="file", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Package release file, example - release.plist'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__directory = YANGDynClass(base=unicode, is_leaf=True, yang_name="directory", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Directory'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__host_key_check = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="host-key-check", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Enable strict host key check'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='empty', is_config=True)
    self.__password = YANGDynClass(base=unicode, is_leaf=True, yang_name="password", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Password', u'suppress-echo': u'true'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="port", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Server port number (default 22)'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)

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
      return [u'brocade_firmware_rpc', u'firmware-download', u'input', u'sftp']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'firmware-download', u'input', u'sftp']

  def _get_user(self):
    """
    Getter method for user, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/user (string)
    """
    return self.__user
      
  def _set_user(self, v, load=False):
    """
    Setter method for user, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/user (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_user is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_user() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="user", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Username'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """user must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="user", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Username'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__user = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_user(self):
    self.__user = YANGDynClass(base=unicode, is_leaf=True, yang_name="user", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Username'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_password(self):
    """
    Getter method for password, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/password (string)
    """
    return self.__password
      
  def _set_password(self, v, load=False):
    """
    Setter method for password, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/password (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_password() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="password", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Password', u'suppress-echo': u'true'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """password must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="password", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Password', u'suppress-echo': u'true'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_password(self):
    self.__password = YANGDynClass(base=unicode, is_leaf=True, yang_name="password", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Password', u'suppress-echo': u'true'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_host(self):
    """
    Getter method for host, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/host (string)
    """
    return self.__host
      
  def _set_host(self, v, load=False):
    """
    Setter method for host, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/host (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="host", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Host ipv4/ipv6 address'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="host", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Host ipv4/ipv6 address'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__host = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host(self):
    self.__host = YANGDynClass(base=unicode, is_leaf=True, yang_name="host", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Host ipv4/ipv6 address'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_directory(self):
    """
    Getter method for directory, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/directory (string)
    """
    return self.__directory
      
  def _set_directory(self, v, load=False):
    """
    Setter method for directory, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/directory (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_directory is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_directory() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="directory", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Directory'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """directory must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="directory", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Directory'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__directory = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_directory(self):
    self.__directory = YANGDynClass(base=unicode, is_leaf=True, yang_name="directory", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Directory'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_file(self):
    """
    Getter method for file, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/file (string)
    """
    return self.__file
      
  def _set_file(self, v, load=False):
    """
    Setter method for file, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/file (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_file is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_file() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="file", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Package release file, example - release.plist'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """file must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="file", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Package release file, example - release.plist'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__file = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_file(self):
    self.__file = YANGDynClass(base=unicode, is_leaf=True, yang_name="file", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Package release file, example - release.plist'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/port (int32)
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/port (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="port", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Server port number (default 22)'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="port", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Server port number (default 22)'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="port", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Server port number (default 22)'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)


  def _get_host_key_check(self):
    """
    Getter method for host_key_check, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/host_key_check (empty)
    """
    return self.__host_key_check
      
  def _set_host_key_check(self, v, load=False):
    """
    Setter method for host_key_check, mapped from YANG variable /brocade_firmware_rpc/firmware_download/input/sftp/host_key_check (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host_key_check is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host_key_check() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="host-key-check", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Enable strict host key check'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host_key_check must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="host-key-check", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Enable strict host key check'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='empty', is_config=True)""",
        })

    self.__host_key_check = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host_key_check(self):
    self.__host_key_check = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="host-key-check", parent=self, choice=(u'protocol-type', u'sftp-protocol'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Enable strict host key check'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='empty', is_config=True)

  user = __builtin__.property(_get_user, _set_user)
  password = __builtin__.property(_get_password, _set_password)
  host = __builtin__.property(_get_host, _set_host)
  directory = __builtin__.property(_get_directory, _set_directory)
  file = __builtin__.property(_get_file, _set_file)
  port = __builtin__.property(_get_port, _set_port)
  host_key_check = __builtin__.property(_get_host_key_check, _set_host_key_check)

  __choices__ = {u'protocol-type': {u'sftp-protocol': [u'user', u'password', u'host', u'directory', u'file', u'port', u'host_key_check']}}
  _pyangbind_elements = {'user': user, 'password': password, 'host': host, 'directory': directory, 'file': file, 'port': port, 'host_key_check': host_key_check, }


