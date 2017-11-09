
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import connector
import port_group
import custom_profile
import profile
class hardware(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-hardware - based on the path /hardware. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This specifies the group of configuration/operational 
elements to manage the hardware chracteristics of this
managed entity.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__connector','__port_group','__custom_profile','__profile',)

  _yang_name = 'hardware'
  _rest_name = 'hardware'

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
    self.__connector = YANGDynClass(base=YANGListType("name",connector.connector, yang_name="connector", rest_name="connector", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure a connector', u'sort-priority': u'39', u'cli-suppress-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'connector-config'}}), is_container='list', yang_name="connector", rest_name="connector", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a connector', u'sort-priority': u'39', u'cli-suppress-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'connector-config'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='list', is_config=True)
    self.__profile = YANGDynClass(base=profile.profile, is_container='container', presence=False, yang_name="profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Hardware Profile on a Switch'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__custom_profile = YANGDynClass(base=custom_profile.custom_profile, is_container='container', presence=False, yang_name="custom-profile", rest_name="custom-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure customized hardware profiles', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__port_group = YANGDynClass(base=YANGListType("name",port_group.port_group, yang_name="port-group", rest_name="port-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure a port-group', u'sort-priority': u'38', u'cli-suppress-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'port-group-config'}}), is_container='list', yang_name="port-group", rest_name="port-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a port-group', u'sort-priority': u'38', u'cli-suppress-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'port-group-config'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='list', is_config=True)

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
      return [u'hardware']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'hardware']

  def _get_connector(self):
    """
    Getter method for connector, mapped from YANG variable /hardware/connector (list)
    """
    return self.__connector
      
  def _set_connector(self, v, load=False):
    """
    Setter method for connector, mapped from YANG variable /hardware/connector (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connector is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connector() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",connector.connector, yang_name="connector", rest_name="connector", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure a connector', u'sort-priority': u'39', u'cli-suppress-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'connector-config'}}), is_container='list', yang_name="connector", rest_name="connector", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a connector', u'sort-priority': u'39', u'cli-suppress-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'connector-config'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connector must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",connector.connector, yang_name="connector", rest_name="connector", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure a connector', u'sort-priority': u'39', u'cli-suppress-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'connector-config'}}), is_container='list', yang_name="connector", rest_name="connector", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a connector', u'sort-priority': u'39', u'cli-suppress-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'connector-config'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='list', is_config=True)""",
        })

    self.__connector = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connector(self):
    self.__connector = YANGDynClass(base=YANGListType("name",connector.connector, yang_name="connector", rest_name="connector", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure a connector', u'sort-priority': u'39', u'cli-suppress-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'connector-config'}}), is_container='list', yang_name="connector", rest_name="connector", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a connector', u'sort-priority': u'39', u'cli-suppress-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'connector-config'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='list', is_config=True)


  def _get_port_group(self):
    """
    Getter method for port_group, mapped from YANG variable /hardware/port_group (list)
    """
    return self.__port_group
      
  def _set_port_group(self, v, load=False):
    """
    Setter method for port_group, mapped from YANG variable /hardware/port_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_group() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",port_group.port_group, yang_name="port-group", rest_name="port-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure a port-group', u'sort-priority': u'38', u'cli-suppress-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'port-group-config'}}), is_container='list', yang_name="port-group", rest_name="port-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a port-group', u'sort-priority': u'38', u'cli-suppress-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'port-group-config'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",port_group.port_group, yang_name="port-group", rest_name="port-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure a port-group', u'sort-priority': u'38', u'cli-suppress-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'port-group-config'}}), is_container='list', yang_name="port-group", rest_name="port-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a port-group', u'sort-priority': u'38', u'cli-suppress-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'port-group-config'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='list', is_config=True)""",
        })

    self.__port_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_group(self):
    self.__port_group = YANGDynClass(base=YANGListType("name",port_group.port_group, yang_name="port-group", rest_name="port-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Configure a port-group', u'sort-priority': u'38', u'cli-suppress-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'port-group-config'}}), is_container='list', yang_name="port-group", rest_name="port-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a port-group', u'sort-priority': u'38', u'cli-suppress-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'port-group-config'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='list', is_config=True)


  def _get_custom_profile(self):
    """
    Getter method for custom_profile, mapped from YANG variable /hardware/custom_profile (container)
    """
    return self.__custom_profile
      
  def _set_custom_profile(self, v, load=False):
    """
    Setter method for custom_profile, mapped from YANG variable /hardware/custom_profile (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_custom_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_custom_profile() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=custom_profile.custom_profile, is_container='container', presence=False, yang_name="custom-profile", rest_name="custom-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure customized hardware profiles', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """custom_profile must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=custom_profile.custom_profile, is_container='container', presence=False, yang_name="custom-profile", rest_name="custom-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure customized hardware profiles', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__custom_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_custom_profile(self):
    self.__custom_profile = YANGDynClass(base=custom_profile.custom_profile, is_container='container', presence=False, yang_name="custom-profile", rest_name="custom-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure customized hardware profiles', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)


  def _get_profile(self):
    """
    Getter method for profile, mapped from YANG variable /hardware/profile (container)
    """
    return self.__profile
      
  def _set_profile(self, v, load=False):
    """
    Setter method for profile, mapped from YANG variable /hardware/profile (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_profile() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=profile.profile, is_container='container', presence=False, yang_name="profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Hardware Profile on a Switch'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """profile must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=profile.profile, is_container='container', presence=False, yang_name="profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Hardware Profile on a Switch'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_profile(self):
    self.__profile = YANGDynClass(base=profile.profile, is_container='container', presence=False, yang_name="profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Hardware Profile on a Switch'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)

  connector = __builtin__.property(_get_connector, _set_connector)
  port_group = __builtin__.property(_get_port_group, _set_port_group)
  custom_profile = __builtin__.property(_get_custom_profile, _set_custom_profile)
  profile = __builtin__.property(_get_profile, _set_profile)


  _pyangbind_elements = {'connector': connector, 'port_group': port_group, 'custom_profile': custom_profile, 'profile': profile, }


