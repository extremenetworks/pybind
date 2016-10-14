
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class global_mtu_conf(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /global-mtu-conf. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__global_l2_mtu',)

  _yang_name = 'global-mtu-conf'

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
    self.__global_l2_mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1522..9216']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2500), is_leaf=True, yang_name="global-l2-mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set L2 mtu value to all interfaces of this cluster', u'alt-name': u'mtu'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='mtu-type', is_config=True)

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
      return [u'global-mtu-conf']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return []

  def _get_global_l2_mtu(self):
    """
    Getter method for global_l2_mtu, mapped from YANG variable /global_mtu_conf/global_l2_mtu (mtu-type)

    YANG Description: The size of the largest packet which can be sent/
received on the interface, specified in bytes.
For interfaces that are used for transmitting network
datagrams, this is the size of the largest network
datagram that can be sent on the interface.
    """
    return self.__global_l2_mtu
      
  def _set_global_l2_mtu(self, v, load=False):
    """
    Setter method for global_l2_mtu, mapped from YANG variable /global_mtu_conf/global_l2_mtu (mtu-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_l2_mtu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_l2_mtu() directly.

    YANG Description: The size of the largest packet which can be sent/
received on the interface, specified in bytes.
For interfaces that are used for transmitting network
datagrams, this is the size of the largest network
datagram that can be sent on the interface.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1522..9216']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2500), is_leaf=True, yang_name="global-l2-mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set L2 mtu value to all interfaces of this cluster', u'alt-name': u'mtu'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='mtu-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_l2_mtu must be of a type compatible with mtu-type""",
          'defined-type': "brocade-interface:mtu-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1522..9216']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2500), is_leaf=True, yang_name="global-l2-mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set L2 mtu value to all interfaces of this cluster', u'alt-name': u'mtu'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='mtu-type', is_config=True)""",
        })

    self.__global_l2_mtu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_l2_mtu(self):
    self.__global_l2_mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1522..9216']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2500), is_leaf=True, yang_name="global-l2-mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set L2 mtu value to all interfaces of this cluster', u'alt-name': u'mtu'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='mtu-type', is_config=True)

  global_l2_mtu = __builtin__.property(_get_global_l2_mtu, _set_global_l2_mtu)


  _pyangbind_elements = {'global_l2_mtu': global_l2_mtu, }


