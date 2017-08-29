
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import pmap_seq
class overlay_policy_map(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-overlay-policy - based on the path /overlay-policy-map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Define a policy-map[Actions on the classified packet].
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__pmap_name','__pmap_seq',)

  _yang_name = 'overlay-policy-map'
  _rest_name = 'overlay-policy-map'

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
    self.__pmap_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="pmap-name", rest_name="pmap-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Overlay Policy Map Name (Max Size - 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='map-name-type', is_config=True)
    self.__pmap_seq = YANGDynClass(base=YANGListType("pmap_seq_num overlay_class",pmap_seq.pmap_seq, yang_name="pmap-seq", rest_name="seq", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pmap-seq-num overlay-class', extensions={u'tailf-common': {u'info': u'Sequence number', u'cli-no-key-completion': None, u'alt-name': u'seq', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'OverlayPolicyMapClassPolicyCallPoint', u'cli-mode-name': u'config-overlay-policymap-class-$(overlay-class)'}}), is_container='list', yang_name="pmap-seq", rest_name="seq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sequence number', u'cli-no-key-completion': None, u'alt-name': u'seq', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'OverlayPolicyMapClassPolicyCallPoint', u'cli-mode-name': u'config-overlay-policymap-class-$(overlay-class)'}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='list', is_config=True)

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
      return [u'overlay-policy-map']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-policy-map']

  def _get_pmap_name(self):
    """
    Getter method for pmap_name, mapped from YANG variable /overlay_policy_map/pmap_name (map-name-type)
    """
    return self.__pmap_name
      
  def _set_pmap_name(self, v, load=False):
    """
    Setter method for pmap_name, mapped from YANG variable /overlay_policy_map/pmap_name (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pmap_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pmap_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="pmap-name", rest_name="pmap-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Overlay Policy Map Name (Max Size - 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pmap_name must be of a type compatible with map-name-type""",
          'defined-type': "brocade-overlay-policy:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="pmap-name", rest_name="pmap-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Overlay Policy Map Name (Max Size - 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='map-name-type', is_config=True)""",
        })

    self.__pmap_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pmap_name(self):
    self.__pmap_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="pmap-name", rest_name="pmap-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Overlay Policy Map Name (Max Size - 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='map-name-type', is_config=True)


  def _get_pmap_seq(self):
    """
    Getter method for pmap_seq, mapped from YANG variable /overlay_policy_map/pmap_seq (list)
    """
    return self.__pmap_seq
      
  def _set_pmap_seq(self, v, load=False):
    """
    Setter method for pmap_seq, mapped from YANG variable /overlay_policy_map/pmap_seq (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pmap_seq is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pmap_seq() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("pmap_seq_num overlay_class",pmap_seq.pmap_seq, yang_name="pmap-seq", rest_name="seq", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pmap-seq-num overlay-class', extensions={u'tailf-common': {u'info': u'Sequence number', u'cli-no-key-completion': None, u'alt-name': u'seq', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'OverlayPolicyMapClassPolicyCallPoint', u'cli-mode-name': u'config-overlay-policymap-class-$(overlay-class)'}}), is_container='list', yang_name="pmap-seq", rest_name="seq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sequence number', u'cli-no-key-completion': None, u'alt-name': u'seq', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'OverlayPolicyMapClassPolicyCallPoint', u'cli-mode-name': u'config-overlay-policymap-class-$(overlay-class)'}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pmap_seq must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("pmap_seq_num overlay_class",pmap_seq.pmap_seq, yang_name="pmap-seq", rest_name="seq", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pmap-seq-num overlay-class', extensions={u'tailf-common': {u'info': u'Sequence number', u'cli-no-key-completion': None, u'alt-name': u'seq', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'OverlayPolicyMapClassPolicyCallPoint', u'cli-mode-name': u'config-overlay-policymap-class-$(overlay-class)'}}), is_container='list', yang_name="pmap-seq", rest_name="seq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sequence number', u'cli-no-key-completion': None, u'alt-name': u'seq', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'OverlayPolicyMapClassPolicyCallPoint', u'cli-mode-name': u'config-overlay-policymap-class-$(overlay-class)'}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='list', is_config=True)""",
        })

    self.__pmap_seq = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pmap_seq(self):
    self.__pmap_seq = YANGDynClass(base=YANGListType("pmap_seq_num overlay_class",pmap_seq.pmap_seq, yang_name="pmap-seq", rest_name="seq", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pmap-seq-num overlay-class', extensions={u'tailf-common': {u'info': u'Sequence number', u'cli-no-key-completion': None, u'alt-name': u'seq', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'OverlayPolicyMapClassPolicyCallPoint', u'cli-mode-name': u'config-overlay-policymap-class-$(overlay-class)'}}), is_container='list', yang_name="pmap-seq", rest_name="seq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sequence number', u'cli-no-key-completion': None, u'alt-name': u'seq', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'OverlayPolicyMapClassPolicyCallPoint', u'cli-mode-name': u'config-overlay-policymap-class-$(overlay-class)'}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='list', is_config=True)

  pmap_name = __builtin__.property(_get_pmap_name, _set_pmap_name)
  pmap_seq = __builtin__.property(_get_pmap_seq, _set_pmap_seq)


  _pyangbind_elements = {'pmap_name': pmap_name, 'pmap_seq': pmap_seq, }


