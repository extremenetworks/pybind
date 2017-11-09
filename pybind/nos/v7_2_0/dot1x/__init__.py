
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import test
class dot1x(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1x - based on the path /dot1x. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This provides grouping of all the dot1x configuration
elements.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__enable','__test',)

  _yang_name = 'dot1x'
  _rest_name = 'dot1x'

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
    self.__test = YANGDynClass(base=test.test, is_container='container', presence=False, yang_name="test", rest_name="test", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='container', is_config=True)
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='empty', is_config=True)

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
      return [u'dot1x']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'dot1x']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /dot1x/enable (empty)

    YANG Description: This specifies if the port authentication is enabled 
globally or not.
                
The presence of this leaf indicates that the port 
authentication is enabled globally.
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /dot1x/enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: This specifies if the port authentication is enabled 
globally or not.
                
The presence of this leaf indicates that the port 
authentication is enabled globally.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='empty', is_config=True)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='empty', is_config=True)


  def _get_test(self):
    """
    Getter method for test, mapped from YANG variable /dot1x/test (container)

    YANG Description: This provides the grouping of dot1x test elements.
    """
    return self.__test
      
  def _set_test(self, v, load=False):
    """
    Setter method for test, mapped from YANG variable /dot1x/test (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_test is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_test() directly.

    YANG Description: This provides the grouping of dot1x test elements.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=test.test, is_container='container', presence=False, yang_name="test", rest_name="test", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """test must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=test.test, is_container='container', presence=False, yang_name="test", rest_name="test", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='container', is_config=True)""",
        })

    self.__test = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_test(self):
    self.__test = YANGDynClass(base=test.test, is_container='container', presence=False, yang_name="test", rest_name="test", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='container', is_config=True)

  enable = __builtin__.property(_get_enable, _set_enable)
  test = __builtin__.property(_get_test, _set_test)


  _pyangbind_elements = {'enable': enable, 'test': test, }


