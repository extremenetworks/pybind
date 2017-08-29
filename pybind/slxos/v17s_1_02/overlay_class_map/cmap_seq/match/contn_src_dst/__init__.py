
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class contn_src_dst(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-overlay-policy - based on the path /overlay-class-map/cmap-seq/match/contn-src-dst. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__source','__destination',)

  _yang_name = 'contn-src-dst'
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
    self.__source = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", rest_name="source", parent=self, choice=(u'overlay-match-ip', u'case-overlay-ip-src-dest'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Source IPv4 Address: A.B.C.D'}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='ipv4-address', is_config=True)
    self.__destination = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destination", rest_name="destination", parent=self, choice=(u'overlay-match-ip', u'case-overlay-ip-src-dest'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Destination IPv4 Address: A.B.C.D'}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='ipv4-address', is_config=True)

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
      return [u'overlay-class-map', u'cmap-seq', u'match', u'contn-src-dst']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-class-map', u'seq', u'match']

  def _get_source(self):
    """
    Getter method for source, mapped from YANG variable /overlay_class_map/cmap_seq/match/contn_src_dst/source (ipv4-address)
    """
    return self.__source
      
  def _set_source(self, v, load=False):
    """
    Setter method for source, mapped from YANG variable /overlay_class_map/cmap_seq/match/contn_src_dst/source (ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", rest_name="source", parent=self, choice=(u'overlay-match-ip', u'case-overlay-ip-src-dest'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Source IPv4 Address: A.B.C.D'}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source must be of a type compatible with ipv4-address""",
          'defined-type': "brocade-overlay-policy:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", rest_name="source", parent=self, choice=(u'overlay-match-ip', u'case-overlay-ip-src-dest'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Source IPv4 Address: A.B.C.D'}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='ipv4-address', is_config=True)""",
        })

    self.__source = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source(self):
    self.__source = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", rest_name="source", parent=self, choice=(u'overlay-match-ip', u'case-overlay-ip-src-dest'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Source IPv4 Address: A.B.C.D'}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='ipv4-address', is_config=True)


  def _get_destination(self):
    """
    Getter method for destination, mapped from YANG variable /overlay_class_map/cmap_seq/match/contn_src_dst/destination (ipv4-address)
    """
    return self.__destination
      
  def _set_destination(self, v, load=False):
    """
    Setter method for destination, mapped from YANG variable /overlay_class_map/cmap_seq/match/contn_src_dst/destination (ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destination", rest_name="destination", parent=self, choice=(u'overlay-match-ip', u'case-overlay-ip-src-dest'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Destination IPv4 Address: A.B.C.D'}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination must be of a type compatible with ipv4-address""",
          'defined-type': "brocade-overlay-policy:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destination", rest_name="destination", parent=self, choice=(u'overlay-match-ip', u'case-overlay-ip-src-dest'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Destination IPv4 Address: A.B.C.D'}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='ipv4-address', is_config=True)""",
        })

    self.__destination = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination(self):
    self.__destination = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destination", rest_name="destination", parent=self, choice=(u'overlay-match-ip', u'case-overlay-ip-src-dest'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Destination IPv4 Address: A.B.C.D'}}, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='ipv4-address', is_config=True)

  source = __builtin__.property(_get_source, _set_source)
  destination = __builtin__.property(_get_destination, _set_destination)

  __choices__ = {u'overlay-match-ip': {u'case-overlay-ip-src-dest': [u'source', u'destination']}}
  _pyangbind_elements = {'source': source, 'destination': destination, }


