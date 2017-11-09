
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ccm_up
import ccm_down
import avg_threshold
import max_threshold
class event(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol/cfm/y1731/action-profile-name/event. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ccm_up','__ccm_down','__avg_threshold','__max_threshold',)

  _yang_name = 'event'
  _rest_name = 'event'

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
    self.__ccm_up = YANGDynClass(base=ccm_up.ccm_up, is_container='container', presence=False, yang_name="ccm-up", rest_name="ccm-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ccm-up event and associate action(s); Event LogID :- EOAM-2001', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)
    self.__avg_threshold = YANGDynClass(base=avg_threshold.avg_threshold, is_container='container', presence=False, yang_name="avg-threshold", rest_name="avg-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure avg-threshold event and associate action(s); Event LogIDs :- ETH-DM : EOAM-3001, ETH-SLM : EOAM-3003(FWD), EOAM-3005(BCKD)', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)
    self.__ccm_down = YANGDynClass(base=ccm_down.ccm_down, is_container='container', presence=False, yang_name="ccm-down", rest_name="ccm-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ccm-down event and associate action(s); Event LogID :- EOAM-2002', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)
    self.__max_threshold = YANGDynClass(base=max_threshold.max_threshold, is_container='container', presence=False, yang_name="max-threshold", rest_name="max-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure max-threshold event and associate action(s); Event LogIDs :- ETH-DM : EOAM-3002, ETH-SLM : EOAM-3004(FWD), EOAM-3006(BCKD)', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)

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
      return [u'protocol', u'cfm', u'y1731', u'action-profile-name', u'event']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'cfm', u'y1731', u'action-profile', u'event']

  def _get_ccm_up(self):
    """
    Getter method for ccm_up, mapped from YANG variable /protocol/cfm/y1731/action_profile_name/event/ccm_up (container)
    """
    return self.__ccm_up
      
  def _set_ccm_up(self, v, load=False):
    """
    Setter method for ccm_up, mapped from YANG variable /protocol/cfm/y1731/action_profile_name/event/ccm_up (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ccm_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ccm_up() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ccm_up.ccm_up, is_container='container', presence=False, yang_name="ccm-up", rest_name="ccm-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ccm-up event and associate action(s); Event LogID :- EOAM-2001', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ccm_up must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ccm_up.ccm_up, is_container='container', presence=False, yang_name="ccm-up", rest_name="ccm-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ccm-up event and associate action(s); Event LogID :- EOAM-2001', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)""",
        })

    self.__ccm_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ccm_up(self):
    self.__ccm_up = YANGDynClass(base=ccm_up.ccm_up, is_container='container', presence=False, yang_name="ccm-up", rest_name="ccm-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ccm-up event and associate action(s); Event LogID :- EOAM-2001', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)


  def _get_ccm_down(self):
    """
    Getter method for ccm_down, mapped from YANG variable /protocol/cfm/y1731/action_profile_name/event/ccm_down (container)
    """
    return self.__ccm_down
      
  def _set_ccm_down(self, v, load=False):
    """
    Setter method for ccm_down, mapped from YANG variable /protocol/cfm/y1731/action_profile_name/event/ccm_down (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ccm_down is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ccm_down() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ccm_down.ccm_down, is_container='container', presence=False, yang_name="ccm-down", rest_name="ccm-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ccm-down event and associate action(s); Event LogID :- EOAM-2002', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ccm_down must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ccm_down.ccm_down, is_container='container', presence=False, yang_name="ccm-down", rest_name="ccm-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ccm-down event and associate action(s); Event LogID :- EOAM-2002', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)""",
        })

    self.__ccm_down = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ccm_down(self):
    self.__ccm_down = YANGDynClass(base=ccm_down.ccm_down, is_container='container', presence=False, yang_name="ccm-down", rest_name="ccm-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ccm-down event and associate action(s); Event LogID :- EOAM-2002', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)


  def _get_avg_threshold(self):
    """
    Getter method for avg_threshold, mapped from YANG variable /protocol/cfm/y1731/action_profile_name/event/avg_threshold (container)
    """
    return self.__avg_threshold
      
  def _set_avg_threshold(self, v, load=False):
    """
    Setter method for avg_threshold, mapped from YANG variable /protocol/cfm/y1731/action_profile_name/event/avg_threshold (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_avg_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_avg_threshold() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=avg_threshold.avg_threshold, is_container='container', presence=False, yang_name="avg-threshold", rest_name="avg-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure avg-threshold event and associate action(s); Event LogIDs :- ETH-DM : EOAM-3001, ETH-SLM : EOAM-3003(FWD), EOAM-3005(BCKD)', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """avg_threshold must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=avg_threshold.avg_threshold, is_container='container', presence=False, yang_name="avg-threshold", rest_name="avg-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure avg-threshold event and associate action(s); Event LogIDs :- ETH-DM : EOAM-3001, ETH-SLM : EOAM-3003(FWD), EOAM-3005(BCKD)', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)""",
        })

    self.__avg_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_avg_threshold(self):
    self.__avg_threshold = YANGDynClass(base=avg_threshold.avg_threshold, is_container='container', presence=False, yang_name="avg-threshold", rest_name="avg-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure avg-threshold event and associate action(s); Event LogIDs :- ETH-DM : EOAM-3001, ETH-SLM : EOAM-3003(FWD), EOAM-3005(BCKD)', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)


  def _get_max_threshold(self):
    """
    Getter method for max_threshold, mapped from YANG variable /protocol/cfm/y1731/action_profile_name/event/max_threshold (container)
    """
    return self.__max_threshold
      
  def _set_max_threshold(self, v, load=False):
    """
    Setter method for max_threshold, mapped from YANG variable /protocol/cfm/y1731/action_profile_name/event/max_threshold (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_threshold() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=max_threshold.max_threshold, is_container='container', presence=False, yang_name="max-threshold", rest_name="max-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure max-threshold event and associate action(s); Event LogIDs :- ETH-DM : EOAM-3002, ETH-SLM : EOAM-3004(FWD), EOAM-3006(BCKD)', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_threshold must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=max_threshold.max_threshold, is_container='container', presence=False, yang_name="max-threshold", rest_name="max-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure max-threshold event and associate action(s); Event LogIDs :- ETH-DM : EOAM-3002, ETH-SLM : EOAM-3004(FWD), EOAM-3006(BCKD)', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)""",
        })

    self.__max_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_threshold(self):
    self.__max_threshold = YANGDynClass(base=max_threshold.max_threshold, is_container='container', presence=False, yang_name="max-threshold", rest_name="max-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure max-threshold event and associate action(s); Event LogIDs :- ETH-DM : EOAM-3002, ETH-SLM : EOAM-3004(FWD), EOAM-3006(BCKD)', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)

  ccm_up = __builtin__.property(_get_ccm_up, _set_ccm_up)
  ccm_down = __builtin__.property(_get_ccm_down, _set_ccm_down)
  avg_threshold = __builtin__.property(_get_avg_threshold, _set_avg_threshold)
  max_threshold = __builtin__.property(_get_max_threshold, _set_max_threshold)


  _pyangbind_elements = {'ccm_up': ccm_up, 'ccm_down': ccm_down, 'avg_threshold': avg_threshold, 'max_threshold': max_threshold, }


