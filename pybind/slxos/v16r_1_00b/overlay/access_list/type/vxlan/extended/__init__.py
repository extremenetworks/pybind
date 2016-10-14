
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ext_seq
class extended(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vxlan-visibility - based on the path /overlay/access-list/type/vxlan/extended. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ext_user_acl_name','__ext_seq',)

  _yang_name = 'extended'

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
    self.__ext_seq = YANGDynClass(base=YANGListType("ext_seq_num",ext_seq.ext_seq, yang_name="ext-seq", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ext-seq-num', extensions={u'tailf-common': {u'info': u'seq <seq-num>', u'cli-suppress-mode': None, u'callpoint': u'VxlanVisibilityExtendedSeqCallpoint', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'seq'}}), is_container='list', yang_name="ext-seq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'seq <seq-num>', u'cli-suppress-mode': None, u'callpoint': u'VxlanVisibilityExtendedSeqCallpoint', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'seq'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)
    self.__ext_user_acl_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="ext-user-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Access List Name (Max 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='user-acl-name-type', is_config=True)

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
      return [u'overlay', u'access-list', u'type', u'vxlan', u'extended']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'overlay', u'access-list', u'type', u'vxlan', u'extended']

  def _get_ext_user_acl_name(self):
    """
    Getter method for ext_user_acl_name, mapped from YANG variable /overlay/access_list/type/vxlan/extended/ext_user_acl_name (user-acl-name-type)
    """
    return self.__ext_user_acl_name
      
  def _set_ext_user_acl_name(self, v, load=False):
    """
    Setter method for ext_user_acl_name, mapped from YANG variable /overlay/access_list/type/vxlan/extended/ext_user_acl_name (user-acl-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ext_user_acl_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ext_user_acl_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="ext-user-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Access List Name (Max 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='user-acl-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ext_user_acl_name must be of a type compatible with user-acl-name-type""",
          'defined-type': "brocade-vxlan-visibility:user-acl-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="ext-user-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Access List Name (Max 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='user-acl-name-type', is_config=True)""",
        })

    self.__ext_user_acl_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ext_user_acl_name(self):
    self.__ext_user_acl_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="ext-user-acl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Access List Name (Max 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='user-acl-name-type', is_config=True)


  def _get_ext_seq(self):
    """
    Getter method for ext_seq, mapped from YANG variable /overlay/access_list/type/vxlan/extended/ext_seq (list)
    """
    return self.__ext_seq
      
  def _set_ext_seq(self, v, load=False):
    """
    Setter method for ext_seq, mapped from YANG variable /overlay/access_list/type/vxlan/extended/ext_seq (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ext_seq is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ext_seq() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ext_seq_num",ext_seq.ext_seq, yang_name="ext-seq", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ext-seq-num', extensions={u'tailf-common': {u'info': u'seq <seq-num>', u'cli-suppress-mode': None, u'callpoint': u'VxlanVisibilityExtendedSeqCallpoint', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'seq'}}), is_container='list', yang_name="ext-seq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'seq <seq-num>', u'cli-suppress-mode': None, u'callpoint': u'VxlanVisibilityExtendedSeqCallpoint', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'seq'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ext_seq must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ext_seq_num",ext_seq.ext_seq, yang_name="ext-seq", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ext-seq-num', extensions={u'tailf-common': {u'info': u'seq <seq-num>', u'cli-suppress-mode': None, u'callpoint': u'VxlanVisibilityExtendedSeqCallpoint', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'seq'}}), is_container='list', yang_name="ext-seq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'seq <seq-num>', u'cli-suppress-mode': None, u'callpoint': u'VxlanVisibilityExtendedSeqCallpoint', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'seq'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)""",
        })

    self.__ext_seq = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ext_seq(self):
    self.__ext_seq = YANGDynClass(base=YANGListType("ext_seq_num",ext_seq.ext_seq, yang_name="ext-seq", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ext-seq-num', extensions={u'tailf-common': {u'info': u'seq <seq-num>', u'cli-suppress-mode': None, u'callpoint': u'VxlanVisibilityExtendedSeqCallpoint', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'seq'}}), is_container='list', yang_name="ext-seq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'seq <seq-num>', u'cli-suppress-mode': None, u'callpoint': u'VxlanVisibilityExtendedSeqCallpoint', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'seq'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)

  ext_user_acl_name = __builtin__.property(_get_ext_user_acl_name, _set_ext_user_acl_name)
  ext_seq = __builtin__.property(_get_ext_seq, _set_ext_seq)


  _pyangbind_elements = {'ext_user_acl_name': ext_user_acl_name, 'ext_seq': ext_seq, }


