
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class start(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1ag - based on the path /cfm-config/protocol/cfm/y1731/test-profile/test-profile-params/start. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__start_type','__start_time','__start_periodic',)

  _yang_name = 'start'
  _rest_name = 'start'

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
    self.__start_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'after': {'value': 2}, u'at': {'value': 1}},), is_leaf=True, yang_name="start-type", rest_name="start-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify start type as at/after sometime', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='schedule-type', is_config=True)
    self.__start_time = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-1][0-9]|[2][0-3]){1}(:[0-5][0-9]){2}'}), is_leaf=True, yang_name="start-time", rest_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify start time in hh:mm:ss', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='time-in-hhmmss', is_config=True)
    self.__start_periodic = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'daily': {'value': 1}},), is_leaf=True, yang_name="start-periodic", rest_name="start-periodic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify start type as periodic', u'cli-optional-in-sequence': None, u'cli-break-sequence-commands': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='y1731-start-periodic', is_config=True)

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
      return [u'cfm-config', u'protocol', u'cfm', u'y1731', u'test-profile', u'test-profile-params', u'start']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'cfm', u'y1731', u'test-profile', u'start']

  def _get_start_type(self):
    """
    Getter method for start_type, mapped from YANG variable /cfm_config/protocol/cfm/y1731/test_profile/test_profile_params/start/start_type (schedule-type)
    """
    return self.__start_type
      
  def _set_start_type(self, v, load=False):
    """
    Setter method for start_type, mapped from YANG variable /cfm_config/protocol/cfm/y1731/test_profile/test_profile_params/start/start_type (schedule-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_start_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_start_type() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'after': {'value': 2}, u'at': {'value': 1}},), is_leaf=True, yang_name="start-type", rest_name="start-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify start type as at/after sometime', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='schedule-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """start_type must be of a type compatible with schedule-type""",
          'defined-type': "brocade-dot1ag:schedule-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'after': {'value': 2}, u'at': {'value': 1}},), is_leaf=True, yang_name="start-type", rest_name="start-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify start type as at/after sometime', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='schedule-type', is_config=True)""",
        })

    self.__start_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_start_type(self):
    self.__start_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'after': {'value': 2}, u'at': {'value': 1}},), is_leaf=True, yang_name="start-type", rest_name="start-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify start type as at/after sometime', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='schedule-type', is_config=True)


  def _get_start_time(self):
    """
    Getter method for start_time, mapped from YANG variable /cfm_config/protocol/cfm/y1731/test_profile/test_profile_params/start/start_time (time-in-hhmmss)
    """
    return self.__start_time
      
  def _set_start_time(self, v, load=False):
    """
    Setter method for start_time, mapped from YANG variable /cfm_config/protocol/cfm/y1731/test_profile/test_profile_params/start/start_time (time-in-hhmmss)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_start_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_start_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-1][0-9]|[2][0-3]){1}(:[0-5][0-9]){2}'}), is_leaf=True, yang_name="start-time", rest_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify start time in hh:mm:ss', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='time-in-hhmmss', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """start_time must be of a type compatible with time-in-hhmmss""",
          'defined-type': "brocade-dot1ag:time-in-hhmmss",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-1][0-9]|[2][0-3]){1}(:[0-5][0-9]){2}'}), is_leaf=True, yang_name="start-time", rest_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify start time in hh:mm:ss', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='time-in-hhmmss', is_config=True)""",
        })

    self.__start_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_start_time(self):
    self.__start_time = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-1][0-9]|[2][0-3]){1}(:[0-5][0-9]){2}'}), is_leaf=True, yang_name="start-time", rest_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify start time in hh:mm:ss', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='time-in-hhmmss', is_config=True)


  def _get_start_periodic(self):
    """
    Getter method for start_periodic, mapped from YANG variable /cfm_config/protocol/cfm/y1731/test_profile/test_profile_params/start/start_periodic (y1731-start-periodic)
    """
    return self.__start_periodic
      
  def _set_start_periodic(self, v, load=False):
    """
    Setter method for start_periodic, mapped from YANG variable /cfm_config/protocol/cfm/y1731/test_profile/test_profile_params/start/start_periodic (y1731-start-periodic)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_start_periodic is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_start_periodic() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'daily': {'value': 1}},), is_leaf=True, yang_name="start-periodic", rest_name="start-periodic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify start type as periodic', u'cli-optional-in-sequence': None, u'cli-break-sequence-commands': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='y1731-start-periodic', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """start_periodic must be of a type compatible with y1731-start-periodic""",
          'defined-type': "brocade-dot1ag:y1731-start-periodic",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'daily': {'value': 1}},), is_leaf=True, yang_name="start-periodic", rest_name="start-periodic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify start type as periodic', u'cli-optional-in-sequence': None, u'cli-break-sequence-commands': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='y1731-start-periodic', is_config=True)""",
        })

    self.__start_periodic = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_start_periodic(self):
    self.__start_periodic = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'daily': {'value': 1}},), is_leaf=True, yang_name="start-periodic", rest_name="start-periodic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify start type as periodic', u'cli-optional-in-sequence': None, u'cli-break-sequence-commands': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='y1731-start-periodic', is_config=True)

  start_type = __builtin__.property(_get_start_type, _set_start_type)
  start_time = __builtin__.property(_get_start_time, _set_start_time)
  start_periodic = __builtin__.property(_get_start_periodic, _set_start_periodic)


  _pyangbind_elements = {'start_type': start_type, 'start_time': start_time, 'start_periodic': start_periodic, }


