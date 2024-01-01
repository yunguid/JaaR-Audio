# -*- coding: utf-8 -*- #
# Copyright 2021 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utility for forming settings for Apt."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals


DEFAULT_TEMPLATE = """\
# To configure your package manager with this repository, do the following:

# Prepare your VM to access the repository using the following instructions:
# https://cloud.google.com/artifact-registry/docs/os-packages/debian/configure#prepare-apt

# Configure your VM to access Artifact Registry packages using the following
# command:

echo "deb ar+https://{location}-apt.pkg.dev/projects/{project} {repo} main" | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list

# Update Apt:
sudo apt update

# For complete setup information, see
# https://cloud.google.com/artifact-registry/docs/os-packages/debian/configure
"""


PUBLIC_TEMPLATE = """\
# To configure your package manager with this repository:

# Configure your VM to access Artifact Registry packages using the following
# command:

echo "deb https://{location}-apt.pkg.dev/projects/{project} {repo} main" | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list

# Update Apt:
sudo apt update

# For complete setup information, see
# https://cloud.google.com/artifact-registry/docs/os-packages/debian/configure
"""
