
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class proto(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fc-auth - based on the path /fcsp-sa/fcsp/auth/proto. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__auth_type','__group','__hash',)

  _yang_name = 'proto'

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
    self.__auth_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dh-chap': {}},), default=unicode("dh-chap"), is_leaf=True, yang_name="auth-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The authentication type'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='fcsp-authtype', is_config=True)
    self.__hash = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'all': {}, u'sha1': {}, u'md5': {}},), default=unicode("all"), is_leaf=True, yang_name="hash", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The hash type'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='fcsp-hashtype', is_config=True)
    self.__group = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-4\\*]'}), default=unicode("*"), is_leaf=True, yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The group value'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='string', is_config=True)

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
      return [u'fcsp-sa', u'fcsp', u'auth', u'proto']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'fcsp', u'auth']

  def _get_auth_type(self):
    """
    Getter method for auth_type, mapped from YANG variable /fcsp_sa/fcsp/auth/proto/auth_type (fcsp-authtype)
    """
    return self.__auth_type
      
  def _set_auth_type(self, v, load=False):
    """
    Setter method for auth_type, mapped from YANG variable /fcsp_sa/fcsp/auth/proto/auth_type (fcsp-authtype)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_type() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dh-chap': {}},), default=unicode("dh-chap"), is_leaf=True, yang_name="auth-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The authentication type'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='fcsp-authtype', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_type must be of a type compatible with fcsp-authtype""",
          'defined-type': "brocade-fc-auth:fcsp-authtype",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dh-chap': {}},), default=unicode("dh-chap"), is_leaf=True, yang_name="auth-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The authentication type'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='fcsp-authtype', is_config=True)""",
        })

    self.__auth_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_type(self):
    self.__auth_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dh-chap': {}},), default=unicode("dh-chap"), is_leaf=True, yang_name="auth-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The authentication type'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='fcsp-authtype', is_config=True)


  def _get_group(self):
    """
    Getter method for group, mapped from YANG variable /fcsp_sa/fcsp/auth/proto/group (string)
    """
    return self.__group
      
  def _set_group(self, v, load=False):
    """
    Setter method for group, mapped from YANG variable /fcsp_sa/fcsp/auth/proto/group (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-4\\*]'}), default=unicode("*"), is_leaf=True, yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The group value'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-4\\*]'}), default=unicode("*"), is_leaf=True, yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The group value'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='string', is_config=True)""",
        })

    self.__group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group(self):
    self.__group = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-4\\*]'}), default=unicode("*"), is_leaf=True, yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The group value'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='string', is_config=True)


  def _get_hash(self):
    """
    Getter method for hash, mapped from YANG variable /fcsp_sa/fcsp/auth/proto/hash (fcsp-hashtype)
    """
    return self.__hash
      
  def _set_hash(self, v, load=False):
    """
    Setter method for hash, mapped from YANG variable /fcsp_sa/fcsp/auth/proto/hash (fcsp-hashtype)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hash is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hash() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'all': {}, u'sha1': {}, u'md5': {}},), default=unicode("all"), is_leaf=True, yang_name="hash", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The hash type'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='fcsp-hashtype', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hash must be of a type compatible with fcsp-hashtype""",
          'defined-type': "brocade-fc-auth:fcsp-hashtype",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'all': {}, u'sha1': {}, u'md5': {}},), default=unicode("all"), is_leaf=True, yang_name="hash", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The hash type'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='fcsp-hashtype', is_config=True)""",
        })

    self.__hash = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hash(self):
    self.__hash = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'all': {}, u'sha1': {}, u'md5': {}},), default=unicode("all"), is_leaf=True, yang_name="hash", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The hash type'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='fcsp-hashtype', is_config=True)

  auth_type = __builtin__.property(_get_auth_type, _set_auth_type)
  group = __builtin__.property(_get_group, _set_group)
  hash = __builtin__.property(_get_hash, _set_hash)


  _pyangbind_elements = {'auth_type': auth_type, 'group': group, 'hash': hash, }


