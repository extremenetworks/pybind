
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import policy
class security(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/threshold-monitor/security. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__apply','__pause','__policy',)

  _yang_name = 'security'
  _rest_name = 'security'

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
    self.__policy = YANGDynClass(base=YANGListType("sec_policy_name",policy.policy, yang_name="policy", rest_name="policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sec_policy_name', extensions=None), is_container='list', yang_name="policy", rest_name="policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='list', is_config=True)
    self.__apply = YANGDynClass(base=unicode, is_leaf=True, yang_name="apply", rest_name="apply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-config', is_config=True)
    self.__pause = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pause", rest_name="pause", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'threshold-monitor', u'security']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'threshold-monitor', u'security']

  def _get_apply(self):
    """
    Getter method for apply, mapped from YANG variable /rbridge_id/threshold_monitor/security/apply (supported-config)
    """
    return self.__apply
      
  def _set_apply(self, v, load=False):
    """
    Setter method for apply, mapped from YANG variable /rbridge_id/threshold_monitor/security/apply (supported-config)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_apply is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_apply() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="apply", rest_name="apply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-config', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """apply must be of a type compatible with supported-config""",
          'defined-type': "brocade-threshold-monitor:supported-config",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="apply", rest_name="apply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-config', is_config=True)""",
        })

    self.__apply = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_apply(self):
    self.__apply = YANGDynClass(base=unicode, is_leaf=True, yang_name="apply", rest_name="apply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-config', is_config=True)


  def _get_pause(self):
    """
    Getter method for pause, mapped from YANG variable /rbridge_id/threshold_monitor/security/pause (empty)
    """
    return self.__pause
      
  def _set_pause(self, v, load=False):
    """
    Setter method for pause, mapped from YANG variable /rbridge_id/threshold_monitor/security/pause (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pause is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pause() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="pause", rest_name="pause", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pause must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pause", rest_name="pause", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='empty', is_config=True)""",
        })

    self.__pause = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pause(self):
    self.__pause = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pause", rest_name="pause", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='empty', is_config=True)


  def _get_policy(self):
    """
    Getter method for policy, mapped from YANG variable /rbridge_id/threshold_monitor/security/policy (list)
    """
    return self.__policy
      
  def _set_policy(self, v, load=False):
    """
    Setter method for policy, mapped from YANG variable /rbridge_id/threshold_monitor/security/policy (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policy() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("sec_policy_name",policy.policy, yang_name="policy", rest_name="policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sec_policy_name', extensions=None), is_container='list', yang_name="policy", rest_name="policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policy must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("sec_policy_name",policy.policy, yang_name="policy", rest_name="policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sec_policy_name', extensions=None), is_container='list', yang_name="policy", rest_name="policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='list', is_config=True)""",
        })

    self.__policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policy(self):
    self.__policy = YANGDynClass(base=YANGListType("sec_policy_name",policy.policy, yang_name="policy", rest_name="policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sec_policy_name', extensions=None), is_container='list', yang_name="policy", rest_name="policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='list', is_config=True)

  apply = __builtin__.property(_get_apply, _set_apply)
  pause = __builtin__.property(_get_pause, _set_pause)
  policy = __builtin__.property(_get_policy, _set_policy)


  _pyangbind_elements = {'apply': apply, 'pause': pause, 'policy': policy, }


