
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import event_handler_list
class event_handler(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-event-handler - based on the path /event-handler. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Event Handler Commands
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__event_handler_list',)

  _yang_name = 'event-handler'

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
    self.__event_handler_list = YANGDynClass(base=YANGListType("name",event_handler_list.event_handler_list, yang_name="event-handler-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Event handler configuration', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None}}), is_container='list', yang_name="event-handler-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler configuration', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='list', is_config=True)

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
      return [u'event-handler']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'event-handler']

  def _get_event_handler_list(self):
    """
    Getter method for event_handler_list, mapped from YANG variable /event_handler/event_handler_list (list)
    """
    return self.__event_handler_list
      
  def _set_event_handler_list(self, v, load=False):
    """
    Setter method for event_handler_list, mapped from YANG variable /event_handler/event_handler_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_event_handler_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_event_handler_list() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("name",event_handler_list.event_handler_list, yang_name="event-handler-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Event handler configuration', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None}}), is_container='list', yang_name="event-handler-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler configuration', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """event_handler_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",event_handler_list.event_handler_list, yang_name="event-handler-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Event handler configuration', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None}}), is_container='list', yang_name="event-handler-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler configuration', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='list', is_config=True)""",
        })

    self.__event_handler_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_event_handler_list(self):
    self.__event_handler_list = YANGDynClass(base=YANGListType("name",event_handler_list.event_handler_list, yang_name="event-handler-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'Event handler configuration', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None}}), is_container='list', yang_name="event-handler-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler configuration', u'cli-no-key-completion': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='list', is_config=True)

  event_handler_list = __builtin__.property(_get_event_handler_list, _set_event_handler_list)


  _pyangbind_elements = {'event_handler_list': event_handler_list, }


