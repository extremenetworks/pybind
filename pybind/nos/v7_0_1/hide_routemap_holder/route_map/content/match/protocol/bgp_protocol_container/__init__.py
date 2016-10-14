
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class bgp_protocol_container(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ip-policy - based on the path /hide-routemap-holder/route-map/content/match/protocol/bgp-protocol-container. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__protocol_bgp','__bgp_route_type',)

  _yang_name = 'bgp-protocol-container'

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
    self.__bgp_route_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'internal': {'value': 3}, u'external': {'value': 1}, u'static-network': {'value': 2}},), is_leaf=True, yang_name="bgp-route-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)
    self.__protocol_bgp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protocol-bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BGP protocol.', u'alt-name': u'bgp', u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)

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
      return [u'hide-routemap-holder', u'route-map', u'content', u'match', u'protocol', u'bgp-protocol-container']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'route-map', u'match', u'protocol']

  def _get_protocol_bgp(self):
    """
    Getter method for protocol_bgp, mapped from YANG variable /hide_routemap_holder/route_map/content/match/protocol/bgp_protocol_container/protocol_bgp (empty)

    YANG Description: BGP protocol.
    """
    return self.__protocol_bgp
      
  def _set_protocol_bgp(self, v, load=False):
    """
    Setter method for protocol_bgp, mapped from YANG variable /hide_routemap_holder/route_map/content/match/protocol/bgp_protocol_container/protocol_bgp (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol_bgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol_bgp() directly.

    YANG Description: BGP protocol.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="protocol-bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BGP protocol.', u'alt-name': u'bgp', u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol_bgp must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protocol-bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BGP protocol.', u'alt-name': u'bgp', u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)""",
        })

    self.__protocol_bgp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol_bgp(self):
    self.__protocol_bgp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protocol-bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BGP protocol.', u'alt-name': u'bgp', u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)


  def _get_bgp_route_type(self):
    """
    Getter method for bgp_route_type, mapped from YANG variable /hide_routemap_holder/route_map/content/match/protocol/bgp_protocol_container/bgp_route_type (enumeration)
    """
    return self.__bgp_route_type
      
  def _set_bgp_route_type(self, v, load=False):
    """
    Setter method for bgp_route_type, mapped from YANG variable /hide_routemap_holder/route_map/content/match/protocol/bgp_protocol_container/bgp_route_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bgp_route_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bgp_route_type() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'internal': {'value': 3}, u'external': {'value': 1}, u'static-network': {'value': 2}},), is_leaf=True, yang_name="bgp-route-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bgp_route_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-ip-policy:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'internal': {'value': 3}, u'external': {'value': 1}, u'static-network': {'value': 2}},), is_leaf=True, yang_name="bgp-route-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)""",
        })

    self.__bgp_route_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bgp_route_type(self):
    self.__bgp_route_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'internal': {'value': 3}, u'external': {'value': 1}, u'static-network': {'value': 2}},), is_leaf=True, yang_name="bgp-route-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)

  protocol_bgp = __builtin__.property(_get_protocol_bgp, _set_protocol_bgp)
  bgp_route_type = __builtin__.property(_get_bgp_route_type, _set_bgp_route_type)


  _pyangbind_elements = {'protocol_bgp': protocol_bgp, 'bgp_route_type': bgp_route_type, }


