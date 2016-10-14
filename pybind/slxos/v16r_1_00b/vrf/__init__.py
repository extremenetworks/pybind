
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import route_target
import address_family
import ip
class vrf(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vrf - based on the path /vrf. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__vrf_name','__route_distiniguisher','__route_target','__address_family','__ip',)

  _yang_name = 'vrf'

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
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF specific IP commands', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='container', is_config=True)
    self.__route_target = YANGDynClass(base=YANGListType("action target_community",route_target.route_target, yang_name="route-target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action target-community', extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'hidden': u'full', u'cli-suppress-mode': None, u'callpoint': u'VrfRouteTarget'}}), is_container='list', yang_name="route-target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'hidden': u'full', u'cli-suppress-mode': None, u'callpoint': u'VrfRouteTarget'}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='list', is_config=True)
    self.__vrf_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<WORD:1-32>;;Name of VRF'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='common-def:vrf-name', is_config=True)
    self.__route_distiniguisher = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((\\s*(((([1-9][0-9]{0,8})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))|(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))))*)'}), is_leaf=True, yang_name="route-distiniguisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Route Distinguisher', u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'rd', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='rd-type', is_config=True)
    self.__address_family = YANGDynClass(base=address_family.address_family, is_container='container', yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enter Address Family command mode', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='container', is_config=True)

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
      return [u'vrf']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'vrf']

  def _get_vrf_name(self):
    """
    Getter method for vrf_name, mapped from YANG variable /vrf/vrf_name (common-def:vrf-name)
    """
    return self.__vrf_name
      
  def _set_vrf_name(self, v, load=False):
    """
    Setter method for vrf_name, mapped from YANG variable /vrf/vrf_name (common-def:vrf-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<WORD:1-32>;;Name of VRF'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='common-def:vrf-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf_name must be of a type compatible with common-def:vrf-name""",
          'defined-type': "common-def:vrf-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<WORD:1-32>;;Name of VRF'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='common-def:vrf-name', is_config=True)""",
        })

    self.__vrf_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf_name(self):
    self.__vrf_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<WORD:1-32>;;Name of VRF'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='common-def:vrf-name', is_config=True)


  def _get_route_distiniguisher(self):
    """
    Getter method for route_distiniguisher, mapped from YANG variable /vrf/route_distiniguisher (rd-type)

    YANG Description: Route distinguisher represented in ASN:nn
format.
    """
    return self.__route_distiniguisher
      
  def _set_route_distiniguisher(self, v, load=False):
    """
    Setter method for route_distiniguisher, mapped from YANG variable /vrf/route_distiniguisher (rd-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_distiniguisher is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_distiniguisher() directly.

    YANG Description: Route distinguisher represented in ASN:nn
format.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((\\s*(((([1-9][0-9]{0,8})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))|(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))))*)'}), is_leaf=True, yang_name="route-distiniguisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Route Distinguisher', u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'rd', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='rd-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_distiniguisher must be of a type compatible with rd-type""",
          'defined-type': "brocade-vrf:rd-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((\\s*(((([1-9][0-9]{0,8})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))|(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))))*)'}), is_leaf=True, yang_name="route-distiniguisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Route Distinguisher', u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'rd', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='rd-type', is_config=True)""",
        })

    self.__route_distiniguisher = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_distiniguisher(self):
    self.__route_distiniguisher = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((\\s*(((([1-9][0-9]{0,8})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))|(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))))*)'}), is_leaf=True, yang_name="route-distiniguisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Route Distinguisher', u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'rd', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='rd-type', is_config=True)


  def _get_route_target(self):
    """
    Getter method for route_target, mapped from YANG variable /vrf/route_target (list)

    YANG Description: Target extended communities. This functionality is not supported
in NOS4.0.0 release
    """
    return self.__route_target
      
  def _set_route_target(self, v, load=False):
    """
    Setter method for route_target, mapped from YANG variable /vrf/route_target (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_target is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_target() directly.

    YANG Description: Target extended communities. This functionality is not supported
in NOS4.0.0 release
    """
    try:
      t = YANGDynClass(v,base=YANGListType("action target_community",route_target.route_target, yang_name="route-target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action target-community', extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'hidden': u'full', u'cli-suppress-mode': None, u'callpoint': u'VrfRouteTarget'}}), is_container='list', yang_name="route-target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'hidden': u'full', u'cli-suppress-mode': None, u'callpoint': u'VrfRouteTarget'}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_target must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("action target_community",route_target.route_target, yang_name="route-target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action target-community', extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'hidden': u'full', u'cli-suppress-mode': None, u'callpoint': u'VrfRouteTarget'}}), is_container='list', yang_name="route-target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'hidden': u'full', u'cli-suppress-mode': None, u'callpoint': u'VrfRouteTarget'}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='list', is_config=True)""",
        })

    self.__route_target = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_target(self):
    self.__route_target = YANGDynClass(base=YANGListType("action target_community",route_target.route_target, yang_name="route-target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action target-community', extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'hidden': u'full', u'cli-suppress-mode': None, u'callpoint': u'VrfRouteTarget'}}), is_container='list', yang_name="route-target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'hidden': u'full', u'cli-suppress-mode': None, u'callpoint': u'VrfRouteTarget'}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='list', is_config=True)


  def _get_address_family(self):
    """
    Getter method for address_family, mapped from YANG variable /vrf/address_family (container)
    """
    return self.__address_family
      
  def _set_address_family(self, v, load=False):
    """
    Setter method for address_family, mapped from YANG variable /vrf/address_family (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address_family is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address_family() directly.
    """
    try:
      t = YANGDynClass(v,base=address_family.address_family, is_container='container', yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enter Address Family command mode', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address_family must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=address_family.address_family, is_container='container', yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enter Address Family command mode', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='container', is_config=True)""",
        })

    self.__address_family = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address_family(self):
    self.__address_family = YANGDynClass(base=address_family.address_family, is_container='container', yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enter Address Family command mode', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='container', is_config=True)


  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /vrf/ip (container)
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /vrf/ip (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.
    """
    try:
      t = YANGDynClass(v,base=ip.ip, is_container='container', yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF specific IP commands', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip.ip, is_container='container', yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF specific IP commands', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='container', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF specific IP commands', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='container', is_config=True)

  vrf_name = __builtin__.property(_get_vrf_name, _set_vrf_name)
  route_distiniguisher = __builtin__.property(_get_route_distiniguisher, _set_route_distiniguisher)
  route_target = __builtin__.property(_get_route_target, _set_route_target)
  address_family = __builtin__.property(_get_address_family, _set_address_family)
  ip = __builtin__.property(_get_ip, _set_ip)


  _pyangbind_elements = {'vrf_name': vrf_name, 'route_distiniguisher': route_distiniguisher, 'route_target': route_target, 'address_family': address_family, 'ip': ip, }


