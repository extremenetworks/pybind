
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class static(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast/default-vrf/af-ipv4-uc-and-vrf-cmds-call-point-holder/redistribute/static. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__redistribute_static','__unicast_static_metric','__static_route_map',)

  _yang_name = 'static'
  _rest_name = 'static'

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
    self.__unicast_static_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="unicast-static-metric", rest_name="unicast-static-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='conn-metric', is_config=True)
    self.__static_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="static-route-map", rest_name="static-route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)
    self.__redistribute_static = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="redistribute-static", rest_name="redistribute-static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'default-vrf', u'af-ipv4-uc-and-vrf-cmds-call-point-holder', u'redistribute', u'static']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'default-vrf', u'af-ipv4-uc-and-vrf-cmds-call-point-holder', u'redistribute', u'static']

  def _get_redistribute_static(self):
    """
    Getter method for redistribute_static, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder/redistribute/static/redistribute_static (empty)
    """
    return self.__redistribute_static
      
  def _set_redistribute_static(self, v, load=False):
    """
    Setter method for redistribute_static, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder/redistribute/static/redistribute_static (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute_static is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute_static() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="redistribute-static", rest_name="redistribute-static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute_static must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="redistribute-static", rest_name="redistribute-static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__redistribute_static = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute_static(self):
    self.__redistribute_static = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="redistribute-static", rest_name="redistribute-static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_unicast_static_metric(self):
    """
    Getter method for unicast_static_metric, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder/redistribute/static/unicast_static_metric (conn-metric)
    """
    return self.__unicast_static_metric
      
  def _set_unicast_static_metric(self, v, load=False):
    """
    Setter method for unicast_static_metric, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder/redistribute/static/unicast_static_metric (conn-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unicast_static_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unicast_static_metric() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="unicast-static-metric", rest_name="unicast-static-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='conn-metric', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unicast_static_metric must be of a type compatible with conn-metric""",
          'defined-type': "brocade-bgp:conn-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="unicast-static-metric", rest_name="unicast-static-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='conn-metric', is_config=True)""",
        })

    self.__unicast_static_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unicast_static_metric(self):
    self.__unicast_static_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="unicast-static-metric", rest_name="unicast-static-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='conn-metric', is_config=True)


  def _get_static_route_map(self):
    """
    Getter method for static_route_map, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder/redistribute/static/static_route_map (rmap-type)
    """
    return self.__static_route_map
      
  def _set_static_route_map(self, v, load=False):
    """
    Setter method for static_route_map, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder/redistribute/static/static_route_map (rmap-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_route_map() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="static-route-map", rest_name="static-route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_route_map must be of a type compatible with rmap-type""",
          'defined-type': "brocade-bgp:rmap-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="static-route-map", rest_name="static-route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)""",
        })

    self.__static_route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_route_map(self):
    self.__static_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="static-route-map", rest_name="static-route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)

  redistribute_static = __builtin__.property(_get_redistribute_static, _set_redistribute_static)
  unicast_static_metric = __builtin__.property(_get_unicast_static_metric, _set_unicast_static_metric)
  static_route_map = __builtin__.property(_get_static_route_map, _set_static_route_map)


  _pyangbind_elements = {'redistribute_static': redistribute_static, 'unicast_static_metric': unicast_static_metric, 'static_route_map': static_route_map, }


