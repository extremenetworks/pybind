
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import lsp_backups
class show_mpls_lsp_backup_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-bypass-lsp-name-debug/output/bypass-lsp/show-mpls-lsp-extensive-info/show-mpls-lsp-backup-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__lsp_backups',)

  _yang_name = 'show-mpls-lsp-backup-info'
  _rest_name = ''

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
    self.__lsp_backups = YANGDynClass(base=YANGListType("lsp_backup_name",lsp_backups.lsp_backups, yang_name="lsp-backups", rest_name="lsp-backups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-backup-name', extensions=None), is_container='list', yang_name="lsp-backups", rest_name="lsp-backups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-bypass-lsp-name-debug', u'output', u'bypass-lsp', u'show-mpls-lsp-extensive-info', u'show-mpls-lsp-backup-info']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-bypass-lsp-name-debug', u'output', u'bypass-lsp']

  def _get_lsp_backups(self):
    """
    Getter method for lsp_backups, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_debug/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups (list)
    """
    return self.__lsp_backups
      
  def _set_lsp_backups(self, v, load=False):
    """
    Setter method for lsp_backups, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_debug/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_backups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_backups() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("lsp_backup_name",lsp_backups.lsp_backups, yang_name="lsp-backups", rest_name="lsp-backups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-backup-name', extensions=None), is_container='list', yang_name="lsp-backups", rest_name="lsp-backups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_backups must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("lsp_backup_name",lsp_backups.lsp_backups, yang_name="lsp-backups", rest_name="lsp-backups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-backup-name', extensions=None), is_container='list', yang_name="lsp-backups", rest_name="lsp-backups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__lsp_backups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_backups(self):
    self.__lsp_backups = YANGDynClass(base=YANGListType("lsp_backup_name",lsp_backups.lsp_backups, yang_name="lsp-backups", rest_name="lsp-backups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-backup-name', extensions=None), is_container='list', yang_name="lsp-backups", rest_name="lsp-backups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

  lsp_backups = __builtin__.property(_get_lsp_backups, _set_lsp_backups)


  _pyangbind_elements = {'lsp_backups': lsp_backups, }

