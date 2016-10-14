
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import node
class area(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/te/database/area. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MPLS TE Database Area Operational Information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__igp_isis','__igp_ospf','__area_id','__level_id','__host_name','__router_id','__total_network_nodes','__total_router_nodes','__total_p2p_links','__total_p2mp_links','__node',)

  _yang_name = 'area'

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
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__node = YANGDynClass(base=YANGListType("local_node_id local_router_id",node.node, yang_name="node", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-node-id local-router-id', extensions={u'tailf-common': {u'callpoint': u'mpls-te-database-node', u'cli-suppress-show-path': None}}), is_container='list', yang_name="node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-te-database-node', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__area_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__total_network_nodes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-network-nodes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__igp_ospf = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__level_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="level-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__total_p2mp_links = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-p2mp-links", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__total_p2p_links = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-p2p-links", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__host_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="host-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__total_router_nodes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-router-nodes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__igp_isis = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-isis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)

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
      return [u'mpls-state', u'te', u'database', u'area']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'mpls-state', u'te', u'database', u'area']

  def _get_igp_isis(self):
    """
    Getter method for igp_isis, mapped from YANG variable /mpls_state/te/database/area/igp_isis (boolean)

    YANG Description: ISIS TE is configured
    """
    return self.__igp_isis
      
  def _set_igp_isis(self, v, load=False):
    """
    Setter method for igp_isis, mapped from YANG variable /mpls_state/te/database/area/igp_isis (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igp_isis is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igp_isis() directly.

    YANG Description: ISIS TE is configured
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="igp-isis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igp_isis must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-isis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__igp_isis = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igp_isis(self):
    self.__igp_isis = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-isis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_igp_ospf(self):
    """
    Getter method for igp_ospf, mapped from YANG variable /mpls_state/te/database/area/igp_ospf (boolean)

    YANG Description: OSPF TE is configured
    """
    return self.__igp_ospf
      
  def _set_igp_ospf(self, v, load=False):
    """
    Setter method for igp_ospf, mapped from YANG variable /mpls_state/te/database/area/igp_ospf (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igp_ospf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igp_ospf() directly.

    YANG Description: OSPF TE is configured
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="igp-ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igp_ospf must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__igp_ospf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igp_ospf(self):
    self.__igp_ospf = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_area_id(self):
    """
    Getter method for area_id, mapped from YANG variable /mpls_state/te/database/area/area_id (inet:ipv4-address)

    YANG Description: OSPF TE Area Id
    """
    return self.__area_id
      
  def _set_area_id(self, v, load=False):
    """
    Setter method for area_id, mapped from YANG variable /mpls_state/te/database/area/area_id (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_area_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_area_id() directly.

    YANG Description: OSPF TE Area Id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """area_id must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__area_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_area_id(self):
    self.__area_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_level_id(self):
    """
    Getter method for level_id, mapped from YANG variable /mpls_state/te/database/area/level_id (uint32)

    YANG Description: ISIS TE Level Id
    """
    return self.__level_id
      
  def _set_level_id(self, v, load=False):
    """
    Setter method for level_id, mapped from YANG variable /mpls_state/te/database/area/level_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level_id() directly.

    YANG Description: ISIS TE Level Id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="level-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="level-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__level_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level_id(self):
    self.__level_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="level-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_host_name(self):
    """
    Getter method for host_name, mapped from YANG variable /mpls_state/te/database/area/host_name (string)

    YANG Description: Host Name
    """
    return self.__host_name
      
  def _set_host_name(self, v, load=False):
    """
    Setter method for host_name, mapped from YANG variable /mpls_state/te/database/area/host_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host_name() directly.

    YANG Description: Host Name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="host-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="host-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__host_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host_name(self):
    self.__host_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="host-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_router_id(self):
    """
    Getter method for router_id, mapped from YANG variable /mpls_state/te/database/area/router_id (inet:ipv4-address)

    YANG Description: MPLS TE Router Id
    """
    return self.__router_id
      
  def _set_router_id(self, v, load=False):
    """
    Setter method for router_id, mapped from YANG variable /mpls_state/te/database/area/router_id (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_id() directly.

    YANG Description: MPLS TE Router Id
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_id must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_id(self):
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_total_network_nodes(self):
    """
    Getter method for total_network_nodes, mapped from YANG variable /mpls_state/te/database/area/total_network_nodes (uint32)

    YANG Description: Total network nodes
    """
    return self.__total_network_nodes
      
  def _set_total_network_nodes(self, v, load=False):
    """
    Setter method for total_network_nodes, mapped from YANG variable /mpls_state/te/database/area/total_network_nodes (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_network_nodes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_network_nodes() directly.

    YANG Description: Total network nodes
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-network-nodes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_network_nodes must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-network-nodes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__total_network_nodes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_network_nodes(self):
    self.__total_network_nodes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-network-nodes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_total_router_nodes(self):
    """
    Getter method for total_router_nodes, mapped from YANG variable /mpls_state/te/database/area/total_router_nodes (uint32)

    YANG Description: Total router nodes
    """
    return self.__total_router_nodes
      
  def _set_total_router_nodes(self, v, load=False):
    """
    Setter method for total_router_nodes, mapped from YANG variable /mpls_state/te/database/area/total_router_nodes (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_router_nodes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_router_nodes() directly.

    YANG Description: Total router nodes
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-router-nodes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_router_nodes must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-router-nodes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__total_router_nodes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_router_nodes(self):
    self.__total_router_nodes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-router-nodes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_total_p2p_links(self):
    """
    Getter method for total_p2p_links, mapped from YANG variable /mpls_state/te/database/area/total_p2p_links (uint32)

    YANG Description: Total point to point links
    """
    return self.__total_p2p_links
      
  def _set_total_p2p_links(self, v, load=False):
    """
    Setter method for total_p2p_links, mapped from YANG variable /mpls_state/te/database/area/total_p2p_links (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_p2p_links is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_p2p_links() directly.

    YANG Description: Total point to point links
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-p2p-links", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_p2p_links must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-p2p-links", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__total_p2p_links = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_p2p_links(self):
    self.__total_p2p_links = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-p2p-links", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_total_p2mp_links(self):
    """
    Getter method for total_p2mp_links, mapped from YANG variable /mpls_state/te/database/area/total_p2mp_links (uint32)

    YANG Description: Total multi access links
    """
    return self.__total_p2mp_links
      
  def _set_total_p2mp_links(self, v, load=False):
    """
    Setter method for total_p2mp_links, mapped from YANG variable /mpls_state/te/database/area/total_p2mp_links (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_p2mp_links is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_p2mp_links() directly.

    YANG Description: Total multi access links
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-p2mp-links", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_p2mp_links must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-p2mp-links", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__total_p2mp_links = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_p2mp_links(self):
    self.__total_p2mp_links = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-p2mp-links", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_node(self):
    """
    Getter method for node, mapped from YANG variable /mpls_state/te/database/area/node (list)

    YANG Description: MPLS TE Database Node Operational Information
    """
    return self.__node
      
  def _set_node(self, v, load=False):
    """
    Setter method for node, mapped from YANG variable /mpls_state/te/database/area/node (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_node is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_node() directly.

    YANG Description: MPLS TE Database Node Operational Information
    """
    try:
      t = YANGDynClass(v,base=YANGListType("local_node_id local_router_id",node.node, yang_name="node", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-node-id local-router-id', extensions={u'tailf-common': {u'callpoint': u'mpls-te-database-node', u'cli-suppress-show-path': None}}), is_container='list', yang_name="node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-te-database-node', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """node must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("local_node_id local_router_id",node.node, yang_name="node", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-node-id local-router-id', extensions={u'tailf-common': {u'callpoint': u'mpls-te-database-node', u'cli-suppress-show-path': None}}), is_container='list', yang_name="node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-te-database-node', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__node = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_node(self):
    self.__node = YANGDynClass(base=YANGListType("local_node_id local_router_id",node.node, yang_name="node", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-node-id local-router-id', extensions={u'tailf-common': {u'callpoint': u'mpls-te-database-node', u'cli-suppress-show-path': None}}), is_container='list', yang_name="node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-te-database-node', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  igp_isis = __builtin__.property(_get_igp_isis)
  igp_ospf = __builtin__.property(_get_igp_ospf)
  area_id = __builtin__.property(_get_area_id)
  level_id = __builtin__.property(_get_level_id)
  host_name = __builtin__.property(_get_host_name)
  router_id = __builtin__.property(_get_router_id)
  total_network_nodes = __builtin__.property(_get_total_network_nodes)
  total_router_nodes = __builtin__.property(_get_total_router_nodes)
  total_p2p_links = __builtin__.property(_get_total_p2p_links)
  total_p2mp_links = __builtin__.property(_get_total_p2mp_links)
  node = __builtin__.property(_get_node)


  _pyangbind_elements = {'igp_isis': igp_isis, 'igp_ospf': igp_ospf, 'area_id': area_id, 'level_id': level_id, 'host_name': host_name, 'router_id': router_id, 'total_network_nodes': total_network_nodes, 'total_router_nodes': total_router_nodes, 'total_p2p_links': total_p2p_links, 'total_p2mp_links': total_p2mp_links, 'node': node, }


