
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import clear_mpls_rsvp_statistics_out
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/clear-mpls-rsvp-statistics/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__clear_mpls_rsvp_statistics_out',)

  _yang_name = 'output'

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
    self.__clear_mpls_rsvp_statistics_out = YANGDynClass(base=clear_mpls_rsvp_statistics_out.clear_mpls_rsvp_statistics_out, is_container='container', yang_name="clear-mpls-rsvp-statistics-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

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
      return [u'brocade_mpls_rpc', u'clear-mpls-rsvp-statistics', u'output']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'clear-mpls-rsvp-statistics', u'output']

  def _get_clear_mpls_rsvp_statistics_out(self):
    """
    Getter method for clear_mpls_rsvp_statistics_out, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_rsvp_statistics/output/clear_mpls_rsvp_statistics_out (container)
    """
    return self.__clear_mpls_rsvp_statistics_out
      
  def _set_clear_mpls_rsvp_statistics_out(self, v, load=False):
    """
    Setter method for clear_mpls_rsvp_statistics_out, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_rsvp_statistics/output/clear_mpls_rsvp_statistics_out (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_clear_mpls_rsvp_statistics_out is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_clear_mpls_rsvp_statistics_out() directly.
    """
    try:
      t = YANGDynClass(v,base=clear_mpls_rsvp_statistics_out.clear_mpls_rsvp_statistics_out, is_container='container', yang_name="clear-mpls-rsvp-statistics-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """clear_mpls_rsvp_statistics_out must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=clear_mpls_rsvp_statistics_out.clear_mpls_rsvp_statistics_out, is_container='container', yang_name="clear-mpls-rsvp-statistics-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__clear_mpls_rsvp_statistics_out = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_clear_mpls_rsvp_statistics_out(self):
    self.__clear_mpls_rsvp_statistics_out = YANGDynClass(base=clear_mpls_rsvp_statistics_out.clear_mpls_rsvp_statistics_out, is_container='container', yang_name="clear-mpls-rsvp-statistics-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

  clear_mpls_rsvp_statistics_out = __builtin__.property(_get_clear_mpls_rsvp_statistics_out, _set_clear_mpls_rsvp_statistics_out)


  _pyangbind_elements = {'clear_mpls_rsvp_statistics_out': clear_mpls_rsvp_statistics_out, }


