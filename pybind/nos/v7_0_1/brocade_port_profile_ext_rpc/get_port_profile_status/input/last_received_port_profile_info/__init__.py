
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class last_received_port_profile_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile-ext - based on the path /brocade_port_profile_ext_rpc/get-port-profile-status/input/last-received-port-profile-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: get request : 
provides data only for a given
port profile based on the input attribute 
port-profile-name.

To begin with, user should provide 
port-profile-name attribute and optional
profile-mac value as 00:00:00:00:00:00.
The response will contain the initial set of
macs associated with the given port profile.

For subsequent calls, user should provide 
port-profile-name along with the 
profile-mac value.
Response will contain the next set of
associated macs for the given port profile.

Response has an attribute is-more, which
will be false, when all the macs associated
with a given port-profile are exhausted.

getnext request : 
To get the next record,
provide both profile-name and profile-mac.

To begin with, user can invoke the rpc 
without providing profile-name and profile-mac
attributes.
The response will contain the initial set of 
macs associated with the first port profile.

For subsequent calls, user should provide 
profile-name along with the profile-mac.

If the user provides profile-name and last 
profile mac associated with the profile, 
the response will contain the next port profile
info.

Response has an attribute is-more, which will
be false, when all the macs associated with all
the port-profiles are exhausted.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__profile_name','__profile_mac',)

  _yang_name = 'last-received-port-profile-info'

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
    self.__profile_mac = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="profile-mac", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='inet:mac-address', is_config=True)
    self.__profile_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="profile-name", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='common-def:name-string64', is_config=True)

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
      return [u'brocade_port_profile_ext_rpc', u'get-port-profile-status', u'input', u'last-received-port-profile-info']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'get-port-profile-status', u'input', u'last-received-port-profile-info']

  def _get_profile_name(self):
    """
    Getter method for profile_name, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status/input/last_received_port_profile_info/profile_name (common-def:name-string64)

    YANG Description: This indicates the name of the last
received port-profile.
    """
    return self.__profile_name
      
  def _set_profile_name(self, v, load=False):
    """
    Setter method for profile_name, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status/input/last_received_port_profile_info/profile_name (common-def:name-string64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_profile_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_profile_name() directly.

    YANG Description: This indicates the name of the last
received port-profile.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="profile-name", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='common-def:name-string64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """profile_name must be of a type compatible with common-def:name-string64""",
          'defined-type': "common-def:name-string64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="profile-name", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='common-def:name-string64', is_config=True)""",
        })

    self.__profile_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_profile_name(self):
    self.__profile_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="profile-name", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='common-def:name-string64', is_config=True)


  def _get_profile_mac(self):
    """
    Getter method for profile_mac, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status/input/last_received_port_profile_info/profile_mac (inet:mac-address)

    YANG Description: This indicates the last received mac
address of the last received port-profile.
    """
    return self.__profile_mac
      
  def _set_profile_mac(self, v, load=False):
    """
    Setter method for profile_mac, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status/input/last_received_port_profile_info/profile_mac (inet:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_profile_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_profile_mac() directly.

    YANG Description: This indicates the last received mac
address of the last received port-profile.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="profile-mac", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='inet:mac-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """profile_mac must be of a type compatible with inet:mac-address""",
          'defined-type': "inet:mac-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="profile-mac", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='inet:mac-address', is_config=True)""",
        })

    self.__profile_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_profile_mac(self):
    self.__profile_mac = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="profile-mac", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='inet:mac-address', is_config=True)

  profile_name = __builtin__.property(_get_profile_name, _set_profile_name)
  profile_mac = __builtin__.property(_get_profile_mac, _set_profile_mac)

  __choices__ = {u'request-type': {u'getnext-request': [u'profile_name', u'profile_mac']}}
  _pyangbind_elements = {'profile_name': profile_name, 'profile_mac': profile_mac, }


