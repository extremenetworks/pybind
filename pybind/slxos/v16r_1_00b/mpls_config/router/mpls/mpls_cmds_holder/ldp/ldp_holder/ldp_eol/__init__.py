
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ldp_eol(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/ldp/ldp-holder/ldp-eol. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ldp_eol_tx_silence','__ldp_eol_notification',)

  _yang_name = 'ldp-eol'

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
    self.__ldp_eol_notification = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..120000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(60000), is_leaf=True, yang_name="ldp-eol-notification", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Notification timer (100-120000 msec)', u'cli-full-no': None, u'alt-name': u'notification-timer'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_eol_tx_silence = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..60000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="ldp-eol-tx-silence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Transmit label silence timer (100-60000 msec)', u'cli-full-no': None, u'alt-name': u'tx-label-silence-timer'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'ldp', u'ldp-holder', u'ldp-eol']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'router', u'mpls', u'ldp', u'eol']

  def _get_ldp_eol_tx_silence(self):
    """
    Getter method for ldp_eol_tx_silence, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_eol/ldp_eol_tx_silence (uint32)
    """
    return self.__ldp_eol_tx_silence
      
  def _set_ldp_eol_tx_silence(self, v, load=False):
    """
    Setter method for ldp_eol_tx_silence, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_eol/ldp_eol_tx_silence (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_eol_tx_silence is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_eol_tx_silence() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..60000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="ldp-eol-tx-silence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Transmit label silence timer (100-60000 msec)', u'cli-full-no': None, u'alt-name': u'tx-label-silence-timer'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_eol_tx_silence must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..60000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="ldp-eol-tx-silence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Transmit label silence timer (100-60000 msec)', u'cli-full-no': None, u'alt-name': u'tx-label-silence-timer'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_eol_tx_silence = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_eol_tx_silence(self):
    self.__ldp_eol_tx_silence = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..60000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="ldp-eol-tx-silence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Transmit label silence timer (100-60000 msec)', u'cli-full-no': None, u'alt-name': u'tx-label-silence-timer'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_eol_notification(self):
    """
    Getter method for ldp_eol_notification, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_eol/ldp_eol_notification (uint32)
    """
    return self.__ldp_eol_notification
      
  def _set_ldp_eol_notification(self, v, load=False):
    """
    Setter method for ldp_eol_notification, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_eol/ldp_eol_notification (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_eol_notification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_eol_notification() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..120000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(60000), is_leaf=True, yang_name="ldp-eol-notification", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Notification timer (100-120000 msec)', u'cli-full-no': None, u'alt-name': u'notification-timer'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_eol_notification must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..120000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(60000), is_leaf=True, yang_name="ldp-eol-notification", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Notification timer (100-120000 msec)', u'cli-full-no': None, u'alt-name': u'notification-timer'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_eol_notification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_eol_notification(self):
    self.__ldp_eol_notification = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..120000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(60000), is_leaf=True, yang_name="ldp-eol-notification", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Notification timer (100-120000 msec)', u'cli-full-no': None, u'alt-name': u'notification-timer'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  ldp_eol_tx_silence = __builtin__.property(_get_ldp_eol_tx_silence, _set_ldp_eol_tx_silence)
  ldp_eol_notification = __builtin__.property(_get_ldp_eol_notification, _set_ldp_eol_notification)


  _pyangbind_elements = {'ldp_eol_tx_silence': ldp_eol_tx_silence, 'ldp_eol_notification': ldp_eol_notification, }


