
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import gshut_timer_attributes
class graceful_shutdown(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/router-bgp-attributes/neighbor/neighbor-ipv6s/neighbor-ipv6-addr/graceful-shutdown. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__gshut_timer_value','__gshut_route_map','__gshut_timer_attributes',)

  _yang_name = 'graceful-shutdown'
  _rest_name = 'graceful-shutdown'

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
    self.__gshut_timer_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'30..600']}), is_leaf=True, yang_name="gshut-timer-value", rest_name="gshut-timer-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-gshut-timer', is_config=True)
    self.__gshut_timer_attributes = YANGDynClass(base=gshut_timer_attributes.gshut_timer_attributes, is_container='container', presence=False, yang_name="gshut-timer-attributes", rest_name="", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-attributes'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__gshut_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="gshut-route-map", rest_name="route-map", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-route-map'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'router-bgp-attributes', u'neighbor', u'neighbor-ipv6s', u'neighbor-ipv6-addr', u'graceful-shutdown']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'neighbor', u'neighbor-ipv6-addr', u'graceful-shutdown']

  def _get_gshut_timer_value(self):
    """
    Getter method for gshut_timer_value, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/graceful_shutdown/gshut_timer_value (bgp-gshut-timer)
    """
    return self.__gshut_timer_value
      
  def _set_gshut_timer_value(self, v, load=False):
    """
    Setter method for gshut_timer_value, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/graceful_shutdown/gshut_timer_value (bgp-gshut-timer)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gshut_timer_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gshut_timer_value() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'30..600']}), is_leaf=True, yang_name="gshut-timer-value", rest_name="gshut-timer-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-gshut-timer', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gshut_timer_value must be of a type compatible with bgp-gshut-timer""",
          'defined-type': "brocade-bgp:bgp-gshut-timer",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'30..600']}), is_leaf=True, yang_name="gshut-timer-value", rest_name="gshut-timer-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-gshut-timer', is_config=True)""",
        })

    self.__gshut_timer_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gshut_timer_value(self):
    self.__gshut_timer_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'30..600']}), is_leaf=True, yang_name="gshut-timer-value", rest_name="gshut-timer-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-gshut-timer', is_config=True)


  def _get_gshut_route_map(self):
    """
    Getter method for gshut_route_map, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/graceful_shutdown/gshut_route_map (rmap-type)
    """
    return self.__gshut_route_map
      
  def _set_gshut_route_map(self, v, load=False):
    """
    Setter method for gshut_route_map, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/graceful_shutdown/gshut_route_map (rmap-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gshut_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gshut_route_map() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="gshut-route-map", rest_name="route-map", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-route-map'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gshut_route_map must be of a type compatible with rmap-type""",
          'defined-type': "brocade-bgp:rmap-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="gshut-route-map", rest_name="route-map", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-route-map'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)""",
        })

    self.__gshut_route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gshut_route_map(self):
    self.__gshut_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="gshut-route-map", rest_name="route-map", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-route-map'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)


  def _get_gshut_timer_attributes(self):
    """
    Getter method for gshut_timer_attributes, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/graceful_shutdown/gshut_timer_attributes (container)
    """
    return self.__gshut_timer_attributes
      
  def _set_gshut_timer_attributes(self, v, load=False):
    """
    Setter method for gshut_timer_attributes, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/graceful_shutdown/gshut_timer_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gshut_timer_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gshut_timer_attributes() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=gshut_timer_attributes.gshut_timer_attributes, is_container='container', presence=False, yang_name="gshut-timer-attributes", rest_name="", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-attributes'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gshut_timer_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=gshut_timer_attributes.gshut_timer_attributes, is_container='container', presence=False, yang_name="gshut-timer-attributes", rest_name="", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-attributes'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__gshut_timer_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gshut_timer_attributes(self):
    self.__gshut_timer_attributes = YANGDynClass(base=gshut_timer_attributes.gshut_timer_attributes, is_container='container', presence=False, yang_name="gshut-timer-attributes", rest_name="", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-attributes'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  gshut_timer_value = __builtin__.property(_get_gshut_timer_value, _set_gshut_timer_value)
  gshut_route_map = __builtin__.property(_get_gshut_route_map, _set_gshut_route_map)
  gshut_timer_attributes = __builtin__.property(_get_gshut_timer_attributes, _set_gshut_timer_attributes)

  __choices__ = {u'ch-gshut-options': {u'ca-gshut-timer-attributes': [u'gshut_timer_attributes'], u'ca-gshut-timer-route-map': [u'gshut_route_map']}}
  _pyangbind_elements = {'gshut_timer_value': gshut_timer_value, 'gshut_route_map': gshut_route_map, 'gshut_timer_attributes': gshut_timer_attributes, }


