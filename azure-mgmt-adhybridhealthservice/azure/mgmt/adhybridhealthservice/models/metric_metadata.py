# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MetricMetadata(Model):
    """The metric meta data.

    :param metrics_processor_class_name: The name of the class which retrieve
     and process the metric.
    :type metrics_processor_class_name: str
    :param metric_name: The metric name
    :type metric_name: str
    :param groupings: The groupings for the metrics.
    :type groupings:
     list[~azure.mgmt.adhybridhealthservice.models.MetricGroup]
    :param display_name: The display name for the metric.
    :type display_name: str
    :param value_kind: Indicates if the metrics is a rate,value, percent or
     duration type.
    :type value_kind: str
    :param min_value: The minimum value.
    :type min_value: int
    :param max_value: The maximum value.
    :type max_value: int
    :param kind: Indicates whether the dashboard to represent the metric is a
     line, bar,pie, area or donut chart.
    :type kind: str
    :param is_default: Indicates if the metric is a default metric or not.
    :type is_default: bool
    :param is_perf_counter: Indicates if the metric is a performance counter
     metric or not.
    :type is_perf_counter: bool
    :param is_dev_ops: Indicates if the metric is visible to DevOps or not.
    :type is_dev_ops: bool
    """

    _attribute_map = {
        'metrics_processor_class_name': {'key': 'metricsProcessorClassName', 'type': 'str'},
        'metric_name': {'key': 'metricName', 'type': 'str'},
        'groupings': {'key': 'groupings', 'type': '[MetricGroup]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'value_kind': {'key': 'valueKind', 'type': 'str'},
        'min_value': {'key': 'minValue', 'type': 'int'},
        'max_value': {'key': 'maxValue', 'type': 'int'},
        'kind': {'key': 'kind', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'is_perf_counter': {'key': 'isPerfCounter', 'type': 'bool'},
        'is_dev_ops': {'key': 'isDevOps', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(MetricMetadata, self).__init__(**kwargs)
        self.metrics_processor_class_name = kwargs.get('metrics_processor_class_name', None)
        self.metric_name = kwargs.get('metric_name', None)
        self.groupings = kwargs.get('groupings', None)
        self.display_name = kwargs.get('display_name', None)
        self.value_kind = kwargs.get('value_kind', None)
        self.min_value = kwargs.get('min_value', None)
        self.max_value = kwargs.get('max_value', None)
        self.kind = kwargs.get('kind', None)
        self.is_default = kwargs.get('is_default', None)
        self.is_perf_counter = kwargs.get('is_perf_counter', None)
        self.is_dev_ops = kwargs.get('is_dev_ops', None)