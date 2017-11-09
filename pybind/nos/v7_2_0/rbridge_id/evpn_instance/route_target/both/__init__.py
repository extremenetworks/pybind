
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class both(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/evpn-instance/route-target/both. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__target_community','__ignore_as',)

  _yang_name = 'both'
  _rest_name = 'both'

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
    self.__ignore_as = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ignore-as", rest_name="ignore-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__target_community = YANGDynClass(base=unicode, is_leaf=True, yang_name="target-community", rest_name="target-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rt-type', is_config=True)

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
      return [u'rbridge-id', u'evpn-instance', u'route-target', u'both']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'evpn-instance', u'route-target', u'both']

  def _get_target_community(self):
    """
    Getter method for target_community, mapped from YANG variable /rbridge_id/evpn_instance/route_target/both/target_community (rt-type)

    YANG Description: Target VPN Extended Community
    """
    return self.__target_community
      
  def _set_target_community(self, v, load=False):
    """
    Setter method for target_community, mapped from YANG variable /rbridge_id/evpn_instance/route_target/both/target_community (rt-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_community() directly.

    YANG Description: Target VPN Extended Community
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="target-community", rest_name="target-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rt-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_community must be of a type compatible with rt-type""",
          'defined-type': "brocade-bgp:rt-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="target-community", rest_name="target-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rt-type', is_config=True)""",
        })

    self.__target_community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_community(self):
    self.__target_community = YANGDynClass(base=unicode, is_leaf=True, yang_name="target-community", rest_name="target-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rt-type', is_config=True)


  def _get_ignore_as(self):
    """
    Getter method for ignore_as, mapped from YANG variable /rbridge_id/evpn_instance/route_target/both/ignore_as (empty)
    """
    return self.__ignore_as
      
  def _set_ignore_as(self, v, load=False):
    """
    Setter method for ignore_as, mapped from YANG variable /rbridge_id/evpn_instance/route_target/both/ignore_as (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ignore_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ignore_as() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ignore-as", rest_name="ignore-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ignore_as must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ignore-as", rest_name="ignore-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__ignore_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ignore_as(self):
    self.__ignore_as = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ignore-as", rest_name="ignore-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  target_community = __builtin__.property(_get_target_community, _set_target_community)
  ignore_as = __builtin__.property(_get_ignore_as, _set_ignore_as)


  _pyangbind_elements = {'target_community': target_community, 'ignore_as': ignore_as, }


