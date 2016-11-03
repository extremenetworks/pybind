
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import map_fport
class map_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ag/nport-menu/nport-interface/nport/map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__map_fport',)

  _yang_name = 'map'
  _rest_name = 'map'

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
    self.__map_fport = YANGDynClass(base=map_fport.map_fport, is_container='container', yang_name="map-fport", rest_name="fport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'fport'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'ag', u'nport-menu', u'nport-interface', u'nport', u'map']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ag', u'nport', u'interface', u'FiberChannel', u'map']

  def _get_map_fport(self):
    """
    Getter method for map_fport, mapped from YANG variable /rbridge_id/ag/nport_menu/nport_interface/nport/map/map_fport (container)
    """
    return self.__map_fport
      
  def _set_map_fport(self, v, load=False):
    """
    Setter method for map_fport, mapped from YANG variable /rbridge_id/ag/nport_menu/nport_interface/nport/map/map_fport (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_fport is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_fport() directly.
    """
    try:
      t = YANGDynClass(v,base=map_fport.map_fport, is_container='container', yang_name="map-fport", rest_name="fport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'fport'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_fport must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=map_fport.map_fport, is_container='container', yang_name="map-fport", rest_name="fport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'fport'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)""",
        })

    self.__map_fport = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_fport(self):
    self.__map_fport = YANGDynClass(base=map_fport.map_fport, is_container='container', yang_name="map-fport", rest_name="fport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'fport'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)

  map_fport = __builtin__.property(_get_map_fport, _set_map_fport)


  _pyangbind_elements = {'map_fport': map_fport, }

