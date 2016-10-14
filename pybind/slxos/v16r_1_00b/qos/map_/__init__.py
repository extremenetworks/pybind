
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import cos_mutation
import cos_traffic_class
import traffic_class_cos
import dscp_mutation
import dscp_traffic_class
import dscp_cos
class map_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mls - based on the path /qos/map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__cos_mutation','__cos_traffic_class','__traffic_class_cos','__dscp_mutation','__dscp_traffic_class','__dscp_cos',)

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
    self.__cos_mutation = YANGDynClass(base=YANGListType("name",cos_mutation.cos_mutation, yang_name="cos-mutation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure CoS-Mutation map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_mutation', u'cli-mode-name': u'cos-mutation-$(name)'}}), is_container='list', yang_name="cos-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-Mutation map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_mutation', u'cli-mode-name': u'cos-mutation-$(name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    self.__traffic_class_cos = YANGDynClass(base=YANGListType("traffic_class_cos_map_name",traffic_class_cos.traffic_class_cos, yang_name="traffic-class-cos", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='traffic-class-cos-map-name', extensions={u'tailf-common': {u'info': u'Configure Traffic-Class-to-CoS map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'traffic_class_cos', u'cli-mode-name': u'traffic-class-cos-$(traffic-class-cos-map-name)'}}), is_container='list', yang_name="traffic-class-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic-Class-to-CoS map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'traffic_class_cos', u'cli-mode-name': u'traffic-class-cos-$(traffic-class-cos-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    self.__dscp_mutation = YANGDynClass(base=YANGListType("dscp_mutation_map_name",dscp_mutation.dscp_mutation, yang_name="dscp-mutation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-mutation-map-name', extensions={u'tailf-common': {u'info': u'Configure DSCP-Mutation map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_mutation', u'cli-mode-name': u'dscp-mutation-$(dscp-mutation-map-name)'}}), is_container='list', yang_name="dscp-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-Mutation map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_mutation', u'cli-mode-name': u'dscp-mutation-$(dscp-mutation-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    self.__dscp_traffic_class = YANGDynClass(base=YANGListType("dscp_traffic_class_map_name",dscp_traffic_class.dscp_traffic_class, yang_name="dscp-traffic-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-traffic-class-map-name', extensions={u'tailf-common': {u'info': u'Configure DSCP-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_traffic_class', u'cli-mode-name': u'dscp-traffic-class-$(dscp-traffic-class-map-name)'}}), is_container='list', yang_name="dscp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_traffic_class', u'cli-mode-name': u'dscp-traffic-class-$(dscp-traffic-class-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    self.__cos_traffic_class = YANGDynClass(base=YANGListType("name",cos_traffic_class.cos_traffic_class, yang_name="cos-traffic-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure CoS-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_traffic_class', u'cli-mode-name': u'cos-traffic-class-$(name)'}}), is_container='list', yang_name="cos-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_traffic_class', u'cli-mode-name': u'cos-traffic-class-$(name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    self.__dscp_cos = YANGDynClass(base=YANGListType("dscp_cos_map_name",dscp_cos.dscp_cos, yang_name="dscp-cos", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-cos-map-name', extensions={u'tailf-common': {u'info': u'Configure DSCP-to-CoS map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_cos', u'cli-mode-name': u'dscp-cos-$(dscp-cos-map-name)'}}), is_container='list', yang_name="dscp-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-CoS map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_cos', u'cli-mode-name': u'dscp-cos-$(dscp-cos-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)

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
      return [u'qos', u'map']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'qos', u'map']

  def _get_cos_mutation(self):
    """
    Getter method for cos_mutation, mapped from YANG variable /qos/map/cos_mutation (list)
    """
    return self.__cos_mutation
      
  def _set_cos_mutation(self, v, load=False):
    """
    Setter method for cos_mutation, mapped from YANG variable /qos/map/cos_mutation (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos_mutation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos_mutation() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("name",cos_mutation.cos_mutation, yang_name="cos-mutation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure CoS-Mutation map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_mutation', u'cli-mode-name': u'cos-mutation-$(name)'}}), is_container='list', yang_name="cos-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-Mutation map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_mutation', u'cli-mode-name': u'cos-mutation-$(name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos_mutation must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",cos_mutation.cos_mutation, yang_name="cos-mutation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure CoS-Mutation map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_mutation', u'cli-mode-name': u'cos-mutation-$(name)'}}), is_container='list', yang_name="cos-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-Mutation map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_mutation', u'cli-mode-name': u'cos-mutation-$(name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)""",
        })

    self.__cos_mutation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos_mutation(self):
    self.__cos_mutation = YANGDynClass(base=YANGListType("name",cos_mutation.cos_mutation, yang_name="cos-mutation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure CoS-Mutation map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_mutation', u'cli-mode-name': u'cos-mutation-$(name)'}}), is_container='list', yang_name="cos-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-Mutation map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_mutation', u'cli-mode-name': u'cos-mutation-$(name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)


  def _get_cos_traffic_class(self):
    """
    Getter method for cos_traffic_class, mapped from YANG variable /qos/map/cos_traffic_class (list)
    """
    return self.__cos_traffic_class
      
  def _set_cos_traffic_class(self, v, load=False):
    """
    Setter method for cos_traffic_class, mapped from YANG variable /qos/map/cos_traffic_class (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos_traffic_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos_traffic_class() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("name",cos_traffic_class.cos_traffic_class, yang_name="cos-traffic-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure CoS-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_traffic_class', u'cli-mode-name': u'cos-traffic-class-$(name)'}}), is_container='list', yang_name="cos-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_traffic_class', u'cli-mode-name': u'cos-traffic-class-$(name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos_traffic_class must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",cos_traffic_class.cos_traffic_class, yang_name="cos-traffic-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure CoS-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_traffic_class', u'cli-mode-name': u'cos-traffic-class-$(name)'}}), is_container='list', yang_name="cos-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_traffic_class', u'cli-mode-name': u'cos-traffic-class-$(name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)""",
        })

    self.__cos_traffic_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos_traffic_class(self):
    self.__cos_traffic_class = YANGDynClass(base=YANGListType("name",cos_traffic_class.cos_traffic_class, yang_name="cos-traffic-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure CoS-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_traffic_class', u'cli-mode-name': u'cos-traffic-class-$(name)'}}), is_container='list', yang_name="cos-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'cos_traffic_class', u'cli-mode-name': u'cos-traffic-class-$(name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)


  def _get_traffic_class_cos(self):
    """
    Getter method for traffic_class_cos, mapped from YANG variable /qos/map/traffic_class_cos (list)
    """
    return self.__traffic_class_cos
      
  def _set_traffic_class_cos(self, v, load=False):
    """
    Setter method for traffic_class_cos, mapped from YANG variable /qos/map/traffic_class_cos (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_traffic_class_cos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_traffic_class_cos() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("traffic_class_cos_map_name",traffic_class_cos.traffic_class_cos, yang_name="traffic-class-cos", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='traffic-class-cos-map-name', extensions={u'tailf-common': {u'info': u'Configure Traffic-Class-to-CoS map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'traffic_class_cos', u'cli-mode-name': u'traffic-class-cos-$(traffic-class-cos-map-name)'}}), is_container='list', yang_name="traffic-class-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic-Class-to-CoS map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'traffic_class_cos', u'cli-mode-name': u'traffic-class-cos-$(traffic-class-cos-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """traffic_class_cos must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("traffic_class_cos_map_name",traffic_class_cos.traffic_class_cos, yang_name="traffic-class-cos", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='traffic-class-cos-map-name', extensions={u'tailf-common': {u'info': u'Configure Traffic-Class-to-CoS map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'traffic_class_cos', u'cli-mode-name': u'traffic-class-cos-$(traffic-class-cos-map-name)'}}), is_container='list', yang_name="traffic-class-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic-Class-to-CoS map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'traffic_class_cos', u'cli-mode-name': u'traffic-class-cos-$(traffic-class-cos-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)""",
        })

    self.__traffic_class_cos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_traffic_class_cos(self):
    self.__traffic_class_cos = YANGDynClass(base=YANGListType("traffic_class_cos_map_name",traffic_class_cos.traffic_class_cos, yang_name="traffic-class-cos", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='traffic-class-cos-map-name', extensions={u'tailf-common': {u'info': u'Configure Traffic-Class-to-CoS map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'traffic_class_cos', u'cli-mode-name': u'traffic-class-cos-$(traffic-class-cos-map-name)'}}), is_container='list', yang_name="traffic-class-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic-Class-to-CoS map', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'traffic_class_cos', u'cli-mode-name': u'traffic-class-cos-$(traffic-class-cos-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)


  def _get_dscp_mutation(self):
    """
    Getter method for dscp_mutation, mapped from YANG variable /qos/map/dscp_mutation (list)
    """
    return self.__dscp_mutation
      
  def _set_dscp_mutation(self, v, load=False):
    """
    Setter method for dscp_mutation, mapped from YANG variable /qos/map/dscp_mutation (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_mutation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_mutation() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("dscp_mutation_map_name",dscp_mutation.dscp_mutation, yang_name="dscp-mutation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-mutation-map-name', extensions={u'tailf-common': {u'info': u'Configure DSCP-Mutation map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_mutation', u'cli-mode-name': u'dscp-mutation-$(dscp-mutation-map-name)'}}), is_container='list', yang_name="dscp-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-Mutation map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_mutation', u'cli-mode-name': u'dscp-mutation-$(dscp-mutation-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_mutation must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("dscp_mutation_map_name",dscp_mutation.dscp_mutation, yang_name="dscp-mutation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-mutation-map-name', extensions={u'tailf-common': {u'info': u'Configure DSCP-Mutation map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_mutation', u'cli-mode-name': u'dscp-mutation-$(dscp-mutation-map-name)'}}), is_container='list', yang_name="dscp-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-Mutation map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_mutation', u'cli-mode-name': u'dscp-mutation-$(dscp-mutation-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)""",
        })

    self.__dscp_mutation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_mutation(self):
    self.__dscp_mutation = YANGDynClass(base=YANGListType("dscp_mutation_map_name",dscp_mutation.dscp_mutation, yang_name="dscp-mutation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-mutation-map-name', extensions={u'tailf-common': {u'info': u'Configure DSCP-Mutation map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_mutation', u'cli-mode-name': u'dscp-mutation-$(dscp-mutation-map-name)'}}), is_container='list', yang_name="dscp-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-Mutation map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_mutation', u'cli-mode-name': u'dscp-mutation-$(dscp-mutation-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)


  def _get_dscp_traffic_class(self):
    """
    Getter method for dscp_traffic_class, mapped from YANG variable /qos/map/dscp_traffic_class (list)
    """
    return self.__dscp_traffic_class
      
  def _set_dscp_traffic_class(self, v, load=False):
    """
    Setter method for dscp_traffic_class, mapped from YANG variable /qos/map/dscp_traffic_class (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_traffic_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_traffic_class() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("dscp_traffic_class_map_name",dscp_traffic_class.dscp_traffic_class, yang_name="dscp-traffic-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-traffic-class-map-name', extensions={u'tailf-common': {u'info': u'Configure DSCP-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_traffic_class', u'cli-mode-name': u'dscp-traffic-class-$(dscp-traffic-class-map-name)'}}), is_container='list', yang_name="dscp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_traffic_class', u'cli-mode-name': u'dscp-traffic-class-$(dscp-traffic-class-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_traffic_class must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("dscp_traffic_class_map_name",dscp_traffic_class.dscp_traffic_class, yang_name="dscp-traffic-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-traffic-class-map-name', extensions={u'tailf-common': {u'info': u'Configure DSCP-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_traffic_class', u'cli-mode-name': u'dscp-traffic-class-$(dscp-traffic-class-map-name)'}}), is_container='list', yang_name="dscp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_traffic_class', u'cli-mode-name': u'dscp-traffic-class-$(dscp-traffic-class-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)""",
        })

    self.__dscp_traffic_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_traffic_class(self):
    self.__dscp_traffic_class = YANGDynClass(base=YANGListType("dscp_traffic_class_map_name",dscp_traffic_class.dscp_traffic_class, yang_name="dscp-traffic-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-traffic-class-map-name', extensions={u'tailf-common': {u'info': u'Configure DSCP-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_traffic_class', u'cli-mode-name': u'dscp-traffic-class-$(dscp-traffic-class-map-name)'}}), is_container='list', yang_name="dscp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-Traffic-Class map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_traffic_class', u'cli-mode-name': u'dscp-traffic-class-$(dscp-traffic-class-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)


  def _get_dscp_cos(self):
    """
    Getter method for dscp_cos, mapped from YANG variable /qos/map/dscp_cos (list)
    """
    return self.__dscp_cos
      
  def _set_dscp_cos(self, v, load=False):
    """
    Setter method for dscp_cos, mapped from YANG variable /qos/map/dscp_cos (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_cos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_cos() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("dscp_cos_map_name",dscp_cos.dscp_cos, yang_name="dscp-cos", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-cos-map-name', extensions={u'tailf-common': {u'info': u'Configure DSCP-to-CoS map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_cos', u'cli-mode-name': u'dscp-cos-$(dscp-cos-map-name)'}}), is_container='list', yang_name="dscp-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-CoS map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_cos', u'cli-mode-name': u'dscp-cos-$(dscp-cos-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_cos must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("dscp_cos_map_name",dscp_cos.dscp_cos, yang_name="dscp-cos", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-cos-map-name', extensions={u'tailf-common': {u'info': u'Configure DSCP-to-CoS map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_cos', u'cli-mode-name': u'dscp-cos-$(dscp-cos-map-name)'}}), is_container='list', yang_name="dscp-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-CoS map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_cos', u'cli-mode-name': u'dscp-cos-$(dscp-cos-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)""",
        })

    self.__dscp_cos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_cos(self):
    self.__dscp_cos = YANGDynClass(base=YANGListType("dscp_cos_map_name",dscp_cos.dscp_cos, yang_name="dscp-cos", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-cos-map-name', extensions={u'tailf-common': {u'info': u'Configure DSCP-to-CoS map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_cos', u'cli-mode-name': u'dscp-cos-$(dscp-cos-map-name)'}}), is_container='list', yang_name="dscp-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-CoS map', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'dscp_cos', u'cli-mode-name': u'dscp-cos-$(dscp-cos-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)

  cos_mutation = __builtin__.property(_get_cos_mutation, _set_cos_mutation)
  cos_traffic_class = __builtin__.property(_get_cos_traffic_class, _set_cos_traffic_class)
  traffic_class_cos = __builtin__.property(_get_traffic_class_cos, _set_traffic_class_cos)
  dscp_mutation = __builtin__.property(_get_dscp_mutation, _set_dscp_mutation)
  dscp_traffic_class = __builtin__.property(_get_dscp_traffic_class, _set_dscp_traffic_class)
  dscp_cos = __builtin__.property(_get_dscp_cos, _set_dscp_cos)


  _pyangbind_elements = {'cos_mutation': cos_mutation, 'cos_traffic_class': cos_traffic_class, 'traffic_class_cos': traffic_class_cos, 'dscp_mutation': dscp_mutation, 'dscp_traffic_class': dscp_traffic_class, 'dscp_cos': dscp_cos, }


