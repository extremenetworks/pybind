
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class layer2(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-opstest - based on the path /opstest-state/routes/route/children/layer2. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__layer2id','__parentkeyid','__grandparentKey','__attr3','__attr4',)

  _yang_name = 'layer2'
  _rest_name = 'layer2'

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
    self.__layer2id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="layer2id", rest_name="layer2id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    self.__grandparentKey = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="grandparentKey", rest_name="grandparentKey", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='inet:ipv4-address', is_config=False)
    self.__attr4 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="attr4", rest_name="attr4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    self.__parentkeyid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="parentkeyid", rest_name="parentkeyid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    self.__attr3 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="attr3", rest_name="attr3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)

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
      return [u'opstest-state', u'routes', u'route', u'children', u'layer2']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'opstest-state', u'routes', u'route', u'children', u'layer2']

  def _get_layer2id(self):
    """
    Getter method for layer2id, mapped from YANG variable /opstest_state/routes/route/children/layer2/layer2id (uint32)
    """
    return self.__layer2id
      
  def _set_layer2id(self, v, load=False):
    """
    Setter method for layer2id, mapped from YANG variable /opstest_state/routes/route/children/layer2/layer2id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_layer2id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_layer2id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="layer2id", rest_name="layer2id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """layer2id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="layer2id", rest_name="layer2id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)""",
        })

    self.__layer2id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_layer2id(self):
    self.__layer2id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="layer2id", rest_name="layer2id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)


  def _get_parentkeyid(self):
    """
    Getter method for parentkeyid, mapped from YANG variable /opstest_state/routes/route/children/layer2/parentkeyid (uint32)
    """
    return self.__parentkeyid
      
  def _set_parentkeyid(self, v, load=False):
    """
    Setter method for parentkeyid, mapped from YANG variable /opstest_state/routes/route/children/layer2/parentkeyid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_parentkeyid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_parentkeyid() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="parentkeyid", rest_name="parentkeyid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """parentkeyid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="parentkeyid", rest_name="parentkeyid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)""",
        })

    self.__parentkeyid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_parentkeyid(self):
    self.__parentkeyid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="parentkeyid", rest_name="parentkeyid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)


  def _get_grandparentKey(self):
    """
    Getter method for grandparentKey, mapped from YANG variable /opstest_state/routes/route/children/layer2/grandparentKey (inet:ipv4-address)
    """
    return self.__grandparentKey
      
  def _set_grandparentKey(self, v, load=False):
    """
    Setter method for grandparentKey, mapped from YANG variable /opstest_state/routes/route/children/layer2/grandparentKey (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_grandparentKey is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_grandparentKey() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="grandparentKey", rest_name="grandparentKey", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """grandparentKey must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="grandparentKey", rest_name="grandparentKey", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__grandparentKey = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_grandparentKey(self):
    self.__grandparentKey = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="grandparentKey", rest_name="grandparentKey", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='inet:ipv4-address', is_config=False)


  def _get_attr3(self):
    """
    Getter method for attr3, mapped from YANG variable /opstest_state/routes/route/children/layer2/attr3 (uint32)
    """
    return self.__attr3
      
  def _set_attr3(self, v, load=False):
    """
    Setter method for attr3, mapped from YANG variable /opstest_state/routes/route/children/layer2/attr3 (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attr3 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attr3() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="attr3", rest_name="attr3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attr3 must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="attr3", rest_name="attr3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)""",
        })

    self.__attr3 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attr3(self):
    self.__attr3 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="attr3", rest_name="attr3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)


  def _get_attr4(self):
    """
    Getter method for attr4, mapped from YANG variable /opstest_state/routes/route/children/layer2/attr4 (uint32)
    """
    return self.__attr4
      
  def _set_attr4(self, v, load=False):
    """
    Setter method for attr4, mapped from YANG variable /opstest_state/routes/route/children/layer2/attr4 (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attr4 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attr4() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="attr4", rest_name="attr4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attr4 must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="attr4", rest_name="attr4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)""",
        })

    self.__attr4 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attr4(self):
    self.__attr4 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="attr4", rest_name="attr4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)

  layer2id = __builtin__.property(_get_layer2id)
  parentkeyid = __builtin__.property(_get_parentkeyid)
  grandparentKey = __builtin__.property(_get_grandparentKey)
  attr3 = __builtin__.property(_get_attr3)
  attr4 = __builtin__.property(_get_attr4)


  _pyangbind_elements = {'layer2id': layer2id, 'parentkeyid': parentkeyid, 'grandparentKey': grandparentKey, 'attr3': attr3, 'attr4': attr4, }

