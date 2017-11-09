
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import authentication
import accounting
import authorization
class aaa(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-aaa - based on the path /aaa-config/aaa. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__authentication','__accounting','__authorization',)

  _yang_name = 'aaa'
  _rest_name = 'aaa'

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
    self.__accounting = YANGDynClass(base=accounting.accounting, is_container='container', presence=False, yang_name="accounting", rest_name="accounting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Login or Command accounting', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)
    self.__authentication = YANGDynClass(base=authentication.authentication, is_container='container', presence=False, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure preferred order for Authentication'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)
    self.__authorization = YANGDynClass(base=authorization.authorization, is_container='container', presence=False, yang_name="authorization", rest_name="authorization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable/Disable Command authorization'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)

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
      return [u'aaa-config', u'aaa']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'aaa']

  def _get_authentication(self):
    """
    Getter method for authentication, mapped from YANG variable /aaa_config/aaa/authentication (container)
    """
    return self.__authentication
      
  def _set_authentication(self, v, load=False):
    """
    Setter method for authentication, mapped from YANG variable /aaa_config/aaa/authentication (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=authentication.authentication, is_container='container', presence=False, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure preferred order for Authentication'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=authentication.authentication, is_container='container', presence=False, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure preferred order for Authentication'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)""",
        })

    self.__authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication(self):
    self.__authentication = YANGDynClass(base=authentication.authentication, is_container='container', presence=False, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure preferred order for Authentication'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)


  def _get_accounting(self):
    """
    Getter method for accounting, mapped from YANG variable /aaa_config/aaa/accounting (container)
    """
    return self.__accounting
      
  def _set_accounting(self, v, load=False):
    """
    Setter method for accounting, mapped from YANG variable /aaa_config/aaa/accounting (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_accounting is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_accounting() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=accounting.accounting, is_container='container', presence=False, yang_name="accounting", rest_name="accounting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Login or Command accounting', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """accounting must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=accounting.accounting, is_container='container', presence=False, yang_name="accounting", rest_name="accounting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Login or Command accounting', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)""",
        })

    self.__accounting = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_accounting(self):
    self.__accounting = YANGDynClass(base=accounting.accounting, is_container='container', presence=False, yang_name="accounting", rest_name="accounting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Login or Command accounting', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)


  def _get_authorization(self):
    """
    Getter method for authorization, mapped from YANG variable /aaa_config/aaa/authorization (container)
    """
    return self.__authorization
      
  def _set_authorization(self, v, load=False):
    """
    Setter method for authorization, mapped from YANG variable /aaa_config/aaa/authorization (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authorization is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authorization() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=authorization.authorization, is_container='container', presence=False, yang_name="authorization", rest_name="authorization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable/Disable Command authorization'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authorization must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=authorization.authorization, is_container='container', presence=False, yang_name="authorization", rest_name="authorization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable/Disable Command authorization'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)""",
        })

    self.__authorization = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authorization(self):
    self.__authorization = YANGDynClass(base=authorization.authorization, is_container='container', presence=False, yang_name="authorization", rest_name="authorization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable/Disable Command authorization'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)

  authentication = __builtin__.property(_get_authentication, _set_authentication)
  accounting = __builtin__.property(_get_accounting, _set_accounting)
  authorization = __builtin__.property(_get_authorization, _set_authorization)


  _pyangbind_elements = {'authentication': authentication, 'accounting': accounting, 'authorization': authorization, }


