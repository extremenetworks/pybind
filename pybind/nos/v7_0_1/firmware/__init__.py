
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import download
import autoupgrade
import autoupgrade_params
class firmware(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-firmware - based on the path /firmware. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__download','__autoupgrade','__autoupgrade_params',)

  _yang_name = 'firmware'

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
    self.__download = YANGDynClass(base=download.download, is_container='container', yang_name="download", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'firmware download', u'action': u'sanity-check'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)
    self.__autoupgrade = YANGDynClass(base=autoupgrade.autoupgrade, is_container='container', yang_name="autoupgrade", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Node auto-upgrade enable/disable', u'hidden': u'built-in-self-test', u'alt-name': u'auto-upgrade', u'cli-incomplete-no': None, u'callpoint': u'FirmwareCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)
    self.__autoupgrade_params = YANGDynClass(base=autoupgrade_params.autoupgrade_params, is_container='container', yang_name="autoupgrade-params", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enter Node auto-upgrade parameters', u'cli-full-no': None, u'callpoint': u'FirmwareCallPoint', u'display-when': u'/vcsmode/vcs-cluster-mode = "true"', u'hidden': u'built-in-self-test', u'alt-name': u'auto-upgrade-params'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)

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
      return [u'firmware']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'firmware']

  def _get_download(self):
    """
    Getter method for download, mapped from YANG variable /firmware/download (container)
    """
    return self.__download
      
  def _set_download(self, v, load=False):
    """
    Setter method for download, mapped from YANG variable /firmware/download (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_download is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_download() directly.
    """
    try:
      t = YANGDynClass(v,base=download.download, is_container='container', yang_name="download", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'firmware download', u'action': u'sanity-check'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """download must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=download.download, is_container='container', yang_name="download", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'firmware download', u'action': u'sanity-check'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)""",
        })

    self.__download = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_download(self):
    self.__download = YANGDynClass(base=download.download, is_container='container', yang_name="download", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'firmware download', u'action': u'sanity-check'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)


  def _get_autoupgrade(self):
    """
    Getter method for autoupgrade, mapped from YANG variable /firmware/autoupgrade (container)
    """
    return self.__autoupgrade
      
  def _set_autoupgrade(self, v, load=False):
    """
    Setter method for autoupgrade, mapped from YANG variable /firmware/autoupgrade (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_autoupgrade is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_autoupgrade() directly.
    """
    try:
      t = YANGDynClass(v,base=autoupgrade.autoupgrade, is_container='container', yang_name="autoupgrade", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Node auto-upgrade enable/disable', u'hidden': u'built-in-self-test', u'alt-name': u'auto-upgrade', u'cli-incomplete-no': None, u'callpoint': u'FirmwareCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """autoupgrade must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=autoupgrade.autoupgrade, is_container='container', yang_name="autoupgrade", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Node auto-upgrade enable/disable', u'hidden': u'built-in-self-test', u'alt-name': u'auto-upgrade', u'cli-incomplete-no': None, u'callpoint': u'FirmwareCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)""",
        })

    self.__autoupgrade = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_autoupgrade(self):
    self.__autoupgrade = YANGDynClass(base=autoupgrade.autoupgrade, is_container='container', yang_name="autoupgrade", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Node auto-upgrade enable/disable', u'hidden': u'built-in-self-test', u'alt-name': u'auto-upgrade', u'cli-incomplete-no': None, u'callpoint': u'FirmwareCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)


  def _get_autoupgrade_params(self):
    """
    Getter method for autoupgrade_params, mapped from YANG variable /firmware/autoupgrade_params (container)
    """
    return self.__autoupgrade_params
      
  def _set_autoupgrade_params(self, v, load=False):
    """
    Setter method for autoupgrade_params, mapped from YANG variable /firmware/autoupgrade_params (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_autoupgrade_params is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_autoupgrade_params() directly.
    """
    try:
      t = YANGDynClass(v,base=autoupgrade_params.autoupgrade_params, is_container='container', yang_name="autoupgrade-params", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enter Node auto-upgrade parameters', u'cli-full-no': None, u'callpoint': u'FirmwareCallPoint', u'display-when': u'/vcsmode/vcs-cluster-mode = "true"', u'hidden': u'built-in-self-test', u'alt-name': u'auto-upgrade-params'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """autoupgrade_params must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=autoupgrade_params.autoupgrade_params, is_container='container', yang_name="autoupgrade-params", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enter Node auto-upgrade parameters', u'cli-full-no': None, u'callpoint': u'FirmwareCallPoint', u'display-when': u'/vcsmode/vcs-cluster-mode = "true"', u'hidden': u'built-in-self-test', u'alt-name': u'auto-upgrade-params'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)""",
        })

    self.__autoupgrade_params = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_autoupgrade_params(self):
    self.__autoupgrade_params = YANGDynClass(base=autoupgrade_params.autoupgrade_params, is_container='container', yang_name="autoupgrade-params", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enter Node auto-upgrade parameters', u'cli-full-no': None, u'callpoint': u'FirmwareCallPoint', u'display-when': u'/vcsmode/vcs-cluster-mode = "true"', u'hidden': u'built-in-self-test', u'alt-name': u'auto-upgrade-params'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)

  download = __builtin__.property(_get_download, _set_download)
  autoupgrade = __builtin__.property(_get_autoupgrade, _set_autoupgrade)
  autoupgrade_params = __builtin__.property(_get_autoupgrade_params, _set_autoupgrade_params)


  _pyangbind_elements = {'download': download, 'autoupgrade': autoupgrade, 'autoupgrade_params': autoupgrade_params, }


