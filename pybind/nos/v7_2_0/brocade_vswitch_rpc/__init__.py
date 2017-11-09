
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import get_vnetwork_hosts
import get_vnetwork_vms
import get_vnetwork_dvpgs
import get_vnetwork_dvs
import get_vnetwork_vswitches
import get_vnetwork_portgroups
import get_vmpolicy_macaddr
class brocade_vswitch(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vswitch - based on the path /brocade_vswitch_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This management submodule is an instrumentation to 
manage Virtual switch features.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__get_vnetwork_hosts','__get_vnetwork_vms','__get_vnetwork_dvpgs','__get_vnetwork_dvs','__get_vnetwork_vswitches','__get_vnetwork_portgroups','__get_vmpolicy_macaddr',)

  _yang_name = 'brocade-vswitch'
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
    self.__get_vnetwork_hosts = YANGDynClass(base=get_vnetwork_hosts.get_vnetwork_hosts, is_leaf=True, yang_name="get-vnetwork-hosts", rest_name="get-vnetwork-hosts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    self.__get_vnetwork_portgroups = YANGDynClass(base=get_vnetwork_portgroups.get_vnetwork_portgroups, is_leaf=True, yang_name="get-vnetwork-portgroups", rest_name="get-vnetwork-portgroups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    self.__get_vmpolicy_macaddr = YANGDynClass(base=get_vmpolicy_macaddr.get_vmpolicy_macaddr, is_leaf=True, yang_name="get-vmpolicy-macaddr", rest_name="get-vmpolicy-macaddr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    self.__get_vnetwork_dvs = YANGDynClass(base=get_vnetwork_dvs.get_vnetwork_dvs, is_leaf=True, yang_name="get-vnetwork-dvs", rest_name="get-vnetwork-dvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    self.__get_vnetwork_dvpgs = YANGDynClass(base=get_vnetwork_dvpgs.get_vnetwork_dvpgs, is_leaf=True, yang_name="get-vnetwork-dvpgs", rest_name="get-vnetwork-dvpgs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    self.__get_vnetwork_vms = YANGDynClass(base=get_vnetwork_vms.get_vnetwork_vms, is_leaf=True, yang_name="get-vnetwork-vms", rest_name="get-vnetwork-vms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    self.__get_vnetwork_vswitches = YANGDynClass(base=get_vnetwork_vswitches.get_vnetwork_vswitches, is_leaf=True, yang_name="get-vnetwork-vswitches", rest_name="get-vnetwork-vswitches", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)

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
      return [u'brocade_vswitch_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_get_vnetwork_hosts(self):
    """
    Getter method for get_vnetwork_hosts, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts (rpc)

    YANG Description: Shows discovered hosts
    """
    return self.__get_vnetwork_hosts
      
  def _set_get_vnetwork_hosts(self, v, load=False):
    """
    Setter method for get_vnetwork_hosts, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_vnetwork_hosts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_vnetwork_hosts() directly.

    YANG Description: Shows discovered hosts
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_vnetwork_hosts.get_vnetwork_hosts, is_leaf=True, yang_name="get-vnetwork-hosts", rest_name="get-vnetwork-hosts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_vnetwork_hosts must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_vnetwork_hosts.get_vnetwork_hosts, is_leaf=True, yang_name="get-vnetwork-hosts", rest_name="get-vnetwork-hosts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)""",
        })

    self.__get_vnetwork_hosts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_vnetwork_hosts(self):
    self.__get_vnetwork_hosts = YANGDynClass(base=get_vnetwork_hosts.get_vnetwork_hosts, is_leaf=True, yang_name="get-vnetwork-hosts", rest_name="get-vnetwork-hosts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)


  def _get_get_vnetwork_vms(self):
    """
    Getter method for get_vnetwork_vms, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_vms (rpc)

    YANG Description: Shows discovered VMs
    """
    return self.__get_vnetwork_vms
      
  def _set_get_vnetwork_vms(self, v, load=False):
    """
    Setter method for get_vnetwork_vms, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_vms (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_vnetwork_vms is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_vnetwork_vms() directly.

    YANG Description: Shows discovered VMs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_vnetwork_vms.get_vnetwork_vms, is_leaf=True, yang_name="get-vnetwork-vms", rest_name="get-vnetwork-vms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_vnetwork_vms must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_vnetwork_vms.get_vnetwork_vms, is_leaf=True, yang_name="get-vnetwork-vms", rest_name="get-vnetwork-vms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)""",
        })

    self.__get_vnetwork_vms = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_vnetwork_vms(self):
    self.__get_vnetwork_vms = YANGDynClass(base=get_vnetwork_vms.get_vnetwork_vms, is_leaf=True, yang_name="get-vnetwork-vms", rest_name="get-vnetwork-vms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)


  def _get_get_vnetwork_dvpgs(self):
    """
    Getter method for get_vnetwork_dvpgs, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_dvpgs (rpc)

    YANG Description: Shows discovered distributed virtual port-groups
    """
    return self.__get_vnetwork_dvpgs
      
  def _set_get_vnetwork_dvpgs(self, v, load=False):
    """
    Setter method for get_vnetwork_dvpgs, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_dvpgs (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_vnetwork_dvpgs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_vnetwork_dvpgs() directly.

    YANG Description: Shows discovered distributed virtual port-groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_vnetwork_dvpgs.get_vnetwork_dvpgs, is_leaf=True, yang_name="get-vnetwork-dvpgs", rest_name="get-vnetwork-dvpgs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_vnetwork_dvpgs must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_vnetwork_dvpgs.get_vnetwork_dvpgs, is_leaf=True, yang_name="get-vnetwork-dvpgs", rest_name="get-vnetwork-dvpgs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)""",
        })

    self.__get_vnetwork_dvpgs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_vnetwork_dvpgs(self):
    self.__get_vnetwork_dvpgs = YANGDynClass(base=get_vnetwork_dvpgs.get_vnetwork_dvpgs, is_leaf=True, yang_name="get-vnetwork-dvpgs", rest_name="get-vnetwork-dvpgs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)


  def _get_get_vnetwork_dvs(self):
    """
    Getter method for get_vnetwork_dvs, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_dvs (rpc)

    YANG Description: Shows discovered Distributed Virtual Switches
    """
    return self.__get_vnetwork_dvs
      
  def _set_get_vnetwork_dvs(self, v, load=False):
    """
    Setter method for get_vnetwork_dvs, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_dvs (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_vnetwork_dvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_vnetwork_dvs() directly.

    YANG Description: Shows discovered Distributed Virtual Switches
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_vnetwork_dvs.get_vnetwork_dvs, is_leaf=True, yang_name="get-vnetwork-dvs", rest_name="get-vnetwork-dvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_vnetwork_dvs must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_vnetwork_dvs.get_vnetwork_dvs, is_leaf=True, yang_name="get-vnetwork-dvs", rest_name="get-vnetwork-dvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)""",
        })

    self.__get_vnetwork_dvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_vnetwork_dvs(self):
    self.__get_vnetwork_dvs = YANGDynClass(base=get_vnetwork_dvs.get_vnetwork_dvs, is_leaf=True, yang_name="get-vnetwork-dvs", rest_name="get-vnetwork-dvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)


  def _get_get_vnetwork_vswitches(self):
    """
    Getter method for get_vnetwork_vswitches, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_vswitches (rpc)

    YANG Description: Shows discovered Virtual Switches
    """
    return self.__get_vnetwork_vswitches
      
  def _set_get_vnetwork_vswitches(self, v, load=False):
    """
    Setter method for get_vnetwork_vswitches, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_vswitches (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_vnetwork_vswitches is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_vnetwork_vswitches() directly.

    YANG Description: Shows discovered Virtual Switches
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_vnetwork_vswitches.get_vnetwork_vswitches, is_leaf=True, yang_name="get-vnetwork-vswitches", rest_name="get-vnetwork-vswitches", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_vnetwork_vswitches must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_vnetwork_vswitches.get_vnetwork_vswitches, is_leaf=True, yang_name="get-vnetwork-vswitches", rest_name="get-vnetwork-vswitches", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)""",
        })

    self.__get_vnetwork_vswitches = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_vnetwork_vswitches(self):
    self.__get_vnetwork_vswitches = YANGDynClass(base=get_vnetwork_vswitches.get_vnetwork_vswitches, is_leaf=True, yang_name="get-vnetwork-vswitches", rest_name="get-vnetwork-vswitches", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)


  def _get_get_vnetwork_portgroups(self):
    """
    Getter method for get_vnetwork_portgroups, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_portgroups (rpc)

    YANG Description: Shows discovered PortGroups
    """
    return self.__get_vnetwork_portgroups
      
  def _set_get_vnetwork_portgroups(self, v, load=False):
    """
    Setter method for get_vnetwork_portgroups, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_portgroups (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_vnetwork_portgroups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_vnetwork_portgroups() directly.

    YANG Description: Shows discovered PortGroups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_vnetwork_portgroups.get_vnetwork_portgroups, is_leaf=True, yang_name="get-vnetwork-portgroups", rest_name="get-vnetwork-portgroups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_vnetwork_portgroups must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_vnetwork_portgroups.get_vnetwork_portgroups, is_leaf=True, yang_name="get-vnetwork-portgroups", rest_name="get-vnetwork-portgroups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)""",
        })

    self.__get_vnetwork_portgroups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_vnetwork_portgroups(self):
    self.__get_vnetwork_portgroups = YANGDynClass(base=get_vnetwork_portgroups.get_vnetwork_portgroups, is_leaf=True, yang_name="get-vnetwork-portgroups", rest_name="get-vnetwork-portgroups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)


  def _get_get_vmpolicy_macaddr(self):
    """
    Getter method for get_vmpolicy_macaddr, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr (rpc)

    YANG Description: Shows vnics/vmknics to portgroup to port-profile association
    """
    return self.__get_vmpolicy_macaddr
      
  def _set_get_vmpolicy_macaddr(self, v, load=False):
    """
    Setter method for get_vmpolicy_macaddr, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_vmpolicy_macaddr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_vmpolicy_macaddr() directly.

    YANG Description: Shows vnics/vmknics to portgroup to port-profile association
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_vmpolicy_macaddr.get_vmpolicy_macaddr, is_leaf=True, yang_name="get-vmpolicy-macaddr", rest_name="get-vmpolicy-macaddr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_vmpolicy_macaddr must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_vmpolicy_macaddr.get_vmpolicy_macaddr, is_leaf=True, yang_name="get-vmpolicy-macaddr", rest_name="get-vmpolicy-macaddr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)""",
        })

    self.__get_vmpolicy_macaddr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_vmpolicy_macaddr(self):
    self.__get_vmpolicy_macaddr = YANGDynClass(base=get_vmpolicy_macaddr.get_vmpolicy_macaddr, is_leaf=True, yang_name="get-vmpolicy-macaddr", rest_name="get-vmpolicy-macaddr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='rpc', is_config=True)

  get_vnetwork_hosts = __builtin__.property(_get_get_vnetwork_hosts, _set_get_vnetwork_hosts)
  get_vnetwork_vms = __builtin__.property(_get_get_vnetwork_vms, _set_get_vnetwork_vms)
  get_vnetwork_dvpgs = __builtin__.property(_get_get_vnetwork_dvpgs, _set_get_vnetwork_dvpgs)
  get_vnetwork_dvs = __builtin__.property(_get_get_vnetwork_dvs, _set_get_vnetwork_dvs)
  get_vnetwork_vswitches = __builtin__.property(_get_get_vnetwork_vswitches, _set_get_vnetwork_vswitches)
  get_vnetwork_portgroups = __builtin__.property(_get_get_vnetwork_portgroups, _set_get_vnetwork_portgroups)
  get_vmpolicy_macaddr = __builtin__.property(_get_get_vmpolicy_macaddr, _set_get_vmpolicy_macaddr)


  _pyangbind_elements = {'get_vnetwork_hosts': get_vnetwork_hosts, 'get_vnetwork_vms': get_vnetwork_vms, 'get_vnetwork_dvpgs': get_vnetwork_dvpgs, 'get_vnetwork_dvs': get_vnetwork_dvs, 'get_vnetwork_vswitches': get_vnetwork_vswitches, 'get_vnetwork_portgroups': get_vnetwork_portgroups, 'get_vmpolicy_macaddr': get_vmpolicy_macaddr, }


