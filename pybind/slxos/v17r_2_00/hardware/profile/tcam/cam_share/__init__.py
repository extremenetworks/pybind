
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class cam_share(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-hardware - based on the path /hardware/profile/tcam/cam-share. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__l2_ingress_acl','__l3_v4_ingress_acl','__l3_v6_ingress_acl','__l3_v4_pbr','__l3_v6_pbr','__openflow_v4','__openflow_v6',)

  _yang_name = 'cam-share'
  _rest_name = 'cam-share'

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
    self.__l2_ingress_acl = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l2-ingress-acl", rest_name="l2-ingress-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 2 ingress ACL'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    self.__l3_v6_pbr = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l3-v6-pbr", rest_name="l3-v6-pbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 IPv6 PBR'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    self.__l3_v4_pbr = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l3-v4-pbr", rest_name="l3-v4-pbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 IPv4 PBR'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    self.__l3_v4_ingress_acl = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l3-v4-ingress-acl", rest_name="l3-v4-ingress-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 IPv4 ingress ACL'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    self.__l3_v6_ingress_acl = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l3-v6-ingress-acl", rest_name="l3-v6-ingress-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 Ipv6 ingress ACL'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    self.__openflow_v6 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="openflow-v6", rest_name="openflow-v6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ipv6 openflow'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    self.__openflow_v4 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="openflow-v4", rest_name="openflow-v4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4 openflow'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)

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
      return [u'hardware', u'profile', u'tcam', u'cam-share']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'hardware', u'profile', u'tcam', u'cam-share']

  def _get_l2_ingress_acl(self):
    """
    Getter method for l2_ingress_acl, mapped from YANG variable /hardware/profile/tcam/cam_share/l2_ingress_acl (empty)
    """
    return self.__l2_ingress_acl
      
  def _set_l2_ingress_acl(self, v, load=False):
    """
    Setter method for l2_ingress_acl, mapped from YANG variable /hardware/profile/tcam/cam_share/l2_ingress_acl (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l2_ingress_acl is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l2_ingress_acl() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="l2-ingress-acl", rest_name="l2-ingress-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 2 ingress ACL'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l2_ingress_acl must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l2-ingress-acl", rest_name="l2-ingress-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 2 ingress ACL'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)""",
        })

    self.__l2_ingress_acl = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l2_ingress_acl(self):
    self.__l2_ingress_acl = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l2-ingress-acl", rest_name="l2-ingress-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 2 ingress ACL'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)


  def _get_l3_v4_ingress_acl(self):
    """
    Getter method for l3_v4_ingress_acl, mapped from YANG variable /hardware/profile/tcam/cam_share/l3_v4_ingress_acl (empty)
    """
    return self.__l3_v4_ingress_acl
      
  def _set_l3_v4_ingress_acl(self, v, load=False):
    """
    Setter method for l3_v4_ingress_acl, mapped from YANG variable /hardware/profile/tcam/cam_share/l3_v4_ingress_acl (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l3_v4_ingress_acl is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l3_v4_ingress_acl() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="l3-v4-ingress-acl", rest_name="l3-v4-ingress-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 IPv4 ingress ACL'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l3_v4_ingress_acl must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l3-v4-ingress-acl", rest_name="l3-v4-ingress-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 IPv4 ingress ACL'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)""",
        })

    self.__l3_v4_ingress_acl = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l3_v4_ingress_acl(self):
    self.__l3_v4_ingress_acl = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l3-v4-ingress-acl", rest_name="l3-v4-ingress-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 IPv4 ingress ACL'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)


  def _get_l3_v6_ingress_acl(self):
    """
    Getter method for l3_v6_ingress_acl, mapped from YANG variable /hardware/profile/tcam/cam_share/l3_v6_ingress_acl (empty)
    """
    return self.__l3_v6_ingress_acl
      
  def _set_l3_v6_ingress_acl(self, v, load=False):
    """
    Setter method for l3_v6_ingress_acl, mapped from YANG variable /hardware/profile/tcam/cam_share/l3_v6_ingress_acl (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l3_v6_ingress_acl is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l3_v6_ingress_acl() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="l3-v6-ingress-acl", rest_name="l3-v6-ingress-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 Ipv6 ingress ACL'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l3_v6_ingress_acl must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l3-v6-ingress-acl", rest_name="l3-v6-ingress-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 Ipv6 ingress ACL'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)""",
        })

    self.__l3_v6_ingress_acl = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l3_v6_ingress_acl(self):
    self.__l3_v6_ingress_acl = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l3-v6-ingress-acl", rest_name="l3-v6-ingress-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 Ipv6 ingress ACL'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)


  def _get_l3_v4_pbr(self):
    """
    Getter method for l3_v4_pbr, mapped from YANG variable /hardware/profile/tcam/cam_share/l3_v4_pbr (empty)
    """
    return self.__l3_v4_pbr
      
  def _set_l3_v4_pbr(self, v, load=False):
    """
    Setter method for l3_v4_pbr, mapped from YANG variable /hardware/profile/tcam/cam_share/l3_v4_pbr (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l3_v4_pbr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l3_v4_pbr() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="l3-v4-pbr", rest_name="l3-v4-pbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 IPv4 PBR'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l3_v4_pbr must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l3-v4-pbr", rest_name="l3-v4-pbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 IPv4 PBR'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)""",
        })

    self.__l3_v4_pbr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l3_v4_pbr(self):
    self.__l3_v4_pbr = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l3-v4-pbr", rest_name="l3-v4-pbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 IPv4 PBR'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)


  def _get_l3_v6_pbr(self):
    """
    Getter method for l3_v6_pbr, mapped from YANG variable /hardware/profile/tcam/cam_share/l3_v6_pbr (empty)
    """
    return self.__l3_v6_pbr
      
  def _set_l3_v6_pbr(self, v, load=False):
    """
    Setter method for l3_v6_pbr, mapped from YANG variable /hardware/profile/tcam/cam_share/l3_v6_pbr (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l3_v6_pbr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l3_v6_pbr() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="l3-v6-pbr", rest_name="l3-v6-pbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 IPv6 PBR'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l3_v6_pbr must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l3-v6-pbr", rest_name="l3-v6-pbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 IPv6 PBR'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)""",
        })

    self.__l3_v6_pbr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l3_v6_pbr(self):
    self.__l3_v6_pbr = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l3-v6-pbr", rest_name="l3-v6-pbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'layer 3 IPv6 PBR'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)


  def _get_openflow_v4(self):
    """
    Getter method for openflow_v4, mapped from YANG variable /hardware/profile/tcam/cam_share/openflow_v4 (empty)
    """
    return self.__openflow_v4
      
  def _set_openflow_v4(self, v, load=False):
    """
    Setter method for openflow_v4, mapped from YANG variable /hardware/profile/tcam/cam_share/openflow_v4 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_openflow_v4 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_openflow_v4() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="openflow-v4", rest_name="openflow-v4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4 openflow'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """openflow_v4 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="openflow-v4", rest_name="openflow-v4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4 openflow'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)""",
        })

    self.__openflow_v4 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_openflow_v4(self):
    self.__openflow_v4 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="openflow-v4", rest_name="openflow-v4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4 openflow'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)


  def _get_openflow_v6(self):
    """
    Getter method for openflow_v6, mapped from YANG variable /hardware/profile/tcam/cam_share/openflow_v6 (empty)
    """
    return self.__openflow_v6
      
  def _set_openflow_v6(self, v, load=False):
    """
    Setter method for openflow_v6, mapped from YANG variable /hardware/profile/tcam/cam_share/openflow_v6 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_openflow_v6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_openflow_v6() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="openflow-v6", rest_name="openflow-v6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ipv6 openflow'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """openflow_v6 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="openflow-v6", rest_name="openflow-v6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ipv6 openflow'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)""",
        })

    self.__openflow_v6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_openflow_v6(self):
    self.__openflow_v6 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="openflow-v6", rest_name="openflow-v6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ipv6 openflow'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)

  l2_ingress_acl = __builtin__.property(_get_l2_ingress_acl, _set_l2_ingress_acl)
  l3_v4_ingress_acl = __builtin__.property(_get_l3_v4_ingress_acl, _set_l3_v4_ingress_acl)
  l3_v6_ingress_acl = __builtin__.property(_get_l3_v6_ingress_acl, _set_l3_v6_ingress_acl)
  l3_v4_pbr = __builtin__.property(_get_l3_v4_pbr, _set_l3_v4_pbr)
  l3_v6_pbr = __builtin__.property(_get_l3_v6_pbr, _set_l3_v6_pbr)
  openflow_v4 = __builtin__.property(_get_openflow_v4, _set_openflow_v4)
  openflow_v6 = __builtin__.property(_get_openflow_v6, _set_openflow_v6)


  _pyangbind_elements = {'l2_ingress_acl': l2_ingress_acl, 'l3_v4_ingress_acl': l3_v4_ingress_acl, 'l3_v6_ingress_acl': l3_v6_ingress_acl, 'l3_v4_pbr': l3_v4_pbr, 'l3_v6_pbr': l3_v6_pbr, 'openflow_v4': openflow_v4, 'openflow_v6': openflow_v6, }

