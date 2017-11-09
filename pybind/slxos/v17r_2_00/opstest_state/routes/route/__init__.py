
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import children
class route(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-opstest - based on the path /opstest-state/routes/route. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__destPrefix','__entryMultipathIndex','__prefixLength','__gateway','__outInterfaceName','__outLabel','__protocol','__vifIndex','__metric','__useCount','__children',)

  _yang_name = 'route'
  _rest_name = 'route'

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
    self.__vifIndex = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vifIndex", rest_name="vifIndex", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    self.__protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='string', is_config=False)
    self.__entryMultipathIndex = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="entryMultipathIndex", rest_name="entryMultipathIndex", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    self.__destPrefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destPrefix", rest_name="destPrefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='inet:ipv4-address', is_config=False)
    self.__outInterfaceName = YANGDynClass(base=unicode, is_leaf=True, yang_name="outInterfaceName", rest_name="outInterfaceName", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='string', is_config=False)
    self.__outLabel = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="outLabel", rest_name="outLabel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    self.__children = YANGDynClass(base=YANGListType("keyid",children.children, yang_name="children", rest_name="children", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='keyid', extensions={u'tailf-common': {u'callpoint': u'MplstestRouteChildren'}}), is_container='list', yang_name="children", rest_name="children", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'MplstestRouteChildren'}}, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='list', is_config=False)
    self.__useCount = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="useCount", rest_name="useCount", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    self.__prefixLength = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="prefixLength", rest_name="prefixLength", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    self.__gateway = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway", rest_name="gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='inet:ipv4-address', is_config=False)
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)

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
      return [u'opstest-state', u'routes', u'route']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'opstest-state', u'routes', u'route']

  def _get_destPrefix(self):
    """
    Getter method for destPrefix, mapped from YANG variable /opstest_state/routes/route/destPrefix (inet:ipv4-address)
    """
    return self.__destPrefix
      
  def _set_destPrefix(self, v, load=False):
    """
    Setter method for destPrefix, mapped from YANG variable /opstest_state/routes/route/destPrefix (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destPrefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destPrefix() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destPrefix", rest_name="destPrefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destPrefix must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destPrefix", rest_name="destPrefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__destPrefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destPrefix(self):
    self.__destPrefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destPrefix", rest_name="destPrefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='inet:ipv4-address', is_config=False)


  def _get_entryMultipathIndex(self):
    """
    Getter method for entryMultipathIndex, mapped from YANG variable /opstest_state/routes/route/entryMultipathIndex (uint32)
    """
    return self.__entryMultipathIndex
      
  def _set_entryMultipathIndex(self, v, load=False):
    """
    Setter method for entryMultipathIndex, mapped from YANG variable /opstest_state/routes/route/entryMultipathIndex (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_entryMultipathIndex is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_entryMultipathIndex() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="entryMultipathIndex", rest_name="entryMultipathIndex", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """entryMultipathIndex must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="entryMultipathIndex", rest_name="entryMultipathIndex", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)""",
        })

    self.__entryMultipathIndex = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_entryMultipathIndex(self):
    self.__entryMultipathIndex = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="entryMultipathIndex", rest_name="entryMultipathIndex", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)


  def _get_prefixLength(self):
    """
    Getter method for prefixLength, mapped from YANG variable /opstest_state/routes/route/prefixLength (uint32)
    """
    return self.__prefixLength
      
  def _set_prefixLength(self, v, load=False):
    """
    Setter method for prefixLength, mapped from YANG variable /opstest_state/routes/route/prefixLength (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefixLength is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefixLength() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="prefixLength", rest_name="prefixLength", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefixLength must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="prefixLength", rest_name="prefixLength", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)""",
        })

    self.__prefixLength = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefixLength(self):
    self.__prefixLength = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="prefixLength", rest_name="prefixLength", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)


  def _get_gateway(self):
    """
    Getter method for gateway, mapped from YANG variable /opstest_state/routes/route/gateway (inet:ipv4-address)
    """
    return self.__gateway
      
  def _set_gateway(self, v, load=False):
    """
    Setter method for gateway, mapped from YANG variable /opstest_state/routes/route/gateway (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gateway is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gateway() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway", rest_name="gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gateway must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway", rest_name="gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__gateway = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gateway(self):
    self.__gateway = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway", rest_name="gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='inet:ipv4-address', is_config=False)


  def _get_outInterfaceName(self):
    """
    Getter method for outInterfaceName, mapped from YANG variable /opstest_state/routes/route/outInterfaceName (string)
    """
    return self.__outInterfaceName
      
  def _set_outInterfaceName(self, v, load=False):
    """
    Setter method for outInterfaceName, mapped from YANG variable /opstest_state/routes/route/outInterfaceName (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_outInterfaceName is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_outInterfaceName() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="outInterfaceName", rest_name="outInterfaceName", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """outInterfaceName must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="outInterfaceName", rest_name="outInterfaceName", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='string', is_config=False)""",
        })

    self.__outInterfaceName = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_outInterfaceName(self):
    self.__outInterfaceName = YANGDynClass(base=unicode, is_leaf=True, yang_name="outInterfaceName", rest_name="outInterfaceName", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='string', is_config=False)


  def _get_outLabel(self):
    """
    Getter method for outLabel, mapped from YANG variable /opstest_state/routes/route/outLabel (uint32)
    """
    return self.__outLabel
      
  def _set_outLabel(self, v, load=False):
    """
    Setter method for outLabel, mapped from YANG variable /opstest_state/routes/route/outLabel (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_outLabel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_outLabel() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="outLabel", rest_name="outLabel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """outLabel must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="outLabel", rest_name="outLabel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)""",
        })

    self.__outLabel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_outLabel(self):
    self.__outLabel = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="outLabel", rest_name="outLabel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)


  def _get_protocol(self):
    """
    Getter method for protocol, mapped from YANG variable /opstest_state/routes/route/protocol (string)
    """
    return self.__protocol
      
  def _set_protocol(self, v, load=False):
    """
    Setter method for protocol, mapped from YANG variable /opstest_state/routes/route/protocol (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='string', is_config=False)""",
        })

    self.__protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol(self):
    self.__protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='string', is_config=False)


  def _get_vifIndex(self):
    """
    Getter method for vifIndex, mapped from YANG variable /opstest_state/routes/route/vifIndex (uint32)
    """
    return self.__vifIndex
      
  def _set_vifIndex(self, v, load=False):
    """
    Setter method for vifIndex, mapped from YANG variable /opstest_state/routes/route/vifIndex (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vifIndex is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vifIndex() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vifIndex", rest_name="vifIndex", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vifIndex must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vifIndex", rest_name="vifIndex", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)""",
        })

    self.__vifIndex = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vifIndex(self):
    self.__vifIndex = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vifIndex", rest_name="vifIndex", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)


  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /opstest_state/routes/route/metric (uint32)
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /opstest_state/routes/route/metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)


  def _get_useCount(self):
    """
    Getter method for useCount, mapped from YANG variable /opstest_state/routes/route/useCount (uint32)
    """
    return self.__useCount
      
  def _set_useCount(self, v, load=False):
    """
    Setter method for useCount, mapped from YANG variable /opstest_state/routes/route/useCount (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_useCount is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_useCount() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="useCount", rest_name="useCount", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """useCount must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="useCount", rest_name="useCount", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)""",
        })

    self.__useCount = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_useCount(self):
    self.__useCount = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="useCount", rest_name="useCount", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='uint32', is_config=False)


  def _get_children(self):
    """
    Getter method for children, mapped from YANG variable /opstest_state/routes/route/children (list)
    """
    return self.__children
      
  def _set_children(self, v, load=False):
    """
    Setter method for children, mapped from YANG variable /opstest_state/routes/route/children (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_children is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_children() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("keyid",children.children, yang_name="children", rest_name="children", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='keyid', extensions={u'tailf-common': {u'callpoint': u'MplstestRouteChildren'}}), is_container='list', yang_name="children", rest_name="children", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'MplstestRouteChildren'}}, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """children must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("keyid",children.children, yang_name="children", rest_name="children", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='keyid', extensions={u'tailf-common': {u'callpoint': u'MplstestRouteChildren'}}), is_container='list', yang_name="children", rest_name="children", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'MplstestRouteChildren'}}, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='list', is_config=False)""",
        })

    self.__children = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_children(self):
    self.__children = YANGDynClass(base=YANGListType("keyid",children.children, yang_name="children", rest_name="children", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='keyid', extensions={u'tailf-common': {u'callpoint': u'MplstestRouteChildren'}}), is_container='list', yang_name="children", rest_name="children", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'MplstestRouteChildren'}}, namespace='urn:brocade.com:mgmt:brocade-opstest', defining_module='brocade-opstest', yang_type='list', is_config=False)

  destPrefix = __builtin__.property(_get_destPrefix)
  entryMultipathIndex = __builtin__.property(_get_entryMultipathIndex)
  prefixLength = __builtin__.property(_get_prefixLength)
  gateway = __builtin__.property(_get_gateway)
  outInterfaceName = __builtin__.property(_get_outInterfaceName)
  outLabel = __builtin__.property(_get_outLabel)
  protocol = __builtin__.property(_get_protocol)
  vifIndex = __builtin__.property(_get_vifIndex)
  metric = __builtin__.property(_get_metric)
  useCount = __builtin__.property(_get_useCount)
  children = __builtin__.property(_get_children)


  _pyangbind_elements = {'destPrefix': destPrefix, 'entryMultipathIndex': entryMultipathIndex, 'prefixLength': prefixLength, 'gateway': gateway, 'outInterfaceName': outInterfaceName, 'outLabel': outLabel, 'protocol': protocol, 'vifIndex': vifIndex, 'metric': metric, 'useCount': useCount, 'children': children, }


