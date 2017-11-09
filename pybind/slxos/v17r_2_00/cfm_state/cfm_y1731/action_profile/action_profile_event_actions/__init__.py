
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class action_profile_event_actions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1ag-operational - based on the path /cfm-state/cfm-y1731/action-profile/action-profile-event-actions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Action Profile Event type and associated actions
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__event','__actions',)

  _yang_name = 'action-profile-event-actions'
  _rest_name = 'action-profile-event-actions'

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
    self.__event = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ccm-down': {'value': 0}, u'max-threshold': {'value': 3}, u'avg-threshold': {'value': 2}, u'ccm-up': {'value': 1}},), is_leaf=True, yang_name="event", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='action-profile-event-type', is_config=False)
    self.__actions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)

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
      return [u'cfm-state', u'cfm-y1731', u'action-profile', u'action-profile-event-actions']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cfm-state', u'cfm-y1731', u'action-profile', u'action-profile-event-actions']

  def _get_event(self):
    """
    Getter method for event, mapped from YANG variable /cfm_state/cfm_y1731/action_profile/action_profile_event_actions/event (action-profile-event-type)

    YANG Description: Action Profile Event type
    """
    return self.__event
      
  def _set_event(self, v, load=False):
    """
    Setter method for event, mapped from YANG variable /cfm_state/cfm_y1731/action_profile/action_profile_event_actions/event (action-profile-event-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_event is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_event() directly.

    YANG Description: Action Profile Event type
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ccm-down': {'value': 0}, u'max-threshold': {'value': 3}, u'avg-threshold': {'value': 2}, u'ccm-up': {'value': 1}},), is_leaf=True, yang_name="event", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='action-profile-event-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """event must be of a type compatible with action-profile-event-type""",
          'defined-type': "brocade-dot1ag-operational:action-profile-event-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ccm-down': {'value': 0}, u'max-threshold': {'value': 3}, u'avg-threshold': {'value': 2}, u'ccm-up': {'value': 1}},), is_leaf=True, yang_name="event", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='action-profile-event-type', is_config=False)""",
        })

    self.__event = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_event(self):
    self.__event = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ccm-down': {'value': 0}, u'max-threshold': {'value': 3}, u'avg-threshold': {'value': 2}, u'ccm-up': {'value': 1}},), is_leaf=True, yang_name="event", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='action-profile-event-type', is_config=False)


  def _get_actions(self):
    """
    Getter method for actions, mapped from YANG variable /cfm_state/cfm_y1731/action_profile/action_profile_event_actions/actions (uint32)

    YANG Description: Actions associated with the event
    """
    return self.__actions
      
  def _set_actions(self, v, load=False):
    """
    Setter method for actions, mapped from YANG variable /cfm_state/cfm_y1731/action_profile/action_profile_event_actions/actions (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_actions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_actions() directly.

    YANG Description: Actions associated with the event
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """actions must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)""",
        })

    self.__actions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_actions(self):
    self.__actions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)

  event = __builtin__.property(_get_event)
  actions = __builtin__.property(_get_actions)


  _pyangbind_elements = {'event': event, 'actions': actions, }


