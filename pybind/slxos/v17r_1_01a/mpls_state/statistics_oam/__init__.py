
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import return_codes
class statistics_oam(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/statistics-oam. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: OAM packet statistics
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__usr_ping_count','__usr_traceroute_count','__echo_req_sent_count','__echo_req_received_count','__echo_req_timeout_count','__echo_resp_sent_count','__echo_resp_received_count','__return_codes',)

  _yang_name = 'statistics-oam'
  _rest_name = 'statistics-oam'

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
    self.__echo_req_timeout_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-req-timeout-count", rest_name="echo-req-timeout-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__usr_traceroute_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr-traceroute-count", rest_name="usr-traceroute-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__return_codes = YANGDynClass(base=YANGListType("number",return_codes.return_codes, yang_name="return-codes", rest_name="return-codes", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='number', extensions=None), is_container='list', yang_name="return-codes", rest_name="return-codes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__echo_resp_received_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-resp-received-count", rest_name="echo-resp-received-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__echo_req_sent_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-req-sent-count", rest_name="echo-req-sent-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__echo_req_received_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-req-received-count", rest_name="echo-req-received-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__echo_resp_sent_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-resp-sent-count", rest_name="echo-resp-sent-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__usr_ping_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr-ping-count", rest_name="usr-ping-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

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
      return [u'mpls-state', u'statistics-oam']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'statistics-oam']

  def _get_usr_ping_count(self):
    """
    Getter method for usr_ping_count, mapped from YANG variable /mpls_state/statistics_oam/usr_ping_count (uint32)

    YANG Description: Count of user initiated ping requests
    """
    return self.__usr_ping_count
      
  def _set_usr_ping_count(self, v, load=False):
    """
    Setter method for usr_ping_count, mapped from YANG variable /mpls_state/statistics_oam/usr_ping_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_usr_ping_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_usr_ping_count() directly.

    YANG Description: Count of user initiated ping requests
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr-ping-count", rest_name="usr-ping-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """usr_ping_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr-ping-count", rest_name="usr-ping-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__usr_ping_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_usr_ping_count(self):
    self.__usr_ping_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr-ping-count", rest_name="usr-ping-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_usr_traceroute_count(self):
    """
    Getter method for usr_traceroute_count, mapped from YANG variable /mpls_state/statistics_oam/usr_traceroute_count (uint32)

    YANG Description: Count of user initiated traceroute requests
    """
    return self.__usr_traceroute_count
      
  def _set_usr_traceroute_count(self, v, load=False):
    """
    Setter method for usr_traceroute_count, mapped from YANG variable /mpls_state/statistics_oam/usr_traceroute_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_usr_traceroute_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_usr_traceroute_count() directly.

    YANG Description: Count of user initiated traceroute requests
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr-traceroute-count", rest_name="usr-traceroute-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """usr_traceroute_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr-traceroute-count", rest_name="usr-traceroute-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__usr_traceroute_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_usr_traceroute_count(self):
    self.__usr_traceroute_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr-traceroute-count", rest_name="usr-traceroute-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_echo_req_sent_count(self):
    """
    Getter method for echo_req_sent_count, mapped from YANG variable /mpls_state/statistics_oam/echo_req_sent_count (uint32)

    YANG Description: Count of MPLS Echo requests sent
    """
    return self.__echo_req_sent_count
      
  def _set_echo_req_sent_count(self, v, load=False):
    """
    Setter method for echo_req_sent_count, mapped from YANG variable /mpls_state/statistics_oam/echo_req_sent_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_echo_req_sent_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_echo_req_sent_count() directly.

    YANG Description: Count of MPLS Echo requests sent
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-req-sent-count", rest_name="echo-req-sent-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """echo_req_sent_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-req-sent-count", rest_name="echo-req-sent-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__echo_req_sent_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_echo_req_sent_count(self):
    self.__echo_req_sent_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-req-sent-count", rest_name="echo-req-sent-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_echo_req_received_count(self):
    """
    Getter method for echo_req_received_count, mapped from YANG variable /mpls_state/statistics_oam/echo_req_received_count (uint32)

    YANG Description: Count of MPLS Echo requests received
    """
    return self.__echo_req_received_count
      
  def _set_echo_req_received_count(self, v, load=False):
    """
    Setter method for echo_req_received_count, mapped from YANG variable /mpls_state/statistics_oam/echo_req_received_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_echo_req_received_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_echo_req_received_count() directly.

    YANG Description: Count of MPLS Echo requests received
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-req-received-count", rest_name="echo-req-received-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """echo_req_received_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-req-received-count", rest_name="echo-req-received-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__echo_req_received_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_echo_req_received_count(self):
    self.__echo_req_received_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-req-received-count", rest_name="echo-req-received-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_echo_req_timeout_count(self):
    """
    Getter method for echo_req_timeout_count, mapped from YANG variable /mpls_state/statistics_oam/echo_req_timeout_count (uint32)

    YANG Description: Count of MPLS Echo requests timedout
    """
    return self.__echo_req_timeout_count
      
  def _set_echo_req_timeout_count(self, v, load=False):
    """
    Setter method for echo_req_timeout_count, mapped from YANG variable /mpls_state/statistics_oam/echo_req_timeout_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_echo_req_timeout_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_echo_req_timeout_count() directly.

    YANG Description: Count of MPLS Echo requests timedout
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-req-timeout-count", rest_name="echo-req-timeout-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """echo_req_timeout_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-req-timeout-count", rest_name="echo-req-timeout-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__echo_req_timeout_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_echo_req_timeout_count(self):
    self.__echo_req_timeout_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-req-timeout-count", rest_name="echo-req-timeout-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_echo_resp_sent_count(self):
    """
    Getter method for echo_resp_sent_count, mapped from YANG variable /mpls_state/statistics_oam/echo_resp_sent_count (uint32)

    YANG Description: Count of MPLS Echo responses sent
    """
    return self.__echo_resp_sent_count
      
  def _set_echo_resp_sent_count(self, v, load=False):
    """
    Setter method for echo_resp_sent_count, mapped from YANG variable /mpls_state/statistics_oam/echo_resp_sent_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_echo_resp_sent_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_echo_resp_sent_count() directly.

    YANG Description: Count of MPLS Echo responses sent
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-resp-sent-count", rest_name="echo-resp-sent-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """echo_resp_sent_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-resp-sent-count", rest_name="echo-resp-sent-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__echo_resp_sent_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_echo_resp_sent_count(self):
    self.__echo_resp_sent_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-resp-sent-count", rest_name="echo-resp-sent-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_echo_resp_received_count(self):
    """
    Getter method for echo_resp_received_count, mapped from YANG variable /mpls_state/statistics_oam/echo_resp_received_count (uint32)

    YANG Description: Count of MPLS Echo responses received
    """
    return self.__echo_resp_received_count
      
  def _set_echo_resp_received_count(self, v, load=False):
    """
    Setter method for echo_resp_received_count, mapped from YANG variable /mpls_state/statistics_oam/echo_resp_received_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_echo_resp_received_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_echo_resp_received_count() directly.

    YANG Description: Count of MPLS Echo responses received
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-resp-received-count", rest_name="echo-resp-received-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """echo_resp_received_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-resp-received-count", rest_name="echo-resp-received-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__echo_resp_received_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_echo_resp_received_count(self):
    self.__echo_resp_received_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="echo-resp-received-count", rest_name="echo-resp-received-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_return_codes(self):
    """
    Getter method for return_codes, mapped from YANG variable /mpls_state/statistics_oam/return_codes (list)

    YANG Description: OAM packet statistics return code
    """
    return self.__return_codes
      
  def _set_return_codes(self, v, load=False):
    """
    Setter method for return_codes, mapped from YANG variable /mpls_state/statistics_oam/return_codes (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_return_codes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_return_codes() directly.

    YANG Description: OAM packet statistics return code
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("number",return_codes.return_codes, yang_name="return-codes", rest_name="return-codes", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='number', extensions=None), is_container='list', yang_name="return-codes", rest_name="return-codes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """return_codes must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("number",return_codes.return_codes, yang_name="return-codes", rest_name="return-codes", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='number', extensions=None), is_container='list', yang_name="return-codes", rest_name="return-codes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__return_codes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_return_codes(self):
    self.__return_codes = YANGDynClass(base=YANGListType("number",return_codes.return_codes, yang_name="return-codes", rest_name="return-codes", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='number', extensions=None), is_container='list', yang_name="return-codes", rest_name="return-codes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  usr_ping_count = __builtin__.property(_get_usr_ping_count)
  usr_traceroute_count = __builtin__.property(_get_usr_traceroute_count)
  echo_req_sent_count = __builtin__.property(_get_echo_req_sent_count)
  echo_req_received_count = __builtin__.property(_get_echo_req_received_count)
  echo_req_timeout_count = __builtin__.property(_get_echo_req_timeout_count)
  echo_resp_sent_count = __builtin__.property(_get_echo_resp_sent_count)
  echo_resp_received_count = __builtin__.property(_get_echo_resp_received_count)
  return_codes = __builtin__.property(_get_return_codes)


  _pyangbind_elements = {'usr_ping_count': usr_ping_count, 'usr_traceroute_count': usr_traceroute_count, 'echo_req_sent_count': echo_req_sent_count, 'echo_req_received_count': echo_req_received_count, 'echo_req_timeout_count': echo_req_timeout_count, 'echo_resp_sent_count': echo_resp_sent_count, 'echo_resp_received_count': echo_resp_received_count, 'return_codes': return_codes, }


