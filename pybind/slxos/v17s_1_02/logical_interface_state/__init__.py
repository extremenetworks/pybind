
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import main_interface_pseudo_wire
import main_interface_tunnel
import main_interface_physical
class logical_interface_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-nsm-operational - based on the path /logical-interface-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Logical interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__main_interface_pseudo_wire','__main_interface_tunnel','__main_interface_physical',)

  _yang_name = 'logical-interface-state'
  _rest_name = 'logical-interface-state'

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
    self.__main_interface_physical = YANGDynClass(base=YANGListType("intf_name",main_interface_physical.main_interface_physical, yang_name="main-interface-physical", rest_name="main-interface-physical", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='intf-name', extensions=None), is_container='list', yang_name="main-interface-physical", rest_name="main-interface-physical", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    self.__main_interface_tunnel = YANGDynClass(base=main_interface_tunnel.main_interface_tunnel, is_container='container', presence=False, yang_name="main-interface-tunnel", rest_name="main-interface-tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='container', is_config=False)
    self.__main_interface_pseudo_wire = YANGDynClass(base=main_interface_pseudo_wire.main_interface_pseudo_wire, is_container='container', presence=False, yang_name="main-interface-pseudo-wire", rest_name="main-interface-pseudo-wire", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='container', is_config=False)

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
      return [u'logical-interface-state']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'logical-interface-state']

  def _get_main_interface_pseudo_wire(self):
    """
    Getter method for main_interface_pseudo_wire, mapped from YANG variable /logical_interface_state/main_interface_pseudo_wire (container)

    YANG Description: main interface pseudo wire
    """
    return self.__main_interface_pseudo_wire
      
  def _set_main_interface_pseudo_wire(self, v, load=False):
    """
    Setter method for main_interface_pseudo_wire, mapped from YANG variable /logical_interface_state/main_interface_pseudo_wire (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_main_interface_pseudo_wire is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_main_interface_pseudo_wire() directly.

    YANG Description: main interface pseudo wire
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=main_interface_pseudo_wire.main_interface_pseudo_wire, is_container='container', presence=False, yang_name="main-interface-pseudo-wire", rest_name="main-interface-pseudo-wire", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """main_interface_pseudo_wire must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=main_interface_pseudo_wire.main_interface_pseudo_wire, is_container='container', presence=False, yang_name="main-interface-pseudo-wire", rest_name="main-interface-pseudo-wire", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='container', is_config=False)""",
        })

    self.__main_interface_pseudo_wire = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_main_interface_pseudo_wire(self):
    self.__main_interface_pseudo_wire = YANGDynClass(base=main_interface_pseudo_wire.main_interface_pseudo_wire, is_container='container', presence=False, yang_name="main-interface-pseudo-wire", rest_name="main-interface-pseudo-wire", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='container', is_config=False)


  def _get_main_interface_tunnel(self):
    """
    Getter method for main_interface_tunnel, mapped from YANG variable /logical_interface_state/main_interface_tunnel (container)

    YANG Description: main interface tunnel
    """
    return self.__main_interface_tunnel
      
  def _set_main_interface_tunnel(self, v, load=False):
    """
    Setter method for main_interface_tunnel, mapped from YANG variable /logical_interface_state/main_interface_tunnel (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_main_interface_tunnel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_main_interface_tunnel() directly.

    YANG Description: main interface tunnel
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=main_interface_tunnel.main_interface_tunnel, is_container='container', presence=False, yang_name="main-interface-tunnel", rest_name="main-interface-tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """main_interface_tunnel must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=main_interface_tunnel.main_interface_tunnel, is_container='container', presence=False, yang_name="main-interface-tunnel", rest_name="main-interface-tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='container', is_config=False)""",
        })

    self.__main_interface_tunnel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_main_interface_tunnel(self):
    self.__main_interface_tunnel = YANGDynClass(base=main_interface_tunnel.main_interface_tunnel, is_container='container', presence=False, yang_name="main-interface-tunnel", rest_name="main-interface-tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='container', is_config=False)


  def _get_main_interface_physical(self):
    """
    Getter method for main_interface_physical, mapped from YANG variable /logical_interface_state/main_interface_physical (list)

    YANG Description: main interface
    """
    return self.__main_interface_physical
      
  def _set_main_interface_physical(self, v, load=False):
    """
    Setter method for main_interface_physical, mapped from YANG variable /logical_interface_state/main_interface_physical (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_main_interface_physical is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_main_interface_physical() directly.

    YANG Description: main interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("intf_name",main_interface_physical.main_interface_physical, yang_name="main-interface-physical", rest_name="main-interface-physical", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='intf-name', extensions=None), is_container='list', yang_name="main-interface-physical", rest_name="main-interface-physical", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """main_interface_physical must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("intf_name",main_interface_physical.main_interface_physical, yang_name="main-interface-physical", rest_name="main-interface-physical", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='intf-name', extensions=None), is_container='list', yang_name="main-interface-physical", rest_name="main-interface-physical", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)""",
        })

    self.__main_interface_physical = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_main_interface_physical(self):
    self.__main_interface_physical = YANGDynClass(base=YANGListType("intf_name",main_interface_physical.main_interface_physical, yang_name="main-interface-physical", rest_name="main-interface-physical", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='intf-name', extensions=None), is_container='list', yang_name="main-interface-physical", rest_name="main-interface-physical", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)

  main_interface_pseudo_wire = __builtin__.property(_get_main_interface_pseudo_wire)
  main_interface_tunnel = __builtin__.property(_get_main_interface_tunnel)
  main_interface_physical = __builtin__.property(_get_main_interface_physical)


  _pyangbind_elements = {'main_interface_pseudo_wire': main_interface_pseudo_wire, 'main_interface_tunnel': main_interface_tunnel, 'main_interface_physical': main_interface_physical, }


