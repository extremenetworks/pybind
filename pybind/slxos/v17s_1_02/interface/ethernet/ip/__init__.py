
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ip_config
import arp_node_config
import interface_eth_dhcp_conf
import icmp
import igmp
import interface_eth_ospf_conf
class ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The IP configurations for an interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ip_config','__arp_node_config','__interface_eth_dhcp_conf','__icmp','__igmp','__interface_eth_ospf_conf',)

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
    self.__interface_eth_ospf_conf = YANGDynClass(base=interface_eth_ospf_conf.interface_eth_ospf_conf, is_container='container', presence=False, yang_name="interface-eth-ospf-conf", rest_name="interface-eth-ospf-conf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__arp_node_config = YANGDynClass(base=arp_node_config.arp_node_config, is_container='container', presence=False, yang_name="arp-node-config", rest_name="arp-node-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)
    self.__interface_eth_dhcp_conf = YANGDynClass(base=interface_eth_dhcp_conf.interface_eth_dhcp_conf, is_container='container', presence=False, yang_name="interface-eth-dhcp-conf", rest_name="interface-eth-dhcp-conf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)
    self.__ip_config = YANGDynClass(base=ip_config.ip_config, is_container='container', presence=False, yang_name="ip-config", rest_name="ip-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)
    self.__icmp = YANGDynClass(base=icmp.icmp, is_container='container', presence=False, yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)
    self.__igmp = YANGDynClass(base=igmp.igmp, is_container='container', presence=False, yang_name="igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='container', is_config=True)

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
      return [u'interface', u'ethernet', u'ip']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'ethernet', u'ip']

  def _get_ip_config(self):
    """
    Getter method for ip_config, mapped from YANG variable /interface/ethernet/ip/ip_config (container)
    """
    return self.__ip_config
      
  def _set_ip_config(self, v, load=False):
    """
    Setter method for ip_config, mapped from YANG variable /interface/ethernet/ip/ip_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_config() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ip_config.ip_config, is_container='container', presence=False, yang_name="ip-config", rest_name="ip-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip_config.ip_config, is_container='container', presence=False, yang_name="ip-config", rest_name="ip-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)""",
        })

    self.__ip_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_config(self):
    self.__ip_config = YANGDynClass(base=ip_config.ip_config, is_container='container', presence=False, yang_name="ip-config", rest_name="ip-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)


  def _get_arp_node_config(self):
    """
    Getter method for arp_node_config, mapped from YANG variable /interface/ethernet/ip/arp_node_config (container)
    """
    return self.__arp_node_config
      
  def _set_arp_node_config(self, v, load=False):
    """
    Setter method for arp_node_config, mapped from YANG variable /interface/ethernet/ip/arp_node_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_arp_node_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_arp_node_config() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=arp_node_config.arp_node_config, is_container='container', presence=False, yang_name="arp-node-config", rest_name="arp-node-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """arp_node_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=arp_node_config.arp_node_config, is_container='container', presence=False, yang_name="arp-node-config", rest_name="arp-node-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)""",
        })

    self.__arp_node_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_arp_node_config(self):
    self.__arp_node_config = YANGDynClass(base=arp_node_config.arp_node_config, is_container='container', presence=False, yang_name="arp-node-config", rest_name="arp-node-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)


  def _get_interface_eth_dhcp_conf(self):
    """
    Getter method for interface_eth_dhcp_conf, mapped from YANG variable /interface/ethernet/ip/interface_eth_dhcp_conf (container)
    """
    return self.__interface_eth_dhcp_conf
      
  def _set_interface_eth_dhcp_conf(self, v, load=False):
    """
    Setter method for interface_eth_dhcp_conf, mapped from YANG variable /interface/ethernet/ip/interface_eth_dhcp_conf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_eth_dhcp_conf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_eth_dhcp_conf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_eth_dhcp_conf.interface_eth_dhcp_conf, is_container='container', presence=False, yang_name="interface-eth-dhcp-conf", rest_name="interface-eth-dhcp-conf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_eth_dhcp_conf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_eth_dhcp_conf.interface_eth_dhcp_conf, is_container='container', presence=False, yang_name="interface-eth-dhcp-conf", rest_name="interface-eth-dhcp-conf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)""",
        })

    self.__interface_eth_dhcp_conf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_eth_dhcp_conf(self):
    self.__interface_eth_dhcp_conf = YANGDynClass(base=interface_eth_dhcp_conf.interface_eth_dhcp_conf, is_container='container', presence=False, yang_name="interface-eth-dhcp-conf", rest_name="interface-eth-dhcp-conf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)


  def _get_icmp(self):
    """
    Getter method for icmp, mapped from YANG variable /interface/ethernet/ip/icmp (container)
    """
    return self.__icmp
      
  def _set_icmp(self, v, load=False):
    """
    Setter method for icmp, mapped from YANG variable /interface/ethernet/ip/icmp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_icmp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_icmp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=icmp.icmp, is_container='container', presence=False, yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """icmp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=icmp.icmp, is_container='container', presence=False, yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)""",
        })

    self.__icmp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_icmp(self):
    self.__icmp = YANGDynClass(base=icmp.icmp, is_container='container', presence=False, yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)


  def _get_igmp(self):
    """
    Getter method for igmp, mapped from YANG variable /interface/ethernet/ip/igmp (container)
    """
    return self.__igmp
      
  def _set_igmp(self, v, load=False):
    """
    Setter method for igmp, mapped from YANG variable /interface/ethernet/ip/igmp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=igmp.igmp, is_container='container', presence=False, yang_name="igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=igmp.igmp, is_container='container', presence=False, yang_name="igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='container', is_config=True)""",
        })

    self.__igmp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmp(self):
    self.__igmp = YANGDynClass(base=igmp.igmp, is_container='container', presence=False, yang_name="igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='container', is_config=True)


  def _get_interface_eth_ospf_conf(self):
    """
    Getter method for interface_eth_ospf_conf, mapped from YANG variable /interface/ethernet/ip/interface_eth_ospf_conf (container)
    """
    return self.__interface_eth_ospf_conf
      
  def _set_interface_eth_ospf_conf(self, v, load=False):
    """
    Setter method for interface_eth_ospf_conf, mapped from YANG variable /interface/ethernet/ip/interface_eth_ospf_conf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_eth_ospf_conf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_eth_ospf_conf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_eth_ospf_conf.interface_eth_ospf_conf, is_container='container', presence=False, yang_name="interface-eth-ospf-conf", rest_name="interface-eth-ospf-conf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_eth_ospf_conf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_eth_ospf_conf.interface_eth_ospf_conf, is_container='container', presence=False, yang_name="interface-eth-ospf-conf", rest_name="interface-eth-ospf-conf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__interface_eth_ospf_conf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_eth_ospf_conf(self):
    self.__interface_eth_ospf_conf = YANGDynClass(base=interface_eth_ospf_conf.interface_eth_ospf_conf, is_container='container', presence=False, yang_name="interface-eth-ospf-conf", rest_name="interface-eth-ospf-conf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)

  ip_config = __builtin__.property(_get_ip_config, _set_ip_config)
  arp_node_config = __builtin__.property(_get_arp_node_config, _set_arp_node_config)
  interface_eth_dhcp_conf = __builtin__.property(_get_interface_eth_dhcp_conf, _set_interface_eth_dhcp_conf)
  icmp = __builtin__.property(_get_icmp, _set_icmp)
  igmp = __builtin__.property(_get_igmp, _set_igmp)
  interface_eth_ospf_conf = __builtin__.property(_get_interface_eth_ospf_conf, _set_interface_eth_ospf_conf)


  _pyangbind_elements = {'ip_config': ip_config, 'arp_node_config': arp_node_config, 'interface_eth_dhcp_conf': interface_eth_dhcp_conf, 'icmp': icmp, 'igmp': igmp, 'interface_eth_ospf_conf': interface_eth_ospf_conf, }


