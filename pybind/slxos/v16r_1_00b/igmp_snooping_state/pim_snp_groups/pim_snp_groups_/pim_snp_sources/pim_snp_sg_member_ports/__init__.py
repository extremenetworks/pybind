
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class pim_snp_sg_member_ports(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mc-hms-operational - based on the path /igmp-snooping-state/pim-snp-groups/pim-snp-groups/pim-snp-sources/pim-snp-sg-member-ports. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_name','__mbr_flags','__flag_string','__mbr_uptime',)

  _yang_name = 'pim-snp-sg-member-ports'

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
    self.__mbr_flags = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="mbr-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__flag_string = YANGDynClass(base=unicode, is_leaf=True, yang_name="flag-string", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__mbr_uptime = YANGDynClass(base=unicode, is_leaf=True, yang_name="mbr-uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)

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
      return [u'igmp-snooping-state', u'pim-snp-groups', u'pim-snp-groups', u'pim-snp-sources', u'pim-snp-sg-member-ports']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'igmp-snooping-state', u'pim-snp-groups', u'pim-snp-groups', u'pim-snp-sources', u'pim-snp-sg-member-ports']

  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/pim_snp_sources/pim_snp_sg_member_ports/interface_name (string)

    YANG Description: pim snooping member port name
    """
    return self.__interface_name
      
  def _set_interface_name(self, v, load=False):
    """
    Setter method for interface_name, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/pim_snp_sources/pim_snp_sg_member_ports/interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.

    YANG Description: pim snooping member port name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_mbr_flags(self):
    """
    Getter method for mbr_flags, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/pim_snp_sources/pim_snp_sg_member_ports/mbr_flags (uint8)

    YANG Description: pim snooping flags
    """
    return self.__mbr_flags
      
  def _set_mbr_flags(self, v, load=False):
    """
    Setter method for mbr_flags, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/pim_snp_sources/pim_snp_sg_member_ports/mbr_flags (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mbr_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mbr_flags() directly.

    YANG Description: pim snooping flags
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="mbr-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mbr_flags must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="mbr-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)""",
        })

    self.__mbr_flags = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mbr_flags(self):
    self.__mbr_flags = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="mbr-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)


  def _get_flag_string(self):
    """
    Getter method for flag_string, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/pim_snp_sources/pim_snp_sg_member_ports/flag_string (string)

    YANG Description: group member port flags
    """
    return self.__flag_string
      
  def _set_flag_string(self, v, load=False):
    """
    Setter method for flag_string, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/pim_snp_sources/pim_snp_sg_member_ports/flag_string (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flag_string is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flag_string() directly.

    YANG Description: group member port flags
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="flag-string", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flag_string must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="flag-string", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__flag_string = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flag_string(self):
    self.__flag_string = YANGDynClass(base=unicode, is_leaf=True, yang_name="flag-string", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_mbr_uptime(self):
    """
    Getter method for mbr_uptime, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/pim_snp_sources/pim_snp_sg_member_ports/mbr_uptime (string)

    YANG Description: membership uptime and expire time
    """
    return self.__mbr_uptime
      
  def _set_mbr_uptime(self, v, load=False):
    """
    Setter method for mbr_uptime, mapped from YANG variable /igmp_snooping_state/pim_snp_groups/pim_snp_groups/pim_snp_sources/pim_snp_sg_member_ports/mbr_uptime (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mbr_uptime is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mbr_uptime() directly.

    YANG Description: membership uptime and expire time
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mbr-uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mbr_uptime must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mbr-uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__mbr_uptime = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mbr_uptime(self):
    self.__mbr_uptime = YANGDynClass(base=unicode, is_leaf=True, yang_name="mbr-uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)

  interface_name = __builtin__.property(_get_interface_name)
  mbr_flags = __builtin__.property(_get_mbr_flags)
  flag_string = __builtin__.property(_get_flag_string)
  mbr_uptime = __builtin__.property(_get_mbr_uptime)


  _pyangbind_elements = {'interface_name': interface_name, 'mbr_flags': mbr_flags, 'flag_string': flag_string, 'mbr_uptime': mbr_uptime, }


