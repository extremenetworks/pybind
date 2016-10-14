
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import exp_traffic_class
import traffic_class_exp
import dscp_exp
import exp_dscp
import inexp_outexp
class map_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mpls - based on the path /qos-mpls/map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__exp_traffic_class','__traffic_class_exp','__dscp_exp','__exp_dscp','__inexp_outexp',)

  _yang_name = 'map'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
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
    self.__exp_dscp = YANGDynClass(base=YANGListType("exp_dscp_map_name",exp_dscp.exp_dscp, yang_name="exp-dscp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp-dscp-map-name', extensions={u'tailf-common': {u'info': u'Configure Exp dscp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd4Callpoint', u'cli-mode-name': u'exp-dscp-$(exp-dscp-map-name)'}}), is_container='list', yang_name="exp-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Exp dscp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd4Callpoint', u'cli-mode-name': u'exp-dscp-$(exp-dscp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)
    self.__traffic_class_exp = YANGDynClass(base=YANGListType("traffic_class_exp_map_name",traffic_class_exp.traffic_class_exp, yang_name="traffic-class-exp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='traffic-class-exp-map-name', extensions={u'tailf-common': {u'info': u'Configure Traffic class exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd2Callpoint', u'cli-mode-name': u'traffic-class-exp-$(traffic-class-exp-map-name)'}}), is_container='list', yang_name="traffic-class-exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic class exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd2Callpoint', u'cli-mode-name': u'traffic-class-exp-$(traffic-class-exp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)
    self.__inexp_outexp = YANGDynClass(base=YANGListType("inexp_outexp_map_name",inexp_outexp.inexp_outexp, yang_name="inexp-outexp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='inexp-outexp-map-name', extensions={u'tailf-common': {u'info': u'Configure Inexp outexp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd5Callpoint', u'hidden': u'full', u'cli-mode-name': u'inexp-outexp-$(inexp-outexp-map-name)'}}), is_container='list', yang_name="inexp-outexp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Inexp outexp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd5Callpoint', u'hidden': u'full', u'cli-mode-name': u'inexp-outexp-$(inexp-outexp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)
    self.__dscp_exp = YANGDynClass(base=YANGListType("dscp_exp_map_name",dscp_exp.dscp_exp, yang_name="dscp-exp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-exp-map-name', extensions={u'tailf-common': {u'info': u'Configure Dscp exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd3Callpoint', u'cli-mode-name': u'dscp-exp-$(dscp-exp-map-name)'}}), is_container='list', yang_name="dscp-exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Dscp exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd3Callpoint', u'cli-mode-name': u'dscp-exp-$(dscp-exp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)
    self.__exp_traffic_class = YANGDynClass(base=YANGListType("exp_traffic_class_map_name",exp_traffic_class.exp_traffic_class, yang_name="exp-traffic-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp-traffic-class-map-name', extensions={u'tailf-common': {u'info': u'Configure Exp traffic class', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCallpoint', u'cli-mode-name': u'exp-traffic-class-$(exp-traffic-class-map-name)'}}), is_container='list', yang_name="exp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Exp traffic class', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCallpoint', u'cli-mode-name': u'exp-traffic-class-$(exp-traffic-class-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)

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
      return [u'qos-mpls', u'map']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'qos-mpls', u'map']

  def _get_exp_traffic_class(self):
    """
    Getter method for exp_traffic_class, mapped from YANG variable /qos_mpls/map/exp_traffic_class (list)
    """
    return self.__exp_traffic_class
      
  def _set_exp_traffic_class(self, v, load=False):
    """
    Setter method for exp_traffic_class, mapped from YANG variable /qos_mpls/map/exp_traffic_class (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exp_traffic_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exp_traffic_class() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("exp_traffic_class_map_name",exp_traffic_class.exp_traffic_class, yang_name="exp-traffic-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp-traffic-class-map-name', extensions={u'tailf-common': {u'info': u'Configure Exp traffic class', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCallpoint', u'cli-mode-name': u'exp-traffic-class-$(exp-traffic-class-map-name)'}}), is_container='list', yang_name="exp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Exp traffic class', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCallpoint', u'cli-mode-name': u'exp-traffic-class-$(exp-traffic-class-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exp_traffic_class must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("exp_traffic_class_map_name",exp_traffic_class.exp_traffic_class, yang_name="exp-traffic-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp-traffic-class-map-name', extensions={u'tailf-common': {u'info': u'Configure Exp traffic class', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCallpoint', u'cli-mode-name': u'exp-traffic-class-$(exp-traffic-class-map-name)'}}), is_container='list', yang_name="exp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Exp traffic class', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCallpoint', u'cli-mode-name': u'exp-traffic-class-$(exp-traffic-class-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)""",
        })

    self.__exp_traffic_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exp_traffic_class(self):
    self.__exp_traffic_class = YANGDynClass(base=YANGListType("exp_traffic_class_map_name",exp_traffic_class.exp_traffic_class, yang_name="exp-traffic-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp-traffic-class-map-name', extensions={u'tailf-common': {u'info': u'Configure Exp traffic class', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCallpoint', u'cli-mode-name': u'exp-traffic-class-$(exp-traffic-class-map-name)'}}), is_container='list', yang_name="exp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Exp traffic class', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCallpoint', u'cli-mode-name': u'exp-traffic-class-$(exp-traffic-class-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)


  def _get_traffic_class_exp(self):
    """
    Getter method for traffic_class_exp, mapped from YANG variable /qos_mpls/map/traffic_class_exp (list)
    """
    return self.__traffic_class_exp
      
  def _set_traffic_class_exp(self, v, load=False):
    """
    Setter method for traffic_class_exp, mapped from YANG variable /qos_mpls/map/traffic_class_exp (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_traffic_class_exp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_traffic_class_exp() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("traffic_class_exp_map_name",traffic_class_exp.traffic_class_exp, yang_name="traffic-class-exp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='traffic-class-exp-map-name', extensions={u'tailf-common': {u'info': u'Configure Traffic class exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd2Callpoint', u'cli-mode-name': u'traffic-class-exp-$(traffic-class-exp-map-name)'}}), is_container='list', yang_name="traffic-class-exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic class exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd2Callpoint', u'cli-mode-name': u'traffic-class-exp-$(traffic-class-exp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """traffic_class_exp must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("traffic_class_exp_map_name",traffic_class_exp.traffic_class_exp, yang_name="traffic-class-exp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='traffic-class-exp-map-name', extensions={u'tailf-common': {u'info': u'Configure Traffic class exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd2Callpoint', u'cli-mode-name': u'traffic-class-exp-$(traffic-class-exp-map-name)'}}), is_container='list', yang_name="traffic-class-exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic class exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd2Callpoint', u'cli-mode-name': u'traffic-class-exp-$(traffic-class-exp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)""",
        })

    self.__traffic_class_exp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_traffic_class_exp(self):
    self.__traffic_class_exp = YANGDynClass(base=YANGListType("traffic_class_exp_map_name",traffic_class_exp.traffic_class_exp, yang_name="traffic-class-exp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='traffic-class-exp-map-name', extensions={u'tailf-common': {u'info': u'Configure Traffic class exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd2Callpoint', u'cli-mode-name': u'traffic-class-exp-$(traffic-class-exp-map-name)'}}), is_container='list', yang_name="traffic-class-exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic class exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd2Callpoint', u'cli-mode-name': u'traffic-class-exp-$(traffic-class-exp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)


  def _get_dscp_exp(self):
    """
    Getter method for dscp_exp, mapped from YANG variable /qos_mpls/map/dscp_exp (list)
    """
    return self.__dscp_exp
      
  def _set_dscp_exp(self, v, load=False):
    """
    Setter method for dscp_exp, mapped from YANG variable /qos_mpls/map/dscp_exp (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_exp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_exp() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("dscp_exp_map_name",dscp_exp.dscp_exp, yang_name="dscp-exp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-exp-map-name', extensions={u'tailf-common': {u'info': u'Configure Dscp exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd3Callpoint', u'cli-mode-name': u'dscp-exp-$(dscp-exp-map-name)'}}), is_container='list', yang_name="dscp-exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Dscp exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd3Callpoint', u'cli-mode-name': u'dscp-exp-$(dscp-exp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_exp must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("dscp_exp_map_name",dscp_exp.dscp_exp, yang_name="dscp-exp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-exp-map-name', extensions={u'tailf-common': {u'info': u'Configure Dscp exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd3Callpoint', u'cli-mode-name': u'dscp-exp-$(dscp-exp-map-name)'}}), is_container='list', yang_name="dscp-exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Dscp exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd3Callpoint', u'cli-mode-name': u'dscp-exp-$(dscp-exp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)""",
        })

    self.__dscp_exp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_exp(self):
    self.__dscp_exp = YANGDynClass(base=YANGListType("dscp_exp_map_name",dscp_exp.dscp_exp, yang_name="dscp-exp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-exp-map-name', extensions={u'tailf-common': {u'info': u'Configure Dscp exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd3Callpoint', u'cli-mode-name': u'dscp-exp-$(dscp-exp-map-name)'}}), is_container='list', yang_name="dscp-exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Dscp exp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd3Callpoint', u'cli-mode-name': u'dscp-exp-$(dscp-exp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)


  def _get_exp_dscp(self):
    """
    Getter method for exp_dscp, mapped from YANG variable /qos_mpls/map/exp_dscp (list)
    """
    return self.__exp_dscp
      
  def _set_exp_dscp(self, v, load=False):
    """
    Setter method for exp_dscp, mapped from YANG variable /qos_mpls/map/exp_dscp (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exp_dscp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exp_dscp() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("exp_dscp_map_name",exp_dscp.exp_dscp, yang_name="exp-dscp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp-dscp-map-name', extensions={u'tailf-common': {u'info': u'Configure Exp dscp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd4Callpoint', u'cli-mode-name': u'exp-dscp-$(exp-dscp-map-name)'}}), is_container='list', yang_name="exp-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Exp dscp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd4Callpoint', u'cli-mode-name': u'exp-dscp-$(exp-dscp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exp_dscp must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("exp_dscp_map_name",exp_dscp.exp_dscp, yang_name="exp-dscp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp-dscp-map-name', extensions={u'tailf-common': {u'info': u'Configure Exp dscp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd4Callpoint', u'cli-mode-name': u'exp-dscp-$(exp-dscp-map-name)'}}), is_container='list', yang_name="exp-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Exp dscp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd4Callpoint', u'cli-mode-name': u'exp-dscp-$(exp-dscp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)""",
        })

    self.__exp_dscp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exp_dscp(self):
    self.__exp_dscp = YANGDynClass(base=YANGListType("exp_dscp_map_name",exp_dscp.exp_dscp, yang_name="exp-dscp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp-dscp-map-name', extensions={u'tailf-common': {u'info': u'Configure Exp dscp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd4Callpoint', u'cli-mode-name': u'exp-dscp-$(exp-dscp-map-name)'}}), is_container='list', yang_name="exp-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Exp dscp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd4Callpoint', u'cli-mode-name': u'exp-dscp-$(exp-dscp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)


  def _get_inexp_outexp(self):
    """
    Getter method for inexp_outexp, mapped from YANG variable /qos_mpls/map/inexp_outexp (list)
    """
    return self.__inexp_outexp
      
  def _set_inexp_outexp(self, v, load=False):
    """
    Setter method for inexp_outexp, mapped from YANG variable /qos_mpls/map/inexp_outexp (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_inexp_outexp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_inexp_outexp() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("inexp_outexp_map_name",inexp_outexp.inexp_outexp, yang_name="inexp-outexp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='inexp-outexp-map-name', extensions={u'tailf-common': {u'info': u'Configure Inexp outexp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd5Callpoint', u'hidden': u'full', u'cli-mode-name': u'inexp-outexp-$(inexp-outexp-map-name)'}}), is_container='list', yang_name="inexp-outexp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Inexp outexp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd5Callpoint', u'hidden': u'full', u'cli-mode-name': u'inexp-outexp-$(inexp-outexp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """inexp_outexp must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("inexp_outexp_map_name",inexp_outexp.inexp_outexp, yang_name="inexp-outexp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='inexp-outexp-map-name', extensions={u'tailf-common': {u'info': u'Configure Inexp outexp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd5Callpoint', u'hidden': u'full', u'cli-mode-name': u'inexp-outexp-$(inexp-outexp-map-name)'}}), is_container='list', yang_name="inexp-outexp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Inexp outexp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd5Callpoint', u'hidden': u'full', u'cli-mode-name': u'inexp-outexp-$(inexp-outexp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)""",
        })

    self.__inexp_outexp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_inexp_outexp(self):
    self.__inexp_outexp = YANGDynClass(base=YANGListType("inexp_outexp_map_name",inexp_outexp.inexp_outexp, yang_name="inexp-outexp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='inexp-outexp-map-name', extensions={u'tailf-common': {u'info': u'Configure Inexp outexp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd5Callpoint', u'hidden': u'full', u'cli-mode-name': u'inexp-outexp-$(inexp-outexp-map-name)'}}), is_container='list', yang_name="inexp-outexp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Inexp outexp', u'cli-sequence-commands': None, u'callpoint': u'QosMplsCmd5Callpoint', u'hidden': u'full', u'cli-mode-name': u'inexp-outexp-$(inexp-outexp-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='list', is_config=True)

  exp_traffic_class = __builtin__.property(_get_exp_traffic_class, _set_exp_traffic_class)
  traffic_class_exp = __builtin__.property(_get_traffic_class_exp, _set_traffic_class_exp)
  dscp_exp = __builtin__.property(_get_dscp_exp, _set_dscp_exp)
  exp_dscp = __builtin__.property(_get_exp_dscp, _set_exp_dscp)
  inexp_outexp = __builtin__.property(_get_inexp_outexp, _set_inexp_outexp)


  _pyangbind_elements = {'exp_traffic_class': exp_traffic_class, 'traffic_class_exp': traffic_class_exp, 'dscp_exp': dscp_exp, 'exp_dscp': exp_dscp, 'inexp_outexp': inexp_outexp, }


