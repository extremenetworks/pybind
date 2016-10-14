
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import rbridge_id
class post(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-diagnostics - based on the path /diag/post. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__rbridge_id','__enable',)

  _yang_name = 'post'

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
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'diagpost-standalone-call-point', u'info': u'enable - enables POST / no enable - disables POST', u'cli-suppress-show-conf-path': None, u'display-when': u'/vcsmode/vcs-mode = "false"', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-diagnostics', defining_module='brocade-diagnostics', yang_type='empty', is_config=True)
    self.__rbridge_id = YANGDynClass(base=YANGListType("rbridge_id",rbridge_id.rbridge_id, yang_name="rbridge-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rbridge-id', extensions={u'tailf-common': {u'callpoint': u'diagpost-call-point', u'cli-suppress-list-no': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'cli-suppress-mode': None}}), is_container='list', yang_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'diagpost-call-point', u'cli-suppress-list-no': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-diagnostics', defining_module='brocade-diagnostics', yang_type='list', is_config=True)

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
      return [u'diag', u'post']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'diag', u'post']

  def _get_rbridge_id(self):
    """
    Getter method for rbridge_id, mapped from YANG variable /diag/post/rbridge_id (list)
    """
    return self.__rbridge_id
      
  def _set_rbridge_id(self, v, load=False):
    """
    Setter method for rbridge_id, mapped from YANG variable /diag/post/rbridge_id (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rbridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rbridge_id() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("rbridge_id",rbridge_id.rbridge_id, yang_name="rbridge-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rbridge-id', extensions={u'tailf-common': {u'callpoint': u'diagpost-call-point', u'cli-suppress-list-no': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'cli-suppress-mode': None}}), is_container='list', yang_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'diagpost-call-point', u'cli-suppress-list-no': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-diagnostics', defining_module='brocade-diagnostics', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rbridge_id must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("rbridge_id",rbridge_id.rbridge_id, yang_name="rbridge-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rbridge-id', extensions={u'tailf-common': {u'callpoint': u'diagpost-call-point', u'cli-suppress-list-no': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'cli-suppress-mode': None}}), is_container='list', yang_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'diagpost-call-point', u'cli-suppress-list-no': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-diagnostics', defining_module='brocade-diagnostics', yang_type='list', is_config=True)""",
        })

    self.__rbridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rbridge_id(self):
    self.__rbridge_id = YANGDynClass(base=YANGListType("rbridge_id",rbridge_id.rbridge_id, yang_name="rbridge-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rbridge-id', extensions={u'tailf-common': {u'callpoint': u'diagpost-call-point', u'cli-suppress-list-no': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'cli-suppress-mode': None}}), is_container='list', yang_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'diagpost-call-point', u'cli-suppress-list-no': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-diagnostics', defining_module='brocade-diagnostics', yang_type='list', is_config=True)


  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /diag/post/enable (empty)
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /diag/post/enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'diagpost-standalone-call-point', u'info': u'enable - enables POST / no enable - disables POST', u'cli-suppress-show-conf-path': None, u'display-when': u'/vcsmode/vcs-mode = "false"', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-diagnostics', defining_module='brocade-diagnostics', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'diagpost-standalone-call-point', u'info': u'enable - enables POST / no enable - disables POST', u'cli-suppress-show-conf-path': None, u'display-when': u'/vcsmode/vcs-mode = "false"', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-diagnostics', defining_module='brocade-diagnostics', yang_type='empty', is_config=True)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'diagpost-standalone-call-point', u'info': u'enable - enables POST / no enable - disables POST', u'cli-suppress-show-conf-path': None, u'display-when': u'/vcsmode/vcs-mode = "false"', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-diagnostics', defining_module='brocade-diagnostics', yang_type='empty', is_config=True)

  rbridge_id = __builtin__.property(_get_rbridge_id, _set_rbridge_id)
  enable = __builtin__.property(_get_enable, _set_enable)


  _pyangbind_elements = {'rbridge_id': rbridge_id, 'enable': enable, }


