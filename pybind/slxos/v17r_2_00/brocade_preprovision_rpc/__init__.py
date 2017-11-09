
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_bare_metal_state
class brocade_preprovision(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-preprovision - based on the path /brocade_preprovision_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This management module is an instrumentation to manage preprovision
feature.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__show_bare_metal_state',)

  _yang_name = 'brocade-preprovision'
  _rest_name = ''

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
    self.__show_bare_metal_state = YANGDynClass(base=show_bare_metal_state.show_bare_metal_state, is_leaf=True, yang_name="show-bare-metal-state", rest_name="show-bare-metal-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve bare-metal state.', u'hidden': u'full', u'actionpoint': u'get-bare-metal-state'}}, namespace='urn:brocade.com:mgmt:brocade-preprovision', defining_module='brocade-preprovision', yang_type='rpc', is_config=True)

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
      return [u'brocade_preprovision_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_show_bare_metal_state(self):
    """
    Getter method for show_bare_metal_state, mapped from YANG variable /brocade_preprovision_rpc/show_bare_metal_state (rpc)
    """
    return self.__show_bare_metal_state
      
  def _set_show_bare_metal_state(self, v, load=False):
    """
    Setter method for show_bare_metal_state, mapped from YANG variable /brocade_preprovision_rpc/show_bare_metal_state (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_bare_metal_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_bare_metal_state() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=show_bare_metal_state.show_bare_metal_state, is_leaf=True, yang_name="show-bare-metal-state", rest_name="show-bare-metal-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve bare-metal state.', u'hidden': u'full', u'actionpoint': u'get-bare-metal-state'}}, namespace='urn:brocade.com:mgmt:brocade-preprovision', defining_module='brocade-preprovision', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_bare_metal_state must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=show_bare_metal_state.show_bare_metal_state, is_leaf=True, yang_name="show-bare-metal-state", rest_name="show-bare-metal-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve bare-metal state.', u'hidden': u'full', u'actionpoint': u'get-bare-metal-state'}}, namespace='urn:brocade.com:mgmt:brocade-preprovision', defining_module='brocade-preprovision', yang_type='rpc', is_config=True)""",
        })

    self.__show_bare_metal_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_bare_metal_state(self):
    self.__show_bare_metal_state = YANGDynClass(base=show_bare_metal_state.show_bare_metal_state, is_leaf=True, yang_name="show-bare-metal-state", rest_name="show-bare-metal-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Retrieve bare-metal state.', u'hidden': u'full', u'actionpoint': u'get-bare-metal-state'}}, namespace='urn:brocade.com:mgmt:brocade-preprovision', defining_module='brocade-preprovision', yang_type='rpc', is_config=True)

  show_bare_metal_state = __builtin__.property(_get_show_bare_metal_state, _set_show_bare_metal_state)


  _pyangbind_elements = {'show_bare_metal_state': show_bare_metal_state, }


