
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

from cassandra.cluster import Cluster

from model.asgs import ASGModel, KEYSPACE

cluster = Cluster(contact_points=['docker-desktop'], port=9042)
session = cluster.connect(KEYSPACE)
connection = connection.register_connection('security-groups', session=session)

# assumes keyspace is already there
# create keyspace security_groups with replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
sync_table(ASGModel, connections=['security-groups'])

rm1 = ASGModel.create(name='dns',
                      org='',
                      space='',
                      dst='127.0.0.1',
                      dst_port='53',
                      logging=False)
rm2 = ASGModel.create(name='dns',
                      org='',
                      space='',
                      dst='192.168.1.10',
                      dst_port='53',
                      logging=False)
rm3 = ASGModel.create(name='syslog',
                      org='',
                      space='',
                      dst='127.0.0.1',
                      dst_port='514,601,6514',
                      logging=False)
rm4 = ASGModel.create(name='ldap',
                      org='',
                      space='',
                      dst='127.0.0.1',
                      dst_port='389,636',
                      logging=False)
