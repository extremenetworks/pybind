
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class tvf_domain(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/tvf-domain. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__tvfdomain_all','__tvfdomain_none','__tvfdomain_add','__tvfdomain_remove','__tvfdomain_except',)

  _yang_name = 'tvf-domain'
  _rest_name = 'tvf-domain'

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
    self.__tvfdomain_except = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="tvfdomain-except", rest_name="except", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'add all except these TVF Domains', u'alt-name': u'except'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='tvf-domain-range', is_config=True)
    self.__tvfdomain_none = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="tvfdomain-none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'remove all TVF Domains', u'cli-suppress-show-conf-path': None, u'alt-name': u'none'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__tvfdomain_remove = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="tvfdomain-remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'remove TVF Domains', u'alt-name': u'remove'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='tvf-domain-range', is_config=True)
    self.__tvfdomain_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="tvfdomain-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'add all TVF Domains', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__tvfdomain_add = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="tvfdomain-add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'add TVF Domains', u'alt-name': u'add'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='tvf-domain-range', is_config=True)

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
      return [u'interface', u'ethernet', u'tvf-domain']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'tvf-domain']

  def _get_tvfdomain_all(self):
    """
    Getter method for tvfdomain_all, mapped from YANG variable /interface/ethernet/tvf_domain/tvfdomain_all (empty)
    """
    return self.__tvfdomain_all
      
  def _set_tvfdomain_all(self, v, load=False):
    """
    Setter method for tvfdomain_all, mapped from YANG variable /interface/ethernet/tvf_domain/tvfdomain_all (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tvfdomain_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tvfdomain_all() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="tvfdomain-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'add all TVF Domains', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tvfdomain_all must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="tvfdomain-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'add all TVF Domains', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__tvfdomain_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tvfdomain_all(self):
    self.__tvfdomain_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="tvfdomain-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'add all TVF Domains', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_tvfdomain_none(self):
    """
    Getter method for tvfdomain_none, mapped from YANG variable /interface/ethernet/tvf_domain/tvfdomain_none (empty)
    """
    return self.__tvfdomain_none
      
  def _set_tvfdomain_none(self, v, load=False):
    """
    Setter method for tvfdomain_none, mapped from YANG variable /interface/ethernet/tvf_domain/tvfdomain_none (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tvfdomain_none is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tvfdomain_none() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="tvfdomain-none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'remove all TVF Domains', u'cli-suppress-show-conf-path': None, u'alt-name': u'none'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tvfdomain_none must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="tvfdomain-none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'remove all TVF Domains', u'cli-suppress-show-conf-path': None, u'alt-name': u'none'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__tvfdomain_none = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tvfdomain_none(self):
    self.__tvfdomain_none = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="tvfdomain-none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'remove all TVF Domains', u'cli-suppress-show-conf-path': None, u'alt-name': u'none'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_tvfdomain_add(self):
    """
    Getter method for tvfdomain_add, mapped from YANG variable /interface/ethernet/tvf_domain/tvfdomain_add (tvf-domain-range)
    """
    return self.__tvfdomain_add
      
  def _set_tvfdomain_add(self, v, load=False):
    """
    Setter method for tvfdomain_add, mapped from YANG variable /interface/ethernet/tvf_domain/tvfdomain_add (tvf-domain-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tvfdomain_add is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tvfdomain_add() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="tvfdomain-add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'add TVF Domains', u'alt-name': u'add'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='tvf-domain-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tvfdomain_add must be of a type compatible with tvf-domain-range""",
          'defined-type': "brocade-interface:tvf-domain-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="tvfdomain-add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'add TVF Domains', u'alt-name': u'add'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='tvf-domain-range', is_config=True)""",
        })

    self.__tvfdomain_add = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tvfdomain_add(self):
    self.__tvfdomain_add = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="tvfdomain-add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'add TVF Domains', u'alt-name': u'add'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='tvf-domain-range', is_config=True)


  def _get_tvfdomain_remove(self):
    """
    Getter method for tvfdomain_remove, mapped from YANG variable /interface/ethernet/tvf_domain/tvfdomain_remove (tvf-domain-range)
    """
    return self.__tvfdomain_remove
      
  def _set_tvfdomain_remove(self, v, load=False):
    """
    Setter method for tvfdomain_remove, mapped from YANG variable /interface/ethernet/tvf_domain/tvfdomain_remove (tvf-domain-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tvfdomain_remove is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tvfdomain_remove() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="tvfdomain-remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'remove TVF Domains', u'alt-name': u'remove'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='tvf-domain-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tvfdomain_remove must be of a type compatible with tvf-domain-range""",
          'defined-type': "brocade-interface:tvf-domain-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="tvfdomain-remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'remove TVF Domains', u'alt-name': u'remove'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='tvf-domain-range', is_config=True)""",
        })

    self.__tvfdomain_remove = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tvfdomain_remove(self):
    self.__tvfdomain_remove = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="tvfdomain-remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'remove TVF Domains', u'alt-name': u'remove'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='tvf-domain-range', is_config=True)


  def _get_tvfdomain_except(self):
    """
    Getter method for tvfdomain_except, mapped from YANG variable /interface/ethernet/tvf_domain/tvfdomain_except (tvf-domain-range)
    """
    return self.__tvfdomain_except
      
  def _set_tvfdomain_except(self, v, load=False):
    """
    Setter method for tvfdomain_except, mapped from YANG variable /interface/ethernet/tvf_domain/tvfdomain_except (tvf-domain-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tvfdomain_except is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tvfdomain_except() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="tvfdomain-except", rest_name="except", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'add all except these TVF Domains', u'alt-name': u'except'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='tvf-domain-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tvfdomain_except must be of a type compatible with tvf-domain-range""",
          'defined-type': "brocade-interface:tvf-domain-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="tvfdomain-except", rest_name="except", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'add all except these TVF Domains', u'alt-name': u'except'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='tvf-domain-range', is_config=True)""",
        })

    self.__tvfdomain_except = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tvfdomain_except(self):
    self.__tvfdomain_except = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-9][0-5])|(4096)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="tvfdomain-except", rest_name="except", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'add all except these TVF Domains', u'alt-name': u'except'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='tvf-domain-range', is_config=True)

  tvfdomain_all = __builtin__.property(_get_tvfdomain_all, _set_tvfdomain_all)
  tvfdomain_none = __builtin__.property(_get_tvfdomain_none, _set_tvfdomain_none)
  tvfdomain_add = __builtin__.property(_get_tvfdomain_add, _set_tvfdomain_add)
  tvfdomain_remove = __builtin__.property(_get_tvfdomain_remove, _set_tvfdomain_remove)
  tvfdomain_except = __builtin__.property(_get_tvfdomain_except, _set_tvfdomain_except)


  _pyangbind_elements = {'tvfdomain_all': tvfdomain_all, 'tvfdomain_none': tvfdomain_none, 'tvfdomain_add': tvfdomain_add, 'tvfdomain_remove': tvfdomain_remove, 'tvfdomain_except': tvfdomain_except, }


