
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import openflow_enable
class openflow_interface_cfg(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/openflow-interface-cfg. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: OpenFlow configuration.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__logical_instance_id','__openflow_enable',)

  _yang_name = 'openflow-interface-cfg'
  _rest_name = 'openflow'

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
    self.__logical_instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="logical-instance-id", rest_name="logical-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'logical-instance'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='instance-id-type', is_config=True)
    self.__openflow_enable = YANGDynClass(base=openflow_enable.openflow_enable, is_container='container', presence=False, yang_name="openflow-enable", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'openflow-interface-cfg']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'openflow']

  def _get_logical_instance_id(self):
    """
    Getter method for logical_instance_id, mapped from YANG variable /interface/gigabitethernet/openflow_interface_cfg/logical_instance_id (instance-id-type)

    YANG Description: OpenFlow logical instance configuration. There can be multiple
logical instances under a physical switch.
    """
    return self.__logical_instance_id
      
  def _set_logical_instance_id(self, v, load=False):
    """
    Setter method for logical_instance_id, mapped from YANG variable /interface/gigabitethernet/openflow_interface_cfg/logical_instance_id (instance-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logical_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logical_instance_id() directly.

    YANG Description: OpenFlow logical instance configuration. There can be multiple
logical instances under a physical switch.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="logical-instance-id", rest_name="logical-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'logical-instance'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='instance-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logical_instance_id must be of a type compatible with instance-id-type""",
          'defined-type': "brocade-openflow:instance-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="logical-instance-id", rest_name="logical-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'logical-instance'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='instance-id-type', is_config=True)""",
        })

    self.__logical_instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logical_instance_id(self):
    self.__logical_instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="logical-instance-id", rest_name="logical-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'logical-instance'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='instance-id-type', is_config=True)


  def _get_openflow_enable(self):
    """
    Getter method for openflow_enable, mapped from YANG variable /interface/gigabitethernet/openflow_interface_cfg/openflow_enable (container)
    """
    return self.__openflow_enable
      
  def _set_openflow_enable(self, v, load=False):
    """
    Setter method for openflow_enable, mapped from YANG variable /interface/gigabitethernet/openflow_interface_cfg/openflow_enable (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_openflow_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_openflow_enable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=openflow_enable.openflow_enable, is_container='container', presence=False, yang_name="openflow-enable", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """openflow_enable must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=openflow_enable.openflow_enable, is_container='container', presence=False, yang_name="openflow-enable", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)""",
        })

    self.__openflow_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_openflow_enable(self):
    self.__openflow_enable = YANGDynClass(base=openflow_enable.openflow_enable, is_container='container', presence=False, yang_name="openflow-enable", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)

  logical_instance_id = __builtin__.property(_get_logical_instance_id, _set_logical_instance_id)
  openflow_enable = __builtin__.property(_get_openflow_enable, _set_openflow_enable)


  _pyangbind_elements = {'logical_instance_id': logical_instance_id, 'openflow_enable': openflow_enable, }


