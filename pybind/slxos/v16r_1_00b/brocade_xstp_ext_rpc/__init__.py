
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import get_stp_brief_info
import get_stp_mst_detail
class brocade_xstp_ext(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-xstp-ext - based on the path /brocade_xstp_ext_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module describes the data model for Spanning Tree
Protocol

Glossary of the terms used:
---------------------------
CIST   Common and Internal Spanning Tree (IEEE 802.1Q)

  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__get_stp_brief_info','__get_stp_mst_detail',)

  _yang_name = 'brocade-xstp-ext'

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
    self.__get_stp_mst_detail = YANGDynClass(base=get_stp_mst_detail.get_stp_mst_detail, is_leaf=True, yang_name="get-stp-mst-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show-spanning-tree-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='rpc', is_config=True)
    self.__get_stp_brief_info = YANGDynClass(base=get_stp_brief_info.get_stp_brief_info, is_leaf=True, yang_name="get-stp-brief-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show-spanning-tree-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='rpc', is_config=True)

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
      return [u'brocade_xstp_ext_rpc']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return []

  def _get_get_stp_brief_info(self):
    """
    Getter method for get_stp_brief_info, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info (rpc)

    YANG Description: RPC to return spanning tree information similar to the
CLI 'show spanning-tree'.
    """
    return self.__get_stp_brief_info
      
  def _set_get_stp_brief_info(self, v, load=False):
    """
    Setter method for get_stp_brief_info, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_stp_brief_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_stp_brief_info() directly.

    YANG Description: RPC to return spanning tree information similar to the
CLI 'show spanning-tree'.
    """
    try:
      t = YANGDynClass(v,base=get_stp_brief_info.get_stp_brief_info, is_leaf=True, yang_name="get-stp-brief-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show-spanning-tree-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_stp_brief_info must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_stp_brief_info.get_stp_brief_info, is_leaf=True, yang_name="get-stp-brief-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show-spanning-tree-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='rpc', is_config=True)""",
        })

    self.__get_stp_brief_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_stp_brief_info(self):
    self.__get_stp_brief_info = YANGDynClass(base=get_stp_brief_info.get_stp_brief_info, is_leaf=True, yang_name="get-stp-brief-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show-spanning-tree-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='rpc', is_config=True)


  def _get_get_stp_mst_detail(self):
    """
    Getter method for get_stp_mst_detail, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail (rpc)

    YANG Description: RPC to return MSTP details.. 
Equivalent to CLI 'show spanning-tree mst detail'.
    """
    return self.__get_stp_mst_detail
      
  def _set_get_stp_mst_detail(self, v, load=False):
    """
    Setter method for get_stp_mst_detail, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_stp_mst_detail is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_stp_mst_detail() directly.

    YANG Description: RPC to return MSTP details.. 
Equivalent to CLI 'show spanning-tree mst detail'.
    """
    try:
      t = YANGDynClass(v,base=get_stp_mst_detail.get_stp_mst_detail, is_leaf=True, yang_name="get-stp-mst-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show-spanning-tree-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_stp_mst_detail must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_stp_mst_detail.get_stp_mst_detail, is_leaf=True, yang_name="get-stp-mst-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show-spanning-tree-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='rpc', is_config=True)""",
        })

    self.__get_stp_mst_detail = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_stp_mst_detail(self):
    self.__get_stp_mst_detail = YANGDynClass(base=get_stp_mst_detail.get_stp_mst_detail, is_leaf=True, yang_name="get-stp-mst-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show-spanning-tree-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='rpc', is_config=True)

  get_stp_brief_info = __builtin__.property(_get_get_stp_brief_info, _set_get_stp_brief_info)
  get_stp_mst_detail = __builtin__.property(_get_get_stp_mst_detail, _set_get_stp_mst_detail)


  _pyangbind_elements = {'get_stp_brief_info': get_stp_brief_info, 'get_stp_mst_detail': get_stp_mst_detail, }


