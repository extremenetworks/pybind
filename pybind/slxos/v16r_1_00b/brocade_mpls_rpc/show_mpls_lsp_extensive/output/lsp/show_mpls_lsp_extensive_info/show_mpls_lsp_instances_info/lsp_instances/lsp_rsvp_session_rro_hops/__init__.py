
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_mpls_lsp_hop_list
class lsp_rsvp_session_rro_hops(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-lsp-extensive/output/lsp/show-mpls-lsp-extensive-info/show-mpls-lsp-instances-info/lsp-instances/lsp-rsvp-session-rro-hops. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__show_mpls_lsp_hop_list',)

  _yang_name = 'lsp-rsvp-session-rro-hops'

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
    self.__show_mpls_lsp_hop_list = YANGDynClass(base=show_mpls_lsp_hop_list.show_mpls_lsp_hop_list, is_container='container', yang_name="show-mpls-lsp-hop-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-lsp-extensive', u'output', u'lsp', u'show-mpls-lsp-extensive-info', u'show-mpls-lsp-instances-info', u'lsp-instances', u'lsp-rsvp-session-rro-hops']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'show-mpls-lsp-extensive', u'output', u'lsp', u'lsp-instances', u'lsp-rsvp-session-rro-hops']

  def _get_show_mpls_lsp_hop_list(self):
    """
    Getter method for show_mpls_lsp_hop_list, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_extensive/output/lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_instances_info/lsp_instances/lsp_rsvp_session_rro_hops/show_mpls_lsp_hop_list (container)
    """
    return self.__show_mpls_lsp_hop_list
      
  def _set_show_mpls_lsp_hop_list(self, v, load=False):
    """
    Setter method for show_mpls_lsp_hop_list, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_extensive/output/lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_instances_info/lsp_instances/lsp_rsvp_session_rro_hops/show_mpls_lsp_hop_list (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_lsp_hop_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_lsp_hop_list() directly.
    """
    try:
      t = YANGDynClass(v,base=show_mpls_lsp_hop_list.show_mpls_lsp_hop_list, is_container='container', yang_name="show-mpls-lsp-hop-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_lsp_hop_list must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_lsp_hop_list.show_mpls_lsp_hop_list, is_container='container', yang_name="show-mpls-lsp-hop-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_lsp_hop_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_lsp_hop_list(self):
    self.__show_mpls_lsp_hop_list = YANGDynClass(base=show_mpls_lsp_hop_list.show_mpls_lsp_hop_list, is_container='container', yang_name="show-mpls-lsp-hop-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

  show_mpls_lsp_hop_list = __builtin__.property(_get_show_mpls_lsp_hop_list, _set_show_mpls_lsp_hop_list)


  _pyangbind_elements = {'show_mpls_lsp_hop_list': show_mpls_lsp_hop_list, }


