
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import http
class http_sa(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-http-config - based on the path /http-sa. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__http',)

  _yang_name = 'http-sa'

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
    self.__http = YANGDynClass(base=http.http, is_container='container', yang_name="http", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure HTTP Server', u'cli-incomplete-no': None, u'sort-priority': u'3'}}, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='container', is_config=True)

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
      return [u'http-sa']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return []

  def _get_http(self):
    """
    Getter method for http, mapped from YANG variable /http_sa/http (container)
    """
    return self.__http
      
  def _set_http(self, v, load=False):
    """
    Setter method for http, mapped from YANG variable /http_sa/http (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_http is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_http() directly.
    """
    try:
      t = YANGDynClass(v,base=http.http, is_container='container', yang_name="http", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure HTTP Server', u'cli-incomplete-no': None, u'sort-priority': u'3'}}, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """http must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=http.http, is_container='container', yang_name="http", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure HTTP Server', u'cli-incomplete-no': None, u'sort-priority': u'3'}}, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='container', is_config=True)""",
        })

    self.__http = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_http(self):
    self.__http = YANGDynClass(base=http.http, is_container='container', yang_name="http", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure HTTP Server', u'cli-incomplete-no': None, u'sort-priority': u'3'}}, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='container', is_config=True)

  http = __builtin__.property(_get_http, _set_http)


  _pyangbind_elements = {'http': http, }


