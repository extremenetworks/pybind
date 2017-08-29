
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import igmps_interface
class igmps_mrouter(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface-vlan/vlan/ip/igmpVlan/snooping/igmps_mrouter. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__igmps_interface',)

  _yang_name = 'igmps_mrouter'
  _rest_name = 'mrouter'

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
    self.__igmps_interface = YANGDynClass(base=YANGListType("igmps_if_type igmps_value",igmps_interface.igmps_interface, yang_name="igmps-interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='igmps-if-type igmps-value', extensions={u'tailf-common': {u'info': u'Interface to use', u'cli-suppress-mode': None, u'alt-name': u'interface', u'cli-suppress-list-no': None}}), is_container='list', yang_name="igmps-interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface to use', u'cli-suppress-mode': None, u'alt-name': u'interface', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='list', is_config=True)

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
      return [u'interface-vlan', u'vlan', u'ip', u'igmpVlan', u'snooping', u'igmps_mrouter']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vlan', u'ip', u'igmp', u'snooping', u'mrouter']

  def _get_igmps_interface(self):
    """
    Getter method for igmps_interface, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_mrouter/igmps_interface (list)
    """
    return self.__igmps_interface
      
  def _set_igmps_interface(self, v, load=False):
    """
    Setter method for igmps_interface, mapped from YANG variable /interface_vlan/vlan/ip/igmpVlan/snooping/igmps_mrouter/igmps_interface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("igmps_if_type igmps_value",igmps_interface.igmps_interface, yang_name="igmps-interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='igmps-if-type igmps-value', extensions={u'tailf-common': {u'info': u'Interface to use', u'cli-suppress-mode': None, u'alt-name': u'interface', u'cli-suppress-list-no': None}}), is_container='list', yang_name="igmps-interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface to use', u'cli-suppress-mode': None, u'alt-name': u'interface', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_interface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("igmps_if_type igmps_value",igmps_interface.igmps_interface, yang_name="igmps-interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='igmps-if-type igmps-value', extensions={u'tailf-common': {u'info': u'Interface to use', u'cli-suppress-mode': None, u'alt-name': u'interface', u'cli-suppress-list-no': None}}), is_container='list', yang_name="igmps-interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface to use', u'cli-suppress-mode': None, u'alt-name': u'interface', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='list', is_config=True)""",
        })

    self.__igmps_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_interface(self):
    self.__igmps_interface = YANGDynClass(base=YANGListType("igmps_if_type igmps_value",igmps_interface.igmps_interface, yang_name="igmps-interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='igmps-if-type igmps-value', extensions={u'tailf-common': {u'info': u'Interface to use', u'cli-suppress-mode': None, u'alt-name': u'interface', u'cli-suppress-list-no': None}}), is_container='list', yang_name="igmps-interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface to use', u'cli-suppress-mode': None, u'alt-name': u'interface', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='list', is_config=True)

  igmps_interface = __builtin__.property(_get_igmps_interface, _set_igmps_interface)


  _pyangbind_elements = {'igmps_interface': igmps_interface, }

