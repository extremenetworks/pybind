
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import flow_info_list
class flow(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/flow. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Flow details
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__data_packets_sent','__data_bytes_sent','__port_based_flows','__hw_generic_flows','__l2_interfaces','__l3_interfaces','__l23_interfaces','__lag_interfaces','__flow_info_list',)

  _yang_name = 'flow'
  _rest_name = 'flow'

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
    self.__flow_info_list = YANGDynClass(base=YANGListType("flow_id",flow_info_list.flow_info_list, yang_name="flow-info-list", rest_name="flow-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='flow-id', extensions=None), is_container='list', yang_name="flow-info-list", rest_name="flow-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    self.__port_based_flows = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-based-flows", rest_name="port-based-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__l3_interfaces = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l3-interfaces", rest_name="l3-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__data_bytes_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="data-bytes-sent", rest_name="data-bytes-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)
    self.__hw_generic_flows = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hw-generic-flows", rest_name="hw-generic-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__l2_interfaces = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l2-interfaces", rest_name="l2-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__l23_interfaces = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l23-interfaces", rest_name="l23-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__lag_interfaces = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lag-interfaces", rest_name="lag-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__data_packets_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="data-packets-sent", rest_name="data-packets-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)

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
      return [u'openflow-state', u'flow']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'flow']

  def _get_data_packets_sent(self):
    """
    Getter method for data_packets_sent, mapped from YANG variable /openflow_state/flow/data_packets_sent (uint64)

    YANG Description: Total Number of data packets sent to controller
    """
    return self.__data_packets_sent
      
  def _set_data_packets_sent(self, v, load=False):
    """
    Setter method for data_packets_sent, mapped from YANG variable /openflow_state/flow/data_packets_sent (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_packets_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_packets_sent() directly.

    YANG Description: Total Number of data packets sent to controller
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="data-packets-sent", rest_name="data-packets-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_packets_sent must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="data-packets-sent", rest_name="data-packets-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)""",
        })

    self.__data_packets_sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_packets_sent(self):
    self.__data_packets_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="data-packets-sent", rest_name="data-packets-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)


  def _get_data_bytes_sent(self):
    """
    Getter method for data_bytes_sent, mapped from YANG variable /openflow_state/flow/data_bytes_sent (uint64)

    YANG Description: Total Number of data bytes sent to controller
    """
    return self.__data_bytes_sent
      
  def _set_data_bytes_sent(self, v, load=False):
    """
    Setter method for data_bytes_sent, mapped from YANG variable /openflow_state/flow/data_bytes_sent (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_bytes_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_bytes_sent() directly.

    YANG Description: Total Number of data bytes sent to controller
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="data-bytes-sent", rest_name="data-bytes-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_bytes_sent must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="data-bytes-sent", rest_name="data-bytes-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)""",
        })

    self.__data_bytes_sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_bytes_sent(self):
    self.__data_bytes_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="data-bytes-sent", rest_name="data-bytes-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)


  def _get_port_based_flows(self):
    """
    Getter method for port_based_flows, mapped from YANG variable /openflow_state/flow/port_based_flows (uint32)

    YANG Description: Total Number of Port based Flows
    """
    return self.__port_based_flows
      
  def _set_port_based_flows(self, v, load=False):
    """
    Setter method for port_based_flows, mapped from YANG variable /openflow_state/flow/port_based_flows (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_based_flows is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_based_flows() directly.

    YANG Description: Total Number of Port based Flows
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-based-flows", rest_name="port-based-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_based_flows must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-based-flows", rest_name="port-based-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__port_based_flows = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_based_flows(self):
    self.__port_based_flows = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-based-flows", rest_name="port-based-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_hw_generic_flows(self):
    """
    Getter method for hw_generic_flows, mapped from YANG variable /openflow_state/flow/hw_generic_flows (uint32)

    YANG Description: Total Number of Generic based Flows
    """
    return self.__hw_generic_flows
      
  def _set_hw_generic_flows(self, v, load=False):
    """
    Setter method for hw_generic_flows, mapped from YANG variable /openflow_state/flow/hw_generic_flows (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hw_generic_flows is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hw_generic_flows() directly.

    YANG Description: Total Number of Generic based Flows
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hw-generic-flows", rest_name="hw-generic-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hw_generic_flows must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hw-generic-flows", rest_name="hw-generic-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__hw_generic_flows = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hw_generic_flows(self):
    self.__hw_generic_flows = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hw-generic-flows", rest_name="hw-generic-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_l2_interfaces(self):
    """
    Getter method for l2_interfaces, mapped from YANG variable /openflow_state/flow/l2_interfaces (uint32)

    YANG Description: Total Number of L2  interfaces
    """
    return self.__l2_interfaces
      
  def _set_l2_interfaces(self, v, load=False):
    """
    Setter method for l2_interfaces, mapped from YANG variable /openflow_state/flow/l2_interfaces (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l2_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l2_interfaces() directly.

    YANG Description: Total Number of L2  interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l2-interfaces", rest_name="l2-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l2_interfaces must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l2-interfaces", rest_name="l2-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__l2_interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l2_interfaces(self):
    self.__l2_interfaces = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l2-interfaces", rest_name="l2-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_l3_interfaces(self):
    """
    Getter method for l3_interfaces, mapped from YANG variable /openflow_state/flow/l3_interfaces (uint32)

    YANG Description: Total Number of L3 interfaces
    """
    return self.__l3_interfaces
      
  def _set_l3_interfaces(self, v, load=False):
    """
    Setter method for l3_interfaces, mapped from YANG variable /openflow_state/flow/l3_interfaces (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l3_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l3_interfaces() directly.

    YANG Description: Total Number of L3 interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l3-interfaces", rest_name="l3-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l3_interfaces must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l3-interfaces", rest_name="l3-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__l3_interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l3_interfaces(self):
    self.__l3_interfaces = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l3-interfaces", rest_name="l3-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_l23_interfaces(self):
    """
    Getter method for l23_interfaces, mapped from YANG variable /openflow_state/flow/l23_interfaces (uint32)

    YANG Description: Total Number of L23 interfaces
    """
    return self.__l23_interfaces
      
  def _set_l23_interfaces(self, v, load=False):
    """
    Setter method for l23_interfaces, mapped from YANG variable /openflow_state/flow/l23_interfaces (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l23_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l23_interfaces() directly.

    YANG Description: Total Number of L23 interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l23-interfaces", rest_name="l23-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l23_interfaces must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l23-interfaces", rest_name="l23-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__l23_interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l23_interfaces(self):
    self.__l23_interfaces = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l23-interfaces", rest_name="l23-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_lag_interfaces(self):
    """
    Getter method for lag_interfaces, mapped from YANG variable /openflow_state/flow/lag_interfaces (uint32)

    YANG Description: Total Number of LAG interfaces
    """
    return self.__lag_interfaces
      
  def _set_lag_interfaces(self, v, load=False):
    """
    Setter method for lag_interfaces, mapped from YANG variable /openflow_state/flow/lag_interfaces (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lag_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lag_interfaces() directly.

    YANG Description: Total Number of LAG interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lag-interfaces", rest_name="lag-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lag_interfaces must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lag-interfaces", rest_name="lag-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__lag_interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lag_interfaces(self):
    self.__lag_interfaces = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lag-interfaces", rest_name="lag-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_flow_info_list(self):
    """
    Getter method for flow_info_list, mapped from YANG variable /openflow_state/flow/flow_info_list (list)
    """
    return self.__flow_info_list
      
  def _set_flow_info_list(self, v, load=False):
    """
    Setter method for flow_info_list, mapped from YANG variable /openflow_state/flow/flow_info_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flow_info_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flow_info_list() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("flow_id",flow_info_list.flow_info_list, yang_name="flow-info-list", rest_name="flow-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='flow-id', extensions=None), is_container='list', yang_name="flow-info-list", rest_name="flow-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flow_info_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("flow_id",flow_info_list.flow_info_list, yang_name="flow-info-list", rest_name="flow-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='flow-id', extensions=None), is_container='list', yang_name="flow-info-list", rest_name="flow-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)""",
        })

    self.__flow_info_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flow_info_list(self):
    self.__flow_info_list = YANGDynClass(base=YANGListType("flow_id",flow_info_list.flow_info_list, yang_name="flow-info-list", rest_name="flow-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='flow-id', extensions=None), is_container='list', yang_name="flow-info-list", rest_name="flow-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)

  data_packets_sent = __builtin__.property(_get_data_packets_sent)
  data_bytes_sent = __builtin__.property(_get_data_bytes_sent)
  port_based_flows = __builtin__.property(_get_port_based_flows)
  hw_generic_flows = __builtin__.property(_get_hw_generic_flows)
  l2_interfaces = __builtin__.property(_get_l2_interfaces)
  l3_interfaces = __builtin__.property(_get_l3_interfaces)
  l23_interfaces = __builtin__.property(_get_l23_interfaces)
  lag_interfaces = __builtin__.property(_get_lag_interfaces)
  flow_info_list = __builtin__.property(_get_flow_info_list)


  _pyangbind_elements = {'data_packets_sent': data_packets_sent, 'data_bytes_sent': data_bytes_sent, 'port_based_flows': port_based_flows, 'hw_generic_flows': hw_generic_flows, 'l2_interfaces': l2_interfaces, 'l3_interfaces': l3_interfaces, 'l23_interfaces': l23_interfaces, 'lag_interfaces': lag_interfaces, 'flow_info_list': flow_info_list, }


