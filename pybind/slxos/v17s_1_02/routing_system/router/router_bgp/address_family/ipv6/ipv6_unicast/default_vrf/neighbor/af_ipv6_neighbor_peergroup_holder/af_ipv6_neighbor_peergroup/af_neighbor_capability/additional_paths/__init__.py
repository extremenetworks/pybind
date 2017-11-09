
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class additional_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv6/ipv6-unicast/default-vrf/neighbor/af-ipv6-neighbor-peergroup-holder/af-ipv6-neighbor-peergroup/af-neighbor-capability/additional-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__add_path_both','__send','__receive',)

  _yang_name = 'additional-paths'
  _rest_name = 'additional-paths'

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
    self.__receive = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__add_path_both = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="add-path-both", rest_name="add-path-both", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__send = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="send", rest_name="send", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'default-vrf', u'neighbor', u'af-ipv6-neighbor-peergroup-holder', u'af-ipv6-neighbor-peergroup', u'af-neighbor-capability', u'additional-paths']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'default-vrf', u'neighbor', u'af-ipv6-neighbor-peergroup-holder', u'af-ipv6-neighbor-peergroup', u'af-neighbor-capability', u'additional-paths']

  def _get_add_path_both(self):
    """
    Getter method for add_path_both, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/af_neighbor_capability/additional_paths/add_path_both (empty)
    """
    return self.__add_path_both
      
  def _set_add_path_both(self, v, load=False):
    """
    Setter method for add_path_both, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/af_neighbor_capability/additional_paths/add_path_both (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_add_path_both is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_add_path_both() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="add-path-both", rest_name="add-path-both", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """add_path_both must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="add-path-both", rest_name="add-path-both", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__add_path_both = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_add_path_both(self):
    self.__add_path_both = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="add-path-both", rest_name="add-path-both", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_send(self):
    """
    Getter method for send, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/af_neighbor_capability/additional_paths/send (empty)
    """
    return self.__send
      
  def _set_send(self, v, load=False):
    """
    Setter method for send, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/af_neighbor_capability/additional_paths/send (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="send", rest_name="send", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="send", rest_name="send", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__send = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send(self):
    self.__send = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="send", rest_name="send", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_receive(self):
    """
    Getter method for receive, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/af_neighbor_capability/additional_paths/receive (empty)
    """
    return self.__receive
      
  def _set_receive(self, v, load=False):
    """
    Setter method for receive, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/af_neighbor_capability/additional_paths/receive (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_receive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_receive() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """receive must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__receive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_receive(self):
    self.__receive = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  add_path_both = __builtin__.property(_get_add_path_both, _set_add_path_both)
  send = __builtin__.property(_get_send, _set_send)
  receive = __builtin__.property(_get_receive, _set_receive)


  _pyangbind_elements = {'add_path_both': add_path_both, 'send': send, 'receive': receive, }


