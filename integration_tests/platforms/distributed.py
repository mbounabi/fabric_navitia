# encoding: utf-8

from fabric.api import env
from fabfile.instance import add_instance
from common import env_common


def distributed(host1, host2):
    env.host1_ip, env.host2_ip = host1, host2
    env_common(tyr=(host1, host2), ed=(host1,), kraken=(host1, host2), jormun=(host1,))
    env.name = 'distributed'
    env.eng_hosts_1 = env.roledefs['eng'][:1]

    env.postgresql_database_host = 'localhost'
    env.use_zmq_socket_file = False
    env.rabbitmq_host = 'localhost'

    add_instance("fr-nw", "passwd", zmq_socket_port=30006, is_free=True, zmq_server='localhost')
    add_instance("fr-ne-amiens", "passwd*", zmq_socket_port=30019, zmq_server=host2)
    add_instance("fr-idf", "passwd", zmq_socket_port=30002, is_free=True, zmq_server=host2)
    add_instance("fr-cen", "passwd", zmq_socket_port=30000, zmq_server=host2)
    add_instance("us-wa", "passwd", zmq_socket_port=30023, is_free=True, zmq_server='localhost')
    add_instance("fr-npdc", "passwd", zmq_socket_port=30018, zmq_server='localhost')

