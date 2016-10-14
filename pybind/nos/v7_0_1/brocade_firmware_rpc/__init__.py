
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fwdl_status
import activate_status
import firmware_download
import logical_chassis_fwdl_sanity
import logical_chassis_fwdl_status
import dad_status
class brocade_firmware(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-firmware - based on the path /brocade_firmware_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This management module is an instrumentation to firmware level
level commands
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__fwdl_status','__activate_status','__firmware_download','__logical_chassis_fwdl_sanity','__logical_chassis_fwdl_status','__dad_status',)

  _yang_name = 'brocade-firmware'

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
    self.__logical_chassis_fwdl_sanity = YANGDynClass(base=logical_chassis_fwdl_sanity.logical_chassis_fwdl_sanity, is_leaf=True, yang_name="logical-chassis-fwdl-sanity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve firmware download sanity check status.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)
    self.__activate_status = YANGDynClass(base=activate_status.activate_status, is_leaf=True, yang_name="activate-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve firmware activation status.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)
    self.__fwdl_status = YANGDynClass(base=fwdl_status.fwdl_status, is_leaf=True, yang_name="fwdl-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Display firmware download status for the specified node', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)
    self.__firmware_download = YANGDynClass(base=firmware_download.firmware_download, is_leaf=True, yang_name="firmware-download", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'To perfrom the firmware download.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)
    self.__logical_chassis_fwdl_status = YANGDynClass(base=logical_chassis_fwdl_status.logical_chassis_fwdl_status, is_leaf=True, yang_name="logical-chassis-fwdl-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve firmware activation status.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)
    self.__dad_status = YANGDynClass(base=dad_status.dad_status, is_leaf=True, yang_name="dad-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Display DHCP auto-deployment status', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)

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
      return [u'brocade_firmware_rpc']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return []

  def _get_fwdl_status(self):
    """
    Getter method for fwdl_status, mapped from YANG variable /brocade_firmware_rpc/fwdl_status (rpc)
    """
    return self.__fwdl_status
      
  def _set_fwdl_status(self, v, load=False):
    """
    Setter method for fwdl_status, mapped from YANG variable /brocade_firmware_rpc/fwdl_status (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fwdl_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fwdl_status() directly.
    """
    try:
      t = YANGDynClass(v,base=fwdl_status.fwdl_status, is_leaf=True, yang_name="fwdl-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Display firmware download status for the specified node', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fwdl_status must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=fwdl_status.fwdl_status, is_leaf=True, yang_name="fwdl-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Display firmware download status for the specified node', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)""",
        })

    self.__fwdl_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fwdl_status(self):
    self.__fwdl_status = YANGDynClass(base=fwdl_status.fwdl_status, is_leaf=True, yang_name="fwdl-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Display firmware download status for the specified node', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)


  def _get_activate_status(self):
    """
    Getter method for activate_status, mapped from YANG variable /brocade_firmware_rpc/activate_status (rpc)
    """
    return self.__activate_status
      
  def _set_activate_status(self, v, load=False):
    """
    Setter method for activate_status, mapped from YANG variable /brocade_firmware_rpc/activate_status (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_activate_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_activate_status() directly.
    """
    try:
      t = YANGDynClass(v,base=activate_status.activate_status, is_leaf=True, yang_name="activate-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve firmware activation status.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """activate_status must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=activate_status.activate_status, is_leaf=True, yang_name="activate-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve firmware activation status.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)""",
        })

    self.__activate_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_activate_status(self):
    self.__activate_status = YANGDynClass(base=activate_status.activate_status, is_leaf=True, yang_name="activate-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve firmware activation status.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)


  def _get_firmware_download(self):
    """
    Getter method for firmware_download, mapped from YANG variable /brocade_firmware_rpc/firmware_download (rpc)
    """
    return self.__firmware_download
      
  def _set_firmware_download(self, v, load=False):
    """
    Setter method for firmware_download, mapped from YANG variable /brocade_firmware_rpc/firmware_download (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_firmware_download is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_firmware_download() directly.
    """
    try:
      t = YANGDynClass(v,base=firmware_download.firmware_download, is_leaf=True, yang_name="firmware-download", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'To perfrom the firmware download.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """firmware_download must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=firmware_download.firmware_download, is_leaf=True, yang_name="firmware-download", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'To perfrom the firmware download.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)""",
        })

    self.__firmware_download = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_firmware_download(self):
    self.__firmware_download = YANGDynClass(base=firmware_download.firmware_download, is_leaf=True, yang_name="firmware-download", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'To perfrom the firmware download.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)


  def _get_logical_chassis_fwdl_sanity(self):
    """
    Getter method for logical_chassis_fwdl_sanity, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity (rpc)
    """
    return self.__logical_chassis_fwdl_sanity
      
  def _set_logical_chassis_fwdl_sanity(self, v, load=False):
    """
    Setter method for logical_chassis_fwdl_sanity, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logical_chassis_fwdl_sanity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logical_chassis_fwdl_sanity() directly.
    """
    try:
      t = YANGDynClass(v,base=logical_chassis_fwdl_sanity.logical_chassis_fwdl_sanity, is_leaf=True, yang_name="logical-chassis-fwdl-sanity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve firmware download sanity check status.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logical_chassis_fwdl_sanity must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=logical_chassis_fwdl_sanity.logical_chassis_fwdl_sanity, is_leaf=True, yang_name="logical-chassis-fwdl-sanity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve firmware download sanity check status.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)""",
        })

    self.__logical_chassis_fwdl_sanity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logical_chassis_fwdl_sanity(self):
    self.__logical_chassis_fwdl_sanity = YANGDynClass(base=logical_chassis_fwdl_sanity.logical_chassis_fwdl_sanity, is_leaf=True, yang_name="logical-chassis-fwdl-sanity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve firmware download sanity check status.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)


  def _get_logical_chassis_fwdl_status(self):
    """
    Getter method for logical_chassis_fwdl_status, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status (rpc)
    """
    return self.__logical_chassis_fwdl_status
      
  def _set_logical_chassis_fwdl_status(self, v, load=False):
    """
    Setter method for logical_chassis_fwdl_status, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logical_chassis_fwdl_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logical_chassis_fwdl_status() directly.
    """
    try:
      t = YANGDynClass(v,base=logical_chassis_fwdl_status.logical_chassis_fwdl_status, is_leaf=True, yang_name="logical-chassis-fwdl-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve firmware activation status.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logical_chassis_fwdl_status must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=logical_chassis_fwdl_status.logical_chassis_fwdl_status, is_leaf=True, yang_name="logical-chassis-fwdl-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve firmware activation status.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)""",
        })

    self.__logical_chassis_fwdl_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logical_chassis_fwdl_status(self):
    self.__logical_chassis_fwdl_status = YANGDynClass(base=logical_chassis_fwdl_status.logical_chassis_fwdl_status, is_leaf=True, yang_name="logical-chassis-fwdl-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve firmware activation status.', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)


  def _get_dad_status(self):
    """
    Getter method for dad_status, mapped from YANG variable /brocade_firmware_rpc/dad_status (rpc)
    """
    return self.__dad_status
      
  def _set_dad_status(self, v, load=False):
    """
    Setter method for dad_status, mapped from YANG variable /brocade_firmware_rpc/dad_status (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dad_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dad_status() directly.
    """
    try:
      t = YANGDynClass(v,base=dad_status.dad_status, is_leaf=True, yang_name="dad-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Display DHCP auto-deployment status', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dad_status must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=dad_status.dad_status, is_leaf=True, yang_name="dad-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Display DHCP auto-deployment status', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)""",
        })

    self.__dad_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dad_status(self):
    self.__dad_status = YANGDynClass(base=dad_status.dad_status, is_leaf=True, yang_name="dad-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Display DHCP auto-deployment status', u'hidden': u'rpccmd', u'actionpoint': u'firmware'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rpc', is_config=True)

  fwdl_status = __builtin__.property(_get_fwdl_status, _set_fwdl_status)
  activate_status = __builtin__.property(_get_activate_status, _set_activate_status)
  firmware_download = __builtin__.property(_get_firmware_download, _set_firmware_download)
  logical_chassis_fwdl_sanity = __builtin__.property(_get_logical_chassis_fwdl_sanity, _set_logical_chassis_fwdl_sanity)
  logical_chassis_fwdl_status = __builtin__.property(_get_logical_chassis_fwdl_status, _set_logical_chassis_fwdl_status)
  dad_status = __builtin__.property(_get_dad_status, _set_dad_status)


  _pyangbind_elements = {'fwdl_status': fwdl_status, 'activate_status': activate_status, 'firmware_download': firmware_download, 'logical_chassis_fwdl_sanity': logical_chassis_fwdl_sanity, 'logical_chassis_fwdl_status': logical_chassis_fwdl_status, 'dad_status': dad_status, }


