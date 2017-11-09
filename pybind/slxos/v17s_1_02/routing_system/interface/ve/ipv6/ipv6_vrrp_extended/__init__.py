
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import auth_type
class ipv6_vrrp_extended(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/ipv6/ipv6-vrrp-extended. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: VRRP Extended
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__auth_type',)

  _yang_name = 'ipv6-vrrp-extended'
  _rest_name = 'ipv6-vrrp-extended'

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
    self.__auth_type = YANGDynClass(base=auth_type.auth_type, is_container='container', presence=False, yang_name="auth-type", rest_name="auth-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='container', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'ipv6', u'ipv6-vrrp-extended']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'routing-system', u'interface', u've', u'ipv6', u'ipv6-vrrp-extended']

  def _get_auth_type(self):
    """
    Getter method for auth_type, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_vrrp_extended/auth_type (container)

    YANG Description: Authentication type
    """
    return self.__auth_type
      
  def _set_auth_type(self, v, load=False):
    """
    Setter method for auth_type, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_vrrp_extended/auth_type (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_type() directly.

    YANG Description: Authentication type
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=auth_type.auth_type, is_container='container', presence=False, yang_name="auth-type", rest_name="auth-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_type must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=auth_type.auth_type, is_container='container', presence=False, yang_name="auth-type", rest_name="auth-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='container', is_config=True)""",
        })

    self.__auth_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_type(self):
    self.__auth_type = YANGDynClass(base=auth_type.auth_type, is_container='container', presence=False, yang_name="auth-type", rest_name="auth-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='container', is_config=True)

  auth_type = __builtin__.property(_get_auth_type, _set_auth_type)


  _pyangbind_elements = {'auth_type': auth_type, }


