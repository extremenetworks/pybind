
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import static_ag_ip_config
import dhcp
import receive
class ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Internet Protoccol (IP). 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__static_ag_ip_config','__dhcp','__receive',)

  _yang_name = 'ip'
  _rest_name = 'ip'

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
    self.__receive = YANGDynClass(base=receive.receive, is_container='container', presence=False, yang_name="receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='container', is_config=True)
    self.__dhcp = YANGDynClass(base=dhcp.dhcp, is_container='container', presence=False, yang_name="dhcp", rest_name="dhcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)
    self.__static_ag_ip_config = YANGDynClass(base=static_ag_ip_config.static_ag_ip_config, is_container='container', presence=False, yang_name="static-ag-ip-config", rest_name="static-ag-ip-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='container', is_config=True)

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
      return [u'routing-system', u'ip']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'routing-system', u'ip']

  def _get_static_ag_ip_config(self):
    """
    Getter method for static_ag_ip_config, mapped from YANG variable /routing_system/ip/static_ag_ip_config (container)
    """
    return self.__static_ag_ip_config
      
  def _set_static_ag_ip_config(self, v, load=False):
    """
    Setter method for static_ag_ip_config, mapped from YANG variable /routing_system/ip/static_ag_ip_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_ag_ip_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_ag_ip_config() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=static_ag_ip_config.static_ag_ip_config, is_container='container', presence=False, yang_name="static-ag-ip-config", rest_name="static-ag-ip-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_ag_ip_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=static_ag_ip_config.static_ag_ip_config, is_container='container', presence=False, yang_name="static-ag-ip-config", rest_name="static-ag-ip-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='container', is_config=True)""",
        })

    self.__static_ag_ip_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_ag_ip_config(self):
    self.__static_ag_ip_config = YANGDynClass(base=static_ag_ip_config.static_ag_ip_config, is_container='container', presence=False, yang_name="static-ag-ip-config", rest_name="static-ag-ip-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='container', is_config=True)


  def _get_dhcp(self):
    """
    Getter method for dhcp, mapped from YANG variable /routing_system/ip/dhcp (container)

    YANG Description: DHCP Global Configuration
    """
    return self.__dhcp
      
  def _set_dhcp(self, v, load=False):
    """
    Setter method for dhcp, mapped from YANG variable /routing_system/ip/dhcp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dhcp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dhcp() directly.

    YANG Description: DHCP Global Configuration
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=dhcp.dhcp, is_container='container', presence=False, yang_name="dhcp", rest_name="dhcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dhcp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dhcp.dhcp, is_container='container', presence=False, yang_name="dhcp", rest_name="dhcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)""",
        })

    self.__dhcp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dhcp(self):
    self.__dhcp = YANGDynClass(base=dhcp.dhcp, is_container='container', presence=False, yang_name="dhcp", rest_name="dhcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)


  def _get_receive(self):
    """
    Getter method for receive, mapped from YANG variable /routing_system/ip/receive (container)
    """
    return self.__receive
      
  def _set_receive(self, v, load=False):
    """
    Setter method for receive, mapped from YANG variable /routing_system/ip/receive (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_receive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_receive() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=receive.receive, is_container='container', presence=False, yang_name="receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """receive must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=receive.receive, is_container='container', presence=False, yang_name="receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='container', is_config=True)""",
        })

    self.__receive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_receive(self):
    self.__receive = YANGDynClass(base=receive.receive, is_container='container', presence=False, yang_name="receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='container', is_config=True)

  static_ag_ip_config = __builtin__.property(_get_static_ag_ip_config, _set_static_ag_ip_config)
  dhcp = __builtin__.property(_get_dhcp, _set_dhcp)
  receive = __builtin__.property(_get_receive, _set_receive)


  _pyangbind_elements = {'static_ag_ip_config': static_ag_ip_config, 'dhcp': dhcp, 'receive': receive, }


