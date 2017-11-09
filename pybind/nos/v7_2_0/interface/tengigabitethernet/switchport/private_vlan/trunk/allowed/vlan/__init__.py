
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/tengigabitethernet/switchport/private-vlan/trunk/allowed/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: VLAN(s) that will be added/removed
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__pvlan_all','__pvlan_none','__pvlan_add','__pvlan_except','__pvlan_remove',)

  _yang_name = 'vlan'
  _rest_name = 'vlan'

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
    self.__pvlan_remove = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="pvlan_remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'remove'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)
    self.__pvlan_add = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="pvlan_add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'add'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)
    self.__pvlan_none = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pvlan_none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'none'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__pvlan_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pvlan_all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__pvlan_except = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="pvlan_except", rest_name="except", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'except'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)

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
      return [u'interface', u'tengigabitethernet', u'switchport', u'private-vlan', u'trunk', u'allowed', u'vlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'TenGigabitEthernet', u'switchport', u'private-vlan', u'trunk', u'allowed', u'vlan']

  def _get_pvlan_all(self):
    """
    Getter method for pvlan_all, mapped from YANG variable /interface/tengigabitethernet/switchport/private_vlan/trunk/allowed/vlan/pvlan_all (empty)
    """
    return self.__pvlan_all
      
  def _set_pvlan_all(self, v, load=False):
    """
    Setter method for pvlan_all, mapped from YANG variable /interface/tengigabitethernet/switchport/private_vlan/trunk/allowed/vlan/pvlan_all (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pvlan_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pvlan_all() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="pvlan_all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pvlan_all must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pvlan_all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__pvlan_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pvlan_all(self):
    self.__pvlan_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pvlan_all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_pvlan_none(self):
    """
    Getter method for pvlan_none, mapped from YANG variable /interface/tengigabitethernet/switchport/private_vlan/trunk/allowed/vlan/pvlan_none (empty)
    """
    return self.__pvlan_none
      
  def _set_pvlan_none(self, v, load=False):
    """
    Setter method for pvlan_none, mapped from YANG variable /interface/tengigabitethernet/switchport/private_vlan/trunk/allowed/vlan/pvlan_none (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pvlan_none is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pvlan_none() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="pvlan_none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'none'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pvlan_none must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pvlan_none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'none'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__pvlan_none = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pvlan_none(self):
    self.__pvlan_none = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pvlan_none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'none'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_pvlan_add(self):
    """
    Getter method for pvlan_add, mapped from YANG variable /interface/tengigabitethernet/switchport/private_vlan/trunk/allowed/vlan/pvlan_add (ui32-1k-vlan-range)
    """
    return self.__pvlan_add
      
  def _set_pvlan_add(self, v, load=False):
    """
    Setter method for pvlan_add, mapped from YANG variable /interface/tengigabitethernet/switchport/private_vlan/trunk/allowed/vlan/pvlan_add (ui32-1k-vlan-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pvlan_add is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pvlan_add() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="pvlan_add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'add'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pvlan_add must be of a type compatible with ui32-1k-vlan-range""",
          'defined-type': "brocade-interface:ui32-1k-vlan-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="pvlan_add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'add'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)""",
        })

    self.__pvlan_add = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pvlan_add(self):
    self.__pvlan_add = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="pvlan_add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'add'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)


  def _get_pvlan_except(self):
    """
    Getter method for pvlan_except, mapped from YANG variable /interface/tengigabitethernet/switchport/private_vlan/trunk/allowed/vlan/pvlan_except (ui32-1k-vlan-range)
    """
    return self.__pvlan_except
      
  def _set_pvlan_except(self, v, load=False):
    """
    Setter method for pvlan_except, mapped from YANG variable /interface/tengigabitethernet/switchport/private_vlan/trunk/allowed/vlan/pvlan_except (ui32-1k-vlan-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pvlan_except is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pvlan_except() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="pvlan_except", rest_name="except", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'except'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pvlan_except must be of a type compatible with ui32-1k-vlan-range""",
          'defined-type': "brocade-interface:ui32-1k-vlan-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="pvlan_except", rest_name="except", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'except'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)""",
        })

    self.__pvlan_except = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pvlan_except(self):
    self.__pvlan_except = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="pvlan_except", rest_name="except", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'except'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)


  def _get_pvlan_remove(self):
    """
    Getter method for pvlan_remove, mapped from YANG variable /interface/tengigabitethernet/switchport/private_vlan/trunk/allowed/vlan/pvlan_remove (ui32-1k-vlan-range)
    """
    return self.__pvlan_remove
      
  def _set_pvlan_remove(self, v, load=False):
    """
    Setter method for pvlan_remove, mapped from YANG variable /interface/tengigabitethernet/switchport/private_vlan/trunk/allowed/vlan/pvlan_remove (ui32-1k-vlan-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pvlan_remove is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pvlan_remove() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="pvlan_remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'remove'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pvlan_remove must be of a type compatible with ui32-1k-vlan-range""",
          'defined-type': "brocade-interface:ui32-1k-vlan-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="pvlan_remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'remove'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)""",
        })

    self.__pvlan_remove = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pvlan_remove(self):
    self.__pvlan_remove = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="pvlan_remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'remove'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)

  pvlan_all = __builtin__.property(_get_pvlan_all, _set_pvlan_all)
  pvlan_none = __builtin__.property(_get_pvlan_none, _set_pvlan_none)
  pvlan_add = __builtin__.property(_get_pvlan_add, _set_pvlan_add)
  pvlan_except = __builtin__.property(_get_pvlan_except, _set_pvlan_except)
  pvlan_remove = __builtin__.property(_get_pvlan_remove, _set_pvlan_remove)


  _pyangbind_elements = {'pvlan_all': pvlan_all, 'pvlan_none': pvlan_none, 'pvlan_add': pvlan_add, 'pvlan_except': pvlan_except, 'pvlan_remove': pvlan_remove, }


