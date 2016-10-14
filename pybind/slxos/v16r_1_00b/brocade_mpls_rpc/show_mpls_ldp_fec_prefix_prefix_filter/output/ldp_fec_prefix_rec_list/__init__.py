
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ldp_fec_out_intf_rec_list
class ldp_fec_prefix_rec_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-ldp-fec-prefix-prefix-filter/output/ldp-fec-prefix-rec-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ldp_fec_destination','__ldp_fec_state','__ldp_fec_out_intf_rec_list','__ldp_fec_ingress','__ldp_fec_egress','__ldp_fec_filtered','__ldp_fec_lwd',)

  _yang_name = 'ldp-fec-prefix-rec-list'

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
    self.__ldp_fec_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'current': {'value': 16384}, u'unknown': {'value': 0}, u'retained': {'value': 49152}, u'down': {'value': 32768}},), is_leaf=True, yang_name="ldp-fec-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='ldp-fec-state', is_config=True)
    self.__ldp_fec_out_intf_rec_list = YANGDynClass(base=YANGListType("ldp_fec_nexthop",ldp_fec_out_intf_rec_list.ldp_fec_out_intf_rec_list, yang_name="ldp-fec-out-intf-rec-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-fec-nexthop', extensions=None), is_container='list', yang_name="ldp-fec-out-intf-rec-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    self.__ldp_fec_destination = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__ldp_fec_ingress = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    self.__ldp_fec_egress = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    self.__ldp_fec_lwd = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    self.__ldp_fec_filtered = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'out': {'value': 2}, u'in': {'value': 1}},), is_leaf=True, yang_name="ldp-fec-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='in-out', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-ldp-fec-prefix-prefix-filter', u'output', u'ldp-fec-prefix-rec-list']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'show-mpls-ldp-fec-prefix-prefix-filter', u'output', u'ldp-fec-prefix-rec-list']

  def _get_ldp_fec_destination(self):
    """
    Getter method for ldp_fec_destination, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_destination (inet:ipv4-address)

    YANG Description: Destination
    """
    return self.__ldp_fec_destination
      
  def _set_ldp_fec_destination(self, v, load=False):
    """
    Setter method for ldp_fec_destination, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_destination (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_destination is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_destination() directly.

    YANG Description: Destination
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_destination must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ldp_fec_destination = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_destination(self):
    self.__ldp_fec_destination = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_ldp_fec_state(self):
    """
    Getter method for ldp_fec_state, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_state (ldp-fec-state)

    YANG Description: State
    """
    return self.__ldp_fec_state
      
  def _set_ldp_fec_state(self, v, load=False):
    """
    Setter method for ldp_fec_state, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_state (ldp-fec-state)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_state() directly.

    YANG Description: State
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'current': {'value': 16384}, u'unknown': {'value': 0}, u'retained': {'value': 49152}, u'down': {'value': 32768}},), is_leaf=True, yang_name="ldp-fec-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='ldp-fec-state', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_state must be of a type compatible with ldp-fec-state""",
          'defined-type': "brocade-mpls:ldp-fec-state",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'current': {'value': 16384}, u'unknown': {'value': 0}, u'retained': {'value': 49152}, u'down': {'value': 32768}},), is_leaf=True, yang_name="ldp-fec-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='ldp-fec-state', is_config=True)""",
        })

    self.__ldp_fec_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_state(self):
    self.__ldp_fec_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'current': {'value': 16384}, u'unknown': {'value': 0}, u'retained': {'value': 49152}, u'down': {'value': 32768}},), is_leaf=True, yang_name="ldp-fec-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='ldp-fec-state', is_config=True)


  def _get_ldp_fec_out_intf_rec_list(self):
    """
    Getter method for ldp_fec_out_intf_rec_list, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_out_intf_rec_list (list)
    """
    return self.__ldp_fec_out_intf_rec_list
      
  def _set_ldp_fec_out_intf_rec_list(self, v, load=False):
    """
    Setter method for ldp_fec_out_intf_rec_list, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_out_intf_rec_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_out_intf_rec_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_out_intf_rec_list() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ldp_fec_nexthop",ldp_fec_out_intf_rec_list.ldp_fec_out_intf_rec_list, yang_name="ldp-fec-out-intf-rec-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-fec-nexthop', extensions=None), is_container='list', yang_name="ldp-fec-out-intf-rec-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_out_intf_rec_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ldp_fec_nexthop",ldp_fec_out_intf_rec_list.ldp_fec_out_intf_rec_list, yang_name="ldp-fec-out-intf-rec-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-fec-nexthop', extensions=None), is_container='list', yang_name="ldp-fec-out-intf-rec-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__ldp_fec_out_intf_rec_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_out_intf_rec_list(self):
    self.__ldp_fec_out_intf_rec_list = YANGDynClass(base=YANGListType("ldp_fec_nexthop",ldp_fec_out_intf_rec_list.ldp_fec_out_intf_rec_list, yang_name="ldp-fec-out-intf-rec-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-fec-nexthop', extensions=None), is_container='list', yang_name="ldp-fec-out-intf-rec-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)


  def _get_ldp_fec_ingress(self):
    """
    Getter method for ldp_fec_ingress, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_ingress (yes-no)

    YANG Description: Ingress
    """
    return self.__ldp_fec_ingress
      
  def _set_ldp_fec_ingress(self, v, load=False):
    """
    Setter method for ldp_fec_ingress, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_ingress (yes-no)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_ingress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_ingress() directly.

    YANG Description: Ingress
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_ingress must be of a type compatible with yes-no""",
          'defined-type': "brocade-mpls:yes-no",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)""",
        })

    self.__ldp_fec_ingress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_ingress(self):
    self.__ldp_fec_ingress = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)


  def _get_ldp_fec_egress(self):
    """
    Getter method for ldp_fec_egress, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_egress (yes-no)

    YANG Description: Egress
    """
    return self.__ldp_fec_egress
      
  def _set_ldp_fec_egress(self, v, load=False):
    """
    Setter method for ldp_fec_egress, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_egress (yes-no)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_egress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_egress() directly.

    YANG Description: Egress
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_egress must be of a type compatible with yes-no""",
          'defined-type': "brocade-mpls:yes-no",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)""",
        })

    self.__ldp_fec_egress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_egress(self):
    self.__ldp_fec_egress = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)


  def _get_ldp_fec_filtered(self):
    """
    Getter method for ldp_fec_filtered, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_filtered (in-out)

    YANG Description: Filtered
    """
    return self.__ldp_fec_filtered
      
  def _set_ldp_fec_filtered(self, v, load=False):
    """
    Setter method for ldp_fec_filtered, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_filtered (in-out)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_filtered is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_filtered() directly.

    YANG Description: Filtered
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'out': {'value': 2}, u'in': {'value': 1}},), is_leaf=True, yang_name="ldp-fec-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='in-out', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_filtered must be of a type compatible with in-out""",
          'defined-type': "brocade-mpls:in-out",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'out': {'value': 2}, u'in': {'value': 1}},), is_leaf=True, yang_name="ldp-fec-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='in-out', is_config=True)""",
        })

    self.__ldp_fec_filtered = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_filtered(self):
    self.__ldp_fec_filtered = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'out': {'value': 2}, u'in': {'value': 1}},), is_leaf=True, yang_name="ldp-fec-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='in-out', is_config=True)


  def _get_ldp_fec_lwd(self):
    """
    Getter method for ldp_fec_lwd, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_lwd (yes-no)

    YANG Description: LWD
    """
    return self.__ldp_fec_lwd
      
  def _set_ldp_fec_lwd(self, v, load=False):
    """
    Setter method for ldp_fec_lwd, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list/ldp_fec_lwd (yes-no)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_lwd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_lwd() directly.

    YANG Description: LWD
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_lwd must be of a type compatible with yes-no""",
          'defined-type': "brocade-mpls:yes-no",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)""",
        })

    self.__ldp_fec_lwd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_lwd(self):
    self.__ldp_fec_lwd = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)

  ldp_fec_destination = __builtin__.property(_get_ldp_fec_destination, _set_ldp_fec_destination)
  ldp_fec_state = __builtin__.property(_get_ldp_fec_state, _set_ldp_fec_state)
  ldp_fec_out_intf_rec_list = __builtin__.property(_get_ldp_fec_out_intf_rec_list, _set_ldp_fec_out_intf_rec_list)
  ldp_fec_ingress = __builtin__.property(_get_ldp_fec_ingress, _set_ldp_fec_ingress)
  ldp_fec_egress = __builtin__.property(_get_ldp_fec_egress, _set_ldp_fec_egress)
  ldp_fec_filtered = __builtin__.property(_get_ldp_fec_filtered, _set_ldp_fec_filtered)
  ldp_fec_lwd = __builtin__.property(_get_ldp_fec_lwd, _set_ldp_fec_lwd)


  _pyangbind_elements = {'ldp_fec_destination': ldp_fec_destination, 'ldp_fec_state': ldp_fec_state, 'ldp_fec_out_intf_rec_list': ldp_fec_out_intf_rec_list, 'ldp_fec_ingress': ldp_fec_ingress, 'ldp_fec_egress': ldp_fec_egress, 'ldp_fec_filtered': ldp_fec_filtered, 'ldp_fec_lwd': ldp_fec_lwd, }


