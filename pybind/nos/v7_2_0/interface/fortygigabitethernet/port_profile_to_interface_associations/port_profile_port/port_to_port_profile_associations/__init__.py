
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class port_to_port_profile_associations(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/port-profile-to-interface-associations/port-profile-port/port-to-port-profile-associations. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The list of automatic port profiles. Each row
provides the name of the port profile associated 
with an interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__port_to_port_profile_association',)

  _yang_name = 'port-to-port-profile-associations'
  _rest_name = 'profile'

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
    self.__port_to_port_profile_association = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,127})'}), is_leaf=True, yang_name="port-to-port-profile-association", rest_name="port-to-port-profile-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='port-profile-name-type', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'port-profile-to-interface-associations', u'port-profile-port', u'port-to-port-profile-associations']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'port-profile-port', u'profile']

  def _get_port_to_port_profile_association(self):
    """
    Getter method for port_to_port_profile_association, mapped from YANG variable /interface/fortygigabitethernet/port_profile_to_interface_associations/port_profile_port/port_to_port_profile_associations/port_to_port_profile_association (port-profile-name-type)

    YANG Description: The name of the port-profile.
    """
    return self.__port_to_port_profile_association
      
  def _set_port_to_port_profile_association(self, v, load=False):
    """
    Setter method for port_to_port_profile_association, mapped from YANG variable /interface/fortygigabitethernet/port_profile_to_interface_associations/port_profile_port/port_to_port_profile_associations/port_to_port_profile_association (port-profile-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_to_port_profile_association is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_to_port_profile_association() directly.

    YANG Description: The name of the port-profile.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,127})'}), is_leaf=True, yang_name="port-to-port-profile-association", rest_name="port-to-port-profile-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='port-profile-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_to_port_profile_association must be of a type compatible with port-profile-name-type""",
          'defined-type': "brocade-port-profile:port-profile-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,127})'}), is_leaf=True, yang_name="port-to-port-profile-association", rest_name="port-to-port-profile-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='port-profile-name-type', is_config=True)""",
        })

    self.__port_to_port_profile_association = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_to_port_profile_association(self):
    self.__port_to_port_profile_association = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,127})'}), is_leaf=True, yang_name="port-to-port-profile-association", rest_name="port-to-port-profile-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='port-profile-name-type', is_config=True)

  port_to_port_profile_association = __builtin__.property(_get_port_to_port_profile_association, _set_port_to_port_profile_association)


  _pyangbind_elements = {'port_to_port_profile_association': port_to_port_profile_association, }


