"""Generated client library for tpu version v2alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.tpu.v2alpha1 import tpu_v2alpha1_messages as messages


class TpuV2alpha1(base_api.BaseApiClient):
  """Generated client library for service tpu version v2alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://tpu.googleapis.com/'
  MTLS_BASE_URL = 'https://tpu.mtls.googleapis.com/'

  _PACKAGE = 'tpu'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v2alpha1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'TpuV2alpha1'
  _URL_VERSION = 'v2alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new tpu handle."""
    url = url or self.BASE_URL
    super(TpuV2alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_acceleratorTypes = self.ProjectsLocationsAcceleratorTypesService(self)
    self.projects_locations_nodes = self.ProjectsLocationsNodesService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_queuedResources = self.ProjectsLocationsQueuedResourcesService(self)
    self.projects_locations_runtimeVersions = self.ProjectsLocationsRuntimeVersionsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsAcceleratorTypesService(base_api.BaseApiService):
    """Service class for the projects_locations_acceleratorTypes resource."""

    _NAME = 'projects_locations_acceleratorTypes'

    def __init__(self, client):
      super(TpuV2alpha1.ProjectsLocationsAcceleratorTypesService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets AcceleratorType.

      Args:
        request: (TpuProjectsLocationsAcceleratorTypesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AcceleratorType) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/acceleratorTypes/{acceleratorTypesId}',
        http_method='GET',
        method_id='tpu.projects.locations.acceleratorTypes.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}',
        request_field='',
        request_type_name='TpuProjectsLocationsAcceleratorTypesGetRequest',
        response_type_name='AcceleratorType',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists accelerator types supported by this API.

      Args:
        request: (TpuProjectsLocationsAcceleratorTypesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAcceleratorTypesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/acceleratorTypes',
        http_method='GET',
        method_id='tpu.projects.locations.acceleratorTypes.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v2alpha1/{+parent}/acceleratorTypes',
        request_field='',
        request_type_name='TpuProjectsLocationsAcceleratorTypesListRequest',
        response_type_name='ListAcceleratorTypesResponse',
        supports_download=False,
    )

  class ProjectsLocationsNodesService(base_api.BaseApiService):
    """Service class for the projects_locations_nodes resource."""

    _NAME = 'projects_locations_nodes'

    def __init__(self, client):
      super(TpuV2alpha1.ProjectsLocationsNodesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a node.

      Args:
        request: (TpuProjectsLocationsNodesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/nodes',
        http_method='POST',
        method_id='tpu.projects.locations.nodes.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['nodeId', 'requestId'],
        relative_path='v2alpha1/{+parent}/nodes',
        request_field='node',
        request_type_name='TpuProjectsLocationsNodesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a node.

      Args:
        request: (TpuProjectsLocationsNodesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/nodes/{nodesId}',
        http_method='DELETE',
        method_id='tpu.projects.locations.nodes.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v2alpha1/{+name}',
        request_field='',
        request_type_name='TpuProjectsLocationsNodesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the details of a node.

      Args:
        request: (TpuProjectsLocationsNodesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Node) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/nodes/{nodesId}',
        http_method='GET',
        method_id='tpu.projects.locations.nodes.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}',
        request_field='',
        request_type_name='TpuProjectsLocationsNodesGetRequest',
        response_type_name='Node',
        supports_download=False,
    )

    def GetGuestAttributes(self, request, global_params=None):
      r"""Retrieves the guest attributes for the node.

      Args:
        request: (TpuProjectsLocationsNodesGetGuestAttributesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetGuestAttributesResponse) The response message.
      """
      config = self.GetMethodConfig('GetGuestAttributes')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetGuestAttributes.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/nodes/{nodesId}:getGuestAttributes',
        http_method='POST',
        method_id='tpu.projects.locations.nodes.getGuestAttributes',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}:getGuestAttributes',
        request_field='getGuestAttributesRequest',
        request_type_name='TpuProjectsLocationsNodesGetGuestAttributesRequest',
        response_type_name='GetGuestAttributesResponse',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists nodes.

      Args:
        request: (TpuProjectsLocationsNodesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListNodesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/nodes',
        http_method='GET',
        method_id='tpu.projects.locations.nodes.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v2alpha1/{+parent}/nodes',
        request_field='',
        request_type_name='TpuProjectsLocationsNodesListRequest',
        response_type_name='ListNodesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the configurations of a node.

      Args:
        request: (TpuProjectsLocationsNodesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/nodes/{nodesId}',
        http_method='PATCH',
        method_id='tpu.projects.locations.nodes.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v2alpha1/{+name}',
        request_field='node',
        request_type_name='TpuProjectsLocationsNodesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def SimulateMaintenanceEvent(self, request, global_params=None):
      r"""Simulates a maintenance event.

      Args:
        request: (TpuProjectsLocationsNodesSimulateMaintenanceEventRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('SimulateMaintenanceEvent')
      return self._RunMethod(
          config, request, global_params=global_params)

    SimulateMaintenanceEvent.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/nodes/{nodesId}:simulateMaintenanceEvent',
        http_method='POST',
        method_id='tpu.projects.locations.nodes.simulateMaintenanceEvent',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}:simulateMaintenanceEvent',
        request_field='simulateMaintenanceEventRequest',
        request_type_name='TpuProjectsLocationsNodesSimulateMaintenanceEventRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Start(self, request, global_params=None):
      r"""Starts a node.

      Args:
        request: (TpuProjectsLocationsNodesStartRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Start')
      return self._RunMethod(
          config, request, global_params=global_params)

    Start.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/nodes/{nodesId}:start',
        http_method='POST',
        method_id='tpu.projects.locations.nodes.start',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}:start',
        request_field='startNodeRequest',
        request_type_name='TpuProjectsLocationsNodesStartRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Stop(self, request, global_params=None):
      r"""Stops a node. This operation is only available with single TPU nodes.

      Args:
        request: (TpuProjectsLocationsNodesStopRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Stop')
      return self._RunMethod(
          config, request, global_params=global_params)

    Stop.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/nodes/{nodesId}:stop',
        http_method='POST',
        method_id='tpu.projects.locations.nodes.stop',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}:stop',
        request_field='stopNodeRequest',
        request_type_name='TpuProjectsLocationsNodesStopRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(TpuV2alpha1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (TpuProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='tpu.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}:cancel',
        request_field='',
        request_type_name='TpuProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (TpuProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='tpu.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}',
        request_field='',
        request_type_name='TpuProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (TpuProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='tpu.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}',
        request_field='',
        request_type_name='TpuProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (TpuProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='tpu.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v2alpha1/{+name}/operations',
        request_field='',
        request_type_name='TpuProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsQueuedResourcesService(base_api.BaseApiService):
    """Service class for the projects_locations_queuedResources resource."""

    _NAME = 'projects_locations_queuedResources'

    def __init__(self, client):
      super(TpuV2alpha1.ProjectsLocationsQueuedResourcesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a QueuedResource TPU instance.

      Args:
        request: (TpuProjectsLocationsQueuedResourcesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/queuedResources',
        http_method='POST',
        method_id='tpu.projects.locations.queuedResources.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['queuedResourceId', 'requestId'],
        relative_path='v2alpha1/{+parent}/queuedResources',
        request_field='queuedResource',
        request_type_name='TpuProjectsLocationsQueuedResourcesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a QueuedResource TPU instance.

      Args:
        request: (TpuProjectsLocationsQueuedResourcesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/queuedResources/{queuedResourcesId}',
        http_method='DELETE',
        method_id='tpu.projects.locations.queuedResources.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['force', 'requestId'],
        relative_path='v2alpha1/{+name}',
        request_field='',
        request_type_name='TpuProjectsLocationsQueuedResourcesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a queued resource.

      Args:
        request: (TpuProjectsLocationsQueuedResourcesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (QueuedResource) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/queuedResources/{queuedResourcesId}',
        http_method='GET',
        method_id='tpu.projects.locations.queuedResources.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}',
        request_field='',
        request_type_name='TpuProjectsLocationsQueuedResourcesGetRequest',
        response_type_name='QueuedResource',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists queued resources.

      Args:
        request: (TpuProjectsLocationsQueuedResourcesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListQueuedResourcesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/queuedResources',
        http_method='GET',
        method_id='tpu.projects.locations.queuedResources.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v2alpha1/{+parent}/queuedResources',
        request_field='',
        request_type_name='TpuProjectsLocationsQueuedResourcesListRequest',
        response_type_name='ListQueuedResourcesResponse',
        supports_download=False,
    )

    def Reset(self, request, global_params=None):
      r"""Resets a QueuedResource TPU instance.

      Args:
        request: (TpuProjectsLocationsQueuedResourcesResetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Reset')
      return self._RunMethod(
          config, request, global_params=global_params)

    Reset.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/queuedResources/{queuedResourcesId}:reset',
        http_method='POST',
        method_id='tpu.projects.locations.queuedResources.reset',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}:reset',
        request_field='resetQueuedResourceRequest',
        request_type_name='TpuProjectsLocationsQueuedResourcesResetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsRuntimeVersionsService(base_api.BaseApiService):
    """Service class for the projects_locations_runtimeVersions resource."""

    _NAME = 'projects_locations_runtimeVersions'

    def __init__(self, client):
      super(TpuV2alpha1.ProjectsLocationsRuntimeVersionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets a runtime version.

      Args:
        request: (TpuProjectsLocationsRuntimeVersionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RuntimeVersion) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/runtimeVersions/{runtimeVersionsId}',
        http_method='GET',
        method_id='tpu.projects.locations.runtimeVersions.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}',
        request_field='',
        request_type_name='TpuProjectsLocationsRuntimeVersionsGetRequest',
        response_type_name='RuntimeVersion',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists runtime versions supported by this API.

      Args:
        request: (TpuProjectsLocationsRuntimeVersionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListRuntimeVersionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}/runtimeVersions',
        http_method='GET',
        method_id='tpu.projects.locations.runtimeVersions.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v2alpha1/{+parent}/runtimeVersions',
        request_field='',
        request_type_name='TpuProjectsLocationsRuntimeVersionsListRequest',
        response_type_name='ListRuntimeVersionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(TpuV2alpha1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def GenerateServiceIdentity(self, request, global_params=None):
      r"""Generates the Cloud TPU service identity for the project.

      Args:
        request: (TpuProjectsLocationsGenerateServiceIdentityRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GenerateServiceIdentityResponse) The response message.
      """
      config = self.GetMethodConfig('GenerateServiceIdentity')
      return self._RunMethod(
          config, request, global_params=global_params)

    GenerateServiceIdentity.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}:generateServiceIdentity',
        http_method='POST',
        method_id='tpu.projects.locations.generateServiceIdentity',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v2alpha1/{+parent}:generateServiceIdentity',
        request_field='generateServiceIdentityRequest',
        request_type_name='TpuProjectsLocationsGenerateServiceIdentityRequest',
        response_type_name='GenerateServiceIdentityResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (TpuProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='tpu.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}',
        request_field='',
        request_type_name='TpuProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (TpuProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='tpu.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v2alpha1/{+name}/locations',
        request_field='',
        request_type_name='TpuProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(TpuV2alpha1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
