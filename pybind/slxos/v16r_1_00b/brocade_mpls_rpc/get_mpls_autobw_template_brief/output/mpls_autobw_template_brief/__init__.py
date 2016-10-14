
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import template_list
class mpls_autobw_template_brief(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/get-mpls-autobw-template-brief/output/mpls-autobw-template-brief. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__num_autobw_template','__template_list',)

  _yang_name = 'mpls-autobw-template-brief'

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
    self.__template_list = YANGDynClass(base=YANGListType("autobwTemplateName",template_list.template_list, yang_name="template-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='autobwTemplateName', extensions=None), is_container='list', yang_name="template-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    self.__num_autobw_template = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-autobw-template", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'get-mpls-autobw-template-brief', u'output', u'mpls-autobw-template-brief']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'get-mpls-autobw-template-brief', u'output', u'mpls-autobw-template-brief']

  def _get_num_autobw_template(self):
    """
    Getter method for num_autobw_template, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_brief/output/mpls_autobw_template_brief/num_autobw_template (uint32)

    YANG Description: Number of auto-bandwidth templates
    """
    return self.__num_autobw_template
      
  def _set_num_autobw_template(self, v, load=False):
    """
    Setter method for num_autobw_template, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_brief/output/mpls_autobw_template_brief/num_autobw_template (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_autobw_template is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_autobw_template() directly.

    YANG Description: Number of auto-bandwidth templates
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-autobw-template", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_autobw_template must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-autobw-template", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__num_autobw_template = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_autobw_template(self):
    self.__num_autobw_template = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-autobw-template", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_template_list(self):
    """
    Getter method for template_list, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_brief/output/mpls_autobw_template_brief/template_list (list)
    """
    return self.__template_list
      
  def _set_template_list(self, v, load=False):
    """
    Setter method for template_list, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_brief/output/mpls_autobw_template_brief/template_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_template_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_template_list() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("autobwTemplateName",template_list.template_list, yang_name="template-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='autobwTemplateName', extensions=None), is_container='list', yang_name="template-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """template_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("autobwTemplateName",template_list.template_list, yang_name="template-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='autobwTemplateName', extensions=None), is_container='list', yang_name="template-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__template_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_template_list(self):
    self.__template_list = YANGDynClass(base=YANGListType("autobwTemplateName",template_list.template_list, yang_name="template-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='autobwTemplateName', extensions=None), is_container='list', yang_name="template-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

  num_autobw_template = __builtin__.property(_get_num_autobw_template, _set_num_autobw_template)
  template_list = __builtin__.property(_get_template_list, _set_template_list)


  _pyangbind_elements = {'num_autobw_template': num_autobw_template, 'template_list': template_list, }


