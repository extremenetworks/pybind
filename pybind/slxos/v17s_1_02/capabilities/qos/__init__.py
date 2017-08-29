
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import cee
import cpu
class qos(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-system-capabilities - based on the path /capabilities/qos. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__system_rx_queue_limit','__system_tx_queue_limit','__show_rx_queue_interface','__conf_rx_queue_interface','__cee','__cpu',)

  _yang_name = 'qos'
  _rest_name = 'qos'

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
    self.__conf_rx_queue_interface = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="conf-rx-queue-interface", rest_name="conf-rx-queue-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    self.__system_rx_queue_limit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="system-rx-queue-limit", rest_name="system-rx-queue-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    self.__cee = YANGDynClass(base=cee.cee, is_container='container', presence=False, yang_name="cee", rest_name="cee", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)
    self.__show_rx_queue_interface = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="show-rx-queue-interface", rest_name="show-rx-queue-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    self.__system_tx_queue_limit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="system-tx-queue-limit", rest_name="system-tx-queue-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    self.__cpu = YANGDynClass(base=cpu.cpu, is_container='container', presence=False, yang_name="cpu", rest_name="cpu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)

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
      return [u'capabilities', u'qos']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'capabilities', u'qos']

  def _get_system_rx_queue_limit(self):
    """
    Getter method for system_rx_queue_limit, mapped from YANG variable /capabilities/qos/system_rx_queue_limit (boolean)
    """
    return self.__system_rx_queue_limit
      
  def _set_system_rx_queue_limit(self, v, load=False):
    """
    Setter method for system_rx_queue_limit, mapped from YANG variable /capabilities/qos/system_rx_queue_limit (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_system_rx_queue_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_system_rx_queue_limit() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="system-rx-queue-limit", rest_name="system-rx-queue-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """system_rx_queue_limit must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="system-rx-queue-limit", rest_name="system-rx-queue-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)""",
        })

    self.__system_rx_queue_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_system_rx_queue_limit(self):
    self.__system_rx_queue_limit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="system-rx-queue-limit", rest_name="system-rx-queue-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)


  def _get_system_tx_queue_limit(self):
    """
    Getter method for system_tx_queue_limit, mapped from YANG variable /capabilities/qos/system_tx_queue_limit (boolean)
    """
    return self.__system_tx_queue_limit
      
  def _set_system_tx_queue_limit(self, v, load=False):
    """
    Setter method for system_tx_queue_limit, mapped from YANG variable /capabilities/qos/system_tx_queue_limit (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_system_tx_queue_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_system_tx_queue_limit() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="system-tx-queue-limit", rest_name="system-tx-queue-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """system_tx_queue_limit must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="system-tx-queue-limit", rest_name="system-tx-queue-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)""",
        })

    self.__system_tx_queue_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_system_tx_queue_limit(self):
    self.__system_tx_queue_limit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="system-tx-queue-limit", rest_name="system-tx-queue-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)


  def _get_show_rx_queue_interface(self):
    """
    Getter method for show_rx_queue_interface, mapped from YANG variable /capabilities/qos/show_rx_queue_interface (boolean)
    """
    return self.__show_rx_queue_interface
      
  def _set_show_rx_queue_interface(self, v, load=False):
    """
    Setter method for show_rx_queue_interface, mapped from YANG variable /capabilities/qos/show_rx_queue_interface (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_rx_queue_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_rx_queue_interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="show-rx-queue-interface", rest_name="show-rx-queue-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_rx_queue_interface must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="show-rx-queue-interface", rest_name="show-rx-queue-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)""",
        })

    self.__show_rx_queue_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_rx_queue_interface(self):
    self.__show_rx_queue_interface = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="show-rx-queue-interface", rest_name="show-rx-queue-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)


  def _get_conf_rx_queue_interface(self):
    """
    Getter method for conf_rx_queue_interface, mapped from YANG variable /capabilities/qos/conf_rx_queue_interface (boolean)
    """
    return self.__conf_rx_queue_interface
      
  def _set_conf_rx_queue_interface(self, v, load=False):
    """
    Setter method for conf_rx_queue_interface, mapped from YANG variable /capabilities/qos/conf_rx_queue_interface (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_conf_rx_queue_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_conf_rx_queue_interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="conf-rx-queue-interface", rest_name="conf-rx-queue-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """conf_rx_queue_interface must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="conf-rx-queue-interface", rest_name="conf-rx-queue-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)""",
        })

    self.__conf_rx_queue_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_conf_rx_queue_interface(self):
    self.__conf_rx_queue_interface = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="conf-rx-queue-interface", rest_name="conf-rx-queue-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)


  def _get_cee(self):
    """
    Getter method for cee, mapped from YANG variable /capabilities/qos/cee (container)
    """
    return self.__cee
      
  def _set_cee(self, v, load=False):
    """
    Setter method for cee, mapped from YANG variable /capabilities/qos/cee (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cee is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cee() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=cee.cee, is_container='container', presence=False, yang_name="cee", rest_name="cee", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cee must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=cee.cee, is_container='container', presence=False, yang_name="cee", rest_name="cee", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)""",
        })

    self.__cee = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cee(self):
    self.__cee = YANGDynClass(base=cee.cee, is_container='container', presence=False, yang_name="cee", rest_name="cee", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)


  def _get_cpu(self):
    """
    Getter method for cpu, mapped from YANG variable /capabilities/qos/cpu (container)
    """
    return self.__cpu
      
  def _set_cpu(self, v, load=False):
    """
    Setter method for cpu, mapped from YANG variable /capabilities/qos/cpu (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cpu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cpu() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=cpu.cpu, is_container='container', presence=False, yang_name="cpu", rest_name="cpu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cpu must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=cpu.cpu, is_container='container', presence=False, yang_name="cpu", rest_name="cpu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)""",
        })

    self.__cpu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cpu(self):
    self.__cpu = YANGDynClass(base=cpu.cpu, is_container='container', presence=False, yang_name="cpu", rest_name="cpu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)

  system_rx_queue_limit = __builtin__.property(_get_system_rx_queue_limit)
  system_tx_queue_limit = __builtin__.property(_get_system_tx_queue_limit)
  show_rx_queue_interface = __builtin__.property(_get_show_rx_queue_interface)
  conf_rx_queue_interface = __builtin__.property(_get_conf_rx_queue_interface)
  cee = __builtin__.property(_get_cee)
  cpu = __builtin__.property(_get_cpu)


  _pyangbind_elements = {'system_rx_queue_limit': system_rx_queue_limit, 'system_tx_queue_limit': system_tx_queue_limit, 'show_rx_queue_interface': show_rx_queue_interface, 'conf_rx_queue_interface': conf_rx_queue_interface, 'cee': cee, 'cpu': cpu, }


