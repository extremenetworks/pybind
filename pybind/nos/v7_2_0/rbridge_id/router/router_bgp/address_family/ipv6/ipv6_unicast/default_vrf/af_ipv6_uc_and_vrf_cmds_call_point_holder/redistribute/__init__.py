
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import bgp
import connected
import ospf
import static
class redistribute(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/ipv6/ipv6-unicast/default-vrf/af-ipv6-uc-and-vrf-cmds-call-point-holder/redistribute. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bgp','__connected','__ospf','__static',)

  _yang_name = 'redistribute'
  _rest_name = 'redistribute'

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
    self.__bgp = YANGDynClass(base=bgp.bgp, is_container='container', presence=False, yang_name="bgp", rest_name="bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__ospf = YANGDynClass(base=ospf.ospf, is_container='container', presence=False, yang_name="ospf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__static = YANGDynClass(base=static.static, is_container='container', presence=False, yang_name="static", rest_name="static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__connected = YANGDynClass(base=connected.connected, is_container='container', presence=False, yang_name="connected", rest_name="connected", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'default-vrf', u'af-ipv6-uc-and-vrf-cmds-call-point-holder', u'redistribute']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'redistribute']

  def _get_bgp(self):
    """
    Getter method for bgp, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/bgp (container)
    """
    return self.__bgp
      
  def _set_bgp(self, v, load=False):
    """
    Setter method for bgp, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/bgp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bgp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bgp.bgp, is_container='container', presence=False, yang_name="bgp", rest_name="bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bgp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bgp.bgp, is_container='container', presence=False, yang_name="bgp", rest_name="bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__bgp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bgp(self):
    self.__bgp = YANGDynClass(base=bgp.bgp, is_container='container', presence=False, yang_name="bgp", rest_name="bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_connected(self):
    """
    Getter method for connected, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/connected (container)
    """
    return self.__connected
      
  def _set_connected(self, v, load=False):
    """
    Setter method for connected, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/connected (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connected is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connected() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=connected.connected, is_container='container', presence=False, yang_name="connected", rest_name="connected", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connected must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=connected.connected, is_container='container', presence=False, yang_name="connected", rest_name="connected", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__connected = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connected(self):
    self.__connected = YANGDynClass(base=connected.connected, is_container='container', presence=False, yang_name="connected", rest_name="connected", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_ospf(self):
    """
    Getter method for ospf, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf (container)
    """
    return self.__ospf
      
  def _set_ospf(self, v, load=False):
    """
    Setter method for ospf, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ospf.ospf, is_container='container', presence=False, yang_name="ospf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ospf.ospf, is_container='container', presence=False, yang_name="ospf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__ospf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf(self):
    self.__ospf = YANGDynClass(base=ospf.ospf, is_container='container', presence=False, yang_name="ospf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_static(self):
    """
    Getter method for static, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/static (container)
    """
    return self.__static
      
  def _set_static(self, v, load=False):
    """
    Setter method for static, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/static (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=static.static, is_container='container', presence=False, yang_name="static", rest_name="static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=static.static, is_container='container', presence=False, yang_name="static", rest_name="static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__static = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static(self):
    self.__static = YANGDynClass(base=static.static, is_container='container', presence=False, yang_name="static", rest_name="static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  bgp = __builtin__.property(_get_bgp, _set_bgp)
  connected = __builtin__.property(_get_connected, _set_connected)
  ospf = __builtin__.property(_get_ospf, _set_ospf)
  static = __builtin__.property(_get_static, _set_static)


  _pyangbind_elements = {'bgp': bgp, 'connected': connected, 'ospf': ospf, 'static': static, }


