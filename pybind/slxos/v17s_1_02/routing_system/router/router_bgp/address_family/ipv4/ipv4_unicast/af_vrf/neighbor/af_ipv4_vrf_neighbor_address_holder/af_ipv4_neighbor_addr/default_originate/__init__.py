
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class default_originate(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast/af-vrf/neighbor/af-ipv4-vrf-neighbor-address-holder/af-ipv4-neighbor-addr/default-originate. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__default_originate_status',)

  _yang_name = 'default-originate'
  _rest_name = 'default-originate'

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
    self.__default_originate_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-originate-status", rest_name="default-originate-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'af-vrf', u'neighbor', u'af-ipv4-vrf-neighbor-address-holder', u'af-ipv4-neighbor-addr', u'default-originate']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'af-vrf', u'neighbor', u'af-ipv4-vrf-neighbor-address-holder', u'af-ipv4-neighbor-addr', u'default-originate']

  def _get_default_originate_status(self):
    """
    Getter method for default_originate_status, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/default_originate/default_originate_status (empty)
    """
    return self.__default_originate_status
      
  def _set_default_originate_status(self, v, load=False):
    """
    Setter method for default_originate_status, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/default_originate/default_originate_status (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_originate_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_originate_status() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="default-originate-status", rest_name="default-originate-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_originate_status must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-originate-status", rest_name="default-originate-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__default_originate_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_originate_status(self):
    self.__default_originate_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-originate-status", rest_name="default-originate-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  default_originate_status = __builtin__.property(_get_default_originate_status, _set_default_originate_status)


  _pyangbind_elements = {'default_originate_status': default_originate_status, }


