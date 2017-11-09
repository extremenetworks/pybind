
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class line(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-terminal - based on the path /terminal-cfg/line. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__sessionid','__exec_timeout',)

  _yang_name = 'line'
  _rest_name = 'line'

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
    self.__sessionid = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'vty': {'value': 2}},), is_leaf=True, yang_name="sessionid", rest_name="sessionid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Terminal type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-terminal', defining_module='brocade-terminal', yang_type='terminal-type', is_config=True)
    self.__exec_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..136']}), is_leaf=True, yang_name="exec-timeout", rest_name="exec-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'CLI session maximum idle time (in minutes) \nbefore automatic logout'}}, namespace='urn:brocade.com:mgmt:brocade-terminal', defining_module='brocade-terminal', yang_type='uint32', is_config=True)

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
      return [u'terminal-cfg', u'line']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'line']

  def _get_sessionid(self):
    """
    Getter method for sessionid, mapped from YANG variable /terminal_cfg/line/sessionid (terminal-type)
    """
    return self.__sessionid
      
  def _set_sessionid(self, v, load=False):
    """
    Setter method for sessionid, mapped from YANG variable /terminal_cfg/line/sessionid (terminal-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sessionid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sessionid() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'vty': {'value': 2}},), is_leaf=True, yang_name="sessionid", rest_name="sessionid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Terminal type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-terminal', defining_module='brocade-terminal', yang_type='terminal-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sessionid must be of a type compatible with terminal-type""",
          'defined-type': "brocade-terminal:terminal-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'vty': {'value': 2}},), is_leaf=True, yang_name="sessionid", rest_name="sessionid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Terminal type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-terminal', defining_module='brocade-terminal', yang_type='terminal-type', is_config=True)""",
        })

    self.__sessionid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sessionid(self):
    self.__sessionid = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'vty': {'value': 2}},), is_leaf=True, yang_name="sessionid", rest_name="sessionid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Terminal type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-terminal', defining_module='brocade-terminal', yang_type='terminal-type', is_config=True)


  def _get_exec_timeout(self):
    """
    Getter method for exec_timeout, mapped from YANG variable /terminal_cfg/line/exec_timeout (uint32)
    """
    return self.__exec_timeout
      
  def _set_exec_timeout(self, v, load=False):
    """
    Setter method for exec_timeout, mapped from YANG variable /terminal_cfg/line/exec_timeout (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exec_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exec_timeout() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..136']}), is_leaf=True, yang_name="exec-timeout", rest_name="exec-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'CLI session maximum idle time (in minutes) \nbefore automatic logout'}}, namespace='urn:brocade.com:mgmt:brocade-terminal', defining_module='brocade-terminal', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exec_timeout must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..136']}), is_leaf=True, yang_name="exec-timeout", rest_name="exec-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'CLI session maximum idle time (in minutes) \nbefore automatic logout'}}, namespace='urn:brocade.com:mgmt:brocade-terminal', defining_module='brocade-terminal', yang_type='uint32', is_config=True)""",
        })

    self.__exec_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exec_timeout(self):
    self.__exec_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..136']}), is_leaf=True, yang_name="exec-timeout", rest_name="exec-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'CLI session maximum idle time (in minutes) \nbefore automatic logout'}}, namespace='urn:brocade.com:mgmt:brocade-terminal', defining_module='brocade-terminal', yang_type='uint32', is_config=True)

  sessionid = __builtin__.property(_get_sessionid, _set_sessionid)
  exec_timeout = __builtin__.property(_get_exec_timeout, _set_exec_timeout)


  _pyangbind_elements = {'sessionid': sessionid, 'exec_timeout': exec_timeout, }


