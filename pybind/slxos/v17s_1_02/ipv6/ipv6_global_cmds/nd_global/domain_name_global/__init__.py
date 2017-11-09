
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class domain_name_global(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /ipv6/ipv6-global-cmds/nd-global/domain-name-global. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__domain_name_string_global','__domain_name_lifetime_global',)

  _yang_name = 'domain-name-global'
  _rest_name = 'domain-name-global'

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
    self.__domain_name_string_global = YANGDynClass(base=unicode, is_leaf=True, yang_name="domain-name-string-global", rest_name="domain-name-string-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='string', is_config=True)
    self.__domain_name_lifetime_global = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..200']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(100), is_leaf=True, yang_name="domain-name-lifetime-global", rest_name="domain-name-lifetime-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='uint32', is_config=True)

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
      return [u'ipv6', u'ipv6-global-cmds', u'nd-global', u'domain-name-global']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'ipv6-global-cmds', u'nd-global', u'domain-name-global']

  def _get_domain_name_string_global(self):
    """
    Getter method for domain_name_string_global, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/domain_name_global/domain_name_string_global (string)
    """
    return self.__domain_name_string_global
      
  def _set_domain_name_string_global(self, v, load=False):
    """
    Setter method for domain_name_string_global, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/domain_name_global/domain_name_string_global (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_domain_name_string_global is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_domain_name_string_global() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="domain-name-string-global", rest_name="domain-name-string-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """domain_name_string_global must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="domain-name-string-global", rest_name="domain-name-string-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='string', is_config=True)""",
        })

    self.__domain_name_string_global = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_domain_name_string_global(self):
    self.__domain_name_string_global = YANGDynClass(base=unicode, is_leaf=True, yang_name="domain-name-string-global", rest_name="domain-name-string-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='string', is_config=True)


  def _get_domain_name_lifetime_global(self):
    """
    Getter method for domain_name_lifetime_global, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/domain_name_global/domain_name_lifetime_global (uint32)
    """
    return self.__domain_name_lifetime_global
      
  def _set_domain_name_lifetime_global(self, v, load=False):
    """
    Setter method for domain_name_lifetime_global, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/domain_name_global/domain_name_lifetime_global (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_domain_name_lifetime_global is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_domain_name_lifetime_global() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..200']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(100), is_leaf=True, yang_name="domain-name-lifetime-global", rest_name="domain-name-lifetime-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """domain_name_lifetime_global must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..200']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(100), is_leaf=True, yang_name="domain-name-lifetime-global", rest_name="domain-name-lifetime-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='uint32', is_config=True)""",
        })

    self.__domain_name_lifetime_global = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_domain_name_lifetime_global(self):
    self.__domain_name_lifetime_global = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..200']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(100), is_leaf=True, yang_name="domain-name-lifetime-global", rest_name="domain-name-lifetime-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='uint32', is_config=True)

  domain_name_string_global = __builtin__.property(_get_domain_name_string_global, _set_domain_name_string_global)
  domain_name_lifetime_global = __builtin__.property(_get_domain_name_lifetime_global, _set_domain_name_lifetime_global)


  _pyangbind_elements = {'domain_name_string_global': domain_name_string_global, 'domain_name_lifetime_global': domain_name_lifetime_global, }


