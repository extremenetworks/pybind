
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class graceful_restart(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/ipv6/ipv6-unicast/default-vrf/af-common-cmds-holder/graceful-restart. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__graceful_restart_status','__restart_time','__purge_time','__stale_routes_time',)

  _yang_name = 'graceful-restart'
  _rest_name = 'graceful-restart'

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
    self.__graceful_restart_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="graceful-restart-status", rest_name="graceful-restart-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__restart_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="restart-time", rest_name="restart-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rtime-type', is_config=True)
    self.__stale_routes_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="stale-routes-time", rest_name="stale-routes-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='st-time-type', is_config=True)
    self.__purge_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="purge-time", rest_name="purge-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ptime-type', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'default-vrf', u'af-common-cmds-holder', u'graceful-restart']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'graceful-restart']

  def _get_graceful_restart_status(self):
    """
    Getter method for graceful_restart_status, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/graceful_restart/graceful_restart_status (empty)
    """
    return self.__graceful_restart_status
      
  def _set_graceful_restart_status(self, v, load=False):
    """
    Setter method for graceful_restart_status, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/graceful_restart/graceful_restart_status (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_graceful_restart_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_graceful_restart_status() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="graceful-restart-status", rest_name="graceful-restart-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """graceful_restart_status must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="graceful-restart-status", rest_name="graceful-restart-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__graceful_restart_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_graceful_restart_status(self):
    self.__graceful_restart_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="graceful-restart-status", rest_name="graceful-restart-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_restart_time(self):
    """
    Getter method for restart_time, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/graceful_restart/restart_time (rtime-type)
    """
    return self.__restart_time
      
  def _set_restart_time(self, v, load=False):
    """
    Setter method for restart_time, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/graceful_restart/restart_time (rtime-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_restart_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_restart_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="restart-time", rest_name="restart-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rtime-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """restart_time must be of a type compatible with rtime-type""",
          'defined-type': "brocade-bgp:rtime-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="restart-time", rest_name="restart-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rtime-type', is_config=True)""",
        })

    self.__restart_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_restart_time(self):
    self.__restart_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="restart-time", rest_name="restart-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rtime-type', is_config=True)


  def _get_purge_time(self):
    """
    Getter method for purge_time, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/graceful_restart/purge_time (ptime-type)
    """
    return self.__purge_time
      
  def _set_purge_time(self, v, load=False):
    """
    Setter method for purge_time, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/graceful_restart/purge_time (ptime-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_purge_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_purge_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="purge-time", rest_name="purge-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ptime-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """purge_time must be of a type compatible with ptime-type""",
          'defined-type': "brocade-bgp:ptime-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="purge-time", rest_name="purge-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ptime-type', is_config=True)""",
        })

    self.__purge_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_purge_time(self):
    self.__purge_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="purge-time", rest_name="purge-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ptime-type', is_config=True)


  def _get_stale_routes_time(self):
    """
    Getter method for stale_routes_time, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/graceful_restart/stale_routes_time (st-time-type)
    """
    return self.__stale_routes_time
      
  def _set_stale_routes_time(self, v, load=False):
    """
    Setter method for stale_routes_time, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/graceful_restart/stale_routes_time (st-time-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_stale_routes_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_stale_routes_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="stale-routes-time", rest_name="stale-routes-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='st-time-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """stale_routes_time must be of a type compatible with st-time-type""",
          'defined-type': "brocade-bgp:st-time-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="stale-routes-time", rest_name="stale-routes-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='st-time-type', is_config=True)""",
        })

    self.__stale_routes_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_stale_routes_time(self):
    self.__stale_routes_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="stale-routes-time", rest_name="stale-routes-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='st-time-type', is_config=True)

  graceful_restart_status = __builtin__.property(_get_graceful_restart_status, _set_graceful_restart_status)
  restart_time = __builtin__.property(_get_restart_time, _set_restart_time)
  purge_time = __builtin__.property(_get_purge_time, _set_purge_time)
  stale_routes_time = __builtin__.property(_get_stale_routes_time, _set_stale_routes_time)


  _pyangbind_elements = {'graceful_restart_status': graceful_restart_status, 'restart_time': restart_time, 'purge_time': purge_time, 'stale_routes_time': stale_routes_time, }


