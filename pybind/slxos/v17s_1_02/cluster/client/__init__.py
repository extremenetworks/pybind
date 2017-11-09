
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import client_interface
import esi
class client(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mct - based on the path /cluster/client. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__client_name','__client_id','__client_interface','__esi','__client_deploy',)

  _yang_name = 'client'
  _rest_name = 'client'

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
    self.__client_interface = YANGDynClass(base=client_interface.client_interface, is_container='container', presence=False, yang_name="client-interface", rest_name="client-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='container', is_config=True)
    self.__client_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="client-name", rest_name="client-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='string', is_config=True)
    self.__client_deploy = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="client-deploy", rest_name="client-deploy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)
    self.__esi = YANGDynClass(base=esi.esi, is_container='container', presence=False, yang_name="esi", rest_name="esi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='container', is_config=True)
    self.__client_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='uint32', is_config=True)

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
      return [u'cluster', u'client']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cluster', u'client']

  def _get_client_name(self):
    """
    Getter method for client_name, mapped from YANG variable /cluster/client/client_name (string)
    """
    return self.__client_name
      
  def _set_client_name(self, v, load=False):
    """
    Setter method for client_name, mapped from YANG variable /cluster/client/client_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="client-name", rest_name="client-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="client-name", rest_name="client-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='string', is_config=True)""",
        })

    self.__client_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_name(self):
    self.__client_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="client-name", rest_name="client-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='string', is_config=True)


  def _get_client_id(self):
    """
    Getter method for client_id, mapped from YANG variable /cluster/client/client_id (uint32)
    """
    return self.__client_id
      
  def _set_client_id(self, v, load=False):
    """
    Setter method for client_id, mapped from YANG variable /cluster/client/client_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='uint32', is_config=True)""",
        })

    self.__client_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_id(self):
    self.__client_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='uint32', is_config=True)


  def _get_client_interface(self):
    """
    Getter method for client_interface, mapped from YANG variable /cluster/client/client_interface (container)
    """
    return self.__client_interface
      
  def _set_client_interface(self, v, load=False):
    """
    Setter method for client_interface, mapped from YANG variable /cluster/client/client_interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=client_interface.client_interface, is_container='container', presence=False, yang_name="client-interface", rest_name="client-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=client_interface.client_interface, is_container='container', presence=False, yang_name="client-interface", rest_name="client-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='container', is_config=True)""",
        })

    self.__client_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_interface(self):
    self.__client_interface = YANGDynClass(base=client_interface.client_interface, is_container='container', presence=False, yang_name="client-interface", rest_name="client-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='container', is_config=True)


  def _get_esi(self):
    """
    Getter method for esi, mapped from YANG variable /cluster/client/esi (container)

    YANG Description: Ethernet Segment Id
    """
    return self.__esi
      
  def _set_esi(self, v, load=False):
    """
    Setter method for esi, mapped from YANG variable /cluster/client/esi (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_esi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_esi() directly.

    YANG Description: Ethernet Segment Id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=esi.esi, is_container='container', presence=False, yang_name="esi", rest_name="esi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """esi must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=esi.esi, is_container='container', presence=False, yang_name="esi", rest_name="esi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='container', is_config=True)""",
        })

    self.__esi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_esi(self):
    self.__esi = YANGDynClass(base=esi.esi, is_container='container', presence=False, yang_name="esi", rest_name="esi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='container', is_config=True)


  def _get_client_deploy(self):
    """
    Getter method for client_deploy, mapped from YANG variable /cluster/client/client_deploy (empty)
    """
    return self.__client_deploy
      
  def _set_client_deploy(self, v, load=False):
    """
    Setter method for client_deploy, mapped from YANG variable /cluster/client/client_deploy (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_deploy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_deploy() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="client-deploy", rest_name="client-deploy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_deploy must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="client-deploy", rest_name="client-deploy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)""",
        })

    self.__client_deploy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_deploy(self):
    self.__client_deploy = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="client-deploy", rest_name="client-deploy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)

  client_name = __builtin__.property(_get_client_name, _set_client_name)
  client_id = __builtin__.property(_get_client_id, _set_client_id)
  client_interface = __builtin__.property(_get_client_interface, _set_client_interface)
  esi = __builtin__.property(_get_esi, _set_esi)
  client_deploy = __builtin__.property(_get_client_deploy, _set_client_deploy)


  _pyangbind_elements = {'client_name': client_name, 'client_id': client_id, 'client_interface': client_interface, 'esi': esi, 'client_deploy': client_deploy, }


