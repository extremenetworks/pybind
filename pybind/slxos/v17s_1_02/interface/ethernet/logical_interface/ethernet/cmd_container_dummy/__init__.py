
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import service_instance_common_commands_dummy
import service_instance_vlan_cmds_dummy_container
class cmd_container_dummy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/logical-interface/ethernet/cmd-container-dummy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__service_instance_common_commands_dummy','__service_instance_vlan_cmds_dummy_container',)

  _yang_name = 'cmd-container-dummy'
  _rest_name = 'cmd-container-dummy'

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
    self.__service_instance_vlan_cmds_dummy_container = YANGDynClass(base=service_instance_vlan_cmds_dummy_container.service_instance_vlan_cmds_dummy_container, is_container='container', presence=False, yang_name="service-instance-vlan-cmds-dummy-container", rest_name="service-instance-vlan-cmds-dummy-container", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)
    self.__service_instance_common_commands_dummy = YANGDynClass(base=service_instance_common_commands_dummy.service_instance_common_commands_dummy, is_container='container', presence=False, yang_name="service-instance-common-commands-dummy", rest_name="service-instance-common-commands-dummy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)

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
      return [u'interface', u'ethernet', u'logical-interface', u'ethernet', u'cmd-container-dummy']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'ethernet', u'logical-interface', u'ethernet', u'cmd-container-dummy']

  def _get_service_instance_common_commands_dummy(self):
    """
    Getter method for service_instance_common_commands_dummy, mapped from YANG variable /interface/ethernet/logical_interface/ethernet/cmd_container_dummy/service_instance_common_commands_dummy (container)
    """
    return self.__service_instance_common_commands_dummy
      
  def _set_service_instance_common_commands_dummy(self, v, load=False):
    """
    Setter method for service_instance_common_commands_dummy, mapped from YANG variable /interface/ethernet/logical_interface/ethernet/cmd_container_dummy/service_instance_common_commands_dummy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_service_instance_common_commands_dummy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_service_instance_common_commands_dummy() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=service_instance_common_commands_dummy.service_instance_common_commands_dummy, is_container='container', presence=False, yang_name="service-instance-common-commands-dummy", rest_name="service-instance-common-commands-dummy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """service_instance_common_commands_dummy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=service_instance_common_commands_dummy.service_instance_common_commands_dummy, is_container='container', presence=False, yang_name="service-instance-common-commands-dummy", rest_name="service-instance-common-commands-dummy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)""",
        })

    self.__service_instance_common_commands_dummy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_service_instance_common_commands_dummy(self):
    self.__service_instance_common_commands_dummy = YANGDynClass(base=service_instance_common_commands_dummy.service_instance_common_commands_dummy, is_container='container', presence=False, yang_name="service-instance-common-commands-dummy", rest_name="service-instance-common-commands-dummy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)


  def _get_service_instance_vlan_cmds_dummy_container(self):
    """
    Getter method for service_instance_vlan_cmds_dummy_container, mapped from YANG variable /interface/ethernet/logical_interface/ethernet/cmd_container_dummy/service_instance_vlan_cmds_dummy_container (container)
    """
    return self.__service_instance_vlan_cmds_dummy_container
      
  def _set_service_instance_vlan_cmds_dummy_container(self, v, load=False):
    """
    Setter method for service_instance_vlan_cmds_dummy_container, mapped from YANG variable /interface/ethernet/logical_interface/ethernet/cmd_container_dummy/service_instance_vlan_cmds_dummy_container (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_service_instance_vlan_cmds_dummy_container is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_service_instance_vlan_cmds_dummy_container() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=service_instance_vlan_cmds_dummy_container.service_instance_vlan_cmds_dummy_container, is_container='container', presence=False, yang_name="service-instance-vlan-cmds-dummy-container", rest_name="service-instance-vlan-cmds-dummy-container", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """service_instance_vlan_cmds_dummy_container must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=service_instance_vlan_cmds_dummy_container.service_instance_vlan_cmds_dummy_container, is_container='container', presence=False, yang_name="service-instance-vlan-cmds-dummy-container", rest_name="service-instance-vlan-cmds-dummy-container", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)""",
        })

    self.__service_instance_vlan_cmds_dummy_container = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_service_instance_vlan_cmds_dummy_container(self):
    self.__service_instance_vlan_cmds_dummy_container = YANGDynClass(base=service_instance_vlan_cmds_dummy_container.service_instance_vlan_cmds_dummy_container, is_container='container', presence=False, yang_name="service-instance-vlan-cmds-dummy-container", rest_name="service-instance-vlan-cmds-dummy-container", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)

  service_instance_common_commands_dummy = __builtin__.property(_get_service_instance_common_commands_dummy, _set_service_instance_common_commands_dummy)
  service_instance_vlan_cmds_dummy_container = __builtin__.property(_get_service_instance_vlan_cmds_dummy_container, _set_service_instance_vlan_cmds_dummy_container)


  _pyangbind_elements = {'service_instance_common_commands_dummy': service_instance_common_commands_dummy, 'service_instance_vlan_cmds_dummy_container': service_instance_vlan_cmds_dummy_container, }


