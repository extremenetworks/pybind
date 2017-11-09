
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class access_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-overlay-policy - based on the path /overlay-policy-map/pmap-seq/ipv6-acl/ipv6/access-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv6_access_list',)

  _yang_name = 'access-group'
  _rest_name = 'access-group'

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
    self.__ipv6_access_list = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="ipv6-access-list", rest_name="ipv6-access-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='mac-ip-acl-name', is_config=True)

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
      return [u'overlay-policy-map', u'pmap-seq', u'ipv6-acl', u'ipv6', u'access-group']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-policy-map', u'pmap-seq', u'ipv6-acl', u'ipv6', u'access-group']

  def _get_ipv6_access_list(self):
    """
    Getter method for ipv6_access_list, mapped from YANG variable /overlay_policy_map/pmap_seq/ipv6_acl/ipv6/access_group/ipv6_access_list (mac-ip-acl-name)
    """
    return self.__ipv6_access_list
      
  def _set_ipv6_access_list(self, v, load=False):
    """
    Setter method for ipv6_access_list, mapped from YANG variable /overlay_policy_map/pmap_seq/ipv6_acl/ipv6/access_group/ipv6_access_list (mac-ip-acl-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_access_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_access_list() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="ipv6-access-list", rest_name="ipv6-access-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='mac-ip-acl-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_access_list must be of a type compatible with mac-ip-acl-name""",
          'defined-type': "brocade-overlay-policy:mac-ip-acl-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="ipv6-access-list", rest_name="ipv6-access-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='mac-ip-acl-name', is_config=True)""",
        })

    self.__ipv6_access_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_access_list(self):
    self.__ipv6_access_list = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="ipv6-access-list", rest_name="ipv6-access-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='mac-ip-acl-name', is_config=True)

  ipv6_access_list = __builtin__.property(_get_ipv6_access_list, _set_ipv6_access_list)


  _pyangbind_elements = {'ipv6_access_list': ipv6_access_list, }


