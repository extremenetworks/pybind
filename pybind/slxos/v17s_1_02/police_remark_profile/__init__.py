
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import action
class police_remark_profile(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mqc - based on the path /police-remark-profile. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__profile_name','__action',)

  _yang_name = 'police-remark-profile'
  _rest_name = 'police-remark-profile'

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
    self.__action = YANGDynClass(base=YANGListType("classification_type action_type",action.action, yang_name="action", rest_name="action", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='classification-type action-type', extensions={u'tailf-common': {u'info': u'Configure policer remark profile actions', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'police_remark_profile_action', u'cli-mode-name': u'police-remark-profile-$(classification-type)-$(action-type)'}}), is_container='list', yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure policer remark profile actions', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'police_remark_profile_action', u'cli-mode-name': u'police-remark-profile-$(classification-type)-$(action-type)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='list', is_config=True)
    self.__profile_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="profile-name", rest_name="profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the profile(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='profile-name-type', is_config=True)

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
      return [u'police-remark-profile']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'police-remark-profile']

  def _get_profile_name(self):
    """
    Getter method for profile_name, mapped from YANG variable /police_remark_profile/profile_name (profile-name-type)
    """
    return self.__profile_name
      
  def _set_profile_name(self, v, load=False):
    """
    Setter method for profile_name, mapped from YANG variable /police_remark_profile/profile_name (profile-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_profile_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_profile_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="profile-name", rest_name="profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the profile(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='profile-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """profile_name must be of a type compatible with profile-name-type""",
          'defined-type': "brocade-qos-mqc:profile-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="profile-name", rest_name="profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the profile(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='profile-name-type', is_config=True)""",
        })

    self.__profile_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_profile_name(self):
    self.__profile_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="profile-name", rest_name="profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the profile(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='profile-name-type', is_config=True)


  def _get_action(self):
    """
    Getter method for action, mapped from YANG variable /police_remark_profile/action (list)
    """
    return self.__action
      
  def _set_action(self, v, load=False):
    """
    Setter method for action, mapped from YANG variable /police_remark_profile/action (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("classification_type action_type",action.action, yang_name="action", rest_name="action", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='classification-type action-type', extensions={u'tailf-common': {u'info': u'Configure policer remark profile actions', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'police_remark_profile_action', u'cli-mode-name': u'police-remark-profile-$(classification-type)-$(action-type)'}}), is_container='list', yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure policer remark profile actions', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'police_remark_profile_action', u'cli-mode-name': u'police-remark-profile-$(classification-type)-$(action-type)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("classification_type action_type",action.action, yang_name="action", rest_name="action", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='classification-type action-type', extensions={u'tailf-common': {u'info': u'Configure policer remark profile actions', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'police_remark_profile_action', u'cli-mode-name': u'police-remark-profile-$(classification-type)-$(action-type)'}}), is_container='list', yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure policer remark profile actions', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'police_remark_profile_action', u'cli-mode-name': u'police-remark-profile-$(classification-type)-$(action-type)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='list', is_config=True)""",
        })

    self.__action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action(self):
    self.__action = YANGDynClass(base=YANGListType("classification_type action_type",action.action, yang_name="action", rest_name="action", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='classification-type action-type', extensions={u'tailf-common': {u'info': u'Configure policer remark profile actions', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'police_remark_profile_action', u'cli-mode-name': u'police-remark-profile-$(classification-type)-$(action-type)'}}), is_container='list', yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure policer remark profile actions', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'police_remark_profile_action', u'cli-mode-name': u'police-remark-profile-$(classification-type)-$(action-type)'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='list', is_config=True)

  profile_name = __builtin__.property(_get_profile_name, _set_profile_name)
  action = __builtin__.property(_get_action, _set_action)


  _pyangbind_elements = {'profile_name': profile_name, 'action': action, }


