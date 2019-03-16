
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

from model.asgs import ASGModel, KEYSPACE

import yaml
import os
import sys

# this assumes keyspace is already in place.  You'll need
# create keyspace security_groups with replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}

cluster = Cluster(contact_points=['docker-desktop'], port=9042)
session = cluster.connect(KEYSPACE)
connection = connection.register_connection('security-groups', session=session)

sync_table(ASGModel, connections=['security-groups'])

if os.path.isfile('data/asg_samples.yml'):
    with open('data/asg_samples.yml') as s:
        data = yaml.load(s)
else:
    print "expected securit groups data structure file in data/asg_samples.yml"
    sys.exit(1)

if 'security_groups' not in data:
    print "expected security_groups key in data"
    sys.exit(1)

sgs = data['security_groups']
for sg in sgs:
    if 'name' not in sg:
        print "name required in sg", sg
        sys.exit(1)
    # if name already exists, we want to overwrite rules
    name = sg['name']
    rules = sg['rules']
    for r in ASGModel.objects.filter(name=name):
        r.delete()
    # set new rules
    for rule in rules:
        row = ASGModel.create(name=name, **rule)
        row.save()
