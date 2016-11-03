
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import metric_style
import summary_address
import ldp_sync
import default_link_metric
import af_common_attributes
class af_ipv4_attributes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/isis/router-isis-cmds-holder/address-family/ipv4/af-ipv4-unicast/af-ipv4-attributes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__metric_style','__summary_address','__ldp_sync','__default_link_metric','__af_common_attributes',)

  _yang_name = 'af-ipv4-attributes'
  _rest_name = ''

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
    self.__default_link_metric = YANGDynClass(base=default_link_metric.default_link_metric, is_container='container', yang_name="default-link-metric", rest_name="default-link-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Default Link Metric', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    self.__metric_style = YANGDynClass(base=metric_style.metric_style, is_container='container', yang_name="metric-style", rest_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Use narrow  or wide metric type', u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    self.__ldp_sync = YANGDynClass(base=ldp_sync.ldp_sync, is_container='container', yang_name="ldp-sync", rest_name="ldp-sync", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable LDP-SYNC on all eligible ISIS interfaces'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    self.__summary_address = YANGDynClass(base=YANGListType("summary_ip summary_ip_mask",summary_address.summary_address, yang_name="summary-address", rest_name="summary-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='summary-ip summary-ip-mask', extensions={u'tailf-common': {u'info': u'Configure Integrated IS-IS address summaries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IsisAfIpv4UcastSummaryAddress', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-full-no': None}}), is_container='list', yang_name="summary-address", rest_name="summary-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Integrated IS-IS address summaries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IsisAfIpv4UcastSummaryAddress', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='list', is_config=True)
    self.__af_common_attributes = YANGDynClass(base=af_common_attributes.af_common_attributes, is_container='container', yang_name="af-common-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'isis', u'router-isis-cmds-holder', u'address-family', u'ipv4', u'af-ipv4-unicast', u'af-ipv4-attributes']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'isis', u'address-family', u'ipv4', u'unicast']

  def _get_metric_style(self):
    """
    Getter method for metric_style, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/metric_style (container)
    """
    return self.__metric_style
      
  def _set_metric_style(self, v, load=False):
    """
    Setter method for metric_style, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/metric_style (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric_style is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric_style() directly.
    """
    try:
      t = YANGDynClass(v,base=metric_style.metric_style, is_container='container', yang_name="metric-style", rest_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Use narrow  or wide metric type', u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric_style must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=metric_style.metric_style, is_container='container', yang_name="metric-style", rest_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Use narrow  or wide metric type', u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__metric_style = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric_style(self):
    self.__metric_style = YANGDynClass(base=metric_style.metric_style, is_container='container', yang_name="metric-style", rest_name="metric-style", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Use narrow  or wide metric type', u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)


  def _get_summary_address(self):
    """
    Getter method for summary_address, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/summary_address (list)
    """
    return self.__summary_address
      
  def _set_summary_address(self, v, load=False):
    """
    Setter method for summary_address, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/summary_address (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summary_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summary_address() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("summary_ip summary_ip_mask",summary_address.summary_address, yang_name="summary-address", rest_name="summary-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='summary-ip summary-ip-mask', extensions={u'tailf-common': {u'info': u'Configure Integrated IS-IS address summaries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IsisAfIpv4UcastSummaryAddress', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-full-no': None}}), is_container='list', yang_name="summary-address", rest_name="summary-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Integrated IS-IS address summaries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IsisAfIpv4UcastSummaryAddress', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summary_address must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("summary_ip summary_ip_mask",summary_address.summary_address, yang_name="summary-address", rest_name="summary-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='summary-ip summary-ip-mask', extensions={u'tailf-common': {u'info': u'Configure Integrated IS-IS address summaries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IsisAfIpv4UcastSummaryAddress', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-full-no': None}}), is_container='list', yang_name="summary-address", rest_name="summary-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Integrated IS-IS address summaries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IsisAfIpv4UcastSummaryAddress', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='list', is_config=True)""",
        })

    self.__summary_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summary_address(self):
    self.__summary_address = YANGDynClass(base=YANGListType("summary_ip summary_ip_mask",summary_address.summary_address, yang_name="summary-address", rest_name="summary-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='summary-ip summary-ip-mask', extensions={u'tailf-common': {u'info': u'Configure Integrated IS-IS address summaries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IsisAfIpv4UcastSummaryAddress', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-full-no': None}}), is_container='list', yang_name="summary-address", rest_name="summary-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Integrated IS-IS address summaries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IsisAfIpv4UcastSummaryAddress', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='list', is_config=True)


  def _get_ldp_sync(self):
    """
    Getter method for ldp_sync, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/ldp_sync (container)
    """
    return self.__ldp_sync
      
  def _set_ldp_sync(self, v, load=False):
    """
    Setter method for ldp_sync, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/ldp_sync (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_sync is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_sync() directly.
    """
    try:
      t = YANGDynClass(v,base=ldp_sync.ldp_sync, is_container='container', yang_name="ldp-sync", rest_name="ldp-sync", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable LDP-SYNC on all eligible ISIS interfaces'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_sync must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ldp_sync.ldp_sync, is_container='container', yang_name="ldp-sync", rest_name="ldp-sync", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable LDP-SYNC on all eligible ISIS interfaces'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__ldp_sync = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_sync(self):
    self.__ldp_sync = YANGDynClass(base=ldp_sync.ldp_sync, is_container='container', yang_name="ldp-sync", rest_name="ldp-sync", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable LDP-SYNC on all eligible ISIS interfaces'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)


  def _get_default_link_metric(self):
    """
    Getter method for default_link_metric, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/default_link_metric (container)
    """
    return self.__default_link_metric
      
  def _set_default_link_metric(self, v, load=False):
    """
    Setter method for default_link_metric, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/default_link_metric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_link_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_link_metric() directly.
    """
    try:
      t = YANGDynClass(v,base=default_link_metric.default_link_metric, is_container='container', yang_name="default-link-metric", rest_name="default-link-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Default Link Metric', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_link_metric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=default_link_metric.default_link_metric, is_container='container', yang_name="default-link-metric", rest_name="default-link-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Default Link Metric', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__default_link_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_link_metric(self):
    self.__default_link_metric = YANGDynClass(base=default_link_metric.default_link_metric, is_container='container', yang_name="default-link-metric", rest_name="default-link-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Default Link Metric', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)


  def _get_af_common_attributes(self):
    """
    Getter method for af_common_attributes, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes (container)
    """
    return self.__af_common_attributes
      
  def _set_af_common_attributes(self, v, load=False):
    """
    Setter method for af_common_attributes, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_af_common_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_af_common_attributes() directly.
    """
    try:
      t = YANGDynClass(v,base=af_common_attributes.af_common_attributes, is_container='container', yang_name="af-common-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """af_common_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=af_common_attributes.af_common_attributes, is_container='container', yang_name="af-common-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__af_common_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_af_common_attributes(self):
    self.__af_common_attributes = YANGDynClass(base=af_common_attributes.af_common_attributes, is_container='container', yang_name="af-common-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)

  metric_style = __builtin__.property(_get_metric_style, _set_metric_style)
  summary_address = __builtin__.property(_get_summary_address, _set_summary_address)
  ldp_sync = __builtin__.property(_get_ldp_sync, _set_ldp_sync)
  default_link_metric = __builtin__.property(_get_default_link_metric, _set_default_link_metric)
  af_common_attributes = __builtin__.property(_get_af_common_attributes, _set_af_common_attributes)


  _pyangbind_elements = {'metric_style': metric_style, 'summary_address': summary_address, 'ldp_sync': ldp_sync, 'default_link_metric': default_link_metric, 'af_common_attributes': af_common_attributes, }

