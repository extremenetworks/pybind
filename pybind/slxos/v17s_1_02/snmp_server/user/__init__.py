
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class user(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-snmp - based on the path /snmp-server/user. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__username','__groupname','__auth','__auth_password','__priv','__priv_password','__encrypted',)

  _yang_name = 'user'
  _rest_name = 'user'

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
    self.__username = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 25']}), is_leaf=True, yang_name="username", rest_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    self.__encrypted = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="encrypted", rest_name="encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='empty', is_config=True)
    self.__auth = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'sha': {'value': 1}, u'md5': {'value': 0}},), is_leaf=True, yang_name="auth", rest_name="auth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='enumeration', is_config=True)
    self.__priv_password = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="priv-password", rest_name="priv-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    self.__groupname = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), is_leaf=True, yang_name="groupname", rest_name="groupname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    self.__auth_password = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="auth-password", rest_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    self.__priv = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AES128': {'value': 2}, u'DES': {'value': 0}},), is_leaf=True, yang_name="priv", rest_name="priv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='enumeration', is_config=True)

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
      return [u'snmp-server', u'user']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'snmp-server', u'user']

  def _get_username(self):
    """
    Getter method for username, mapped from YANG variable /snmp_server/user/username (string)
    """
    return self.__username
      
  def _set_username(self, v, load=False):
    """
    Setter method for username, mapped from YANG variable /snmp_server/user/username (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_username is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_username() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 25']}), is_leaf=True, yang_name="username", rest_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """username must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 25']}), is_leaf=True, yang_name="username", rest_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)""",
        })

    self.__username = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_username(self):
    self.__username = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 25']}), is_leaf=True, yang_name="username", rest_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)


  def _get_groupname(self):
    """
    Getter method for groupname, mapped from YANG variable /snmp_server/user/groupname (string)
    """
    return self.__groupname
      
  def _set_groupname(self, v, load=False):
    """
    Setter method for groupname, mapped from YANG variable /snmp_server/user/groupname (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_groupname is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_groupname() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), is_leaf=True, yang_name="groupname", rest_name="groupname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """groupname must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), is_leaf=True, yang_name="groupname", rest_name="groupname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)""",
        })

    self.__groupname = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_groupname(self):
    self.__groupname = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), is_leaf=True, yang_name="groupname", rest_name="groupname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)


  def _get_auth(self):
    """
    Getter method for auth, mapped from YANG variable /snmp_server/user/auth (enumeration)
    """
    return self.__auth
      
  def _set_auth(self, v, load=False):
    """
    Setter method for auth, mapped from YANG variable /snmp_server/user/auth (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'sha': {'value': 1}, u'md5': {'value': 0}},), is_leaf=True, yang_name="auth", rest_name="auth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth must be of a type compatible with enumeration""",
          'defined-type': "brocade-snmp:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'sha': {'value': 1}, u'md5': {'value': 0}},), is_leaf=True, yang_name="auth", rest_name="auth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='enumeration', is_config=True)""",
        })

    self.__auth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth(self):
    self.__auth = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'sha': {'value': 1}, u'md5': {'value': 0}},), is_leaf=True, yang_name="auth", rest_name="auth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='enumeration', is_config=True)


  def _get_auth_password(self):
    """
    Getter method for auth_password, mapped from YANG variable /snmp_server/user/auth_password (string)
    """
    return self.__auth_password
      
  def _set_auth_password(self, v, load=False):
    """
    Setter method for auth_password, mapped from YANG variable /snmp_server/user/auth_password (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_password() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, default=unicode(""), is_leaf=True, yang_name="auth-password", rest_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_password must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="auth-password", rest_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)""",
        })

    self.__auth_password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_password(self):
    self.__auth_password = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="auth-password", rest_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)


  def _get_priv(self):
    """
    Getter method for priv, mapped from YANG variable /snmp_server/user/priv (enumeration)
    """
    return self.__priv
      
  def _set_priv(self, v, load=False):
    """
    Setter method for priv, mapped from YANG variable /snmp_server/user/priv (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priv() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AES128': {'value': 2}, u'DES': {'value': 0}},), is_leaf=True, yang_name="priv", rest_name="priv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priv must be of a type compatible with enumeration""",
          'defined-type': "brocade-snmp:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AES128': {'value': 2}, u'DES': {'value': 0}},), is_leaf=True, yang_name="priv", rest_name="priv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='enumeration', is_config=True)""",
        })

    self.__priv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priv(self):
    self.__priv = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AES128': {'value': 2}, u'DES': {'value': 0}},), is_leaf=True, yang_name="priv", rest_name="priv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='enumeration', is_config=True)


  def _get_priv_password(self):
    """
    Getter method for priv_password, mapped from YANG variable /snmp_server/user/priv_password (string)
    """
    return self.__priv_password
      
  def _set_priv_password(self, v, load=False):
    """
    Setter method for priv_password, mapped from YANG variable /snmp_server/user/priv_password (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priv_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priv_password() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, default=unicode(""), is_leaf=True, yang_name="priv-password", rest_name="priv-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priv_password must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="priv-password", rest_name="priv-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)""",
        })

    self.__priv_password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priv_password(self):
    self.__priv_password = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="priv-password", rest_name="priv-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)


  def _get_encrypted(self):
    """
    Getter method for encrypted, mapped from YANG variable /snmp_server/user/encrypted (empty)
    """
    return self.__encrypted
      
  def _set_encrypted(self, v, load=False):
    """
    Setter method for encrypted, mapped from YANG variable /snmp_server/user/encrypted (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encrypted is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encrypted() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="encrypted", rest_name="encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encrypted must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="encrypted", rest_name="encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='empty', is_config=True)""",
        })

    self.__encrypted = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encrypted(self):
    self.__encrypted = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="encrypted", rest_name="encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='empty', is_config=True)

  username = __builtin__.property(_get_username, _set_username)
  groupname = __builtin__.property(_get_groupname, _set_groupname)
  auth = __builtin__.property(_get_auth, _set_auth)
  auth_password = __builtin__.property(_get_auth_password, _set_auth_password)
  priv = __builtin__.property(_get_priv, _set_priv)
  priv_password = __builtin__.property(_get_priv_password, _set_priv_password)
  encrypted = __builtin__.property(_get_encrypted, _set_encrypted)


  _pyangbind_elements = {'username': username, 'groupname': groupname, 'auth': auth, 'auth_password': auth_password, 'priv': priv, 'priv_password': priv_password, 'encrypted': encrypted, }


