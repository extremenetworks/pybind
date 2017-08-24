
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
  from YANG module brocade-interface - based on the path /interface/ethernet/switchport/trunk/allowed/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__all','__none','__add_','__except_','__remove_',)

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
    self.__add_ = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..20000']}), is_leaf=True, yang_name="add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow these VLANs to Xmit/Rx \nthrough the Layer2 interface'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-vlan-20k-range', is_config=True)
    self.__except_ = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="except", rest_name="except", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow all VLANs except this vlan \nrange to Xmit/Rx through the Layer2 \ninterface', u'cli-suppress-show-conf-path': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)
    self.__all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow all Dot1Q VLANs to Xmit/Rx through the\nLayer2 interface'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__none = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow no Dot1Q VLANs to Xmit/Rx through the\nLayer2 interface', u'cli-suppress-show-conf-path': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__remove_ = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Remove a VLAN range that Xmit/Rx \nthrough the Layer2 interface'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)

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
      return [u'interface', u'ethernet', u'switchport', u'trunk', u'allowed', u'vlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'switchport', u'trunk', u'allowed', u'vlan']

  def _get_all(self):
    """
    Getter method for all, mapped from YANG variable /interface/ethernet/switchport/trunk/allowed/vlan/all (empty)

    YANG Description: This is to specify all dot1q vlans or not.
Presence of this leaf indicates all
dot1q vlans are allowed.
    """
    return self.__all
      
  def _set_all(self, v, load=False):
    """
    Setter method for all, mapped from YANG variable /interface/ethernet/switchport/trunk/allowed/vlan/all (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_all() directly.

    YANG Description: This is to specify all dot1q vlans or not.
Presence of this leaf indicates all
dot1q vlans are allowed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow all Dot1Q VLANs to Xmit/Rx through the\nLayer2 interface'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """all must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow all Dot1Q VLANs to Xmit/Rx through the\nLayer2 interface'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_all(self):
    self.__all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow all Dot1Q VLANs to Xmit/Rx through the\nLayer2 interface'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_none(self):
    """
    Getter method for none, mapped from YANG variable /interface/ethernet/switchport/trunk/allowed/vlan/none (empty)

    YANG Description: This is to specify 'no dot1q vlans' or not. 
Presence of this leaf indicates no dot1q
vlans are allowed.
    """
    return self.__none
      
  def _set_none(self, v, load=False):
    """
    Setter method for none, mapped from YANG variable /interface/ethernet/switchport/trunk/allowed/vlan/none (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_none is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_none() directly.

    YANG Description: This is to specify 'no dot1q vlans' or not. 
Presence of this leaf indicates no dot1q
vlans are allowed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow no Dot1Q VLANs to Xmit/Rx through the\nLayer2 interface', u'cli-suppress-show-conf-path': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """none must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow no Dot1Q VLANs to Xmit/Rx through the\nLayer2 interface', u'cli-suppress-show-conf-path': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__none = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_none(self):
    self.__none = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow no Dot1Q VLANs to Xmit/Rx through the\nLayer2 interface', u'cli-suppress-show-conf-path': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_add_(self):
    """
    Getter method for add_, mapped from YANG variable /interface/ethernet/switchport/trunk/allowed/vlan/add (ui32-vlan-20k-range)

    YANG Description: This specifies list of vlans to 
be added.
    """
    return self.__add_
      
  def _set_add_(self, v, load=False):
    """
    Setter method for add_, mapped from YANG variable /interface/ethernet/switchport/trunk/allowed/vlan/add (ui32-vlan-20k-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_add_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_add_() directly.

    YANG Description: This specifies list of vlans to 
be added.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..20000']}), is_leaf=True, yang_name="add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow these VLANs to Xmit/Rx \nthrough the Layer2 interface'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-vlan-20k-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """add_ must be of a type compatible with ui32-vlan-20k-range""",
          'defined-type': "brocade-interface:ui32-vlan-20k-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..20000']}), is_leaf=True, yang_name="add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow these VLANs to Xmit/Rx \nthrough the Layer2 interface'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-vlan-20k-range', is_config=True)""",
        })

    self.__add_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_add_(self):
    self.__add_ = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..20000']}), is_leaf=True, yang_name="add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow these VLANs to Xmit/Rx \nthrough the Layer2 interface'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-vlan-20k-range', is_config=True)


  def _get_except_(self):
    """
    Getter method for except_, mapped from YANG variable /interface/ethernet/switchport/trunk/allowed/vlan/except (ui32-1k-vlan-range)

    YANG Description: This specifies exception list of 
vlans.
    """
    return self.__except_
      
  def _set_except_(self, v, load=False):
    """
    Setter method for except_, mapped from YANG variable /interface/ethernet/switchport/trunk/allowed/vlan/except (ui32-1k-vlan-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_except_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_except_() directly.

    YANG Description: This specifies exception list of 
vlans.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="except", rest_name="except", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow all VLANs except this vlan \nrange to Xmit/Rx through the Layer2 \ninterface', u'cli-suppress-show-conf-path': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """except_ must be of a type compatible with ui32-1k-vlan-range""",
          'defined-type': "brocade-interface:ui32-1k-vlan-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="except", rest_name="except", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow all VLANs except this vlan \nrange to Xmit/Rx through the Layer2 \ninterface', u'cli-suppress-show-conf-path': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)""",
        })

    self.__except_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_except_(self):
    self.__except_ = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="except", rest_name="except", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow all VLANs except this vlan \nrange to Xmit/Rx through the Layer2 \ninterface', u'cli-suppress-show-conf-path': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)


  def _get_remove_(self):
    """
    Getter method for remove_, mapped from YANG variable /interface/ethernet/switchport/trunk/allowed/vlan/remove (ui32-1k-vlan-range)

    YANG Description: This specifies the list of vlans 
to be removed.
    """
    return self.__remove_
      
  def _set_remove_(self, v, load=False):
    """
    Setter method for remove_, mapped from YANG variable /interface/ethernet/switchport/trunk/allowed/vlan/remove (ui32-1k-vlan-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remove_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remove_() directly.

    YANG Description: This specifies the list of vlans 
to be removed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Remove a VLAN range that Xmit/Rx \nthrough the Layer2 interface'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remove_ must be of a type compatible with ui32-1k-vlan-range""",
          'defined-type': "brocade-interface:ui32-1k-vlan-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Remove a VLAN range that Xmit/Rx \nthrough the Layer2 interface'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)""",
        })

    self.__remove_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remove_(self):
    self.__remove_ = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Remove a VLAN range that Xmit/Rx \nthrough the Layer2 interface'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-1k-vlan-range', is_config=True)

  all = __builtin__.property(_get_all, _set_all)
  none = __builtin__.property(_get_none, _set_none)
  add_ = __builtin__.property(_get_add_, _set_add_)
  except_ = __builtin__.property(_get_except_, _set_except_)
  remove_ = __builtin__.property(_get_remove_, _set_remove_)


  _pyangbind_elements = {'all': all, 'none': none, 'add_': add_, 'except_': except_, 'remove_': remove_, }

