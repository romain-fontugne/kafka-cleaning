import sys
import os

def delete_topics(topics):
    """ delete topics """

    for topic in topics:
        print(f'Deleting {topic}')
        os.system(f'zookeeper-shell kafka1.storage.iijlab.net:2181 deleteall /brokers/topics/{topic}')
        os.system(f'zookeeper-shell kafka1.storage.iijlab.net:2181 deleteall /admin/delete_topics/{topic}')

def main(fname):

    with open(fname, 'r') as fp:
        topics = fp.read().splitlines()

    delete_topics(topics) 

if __name__ == '__main__':

    fname = sys.argv[1]
    main(fname)
# deleteall /brokers/topics/ihr_bcscore_prefix_ipv4_route-views5
# deleteall /admin/delete_topics/ihr_bcscore_prefix_ipv4_route-views5


