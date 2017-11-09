
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import pim_snp_sources
import pim_snp_wg_member_ports
class pim_snp_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mc-hms-operational - based on the path /igmp-snooping-state/pim-snp-groups/pim-snp-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Pim Snooping Group Information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__group_addr','__vlan_id','__uptime','__expiry_time','__last_reporter','__pim_snp_sources','__pim_snp_wg_member_ports',)

  _yang_name = 'pim-snp-groups'
  _rest_name = 'pim-snp-groups'

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
    self.__uptime = YANGDynClass(base=unicode, is_leaf=True, yang_name="uptime", rest_name="uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__expiry_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="expiry-time", rest_name="expiry-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__group_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="group-addr", rest_name="group-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__pim_snp_sources = YANGDynClass(base=YANGListType("src_addr",pim_snp_sources.pim_snp_sources, yang_name="pim-snp-sources", rest_name="pim-snp-sources", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='src-addr', extensions={u'tailf-common': {u'callpoint': u'mc-hms-pim-snp-source', u'cli-suppress-show-path': None}}), is_container='list', yang_name="pim-snp-sources", rest_name="pim-snp-sources", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-pim-snp-source', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)
    self.__pim_snp_wg_member_ports = YANGDynClass(base=YANGListType("interface_name",pim_snp_wg_member_ports.pim_snp_wg_member_ports, yang_name="pim-snp-wg-member-ports", rest_name="pim-snp-wg-member-ports", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-name', extensions={u'tailf-common': {u'callpoint': u'mc_hms-pim-snp-member-port-pim-snp-wg-member-ports-2'}}), is_container='list', yang_name="pim-snp-wg-member-ports", rest_name="pim-snp-wg-member-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc_hms-pim-snp-member-port-pim-snp-wg-member-ports-2'}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)
    self.__last_reporter = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="last-reporter", rest_name="last-reporter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)

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
      return [u'igmp-snooping-state', u'pim-snp-groups', u'pim-snp-groups']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'igmp-snooping-state', u'pim-snp-groups', u'pim-snp-groups']

  def _get_group_addr(self):
    """
    Getter method for group_addr, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/group_addr (inet:ipv4-address)

    YANG Description: group ip address
    """
    return self.__group_addr
      
  def _set_group_addr(self, v, load=False):
    """
    Setter method for group_addr, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/group_addr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_addr() directly.

    YANG Description: group ip address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="group-addr", rest_name="group-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_addr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="group-addr", rest_name="group-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__group_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_addr(self):
    self.__group_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="group-addr", rest_name="group-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/vlan_id (uint32)

    YANG Description: vlan id
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/vlan_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: vlan id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_uptime(self):
    """
    Getter method for uptime, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/uptime (string)

    YANG Description: group up time
    """
    return self.__uptime
      
  def _set_uptime(self, v, load=False):
    """
    Setter method for uptime, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/uptime (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_uptime is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_uptime() directly.

    YANG Description: group up time
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="uptime", rest_name="uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """uptime must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="uptime", rest_name="uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__uptime = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_uptime(self):
    self.__uptime = YANGDynClass(base=unicode, is_leaf=True, yang_name="uptime", rest_name="uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_expiry_time(self):
    """
    Getter method for expiry_time, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/expiry_time (string)

    YANG Description: group expiry time
    """
    return self.__expiry_time
      
  def _set_expiry_time(self, v, load=False):
    """
    Setter method for expiry_time, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/expiry_time (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_expiry_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_expiry_time() directly.

    YANG Description: group expiry time
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="expiry-time", rest_name="expiry-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """expiry_time must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="expiry-time", rest_name="expiry-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__expiry_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_expiry_time(self):
    self.__expiry_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="expiry-time", rest_name="expiry-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_last_reporter(self):
    """
    Getter method for last_reporter, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/last_reporter (inet:ipv4-address)

    YANG Description: last reporter
    """
    return self.__last_reporter
      
  def _set_last_reporter(self, v, load=False):
    """
    Setter method for last_reporter, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/last_reporter (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_reporter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_reporter() directly.

    YANG Description: last reporter
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="last-reporter", rest_name="last-reporter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_reporter must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="last-reporter", rest_name="last-reporter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__last_reporter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_reporter(self):
    self.__last_reporter = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="last-reporter", rest_name="last-reporter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_pim_snp_sources(self):
    """
    Getter method for pim_snp_sources, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/pim_snp_sources (list)

    YANG Description: pim snooping source instance
    """
    return self.__pim_snp_sources
      
  def _set_pim_snp_sources(self, v, load=False):
    """
    Setter method for pim_snp_sources, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/pim_snp_sources (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pim_snp_sources is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pim_snp_sources() directly.

    YANG Description: pim snooping source instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("src_addr",pim_snp_sources.pim_snp_sources, yang_name="pim-snp-sources", rest_name="pim-snp-sources", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='src-addr', extensions={u'tailf-common': {u'callpoint': u'mc-hms-pim-snp-source', u'cli-suppress-show-path': None}}), is_container='list', yang_name="pim-snp-sources", rest_name="pim-snp-sources", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-pim-snp-source', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pim_snp_sources must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("src_addr",pim_snp_sources.pim_snp_sources, yang_name="pim-snp-sources", rest_name="pim-snp-sources", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='src-addr', extensions={u'tailf-common': {u'callpoint': u'mc-hms-pim-snp-source', u'cli-suppress-show-path': None}}), is_container='list', yang_name="pim-snp-sources", rest_name="pim-snp-sources", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-pim-snp-source', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)""",
        })

    self.__pim_snp_sources = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pim_snp_sources(self):
    self.__pim_snp_sources = YANGDynClass(base=YANGListType("src_addr",pim_snp_sources.pim_snp_sources, yang_name="pim-snp-sources", rest_name="pim-snp-sources", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='src-addr', extensions={u'tailf-common': {u'callpoint': u'mc-hms-pim-snp-source', u'cli-suppress-show-path': None}}), is_container='list', yang_name="pim-snp-sources", rest_name="pim-snp-sources", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-pim-snp-source', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)


  def _get_pim_snp_wg_member_ports(self):
    """
    Getter method for pim_snp_wg_member_ports, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/pim_snp_wg_member_ports (list)
    """
    return self.__pim_snp_wg_member_ports
      
  def _set_pim_snp_wg_member_ports(self, v, load=False):
    """
    Setter method for pim_snp_wg_member_ports, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/pim_snp_wg_member_ports (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pim_snp_wg_member_ports is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pim_snp_wg_member_ports() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("interface_name",pim_snp_wg_member_ports.pim_snp_wg_member_ports, yang_name="pim-snp-wg-member-ports", rest_name="pim-snp-wg-member-ports", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-name', extensions={u'tailf-common': {u'callpoint': u'mc_hms-pim-snp-member-port-pim-snp-wg-member-ports-2'}}), is_container='list', yang_name="pim-snp-wg-member-ports", rest_name="pim-snp-wg-member-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc_hms-pim-snp-member-port-pim-snp-wg-member-ports-2'}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pim_snp_wg_member_ports must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("interface_name",pim_snp_wg_member_ports.pim_snp_wg_member_ports, yang_name="pim-snp-wg-member-ports", rest_name="pim-snp-wg-member-ports", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-name', extensions={u'tailf-common': {u'callpoint': u'mc_hms-pim-snp-member-port-pim-snp-wg-member-ports-2'}}), is_container='list', yang_name="pim-snp-wg-member-ports", rest_name="pim-snp-wg-member-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc_hms-pim-snp-member-port-pim-snp-wg-member-ports-2'}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)""",
        })

    self.__pim_snp_wg_member_ports = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pim_snp_wg_member_ports(self):
    self.__pim_snp_wg_member_ports = YANGDynClass(base=YANGListType("interface_name",pim_snp_wg_member_ports.pim_snp_wg_member_ports, yang_name="pim-snp-wg-member-ports", rest_name="pim-snp-wg-member-ports", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-name', extensions={u'tailf-common': {u'callpoint': u'mc_hms-pim-snp-member-port-pim-snp-wg-member-ports-2'}}), is_container='list', yang_name="pim-snp-wg-member-ports", rest_name="pim-snp-wg-member-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc_hms-pim-snp-member-port-pim-snp-wg-member-ports-2'}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)

  group_addr = __builtin__.property(_get_group_addr)
  vlan_id = __builtin__.property(_get_vlan_id)
  uptime = __builtin__.property(_get_uptime)
  expiry_time = __builtin__.property(_get_expiry_time)
  last_reporter = __builtin__.property(_get_last_reporter)
  pim_snp_sources = __builtin__.property(_get_pim_snp_sources)
  pim_snp_wg_member_ports = __builtin__.property(_get_pim_snp_wg_member_ports)


  _pyangbind_elements = {'group_addr': group_addr, 'vlan_id': vlan_id, 'uptime': uptime, 'expiry_time': expiry_time, 'last_reporter': last_reporter, 'pim_snp_sources': pim_snp_sources, 'pim_snp_wg_member_ports': pim_snp_wg_member_ports, }


