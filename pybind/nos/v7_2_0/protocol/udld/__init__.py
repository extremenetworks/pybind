
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class udld(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol/udld. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: UDLD protocol configuration. UDLD protocol will be
enabled when '/protocol/udld' container is created. To
disable delete it or set '/protocol/udld/shutdown'
leaf
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__hello','__multiplier','__shutdown',)

  _yang_name = 'udld'
  _rest_name = 'udld'

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
    self.__hello = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..60']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(5), is_leaf=True, yang_name="hello", rest_name="hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='uint32', is_config=True)
    self.__shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='empty', is_config=True)
    self.__multiplier = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(5), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='uint32', is_config=True)

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
      return [u'protocol', u'udld']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'udld']

  def _get_hello(self):
    """
    Getter method for hello, mapped from YANG variable /protocol/udld/hello (uint32)

    YANG Description: Hello interval is the time period between
successive PDU transmissions. UDLD protocol also
expects to receive PDUs from the peer at the same
rate.
Hello interval is measured in deciseconds (100 
milliseconds). Default hello interval is 5.

    """
    return self.__hello
      
  def _set_hello(self, v, load=False):
    """
    Setter method for hello, mapped from YANG variable /protocol/udld/hello (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello() directly.

    YANG Description: Hello interval is the time period between
successive PDU transmissions. UDLD protocol also
expects to receive PDUs from the peer at the same
rate.
Hello interval is measured in deciseconds (100 
milliseconds). Default hello interval is 5.

    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..60']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(5), is_leaf=True, yang_name="hello", rest_name="hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..60']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(5), is_leaf=True, yang_name="hello", rest_name="hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='uint32', is_config=True)""",
        })

    self.__hello = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello(self):
    self.__hello = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..60']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(5), is_leaf=True, yang_name="hello", rest_name="hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='uint32', is_config=True)


  def _get_multiplier(self):
    """
    Getter method for multiplier, mapped from YANG variable /protocol/udld/multiplier (uint32)

    YANG Description: Multiplier configures UDLD protocol timeout, which
is the product of multiplier and hello interval. If
no UDLD PDU is received over a link during timeout
period, the link is deemed unidirectional.
Default multiplier value is 5.

    """
    return self.__multiplier
      
  def _set_multiplier(self, v, load=False):
    """
    Setter method for multiplier, mapped from YANG variable /protocol/udld/multiplier (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multiplier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multiplier() directly.

    YANG Description: Multiplier configures UDLD protocol timeout, which
is the product of multiplier and hello interval. If
no UDLD PDU is received over a link during timeout
period, the link is deemed unidirectional.
Default multiplier value is 5.

    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(5), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multiplier must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(5), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='uint32', is_config=True)""",
        })

    self.__multiplier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multiplier(self):
    self.__multiplier = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(5), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='uint32', is_config=True)


  def _get_shutdown(self):
    """
    Getter method for shutdown, mapped from YANG variable /protocol/udld/shutdown (empty)

    YANG Description: When present indicates that UDLD protocol is
disabled on this switch. Disabling UDLD protocol
will not clear other configurations.
    """
    return self.__shutdown
      
  def _set_shutdown(self, v, load=False):
    """
    Setter method for shutdown, mapped from YANG variable /protocol/udld/shutdown (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shutdown is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shutdown() directly.

    YANG Description: When present indicates that UDLD protocol is
disabled on this switch. Disabling UDLD protocol
will not clear other configurations.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shutdown must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='empty', is_config=True)""",
        })

    self.__shutdown = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shutdown(self):
    self.__shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='empty', is_config=True)

  hello = __builtin__.property(_get_hello, _set_hello)
  multiplier = __builtin__.property(_get_multiplier, _set_multiplier)
  shutdown = __builtin__.property(_get_shutdown, _set_shutdown)


  _pyangbind_elements = {'hello': hello, 'multiplier': multiplier, 'shutdown': shutdown, }


