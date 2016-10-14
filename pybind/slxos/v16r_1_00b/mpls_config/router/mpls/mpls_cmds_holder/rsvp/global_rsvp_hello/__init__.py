
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class global_rsvp_hello(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/rsvp/global-rsvp-hello. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__global_rsvp_hello_interval','__global_rsvp_hello_tolerance',)

  _yang_name = 'global-rsvp-hello'

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
    self.__global_rsvp_hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..60']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(9), is_leaf=True, yang_name="global-rsvp-hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interval between two RSVP Hello requests', u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__global_rsvp_hello_tolerance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="global-rsvp-hello-tolerance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of unacknowledged RSVP Hello requests before timeout', u'alt-name': u'tolerance'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'rsvp', u'global-rsvp-hello']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'router', u'mpls', u'rsvp', u'hello']

  def _get_global_rsvp_hello_interval(self):
    """
    Getter method for global_rsvp_hello_interval, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/global_rsvp_hello/global_rsvp_hello_interval (uint32)
    """
    return self.__global_rsvp_hello_interval
      
  def _set_global_rsvp_hello_interval(self, v, load=False):
    """
    Setter method for global_rsvp_hello_interval, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/global_rsvp_hello/global_rsvp_hello_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_rsvp_hello_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_rsvp_hello_interval() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..60']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(9), is_leaf=True, yang_name="global-rsvp-hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interval between two RSVP Hello requests', u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_rsvp_hello_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..60']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(9), is_leaf=True, yang_name="global-rsvp-hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interval between two RSVP Hello requests', u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__global_rsvp_hello_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_rsvp_hello_interval(self):
    self.__global_rsvp_hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..60']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(9), is_leaf=True, yang_name="global-rsvp-hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interval between two RSVP Hello requests', u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_global_rsvp_hello_tolerance(self):
    """
    Getter method for global_rsvp_hello_tolerance, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/global_rsvp_hello/global_rsvp_hello_tolerance (uint32)
    """
    return self.__global_rsvp_hello_tolerance
      
  def _set_global_rsvp_hello_tolerance(self, v, load=False):
    """
    Setter method for global_rsvp_hello_tolerance, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/global_rsvp_hello/global_rsvp_hello_tolerance (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_rsvp_hello_tolerance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_rsvp_hello_tolerance() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="global-rsvp-hello-tolerance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of unacknowledged RSVP Hello requests before timeout', u'alt-name': u'tolerance'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_rsvp_hello_tolerance must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="global-rsvp-hello-tolerance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of unacknowledged RSVP Hello requests before timeout', u'alt-name': u'tolerance'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__global_rsvp_hello_tolerance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_rsvp_hello_tolerance(self):
    self.__global_rsvp_hello_tolerance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="global-rsvp-hello-tolerance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of unacknowledged RSVP Hello requests before timeout', u'alt-name': u'tolerance'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  global_rsvp_hello_interval = __builtin__.property(_get_global_rsvp_hello_interval, _set_global_rsvp_hello_interval)
  global_rsvp_hello_tolerance = __builtin__.property(_get_global_rsvp_hello_tolerance, _set_global_rsvp_hello_tolerance)


  _pyangbind_elements = {'global_rsvp_hello_interval': global_rsvp_hello_interval, 'global_rsvp_hello_tolerance': global_rsvp_hello_tolerance, }


