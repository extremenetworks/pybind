
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ethernet_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/router-bgp-attributes/neighbor/neighbor-ipv6s/neighbor-ipv6-addr/update-source/ethernet-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interface_type','__ethernet',)

  _yang_name = 'ethernet-interface'
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
    self.__ethernet = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="ethernet", rest_name="", parent=self, choice=(u'ch-update-source', u'ca-eth'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ethernet Interface', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='interface:interface-type', is_config=True)
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 3}, u'gigabitethernet': {'value': 1}, u'tengigabitethernet': {'value': 2}, u'hundredgigabitethernet': {'value': 4}},), is_leaf=True, yang_name="interface-type", rest_name="", parent=self, choice=(u'ch-update-source', u'ca-eth'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='enumeration', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'router-bgp-attributes', u'neighbor', u'neighbor-ipv6s', u'neighbor-ipv6-addr', u'update-source', u'ethernet-interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'neighbor', u'update-source']

  def _get_interface_type(self):
    """
    Getter method for interface_type, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/ethernet_interface/interface_type (enumeration)
    """
    return self.__interface_type
      
  def _set_interface_type(self, v, load=False):
    """
    Setter method for interface_type, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/ethernet_interface/interface_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_type() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 3}, u'gigabitethernet': {'value': 1}, u'tengigabitethernet': {'value': 2}, u'hundredgigabitethernet': {'value': 4}},), is_leaf=True, yang_name="interface-type", rest_name="", parent=self, choice=(u'ch-update-source', u'ca-eth'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-bgp:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 3}, u'gigabitethernet': {'value': 1}, u'tengigabitethernet': {'value': 2}, u'hundredgigabitethernet': {'value': 4}},), is_leaf=True, yang_name="interface-type", rest_name="", parent=self, choice=(u'ch-update-source', u'ca-eth'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='enumeration', is_config=True)""",
        })

    self.__interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_type(self):
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 3}, u'gigabitethernet': {'value': 1}, u'tengigabitethernet': {'value': 2}, u'hundredgigabitethernet': {'value': 4}},), is_leaf=True, yang_name="interface-type", rest_name="", parent=self, choice=(u'ch-update-source', u'ca-eth'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='enumeration', is_config=True)


  def _get_ethernet(self):
    """
    Getter method for ethernet, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/ethernet_interface/ethernet (interface:interface-type)
    """
    return self.__ethernet
      
  def _set_ethernet(self, v, load=False):
    """
    Setter method for ethernet, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/ethernet_interface/ethernet (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ethernet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ethernet() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="ethernet", rest_name="", parent=self, choice=(u'ch-update-source', u'ca-eth'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ethernet Interface', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ethernet must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="ethernet", rest_name="", parent=self, choice=(u'ch-update-source', u'ca-eth'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ethernet Interface', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__ethernet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ethernet(self):
    self.__ethernet = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="ethernet", rest_name="", parent=self, choice=(u'ch-update-source', u'ca-eth'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ethernet Interface', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='interface:interface-type', is_config=True)

  interface_type = __builtin__.property(_get_interface_type, _set_interface_type)
  ethernet = __builtin__.property(_get_ethernet, _set_ethernet)

  __choices__ = {u'ch-update-source': {u'ca-eth': [u'interface_type', u'ethernet']}}
  _pyangbind_elements = {'interface_type': interface_type, 'ethernet': ethernet, }

