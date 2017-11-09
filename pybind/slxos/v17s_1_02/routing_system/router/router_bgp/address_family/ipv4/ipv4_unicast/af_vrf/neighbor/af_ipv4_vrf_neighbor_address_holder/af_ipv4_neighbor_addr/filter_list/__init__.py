
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import direction_in
import direction_out
class filter_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast/af-vrf/neighbor/af-ipv4-vrf-neighbor-address-holder/af-ipv4-neighbor-addr/filter-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__direction_in','__direction_out',)

  _yang_name = 'filter-list'
  _rest_name = 'filter-list'

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
    self.__direction_in = YANGDynClass(base=direction_in.direction_in, is_container='container', presence=False, yang_name="direction-in", rest_name="direction-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__direction_out = YANGDynClass(base=direction_out.direction_out, is_container='container', presence=False, yang_name="direction-out", rest_name="direction-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'af-vrf', u'neighbor', u'af-ipv4-vrf-neighbor-address-holder', u'af-ipv4-neighbor-addr', u'filter-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'af-vrf', u'neighbor', u'af-ipv4-vrf-neighbor-address-holder', u'af-ipv4-neighbor-addr', u'filter-list']

  def _get_direction_in(self):
    """
    Getter method for direction_in, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/filter_list/direction_in (container)
    """
    return self.__direction_in
      
  def _set_direction_in(self, v, load=False):
    """
    Setter method for direction_in, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/filter_list/direction_in (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_direction_in is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_direction_in() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=direction_in.direction_in, is_container='container', presence=False, yang_name="direction-in", rest_name="direction-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """direction_in must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=direction_in.direction_in, is_container='container', presence=False, yang_name="direction-in", rest_name="direction-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__direction_in = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_direction_in(self):
    self.__direction_in = YANGDynClass(base=direction_in.direction_in, is_container='container', presence=False, yang_name="direction-in", rest_name="direction-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_direction_out(self):
    """
    Getter method for direction_out, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/filter_list/direction_out (container)
    """
    return self.__direction_out
      
  def _set_direction_out(self, v, load=False):
    """
    Setter method for direction_out, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/filter_list/direction_out (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_direction_out is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_direction_out() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=direction_out.direction_out, is_container='container', presence=False, yang_name="direction-out", rest_name="direction-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """direction_out must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=direction_out.direction_out, is_container='container', presence=False, yang_name="direction-out", rest_name="direction-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__direction_out = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_direction_out(self):
    self.__direction_out = YANGDynClass(base=direction_out.direction_out, is_container='container', presence=False, yang_name="direction-out", rest_name="direction-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  direction_in = __builtin__.property(_get_direction_in, _set_direction_in)
  direction_out = __builtin__.property(_get_direction_out, _set_direction_out)


  _pyangbind_elements = {'direction_in': direction_in, 'direction_out': direction_out, }


