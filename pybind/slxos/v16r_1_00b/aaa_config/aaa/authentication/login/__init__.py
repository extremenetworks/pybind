
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class login(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-aaa - based on the path /aaa-config/aaa/authentication/login. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__first','__second',)

  _yang_name = 'login'

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
    self.__second = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'local-auth-fallback': {'value': 5}, u'local': {'value': 4}},), is_leaf=True, yang_name="second", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Secondary source of authentication', u'cli-drop-node-name': None, u'display-when': u"../first = 'radius' or\n../first = 'tacacs+' or\n../first = 'ldap'"}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)
    self.__first = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {'value': 0}, u'tacacs+': {'value': 2}, u'local': {'value': 4}, u'radius': {'value': 1}, u'ldap': {'value': 3}},), is_leaf=True, yang_name="first", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Primary source of authentication', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)

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
      return [u'aaa-config', u'aaa', u'authentication', u'login']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'aaa', u'authentication', u'login']

  def _get_first(self):
    """
    Getter method for first, mapped from YANG variable /aaa_config/aaa/authentication/login/first (enumeration)
    """
    return self.__first
      
  def _set_first(self, v, load=False):
    """
    Setter method for first, mapped from YANG variable /aaa_config/aaa/authentication/login/first (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_first is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_first() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {'value': 0}, u'tacacs+': {'value': 2}, u'local': {'value': 4}, u'radius': {'value': 1}, u'ldap': {'value': 3}},), is_leaf=True, yang_name="first", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Primary source of authentication', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """first must be of a type compatible with enumeration""",
          'defined-type': "brocade-aaa:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {'value': 0}, u'tacacs+': {'value': 2}, u'local': {'value': 4}, u'radius': {'value': 1}, u'ldap': {'value': 3}},), is_leaf=True, yang_name="first", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Primary source of authentication', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)""",
        })

    self.__first = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_first(self):
    self.__first = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {'value': 0}, u'tacacs+': {'value': 2}, u'local': {'value': 4}, u'radius': {'value': 1}, u'ldap': {'value': 3}},), is_leaf=True, yang_name="first", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Primary source of authentication', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)


  def _get_second(self):
    """
    Getter method for second, mapped from YANG variable /aaa_config/aaa/authentication/login/second (enumeration)
    """
    return self.__second
      
  def _set_second(self, v, load=False):
    """
    Setter method for second, mapped from YANG variable /aaa_config/aaa/authentication/login/second (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_second is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_second() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'local-auth-fallback': {'value': 5}, u'local': {'value': 4}},), is_leaf=True, yang_name="second", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Secondary source of authentication', u'cli-drop-node-name': None, u'display-when': u"../first = 'radius' or\n../first = 'tacacs+' or\n../first = 'ldap'"}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """second must be of a type compatible with enumeration""",
          'defined-type': "brocade-aaa:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'local-auth-fallback': {'value': 5}, u'local': {'value': 4}},), is_leaf=True, yang_name="second", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Secondary source of authentication', u'cli-drop-node-name': None, u'display-when': u"../first = 'radius' or\n../first = 'tacacs+' or\n../first = 'ldap'"}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)""",
        })

    self.__second = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_second(self):
    self.__second = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'local-auth-fallback': {'value': 5}, u'local': {'value': 4}},), is_leaf=True, yang_name="second", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Secondary source of authentication', u'cli-drop-node-name': None, u'display-when': u"../first = 'radius' or\n../first = 'tacacs+' or\n../first = 'ldap'"}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)

  first = __builtin__.property(_get_first, _set_first)
  second = __builtin__.property(_get_second, _set_second)


  _pyangbind_elements = {'first': first, 'second': second, }


