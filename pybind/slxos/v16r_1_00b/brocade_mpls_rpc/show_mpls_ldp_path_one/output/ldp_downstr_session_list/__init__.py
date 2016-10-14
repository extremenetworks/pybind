
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ldp_downstr_session_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-ldp-path-one/output/ldp-downstr-session-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ldp_downstr_session_ip',)

  _yang_name = 'ldp-downstr-session-list'

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
    self.__ldp_downstr_session_ip = YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-downstr-session-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-ldp-path-one', u'output', u'ldp-downstr-session-list']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'show-mpls-ldp-path-one', u'output', u'ldp-downstr-session-list']

  def _get_ldp_downstr_session_ip(self):
    """
    Getter method for ldp_downstr_session_ip, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_path_one/output/ldp_downstr_session_list/ldp_downstr_session_ip (string)

    YANG Description: Downstr-session
    """
    return self.__ldp_downstr_session_ip
      
  def _set_ldp_downstr_session_ip(self, v, load=False):
    """
    Setter method for ldp_downstr_session_ip, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_path_one/output/ldp_downstr_session_list/ldp_downstr_session_ip (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_downstr_session_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_downstr_session_ip() directly.

    YANG Description: Downstr-session
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ldp-downstr-session-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_downstr_session_ip must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-downstr-session-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__ldp_downstr_session_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_downstr_session_ip(self):
    self.__ldp_downstr_session_ip = YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-downstr-session-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

  ldp_downstr_session_ip = __builtin__.property(_get_ldp_downstr_session_ip, _set_ldp_downstr_session_ip)


  _pyangbind_elements = {'ldp_downstr_session_ip': ldp_downstr_session_ip, }


