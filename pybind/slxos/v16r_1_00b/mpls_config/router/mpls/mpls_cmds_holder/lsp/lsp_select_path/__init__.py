
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class lsp_select_path(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/lsp/lsp-select-path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__lsp_select_path_mode','__lsp_select_path_primary','__lsp_select_path_secondary_name',)

  _yang_name = 'lsp-select-path'

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
    self.__lsp_select_path_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'manual': {'value': 1}, u'unconditional': {'value': 2}},), is_leaf=True, yang_name="lsp-select-path-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)
    self.__lsp_select_path_primary = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-select-path-primary", parent=self, choice=(u'choice-lsp-select-path-type', u'case-lsp-select-path-type-primary'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Choose the primary path as selected path', u'alt-name': u'primary'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__lsp_select_path_secondary_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="lsp-select-path-secondary-name", parent=self, choice=(u'choice-lsp-select-path-type', u'case-lsp-select-path-type-secondary'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Choose a secondary path as selected path', u'alt-name': u'secondary'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'lsp', u'lsp-select-path']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'router', u'mpls', u'lsp', u'select-path']

  def _get_lsp_select_path_mode(self):
    """
    Getter method for lsp_select_path_mode, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_select_path/lsp_select_path_mode (enumeration)
    """
    return self.__lsp_select_path_mode
      
  def _set_lsp_select_path_mode(self, v, load=False):
    """
    Setter method for lsp_select_path_mode, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_select_path/lsp_select_path_mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_select_path_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_select_path_mode() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'manual': {'value': 1}, u'unconditional': {'value': 2}},), is_leaf=True, yang_name="lsp-select-path-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_select_path_mode must be of a type compatible with enumeration""",
          'defined-type': "brocade-mpls:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'manual': {'value': 1}, u'unconditional': {'value': 2}},), is_leaf=True, yang_name="lsp-select-path-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)""",
        })

    self.__lsp_select_path_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_select_path_mode(self):
    self.__lsp_select_path_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'manual': {'value': 1}, u'unconditional': {'value': 2}},), is_leaf=True, yang_name="lsp-select-path-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)


  def _get_lsp_select_path_primary(self):
    """
    Getter method for lsp_select_path_primary, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_select_path/lsp_select_path_primary (empty)
    """
    return self.__lsp_select_path_primary
      
  def _set_lsp_select_path_primary(self, v, load=False):
    """
    Setter method for lsp_select_path_primary, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_select_path/lsp_select_path_primary (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_select_path_primary is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_select_path_primary() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-select-path-primary", parent=self, choice=(u'choice-lsp-select-path-type', u'case-lsp-select-path-type-primary'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Choose the primary path as selected path', u'alt-name': u'primary'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_select_path_primary must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-select-path-primary", parent=self, choice=(u'choice-lsp-select-path-type', u'case-lsp-select-path-type-primary'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Choose the primary path as selected path', u'alt-name': u'primary'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__lsp_select_path_primary = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_select_path_primary(self):
    self.__lsp_select_path_primary = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-select-path-primary", parent=self, choice=(u'choice-lsp-select-path-type', u'case-lsp-select-path-type-primary'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Choose the primary path as selected path', u'alt-name': u'primary'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_lsp_select_path_secondary_name(self):
    """
    Getter method for lsp_select_path_secondary_name, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_select_path/lsp_select_path_secondary_name (string)
    """
    return self.__lsp_select_path_secondary_name
      
  def _set_lsp_select_path_secondary_name(self, v, load=False):
    """
    Setter method for lsp_select_path_secondary_name, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_select_path/lsp_select_path_secondary_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_select_path_secondary_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_select_path_secondary_name() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="lsp-select-path-secondary-name", parent=self, choice=(u'choice-lsp-select-path-type', u'case-lsp-select-path-type-secondary'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Choose a secondary path as selected path', u'alt-name': u'secondary'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_select_path_secondary_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="lsp-select-path-secondary-name", parent=self, choice=(u'choice-lsp-select-path-type', u'case-lsp-select-path-type-secondary'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Choose a secondary path as selected path', u'alt-name': u'secondary'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__lsp_select_path_secondary_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_select_path_secondary_name(self):
    self.__lsp_select_path_secondary_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="lsp-select-path-secondary-name", parent=self, choice=(u'choice-lsp-select-path-type', u'case-lsp-select-path-type-secondary'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Choose a secondary path as selected path', u'alt-name': u'secondary'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

  lsp_select_path_mode = __builtin__.property(_get_lsp_select_path_mode, _set_lsp_select_path_mode)
  lsp_select_path_primary = __builtin__.property(_get_lsp_select_path_primary, _set_lsp_select_path_primary)
  lsp_select_path_secondary_name = __builtin__.property(_get_lsp_select_path_secondary_name, _set_lsp_select_path_secondary_name)

  __choices__ = {u'choice-lsp-select-path-type': {u'case-lsp-select-path-type-secondary': [u'lsp_select_path_secondary_name'], u'case-lsp-select-path-type-primary': [u'lsp_select_path_primary']}}
  _pyangbind_elements = {'lsp_select_path_mode': lsp_select_path_mode, 'lsp_select_path_primary': lsp_select_path_primary, 'lsp_select_path_secondary_name': lsp_select_path_secondary_name, }


