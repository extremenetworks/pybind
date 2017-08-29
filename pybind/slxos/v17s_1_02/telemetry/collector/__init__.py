
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import collector_ip
import collector_profile
class collector(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-telemetry - based on the path /telemetry/collector. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__collector_name','__collector_ip','__collector_profile','__collector_activate','__collector_encoding',)

  _yang_name = 'collector'
  _rest_name = 'collector'

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
    self.__collector_activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="collector-activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Activate the collector profile', u'alt-name': u'activate'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='empty', is_config=True)
    self.__collector_ip = YANGDynClass(base=collector_ip.collector_ip, is_container='container', presence=False, yang_name="collector-ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Collector IP Address Configuration', u'cli-incomplete-no': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'ip', u'cli-flatten-container': None}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='container', is_config=True)
    self.__collector_encoding = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'json': {'value': 2}, u'gpb': {'value': 1}},), is_leaf=True, yang_name="collector-encoding", rest_name="encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Collector encoding format', u'alt-name': u'encoding', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='collector-encoding-type', is_config=True)
    self.__collector_profile = YANGDynClass(base=YANGListType("collector_profiletype collector_profilename",collector_profile.collector_profile, yang_name="collector-profile", rest_name="profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='collector-profiletype collector-profilename', extensions={u'tailf-common': {u'info': u'Create a profile for Collector', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'profile', u'cli-full-command': None, u'callpoint': u'CollectorProfile'}}), is_container='list', yang_name="collector-profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Create a profile for Collector', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'profile', u'cli-full-command': None, u'callpoint': u'CollectorProfile'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='list', is_config=True)
    self.__collector_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="collector-name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Telemetry Collector Name', u'alt-name': u'name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='common-def:name-string32', is_config=True)

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
      return [u'telemetry', u'collector']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'telemetry', u'collector']

  def _get_collector_name(self):
    """
    Getter method for collector_name, mapped from YANG variable /telemetry/collector/collector_name (common-def:name-string32)
    """
    return self.__collector_name
      
  def _set_collector_name(self, v, load=False):
    """
    Setter method for collector_name, mapped from YANG variable /telemetry/collector/collector_name (common-def:name-string32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_collector_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_collector_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="collector-name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Telemetry Collector Name', u'alt-name': u'name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='common-def:name-string32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """collector_name must be of a type compatible with common-def:name-string32""",
          'defined-type': "common-def:name-string32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="collector-name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Telemetry Collector Name', u'alt-name': u'name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='common-def:name-string32', is_config=True)""",
        })

    self.__collector_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_collector_name(self):
    self.__collector_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="collector-name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Telemetry Collector Name', u'alt-name': u'name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='common-def:name-string32', is_config=True)


  def _get_collector_ip(self):
    """
    Getter method for collector_ip, mapped from YANG variable /telemetry/collector/collector_ip (container)
    """
    return self.__collector_ip
      
  def _set_collector_ip(self, v, load=False):
    """
    Setter method for collector_ip, mapped from YANG variable /telemetry/collector/collector_ip (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_collector_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_collector_ip() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=collector_ip.collector_ip, is_container='container', presence=False, yang_name="collector-ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Collector IP Address Configuration', u'cli-incomplete-no': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'ip', u'cli-flatten-container': None}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """collector_ip must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=collector_ip.collector_ip, is_container='container', presence=False, yang_name="collector-ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Collector IP Address Configuration', u'cli-incomplete-no': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'ip', u'cli-flatten-container': None}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='container', is_config=True)""",
        })

    self.__collector_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_collector_ip(self):
    self.__collector_ip = YANGDynClass(base=collector_ip.collector_ip, is_container='container', presence=False, yang_name="collector-ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Collector IP Address Configuration', u'cli-incomplete-no': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'ip', u'cli-flatten-container': None}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='container', is_config=True)


  def _get_collector_profile(self):
    """
    Getter method for collector_profile, mapped from YANG variable /telemetry/collector/collector_profile (list)
    """
    return self.__collector_profile
      
  def _set_collector_profile(self, v, load=False):
    """
    Setter method for collector_profile, mapped from YANG variable /telemetry/collector/collector_profile (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_collector_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_collector_profile() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("collector_profiletype collector_profilename",collector_profile.collector_profile, yang_name="collector-profile", rest_name="profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='collector-profiletype collector-profilename', extensions={u'tailf-common': {u'info': u'Create a profile for Collector', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'profile', u'cli-full-command': None, u'callpoint': u'CollectorProfile'}}), is_container='list', yang_name="collector-profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Create a profile for Collector', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'profile', u'cli-full-command': None, u'callpoint': u'CollectorProfile'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """collector_profile must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("collector_profiletype collector_profilename",collector_profile.collector_profile, yang_name="collector-profile", rest_name="profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='collector-profiletype collector-profilename', extensions={u'tailf-common': {u'info': u'Create a profile for Collector', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'profile', u'cli-full-command': None, u'callpoint': u'CollectorProfile'}}), is_container='list', yang_name="collector-profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Create a profile for Collector', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'profile', u'cli-full-command': None, u'callpoint': u'CollectorProfile'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='list', is_config=True)""",
        })

    self.__collector_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_collector_profile(self):
    self.__collector_profile = YANGDynClass(base=YANGListType("collector_profiletype collector_profilename",collector_profile.collector_profile, yang_name="collector-profile", rest_name="profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='collector-profiletype collector-profilename', extensions={u'tailf-common': {u'info': u'Create a profile for Collector', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'profile', u'cli-full-command': None, u'callpoint': u'CollectorProfile'}}), is_container='list', yang_name="collector-profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Create a profile for Collector', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'profile', u'cli-full-command': None, u'callpoint': u'CollectorProfile'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='list', is_config=True)


  def _get_collector_activate(self):
    """
    Getter method for collector_activate, mapped from YANG variable /telemetry/collector/collector_activate (empty)
    """
    return self.__collector_activate
      
  def _set_collector_activate(self, v, load=False):
    """
    Setter method for collector_activate, mapped from YANG variable /telemetry/collector/collector_activate (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_collector_activate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_collector_activate() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="collector-activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Activate the collector profile', u'alt-name': u'activate'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """collector_activate must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="collector-activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Activate the collector profile', u'alt-name': u'activate'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='empty', is_config=True)""",
        })

    self.__collector_activate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_collector_activate(self):
    self.__collector_activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="collector-activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Activate the collector profile', u'alt-name': u'activate'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='empty', is_config=True)


  def _get_collector_encoding(self):
    """
    Getter method for collector_encoding, mapped from YANG variable /telemetry/collector/collector_encoding (collector-encoding-type)
    """
    return self.__collector_encoding
      
  def _set_collector_encoding(self, v, load=False):
    """
    Setter method for collector_encoding, mapped from YANG variable /telemetry/collector/collector_encoding (collector-encoding-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_collector_encoding is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_collector_encoding() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'json': {'value': 2}, u'gpb': {'value': 1}},), is_leaf=True, yang_name="collector-encoding", rest_name="encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Collector encoding format', u'alt-name': u'encoding', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='collector-encoding-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """collector_encoding must be of a type compatible with collector-encoding-type""",
          'defined-type': "brocade-telemetry:collector-encoding-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'json': {'value': 2}, u'gpb': {'value': 1}},), is_leaf=True, yang_name="collector-encoding", rest_name="encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Collector encoding format', u'alt-name': u'encoding', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='collector-encoding-type', is_config=True)""",
        })

    self.__collector_encoding = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_collector_encoding(self):
    self.__collector_encoding = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'json': {'value': 2}, u'gpb': {'value': 1}},), is_leaf=True, yang_name="collector-encoding", rest_name="encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Collector encoding format', u'alt-name': u'encoding', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='collector-encoding-type', is_config=True)

  collector_name = __builtin__.property(_get_collector_name, _set_collector_name)
  collector_ip = __builtin__.property(_get_collector_ip, _set_collector_ip)
  collector_profile = __builtin__.property(_get_collector_profile, _set_collector_profile)
  collector_activate = __builtin__.property(_get_collector_activate, _set_collector_activate)
  collector_encoding = __builtin__.property(_get_collector_encoding, _set_collector_encoding)


  _pyangbind_elements = {'collector_name': collector_name, 'collector_ip': collector_ip, 'collector_profile': collector_profile, 'collector_activate': collector_activate, 'collector_encoding': collector_encoding, }


