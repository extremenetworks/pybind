
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vlan_add
import evpn_vlan
class vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/evpn-config/evpn/evpn-instance/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vlan_add','__evpn_vlan',)

  _yang_name = 'vlan'
  _rest_name = 'vlan'

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
    self.__evpn_vlan = YANGDynClass(base=YANGListType("vlan_number",evpn_vlan.evpn_vlan, yang_name="evpn-vlan", rest_name="evpn-vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-number', extensions=None), is_container='list', yang_name="evpn-vlan", rest_name="evpn-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    self.__vlan_add = YANGDynClass(base=vlan_add.vlan_add, is_container='container', presence=False, yang_name="vlan-add", rest_name="vlan-add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'routing-system', u'evpn-config', u'evpn', u'evpn-instance', u'vlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'routing-system', u'evpn-config', u'evpn', u'evpn-instance', u'vlan']

  def _get_vlan_add(self):
    """
    Getter method for vlan_add, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/vlan/vlan_add (container)
    """
    return self.__vlan_add
      
  def _set_vlan_add(self, v, load=False):
    """
    Setter method for vlan_add, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/vlan/vlan_add (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_add is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_add() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vlan_add.vlan_add, is_container='container', presence=False, yang_name="vlan-add", rest_name="vlan-add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_add must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vlan_add.vlan_add, is_container='container', presence=False, yang_name="vlan-add", rest_name="vlan-add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__vlan_add = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_add(self):
    self.__vlan_add = YANGDynClass(base=vlan_add.vlan_add, is_container='container', presence=False, yang_name="vlan-add", rest_name="vlan-add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_evpn_vlan(self):
    """
    Getter method for evpn_vlan, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/vlan/evpn_vlan (list)

    YANG Description: EVPN instance config
    """
    return self.__evpn_vlan
      
  def _set_evpn_vlan(self, v, load=False):
    """
    Setter method for evpn_vlan, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/vlan/evpn_vlan (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_evpn_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_evpn_vlan() directly.

    YANG Description: EVPN instance config
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vlan_number",evpn_vlan.evpn_vlan, yang_name="evpn-vlan", rest_name="evpn-vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-number', extensions=None), is_container='list', yang_name="evpn-vlan", rest_name="evpn-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """evpn_vlan must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vlan_number",evpn_vlan.evpn_vlan, yang_name="evpn-vlan", rest_name="evpn-vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-number', extensions=None), is_container='list', yang_name="evpn-vlan", rest_name="evpn-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__evpn_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_evpn_vlan(self):
    self.__evpn_vlan = YANGDynClass(base=YANGListType("vlan_number",evpn_vlan.evpn_vlan, yang_name="evpn-vlan", rest_name="evpn-vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-number', extensions=None), is_container='list', yang_name="evpn-vlan", rest_name="evpn-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)

  vlan_add = __builtin__.property(_get_vlan_add, _set_vlan_add)
  evpn_vlan = __builtin__.property(_get_evpn_vlan, _set_evpn_vlan)


  _pyangbind_elements = {'vlan_add': vlan_add, 'evpn_vlan': evpn_vlan, }


