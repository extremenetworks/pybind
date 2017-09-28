
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class packet_encap_info_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-nsm-operational - based on the path /packet-encap-processing-state/packet-encap-info-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Packet Encapsulation Processing Information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__port_name','__link_status','__encap_type','__strip_status',)

  _yang_name = 'packet-encap-info-list'
  _rest_name = 'packet-encap-info-list'

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
    self.__encap_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="encap-type", rest_name="encap-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    self.__strip_status = YANGDynClass(base=unicode, is_leaf=True, yang_name="strip-status", rest_name="strip-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    self.__port_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="port-name", rest_name="port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    self.__link_status = YANGDynClass(base=unicode, is_leaf=True, yang_name="link-status", rest_name="link-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)

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
      return [u'packet-encap-processing-state', u'packet-encap-info-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'packet-encap-processing-state', u'packet-encap-info-list']

  def _get_port_name(self):
    """
    Getter method for port_name, mapped from YANG variable /packet_encap_processing_state/packet_encap_info_list/port_name (string)

    YANG Description: Port name
    """
    return self.__port_name
      
  def _set_port_name(self, v, load=False):
    """
    Setter method for port_name, mapped from YANG variable /packet_encap_processing_state/packet_encap_info_list/port_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_name() directly.

    YANG Description: Port name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="port-name", rest_name="port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="port-name", rest_name="port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__port_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_name(self):
    self.__port_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="port-name", rest_name="port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)


  def _get_link_status(self):
    """
    Getter method for link_status, mapped from YANG variable /packet_encap_processing_state/packet_encap_info_list/link_status (string)

    YANG Description: Link Status
    """
    return self.__link_status
      
  def _set_link_status(self, v, load=False):
    """
    Setter method for link_status, mapped from YANG variable /packet_encap_processing_state/packet_encap_info_list/link_status (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_status() directly.

    YANG Description: Link Status
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="link-status", rest_name="link-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_status must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="link-status", rest_name="link-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__link_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_status(self):
    self.__link_status = YANGDynClass(base=unicode, is_leaf=True, yang_name="link-status", rest_name="link-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)


  def _get_encap_type(self):
    """
    Getter method for encap_type, mapped from YANG variable /packet_encap_processing_state/packet_encap_info_list/encap_type (string)

    YANG Description: Encap Type
    """
    return self.__encap_type
      
  def _set_encap_type(self, v, load=False):
    """
    Setter method for encap_type, mapped from YANG variable /packet_encap_processing_state/packet_encap_info_list/encap_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encap_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encap_type() directly.

    YANG Description: Encap Type
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="encap-type", rest_name="encap-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encap_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="encap-type", rest_name="encap-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__encap_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encap_type(self):
    self.__encap_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="encap-type", rest_name="encap-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)


  def _get_strip_status(self):
    """
    Getter method for strip_status, mapped from YANG variable /packet_encap_processing_state/packet_encap_info_list/strip_status (string)

    YANG Description: Feature Status
    """
    return self.__strip_status
      
  def _set_strip_status(self, v, load=False):
    """
    Setter method for strip_status, mapped from YANG variable /packet_encap_processing_state/packet_encap_info_list/strip_status (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_strip_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_strip_status() directly.

    YANG Description: Feature Status
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="strip-status", rest_name="strip-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """strip_status must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="strip-status", rest_name="strip-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__strip_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_strip_status(self):
    self.__strip_status = YANGDynClass(base=unicode, is_leaf=True, yang_name="strip-status", rest_name="strip-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)

  port_name = __builtin__.property(_get_port_name)
  link_status = __builtin__.property(_get_link_status)
  encap_type = __builtin__.property(_get_encap_type)
  strip_status = __builtin__.property(_get_strip_status)


  _pyangbind_elements = {'port_name': port_name, 'link_status': link_status, 'encap_type': encap_type, 'strip_status': strip_status, }


