
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import igmps_querier
import igmps_mrouter
import igmps_static_group
class snooping(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface-vlan/vlan/ip/igmpVlan/snooping. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__igmps_version','__igmps_last_member_query_interval','__igmps_query_interval','__igmps_query_max_response_time','__igmps_enable','__igmps_fast_leave','__igmps_querier','__igmps_mrouter','__igmps_static_group',)

  _yang_name = 'snooping'
  _rest_name = 'snooping'

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
    self.__igmps_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igmps-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Enable', u'cli-full-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='empty', is_config=True)
    self.__igmps_last_member_query_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..25500']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="igmps-last-member-query-interval", rest_name="last-member-query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Last Member Query Interval', u'cli-full-command': None, u'alt-name': u'last-member-query-interval'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='lmqt-type', is_config=True)
    self.__igmps_mrouter = YANGDynClass(base=igmps_mrouter.igmps_mrouter, is_container='container', presence=False, yang_name="igmps_mrouter", rest_name="mrouter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'IgmpsMrtrVlan', u'info': u'Multicast Router', u'alt-name': u'mrouter', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)
    self.__igmps_static_group = YANGDynClass(base=YANGListType("igmps_mcast_address igmps_interface igmps_if_type igmps_value",igmps_static_group.igmps_static_group, yang_name="igmps_static-group", rest_name="static-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='igmps-mcast-address igmps-interface igmps-if-type igmps-value', extensions={u'tailf-common': {u'callpoint': u'IgmpsSgVlan', u'cli-suppress-mode': None, u'alt-name': u'static-group', u'info': u'Static Group to be Joined', u'cli-suppress-list-no': None}}), is_container='list', yang_name="igmps_static-group", rest_name="static-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'IgmpsSgVlan', u'cli-suppress-mode': None, u'alt-name': u'static-group', u'info': u'Static Group to be Joined', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='list', is_config=True)
    self.__igmps_query_max_response_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..25']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="igmps-query-max-response-time", rest_name="query-max-response-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Max Query Response Time', u'cli-full-command': None, u'alt-name': u'query-max-response-time'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='qmrt-type', is_config=True)
    self.__igmps_query_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..18000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(125), is_leaf=True, yang_name="igmps-query-interval", rest_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Query Interval', u'cli-full-command': None, u'alt-name': u'query-interval'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='qi-type', is_config=True)
    self.__igmps_version = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="igmps-version", rest_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Snooping Version', u'cli-full-command': None, u'alt-name': u'version'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='igmps-version-type', is_config=True)
    self.__igmps_querier = YANGDynClass(base=igmps_querier.igmps_querier, is_container='container', presence=False, yang_name="igmps-querier", rest_name="querier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Querier', u'alt-name': u'querier', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)
    self.__igmps_fast_leave = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igmps-fast-leave", rest_name="fast-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fast Leave Processing', u'cli-full-command': None, u'alt-name': u'fast-leave'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='empty', is_config=True)

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
      return [u'interface-vlan', u'vlan', u'ip', u'igmpVlan', u'snooping']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vlan', u'ip', u'igmp', u'snooping']

  def _get_igmps_version(self):
    """
    Getter method for igmps_version, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_version (igmps-version-type)
    """
    return self.__igmps_version
      
  def _set_igmps_version(self, v, load=False):
    """
    Setter method for igmps_version, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_version (igmps-version-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_version() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="igmps-version", rest_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Snooping Version', u'cli-full-command': None, u'alt-name': u'version'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='igmps-version-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_version must be of a type compatible with igmps-version-type""",
          'defined-type': "brocade-igmp-snooping:igmps-version-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="igmps-version", rest_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Snooping Version', u'cli-full-command': None, u'alt-name': u'version'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='igmps-version-type', is_config=True)""",
        })

    self.__igmps_version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_version(self):
    self.__igmps_version = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="igmps-version", rest_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Snooping Version', u'cli-full-command': None, u'alt-name': u'version'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='igmps-version-type', is_config=True)


  def _get_igmps_last_member_query_interval(self):
    """
    Getter method for igmps_last_member_query_interval, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_last_member_query_interval (lmqt-type)
    """
    return self.__igmps_last_member_query_interval
      
  def _set_igmps_last_member_query_interval(self, v, load=False):
    """
    Setter method for igmps_last_member_query_interval, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_last_member_query_interval (lmqt-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_last_member_query_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_last_member_query_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..25500']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="igmps-last-member-query-interval", rest_name="last-member-query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Last Member Query Interval', u'cli-full-command': None, u'alt-name': u'last-member-query-interval'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='lmqt-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_last_member_query_interval must be of a type compatible with lmqt-type""",
          'defined-type': "brocade-igmp-snooping:lmqt-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..25500']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="igmps-last-member-query-interval", rest_name="last-member-query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Last Member Query Interval', u'cli-full-command': None, u'alt-name': u'last-member-query-interval'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='lmqt-type', is_config=True)""",
        })

    self.__igmps_last_member_query_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_last_member_query_interval(self):
    self.__igmps_last_member_query_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..25500']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="igmps-last-member-query-interval", rest_name="last-member-query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Last Member Query Interval', u'cli-full-command': None, u'alt-name': u'last-member-query-interval'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='lmqt-type', is_config=True)


  def _get_igmps_query_interval(self):
    """
    Getter method for igmps_query_interval, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_query_interval (qi-type)
    """
    return self.__igmps_query_interval
      
  def _set_igmps_query_interval(self, v, load=False):
    """
    Setter method for igmps_query_interval, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_query_interval (qi-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_query_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_query_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..18000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(125), is_leaf=True, yang_name="igmps-query-interval", rest_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Query Interval', u'cli-full-command': None, u'alt-name': u'query-interval'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='qi-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_query_interval must be of a type compatible with qi-type""",
          'defined-type': "brocade-igmp-snooping:qi-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..18000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(125), is_leaf=True, yang_name="igmps-query-interval", rest_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Query Interval', u'cli-full-command': None, u'alt-name': u'query-interval'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='qi-type', is_config=True)""",
        })

    self.__igmps_query_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_query_interval(self):
    self.__igmps_query_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..18000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(125), is_leaf=True, yang_name="igmps-query-interval", rest_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Query Interval', u'cli-full-command': None, u'alt-name': u'query-interval'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='qi-type', is_config=True)


  def _get_igmps_query_max_response_time(self):
    """
    Getter method for igmps_query_max_response_time, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_query_max_response_time (qmrt-type)
    """
    return self.__igmps_query_max_response_time
      
  def _set_igmps_query_max_response_time(self, v, load=False):
    """
    Setter method for igmps_query_max_response_time, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_query_max_response_time (qmrt-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_query_max_response_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_query_max_response_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..25']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="igmps-query-max-response-time", rest_name="query-max-response-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Max Query Response Time', u'cli-full-command': None, u'alt-name': u'query-max-response-time'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='qmrt-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_query_max_response_time must be of a type compatible with qmrt-type""",
          'defined-type': "brocade-igmp-snooping:qmrt-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..25']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="igmps-query-max-response-time", rest_name="query-max-response-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Max Query Response Time', u'cli-full-command': None, u'alt-name': u'query-max-response-time'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='qmrt-type', is_config=True)""",
        })

    self.__igmps_query_max_response_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_query_max_response_time(self):
    self.__igmps_query_max_response_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..25']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="igmps-query-max-response-time", rest_name="query-max-response-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Max Query Response Time', u'cli-full-command': None, u'alt-name': u'query-max-response-time'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='qmrt-type', is_config=True)


  def _get_igmps_enable(self):
    """
    Getter method for igmps_enable, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_enable (empty)
    """
    return self.__igmps_enable
      
  def _set_igmps_enable(self, v, load=False):
    """
    Setter method for igmps_enable, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_enable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="igmps-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Enable', u'cli-full-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igmps-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Enable', u'cli-full-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='empty', is_config=True)""",
        })

    self.__igmps_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_enable(self):
    self.__igmps_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igmps-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMP Enable', u'cli-full-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='empty', is_config=True)


  def _get_igmps_fast_leave(self):
    """
    Getter method for igmps_fast_leave, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_fast_leave (empty)
    """
    return self.__igmps_fast_leave
      
  def _set_igmps_fast_leave(self, v, load=False):
    """
    Setter method for igmps_fast_leave, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_fast_leave (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_fast_leave is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_fast_leave() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="igmps-fast-leave", rest_name="fast-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fast Leave Processing', u'cli-full-command': None, u'alt-name': u'fast-leave'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_fast_leave must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igmps-fast-leave", rest_name="fast-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fast Leave Processing', u'cli-full-command': None, u'alt-name': u'fast-leave'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='empty', is_config=True)""",
        })

    self.__igmps_fast_leave = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_fast_leave(self):
    self.__igmps_fast_leave = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igmps-fast-leave", rest_name="fast-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fast Leave Processing', u'cli-full-command': None, u'alt-name': u'fast-leave'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='empty', is_config=True)


  def _get_igmps_querier(self):
    """
    Getter method for igmps_querier, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_querier (container)
    """
    return self.__igmps_querier
      
  def _set_igmps_querier(self, v, load=False):
    """
    Setter method for igmps_querier, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_querier (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_querier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_querier() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=igmps_querier.igmps_querier, is_container='container', presence=False, yang_name="igmps-querier", rest_name="querier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Querier', u'alt-name': u'querier', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_querier must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=igmps_querier.igmps_querier, is_container='container', presence=False, yang_name="igmps-querier", rest_name="querier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Querier', u'alt-name': u'querier', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)""",
        })

    self.__igmps_querier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_querier(self):
    self.__igmps_querier = YANGDynClass(base=igmps_querier.igmps_querier, is_container='container', presence=False, yang_name="igmps-querier", rest_name="querier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Querier', u'alt-name': u'querier', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)


  def _get_igmps_mrouter(self):
    """
    Getter method for igmps_mrouter, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_mrouter (container)
    """
    return self.__igmps_mrouter
      
  def _set_igmps_mrouter(self, v, load=False):
    """
    Setter method for igmps_mrouter, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_mrouter (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_mrouter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_mrouter() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=igmps_mrouter.igmps_mrouter, is_container='container', presence=False, yang_name="igmps_mrouter", rest_name="mrouter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'IgmpsMrtrVlan', u'info': u'Multicast Router', u'alt-name': u'mrouter', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_mrouter must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=igmps_mrouter.igmps_mrouter, is_container='container', presence=False, yang_name="igmps_mrouter", rest_name="mrouter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'IgmpsMrtrVlan', u'info': u'Multicast Router', u'alt-name': u'mrouter', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)""",
        })

    self.__igmps_mrouter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_mrouter(self):
    self.__igmps_mrouter = YANGDynClass(base=igmps_mrouter.igmps_mrouter, is_container='container', presence=False, yang_name="igmps_mrouter", rest_name="mrouter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'IgmpsMrtrVlan', u'info': u'Multicast Router', u'alt-name': u'mrouter', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)


  def _get_igmps_static_group(self):
    """
    Getter method for igmps_static_group, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_static_group (list)
    """
    return self.__igmps_static_group
      
  def _set_igmps_static_group(self, v, load=False):
    """
    Setter method for igmps_static_group, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_static_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_static_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_static_group() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("igmps_mcast_address igmps_interface igmps_if_type igmps_value",igmps_static_group.igmps_static_group, yang_name="igmps_static-group", rest_name="static-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='igmps-mcast-address igmps-interface igmps-if-type igmps-value', extensions={u'tailf-common': {u'callpoint': u'IgmpsSgVlan', u'cli-suppress-mode': None, u'alt-name': u'static-group', u'info': u'Static Group to be Joined', u'cli-suppress-list-no': None}}), is_container='list', yang_name="igmps_static-group", rest_name="static-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'IgmpsSgVlan', u'cli-suppress-mode': None, u'alt-name': u'static-group', u'info': u'Static Group to be Joined', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_static_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("igmps_mcast_address igmps_interface igmps_if_type igmps_value",igmps_static_group.igmps_static_group, yang_name="igmps_static-group", rest_name="static-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='igmps-mcast-address igmps-interface igmps-if-type igmps-value', extensions={u'tailf-common': {u'callpoint': u'IgmpsSgVlan', u'cli-suppress-mode': None, u'alt-name': u'static-group', u'info': u'Static Group to be Joined', u'cli-suppress-list-no': None}}), is_container='list', yang_name="igmps_static-group", rest_name="static-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'IgmpsSgVlan', u'cli-suppress-mode': None, u'alt-name': u'static-group', u'info': u'Static Group to be Joined', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='list', is_config=True)""",
        })

    self.__igmps_static_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_static_group(self):
    self.__igmps_static_group = YANGDynClass(base=YANGListType("igmps_mcast_address igmps_interface igmps_if_type igmps_value",igmps_static_group.igmps_static_group, yang_name="igmps_static-group", rest_name="static-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='igmps-mcast-address igmps-interface igmps-if-type igmps-value', extensions={u'tailf-common': {u'callpoint': u'IgmpsSgVlan', u'cli-suppress-mode': None, u'alt-name': u'static-group', u'info': u'Static Group to be Joined', u'cli-suppress-list-no': None}}), is_container='list', yang_name="igmps_static-group", rest_name="static-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'IgmpsSgVlan', u'cli-suppress-mode': None, u'alt-name': u'static-group', u'info': u'Static Group to be Joined', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='list', is_config=True)

  igmps_version = __builtin__.property(_get_igmps_version, _set_igmps_version)
  igmps_last_member_query_interval = __builtin__.property(_get_igmps_last_member_query_interval, _set_igmps_last_member_query_interval)
  igmps_query_interval = __builtin__.property(_get_igmps_query_interval, _set_igmps_query_interval)
  igmps_query_max_response_time = __builtin__.property(_get_igmps_query_max_response_time, _set_igmps_query_max_response_time)
  igmps_enable = __builtin__.property(_get_igmps_enable, _set_igmps_enable)
  igmps_fast_leave = __builtin__.property(_get_igmps_fast_leave, _set_igmps_fast_leave)
  igmps_querier = __builtin__.property(_get_igmps_querier, _set_igmps_querier)
  igmps_mrouter = __builtin__.property(_get_igmps_mrouter, _set_igmps_mrouter)
  igmps_static_group = __builtin__.property(_get_igmps_static_group, _set_igmps_static_group)


  _pyangbind_elements = {'igmps_version': igmps_version, 'igmps_last_member_query_interval': igmps_last_member_query_interval, 'igmps_query_interval': igmps_query_interval, 'igmps_query_max_response_time': igmps_query_max_response_time, 'igmps_enable': igmps_enable, 'igmps_fast_leave': igmps_fast_leave, 'igmps_querier': igmps_querier, 'igmps_mrouter': igmps_mrouter, 'igmps_static_group': igmps_static_group, }

