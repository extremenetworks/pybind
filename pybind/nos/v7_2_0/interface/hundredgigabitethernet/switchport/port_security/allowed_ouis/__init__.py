
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class allowed_ouis(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/switchport/port-security/allowed-ouis. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of allowed OUIs
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__oui',)

  _yang_name = 'allowed-ouis'
  _rest_name = 'allowed-ouis'

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
    self.__oui = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{4}\\.[0-9a-fA-F]{2}00\\.0000'}), is_leaf=True, yang_name="oui", rest_name="oui", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='oui-type', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'switchport', u'port-security', u'allowed-ouis']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'switchport', u'port-security', u'allowed-ouis']

  def _get_oui(self):
    """
    Getter method for oui, mapped from YANG variable /interface/hundredgigabitethernet/switchport/port_security/allowed_ouis/oui (oui-type)

    YANG Description: <OUI> OUI in HHHH.HH00.0000 format
    """
    return self.__oui
      
  def _set_oui(self, v, load=False):
    """
    Setter method for oui, mapped from YANG variable /interface/hundredgigabitethernet/switchport/port_security/allowed_ouis/oui (oui-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oui is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oui() directly.

    YANG Description: <OUI> OUI in HHHH.HH00.0000 format
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{4}\\.[0-9a-fA-F]{2}00\\.0000'}), is_leaf=True, yang_name="oui", rest_name="oui", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='oui-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oui must be of a type compatible with oui-type""",
          'defined-type': "brocade-interface:oui-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{4}\\.[0-9a-fA-F]{2}00\\.0000'}), is_leaf=True, yang_name="oui", rest_name="oui", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='oui-type', is_config=True)""",
        })

    self.__oui = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oui(self):
    self.__oui = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{4}\\.[0-9a-fA-F]{2}00\\.0000'}), is_leaf=True, yang_name="oui", rest_name="oui", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='oui-type', is_config=True)

  oui = __builtin__.property(_get_oui, _set_oui)


  _pyangbind_elements = {'oui': oui, }


