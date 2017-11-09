
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class rsvp_intf_flooding_threshold(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/mpls-interface/rsvp/rsvp-intf-flooding-threshold. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rsvp_intf_flooding_threshold_down','__rsvp_intf_flooding_threshold_up',)

  _yang_name = 'rsvp-intf-flooding-threshold'
  _rest_name = 'rsvp-intf-flooding-threshold'

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
    self.__rsvp_intf_flooding_threshold_down = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..99']})), is_leaf=False, yang_name="rsvp-intf-flooding-threshold-down", rest_name="rsvp-intf-flooding-threshold-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__rsvp_intf_flooding_threshold_up = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100']})), is_leaf=False, yang_name="rsvp-intf-flooding-threshold-up", rest_name="rsvp-intf-flooding-threshold-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'mpls-interface', u'rsvp', u'rsvp-intf-flooding-threshold']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'mpls-interface', u'rsvp', u'rsvp-intf-flooding-threshold']

  def _get_rsvp_intf_flooding_threshold_down(self):
    """
    Getter method for rsvp_intf_flooding_threshold_down, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp/rsvp_intf_flooding_threshold/rsvp_intf_flooding_threshold_down (uint32)
    """
    return self.__rsvp_intf_flooding_threshold_down
      
  def _set_rsvp_intf_flooding_threshold_down(self, v, load=False):
    """
    Setter method for rsvp_intf_flooding_threshold_down, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp/rsvp_intf_flooding_threshold/rsvp_intf_flooding_threshold_down (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rsvp_intf_flooding_threshold_down is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rsvp_intf_flooding_threshold_down() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..99']})), is_leaf=False, yang_name="rsvp-intf-flooding-threshold-down", rest_name="rsvp-intf-flooding-threshold-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rsvp_intf_flooding_threshold_down must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..99']})), is_leaf=False, yang_name="rsvp-intf-flooding-threshold-down", rest_name="rsvp-intf-flooding-threshold-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__rsvp_intf_flooding_threshold_down = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rsvp_intf_flooding_threshold_down(self):
    self.__rsvp_intf_flooding_threshold_down = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..99']})), is_leaf=False, yang_name="rsvp-intf-flooding-threshold-down", rest_name="rsvp-intf-flooding-threshold-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_rsvp_intf_flooding_threshold_up(self):
    """
    Getter method for rsvp_intf_flooding_threshold_up, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp/rsvp_intf_flooding_threshold/rsvp_intf_flooding_threshold_up (uint32)
    """
    return self.__rsvp_intf_flooding_threshold_up
      
  def _set_rsvp_intf_flooding_threshold_up(self, v, load=False):
    """
    Setter method for rsvp_intf_flooding_threshold_up, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp/rsvp_intf_flooding_threshold/rsvp_intf_flooding_threshold_up (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rsvp_intf_flooding_threshold_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rsvp_intf_flooding_threshold_up() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100']})), is_leaf=False, yang_name="rsvp-intf-flooding-threshold-up", rest_name="rsvp-intf-flooding-threshold-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rsvp_intf_flooding_threshold_up must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100']})), is_leaf=False, yang_name="rsvp-intf-flooding-threshold-up", rest_name="rsvp-intf-flooding-threshold-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__rsvp_intf_flooding_threshold_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rsvp_intf_flooding_threshold_up(self):
    self.__rsvp_intf_flooding_threshold_up = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100']})), is_leaf=False, yang_name="rsvp-intf-flooding-threshold-up", rest_name="rsvp-intf-flooding-threshold-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  rsvp_intf_flooding_threshold_down = __builtin__.property(_get_rsvp_intf_flooding_threshold_down, _set_rsvp_intf_flooding_threshold_down)
  rsvp_intf_flooding_threshold_up = __builtin__.property(_get_rsvp_intf_flooding_threshold_up, _set_rsvp_intf_flooding_threshold_up)


  _pyangbind_elements = {'rsvp_intf_flooding_threshold_down': rsvp_intf_flooding_threshold_down, 'rsvp_intf_flooding_threshold_up': rsvp_intf_flooding_threshold_up, }


