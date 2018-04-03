
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import event_entry
import alarm_entry
class rmon(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rmon - based on the path /rmon. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__event_entry','__alarm_entry',)

  _yang_name = 'rmon'
  _rest_name = 'rmon'

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
    self.__alarm_entry = YANGDynClass(base=YANGListType("alarm_index",alarm_entry.alarm_entry, yang_name="alarm-entry", rest_name="alarm", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='alarm-index', extensions={u'tailf-common': {u'info': u'RMON alarm', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'alarm', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'rmon_alarm'}}), is_container='list', yang_name="alarm-entry", rest_name="alarm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON alarm', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'alarm', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'rmon_alarm'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)
    self.__event_entry = YANGDynClass(base=YANGListType("event_index",event_entry.event_entry, yang_name="event-entry", rest_name="event", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='event-index', extensions={u'tailf-common': {u'info': u'RMON event', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'event', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_event'}}), is_container='list', yang_name="event-entry", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON event', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'event', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_event'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)

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
      return [u'rmon']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rmon']

  def _get_event_entry(self):
    """
    Getter method for event_entry, mapped from YANG variable /rmon/event_entry (list)
    """
    return self.__event_entry
      
  def _set_event_entry(self, v, load=False):
    """
    Setter method for event_entry, mapped from YANG variable /rmon/event_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_event_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_event_entry() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("event_index",event_entry.event_entry, yang_name="event-entry", rest_name="event", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='event-index', extensions={u'tailf-common': {u'info': u'RMON event', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'event', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_event'}}), is_container='list', yang_name="event-entry", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON event', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'event', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_event'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """event_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("event_index",event_entry.event_entry, yang_name="event-entry", rest_name="event", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='event-index', extensions={u'tailf-common': {u'info': u'RMON event', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'event', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_event'}}), is_container='list', yang_name="event-entry", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON event', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'event', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_event'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)""",
        })

    self.__event_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_event_entry(self):
    self.__event_entry = YANGDynClass(base=YANGListType("event_index",event_entry.event_entry, yang_name="event-entry", rest_name="event", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='event-index', extensions={u'tailf-common': {u'info': u'RMON event', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'event', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_event'}}), is_container='list', yang_name="event-entry", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON event', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'event', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_event'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)


  def _get_alarm_entry(self):
    """
    Getter method for alarm_entry, mapped from YANG variable /rmon/alarm_entry (list)
    """
    return self.__alarm_entry
      
  def _set_alarm_entry(self, v, load=False):
    """
    Setter method for alarm_entry, mapped from YANG variable /rmon/alarm_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alarm_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alarm_entry() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("alarm_index",alarm_entry.alarm_entry, yang_name="alarm-entry", rest_name="alarm", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='alarm-index', extensions={u'tailf-common': {u'info': u'RMON alarm', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'alarm', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'rmon_alarm'}}), is_container='list', yang_name="alarm-entry", rest_name="alarm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON alarm', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'alarm', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'rmon_alarm'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alarm_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("alarm_index",alarm_entry.alarm_entry, yang_name="alarm-entry", rest_name="alarm", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='alarm-index', extensions={u'tailf-common': {u'info': u'RMON alarm', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'alarm', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'rmon_alarm'}}), is_container='list', yang_name="alarm-entry", rest_name="alarm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON alarm', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'alarm', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'rmon_alarm'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)""",
        })

    self.__alarm_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alarm_entry(self):
    self.__alarm_entry = YANGDynClass(base=YANGListType("alarm_index",alarm_entry.alarm_entry, yang_name="alarm-entry", rest_name="alarm", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='alarm-index', extensions={u'tailf-common': {u'info': u'RMON alarm', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'alarm', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'rmon_alarm'}}), is_container='list', yang_name="alarm-entry", rest_name="alarm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON alarm', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'alarm', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'rmon_alarm'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)

  event_entry = __builtin__.property(_get_event_entry, _set_event_entry)
  alarm_entry = __builtin__.property(_get_alarm_entry, _set_alarm_entry)


  _pyangbind_elements = {'event_entry': event_entry, 'alarm_entry': alarm_entry, }

