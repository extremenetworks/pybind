
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import source_interface
class client(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sec-services - based on the path /ssh-sa/ssh/client. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cipher','__mac','__key_exchange','__source_interface',)

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
    self.__key_exchange = YANGDynClass(base=unicode, is_leaf=True, yang_name="key-exchange", rest_name="key-exchange", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)
    self.__mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)
    self.__cipher = YANGDynClass(base=unicode, is_leaf=True, yang_name="cipher", rest_name="cipher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)
    self.__source_interface = YANGDynClass(base=source_interface.source_interface, is_container='container', presence=False, yang_name="source-interface", rest_name="source-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)

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
      return [u'ssh-sa', u'ssh', u'client']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ssh-sa', u'ssh', u'client']

  def _get_cipher(self):
    """
    Getter method for cipher, mapped from YANG variable /ssh_sa/ssh/client/cipher (string)
    """
    return self.__cipher
      
  def _set_cipher(self, v, load=False):
    """
    Setter method for cipher, mapped from YANG variable /ssh_sa/ssh/client/cipher (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cipher is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cipher() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="cipher", rest_name="cipher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cipher must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="cipher", rest_name="cipher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)""",
        })

    self.__cipher = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cipher(self):
    self.__cipher = YANGDynClass(base=unicode, is_leaf=True, yang_name="cipher", rest_name="cipher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)


  def _get_mac(self):
    """
    Getter method for mac, mapped from YANG variable /ssh_sa/ssh/client/mac (string)
    """
    return self.__mac
      
  def _set_mac(self, v, load=False):
    """
    Setter method for mac, mapped from YANG variable /ssh_sa/ssh/client/mac (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)""",
        })

    self.__mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac(self):
    self.__mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)


  def _get_key_exchange(self):
    """
    Getter method for key_exchange, mapped from YANG variable /ssh_sa/ssh/client/key_exchange (string)
    """
    return self.__key_exchange
      
  def _set_key_exchange(self, v, load=False):
    """
    Setter method for key_exchange, mapped from YANG variable /ssh_sa/ssh/client/key_exchange (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_exchange is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_exchange() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="key-exchange", rest_name="key-exchange", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_exchange must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="key-exchange", rest_name="key-exchange", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)""",
        })

    self.__key_exchange = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_exchange(self):
    self.__key_exchange = YANGDynClass(base=unicode, is_leaf=True, yang_name="key-exchange", rest_name="key-exchange", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)


  def _get_source_interface(self):
    """
    Getter method for source_interface, mapped from YANG variable /ssh_sa/ssh/client/source_interface (container)
    """
    return self.__source_interface
      
  def _set_source_interface(self, v, load=False):
    """
    Setter method for source_interface, mapped from YANG variable /ssh_sa/ssh/client/source_interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=source_interface.source_interface, is_container='container', presence=False, yang_name="source-interface", rest_name="source-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=source_interface.source_interface, is_container='container', presence=False, yang_name="source-interface", rest_name="source-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)""",
        })

    self.__source_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_interface(self):
    self.__source_interface = YANGDynClass(base=source_interface.source_interface, is_container='container', presence=False, yang_name="source-interface", rest_name="source-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)

  cipher = __builtin__.property(_get_cipher, _set_cipher)
  mac = __builtin__.property(_get_mac, _set_mac)
  key_exchange = __builtin__.property(_get_key_exchange, _set_key_exchange)
  source_interface = __builtin__.property(_get_source_interface, _set_source_interface)


  _pyangbind_elements = {'cipher': cipher, 'mac': mac, 'key_exchange': key_exchange, 'source_interface': source_interface, }


