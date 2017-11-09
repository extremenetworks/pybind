
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ca(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/crypto/ca. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__trustpoint','__keypair',)

  _yang_name = 'ca'
  _rest_name = 'ca'

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
    self.__keypair = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..64']}), default=unicode(""), is_leaf=True, yang_name="keypair", rest_name="keypair", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='string', is_config=True)
    self.__trustpoint = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="trustpoint", rest_name="trustpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='string', is_config=True)

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
      return [u'rbridge-id', u'crypto', u'ca']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'crypto', u'ca']

  def _get_trustpoint(self):
    """
    Getter method for trustpoint, mapped from YANG variable /rbridge_id/crypto/ca/trustpoint (string)
    """
    return self.__trustpoint
      
  def _set_trustpoint(self, v, load=False):
    """
    Setter method for trustpoint, mapped from YANG variable /rbridge_id/crypto/ca/trustpoint (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trustpoint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trustpoint() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="trustpoint", rest_name="trustpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trustpoint must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="trustpoint", rest_name="trustpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='string', is_config=True)""",
        })

    self.__trustpoint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trustpoint(self):
    self.__trustpoint = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="trustpoint", rest_name="trustpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='string', is_config=True)


  def _get_keypair(self):
    """
    Getter method for keypair, mapped from YANG variable /rbridge_id/crypto/ca/keypair (string)
    """
    return self.__keypair
      
  def _set_keypair(self, v, load=False):
    """
    Setter method for keypair, mapped from YANG variable /rbridge_id/crypto/ca/keypair (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_keypair is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_keypair() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..64']}), default=unicode(""), is_leaf=True, yang_name="keypair", rest_name="keypair", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """keypair must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..64']}), default=unicode(""), is_leaf=True, yang_name="keypair", rest_name="keypair", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='string', is_config=True)""",
        })

    self.__keypair = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_keypair(self):
    self.__keypair = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..64']}), default=unicode(""), is_leaf=True, yang_name="keypair", rest_name="keypair", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='string', is_config=True)

  trustpoint = __builtin__.property(_get_trustpoint, _set_trustpoint)
  keypair = __builtin__.property(_get_keypair, _set_keypair)


  _pyangbind_elements = {'trustpoint': trustpoint, 'keypair': keypair, }


