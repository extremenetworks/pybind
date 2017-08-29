
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class discard_voq_packet(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-system-monitor - based on the path /system-monitor/tm/discard-voq-packet. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__tm_discard_voq_packet_action','__tm_discard_voq_packet_threshold','__tm_discard_voq_packet_interval',)

  _yang_name = 'discard-voq-packet'
  _rest_name = 'discard-voq-packet'

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
    self.__tm_discard_voq_packet_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'10 .. 2880']}), is_leaf=True, yang_name="tm-discard-voq-packet-interval", rest_name="logging-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'tm-disc-voq-pkt-intvl', u'cli-full-no': None, u'info': u'Set discard VOQ packet logging interval', u'alt-name': u'logging-interval'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint16', is_config=True)
    self.__tm_discard_voq_packet_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 10000']}), is_leaf=True, yang_name="tm-discard-voq-packet-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'tm-disc-voq-pkt-th', u'cli-full-no': None, u'info': u'Set discard VOQ packet monitoring threshold', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint32', is_config=True)
    self.__tm_discard_voq_packet_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raslog': {'value': 1}},), is_leaf=True, yang_name="tm-discard-voq-packet-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'tm-disc-voq-pkt-act', u'cli-full-no': None, u'info': u'Set Discard VOQ Packet Monitoring Action', u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='enumeration', is_config=True)

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
      return [u'system-monitor', u'tm', u'discard-voq-packet']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'system-monitor', u'tm', u'discard-voq-packet']

  def _get_tm_discard_voq_packet_action(self):
    """
    Getter method for tm_discard_voq_packet_action, mapped from YANG variable /system_monitor/tm/discard_voq_packet/tm_discard_voq_packet_action (enumeration)
    """
    return self.__tm_discard_voq_packet_action
      
  def _set_tm_discard_voq_packet_action(self, v, load=False):
    """
    Setter method for tm_discard_voq_packet_action, mapped from YANG variable /system_monitor/tm/discard_voq_packet/tm_discard_voq_packet_action (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tm_discard_voq_packet_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tm_discard_voq_packet_action() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raslog': {'value': 1}},), is_leaf=True, yang_name="tm-discard-voq-packet-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'tm-disc-voq-pkt-act', u'cli-full-no': None, u'info': u'Set Discard VOQ Packet Monitoring Action', u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tm_discard_voq_packet_action must be of a type compatible with enumeration""",
          'defined-type': "brocade-system-monitor:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raslog': {'value': 1}},), is_leaf=True, yang_name="tm-discard-voq-packet-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'tm-disc-voq-pkt-act', u'cli-full-no': None, u'info': u'Set Discard VOQ Packet Monitoring Action', u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='enumeration', is_config=True)""",
        })

    self.__tm_discard_voq_packet_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tm_discard_voq_packet_action(self):
    self.__tm_discard_voq_packet_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raslog': {'value': 1}},), is_leaf=True, yang_name="tm-discard-voq-packet-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'tm-disc-voq-pkt-act', u'cli-full-no': None, u'info': u'Set Discard VOQ Packet Monitoring Action', u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='enumeration', is_config=True)


  def _get_tm_discard_voq_packet_threshold(self):
    """
    Getter method for tm_discard_voq_packet_threshold, mapped from YANG variable /system_monitor/tm/discard_voq_packet/tm_discard_voq_packet_threshold (uint32)
    """
    return self.__tm_discard_voq_packet_threshold
      
  def _set_tm_discard_voq_packet_threshold(self, v, load=False):
    """
    Setter method for tm_discard_voq_packet_threshold, mapped from YANG variable /system_monitor/tm/discard_voq_packet/tm_discard_voq_packet_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tm_discard_voq_packet_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tm_discard_voq_packet_threshold() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 10000']}), is_leaf=True, yang_name="tm-discard-voq-packet-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'tm-disc-voq-pkt-th', u'cli-full-no': None, u'info': u'Set discard VOQ packet monitoring threshold', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tm_discard_voq_packet_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 10000']}), is_leaf=True, yang_name="tm-discard-voq-packet-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'tm-disc-voq-pkt-th', u'cli-full-no': None, u'info': u'Set discard VOQ packet monitoring threshold', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint32', is_config=True)""",
        })

    self.__tm_discard_voq_packet_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tm_discard_voq_packet_threshold(self):
    self.__tm_discard_voq_packet_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 10000']}), is_leaf=True, yang_name="tm-discard-voq-packet-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'tm-disc-voq-pkt-th', u'cli-full-no': None, u'info': u'Set discard VOQ packet monitoring threshold', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint32', is_config=True)


  def _get_tm_discard_voq_packet_interval(self):
    """
    Getter method for tm_discard_voq_packet_interval, mapped from YANG variable /system_monitor/tm/discard_voq_packet/tm_discard_voq_packet_interval (uint16)
    """
    return self.__tm_discard_voq_packet_interval
      
  def _set_tm_discard_voq_packet_interval(self, v, load=False):
    """
    Setter method for tm_discard_voq_packet_interval, mapped from YANG variable /system_monitor/tm/discard_voq_packet/tm_discard_voq_packet_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tm_discard_voq_packet_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tm_discard_voq_packet_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'10 .. 2880']}), is_leaf=True, yang_name="tm-discard-voq-packet-interval", rest_name="logging-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'tm-disc-voq-pkt-intvl', u'cli-full-no': None, u'info': u'Set discard VOQ packet logging interval', u'alt-name': u'logging-interval'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tm_discard_voq_packet_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'10 .. 2880']}), is_leaf=True, yang_name="tm-discard-voq-packet-interval", rest_name="logging-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'tm-disc-voq-pkt-intvl', u'cli-full-no': None, u'info': u'Set discard VOQ packet logging interval', u'alt-name': u'logging-interval'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint16', is_config=True)""",
        })

    self.__tm_discard_voq_packet_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tm_discard_voq_packet_interval(self):
    self.__tm_discard_voq_packet_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'10 .. 2880']}), is_leaf=True, yang_name="tm-discard-voq-packet-interval", rest_name="logging-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'tm-disc-voq-pkt-intvl', u'cli-full-no': None, u'info': u'Set discard VOQ packet logging interval', u'alt-name': u'logging-interval'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint16', is_config=True)

  tm_discard_voq_packet_action = __builtin__.property(_get_tm_discard_voq_packet_action, _set_tm_discard_voq_packet_action)
  tm_discard_voq_packet_threshold = __builtin__.property(_get_tm_discard_voq_packet_threshold, _set_tm_discard_voq_packet_threshold)
  tm_discard_voq_packet_interval = __builtin__.property(_get_tm_discard_voq_packet_interval, _set_tm_discard_voq_packet_interval)


  _pyangbind_elements = {'tm_discard_voq_packet_action': tm_discard_voq_packet_action, 'tm_discard_voq_packet_threshold': tm_discard_voq_packet_threshold, 'tm_discard_voq_packet_interval': tm_discard_voq_packet_interval, }

