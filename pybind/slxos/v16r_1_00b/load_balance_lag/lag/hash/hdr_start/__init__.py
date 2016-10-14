
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class hdr_start(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge-lag - based on the path /load-balance-lag/lag/hash/hdr-start. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__fwd_term',)

  _yang_name = 'hdr-start'

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
    self.__fwd_term = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fwd': {'value': 1}, u'term': {'value': 2}},), is_leaf=True, yang_name="fwd-term", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='enumeration', is_config=True)

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
      return [u'load-balance-lag', u'lag', u'hash', u'hdr-start']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'lag', u'hash', u'hdr-start']

  def _get_fwd_term(self):
    """
    Getter method for fwd_term, mapped from YANG variable /load_balance_lag/lag/hash/hdr_start/fwd_term (enumeration)
    """
    return self.__fwd_term
      
  def _set_fwd_term(self, v, load=False):
    """
    Setter method for fwd_term, mapped from YANG variable /load_balance_lag/lag/hash/hdr_start/fwd_term (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fwd_term is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fwd_term() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fwd': {'value': 1}, u'term': {'value': 2}},), is_leaf=True, yang_name="fwd-term", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fwd_term must be of a type compatible with enumeration""",
          'defined-type': "brocade-rbridge-lag:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fwd': {'value': 1}, u'term': {'value': 2}},), is_leaf=True, yang_name="fwd-term", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='enumeration', is_config=True)""",
        })

    self.__fwd_term = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fwd_term(self):
    self.__fwd_term = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fwd': {'value': 1}, u'term': {'value': 2}},), is_leaf=True, yang_name="fwd-term", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='enumeration', is_config=True)

  fwd_term = __builtin__.property(_get_fwd_term, _set_fwd_term)


  _pyangbind_elements = {'fwd_term': fwd_term, }


