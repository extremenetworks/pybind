
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class peer_info_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-nsm-operational - based on the path /mct-state/show-cluster/peer-info-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Peer Info
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__peer_ip_addr','__peer_state','__peer_interface',)

  _yang_name = 'peer-info-list'
  _rest_name = 'peer-info-list'

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
    self.__peer_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-ip-addr", rest_name="peer-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    self.__peer_state = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="peer-state", rest_name="peer-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    self.__peer_interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="peer-interface", rest_name="peer-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)

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
      return [u'mct-state', u'show-cluster', u'peer-info-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mct-state', u'show-cluster', u'peer-info-list']

  def _get_peer_ip_addr(self):
    """
    Getter method for peer_ip_addr, mapped from YANG variable /mct_state/show_cluster/peer_info_list/peer_ip_addr (uint32)

    YANG Description: Peer IP address
    """
    return self.__peer_ip_addr
      
  def _set_peer_ip_addr(self, v, load=False):
    """
    Setter method for peer_ip_addr, mapped from YANG variable /mct_state/show_cluster/peer_info_list/peer_ip_addr (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_ip_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_ip_addr() directly.

    YANG Description: Peer IP address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-ip-addr", rest_name="peer-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_ip_addr must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-ip-addr", rest_name="peer-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__peer_ip_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_ip_addr(self):
    self.__peer_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-ip-addr", rest_name="peer-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)


  def _get_peer_state(self):
    """
    Getter method for peer_state, mapped from YANG variable /mct_state/show_cluster/peer_info_list/peer_state (boolean)

    YANG Description: Peer state
    """
    return self.__peer_state
      
  def _set_peer_state(self, v, load=False):
    """
    Setter method for peer_state, mapped from YANG variable /mct_state/show_cluster/peer_info_list/peer_state (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_state() directly.

    YANG Description: Peer state
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="peer-state", rest_name="peer-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_state must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="peer-state", rest_name="peer-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)""",
        })

    self.__peer_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_state(self):
    self.__peer_state = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="peer-state", rest_name="peer-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)


  def _get_peer_interface(self):
    """
    Getter method for peer_interface, mapped from YANG variable /mct_state/show_cluster/peer_info_list/peer_interface (string)

    YANG Description: Peer Interface
    """
    return self.__peer_interface
      
  def _set_peer_interface(self, v, load=False):
    """
    Setter method for peer_interface, mapped from YANG variable /mct_state/show_cluster/peer_info_list/peer_interface (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_interface() directly.

    YANG Description: Peer Interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="peer-interface", rest_name="peer-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_interface must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="peer-interface", rest_name="peer-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__peer_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_interface(self):
    self.__peer_interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="peer-interface", rest_name="peer-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)

  peer_ip_addr = __builtin__.property(_get_peer_ip_addr)
  peer_state = __builtin__.property(_get_peer_state)
  peer_interface = __builtin__.property(_get_peer_interface)


  _pyangbind_elements = {'peer_ip_addr': peer_ip_addr, 'peer_state': peer_state, 'peer_interface': peer_interface, }


