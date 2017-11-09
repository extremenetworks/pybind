
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class shutdown(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/logical-interface/port-channel/pc-cmd-container-dummy/service-instance-common-commands-dummy/shutdown. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__shutdown_status',)

  _yang_name = 'shutdown'
  _rest_name = 'shutdown'

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
    self.__shutdown_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown-status", rest_name="shutdown-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='empty', is_config=True)

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
      return [u'interface', u'port-channel', u'logical-interface', u'port-channel', u'pc-cmd-container-dummy', u'service-instance-common-commands-dummy', u'shutdown']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'port-channel', u'logical-interface', u'port-channel', u'pc-cmd-container-dummy', u'service-instance-common-commands-dummy', u'shutdown']

  def _get_shutdown_status(self):
    """
    Getter method for shutdown_status, mapped from YANG variable /interface/port_channel/logical_interface/port_channel/pc_cmd_container_dummy/service_instance_common_commands_dummy/shutdown/shutdown_status (empty)
    """
    return self.__shutdown_status
      
  def _set_shutdown_status(self, v, load=False):
    """
    Setter method for shutdown_status, mapped from YANG variable /interface/port_channel/logical_interface/port_channel/pc_cmd_container_dummy/service_instance_common_commands_dummy/shutdown/shutdown_status (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shutdown_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shutdown_status() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="shutdown-status", rest_name="shutdown-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shutdown_status must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown-status", rest_name="shutdown-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='empty', is_config=True)""",
        })

    self.__shutdown_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shutdown_status(self):
    self.__shutdown_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown-status", rest_name="shutdown-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='empty', is_config=True)

  shutdown_status = __builtin__.property(_get_shutdown_status, _set_shutdown_status)


  _pyangbind_elements = {'shutdown_status': shutdown_status, }


