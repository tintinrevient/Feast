# version 1
from feast import FeatureStore

# feature_store is de-serialized from registry
feature_store = FeatureStore(repo_path="feature_repo")

for feature_view in feature_store.list_feature_views():
    print('version 1 feature view ->', feature_view.name)

# version 2
from feast.protos.feast.core import Registry_pb2

# Registry_pb2.py is compiled from https://github.com/feast-dev/feast/blob/master/protos/feast/core/Registry.proto
registry = Registry_pb2.Registry()

with open('feature_repo/data/registry.db', "rb") as f:
    registry.ParseFromString(f.read())

for feature_view in registry.feature_views:
    print('version 2 feature view ->', feature_view.spec.name)