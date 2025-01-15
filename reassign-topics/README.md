# Script for re-balancing partitions on nodes

reference:
- https://rafael-natali.medium.com/automatically-reassigning-partitions-in-apache-kafka-cluster-cd2d920fd5c9
- https://github.com/rafaelmnatali/kafka-k8s/tree/main/scripts

Usage:
- Update kafka-topics.txt with the list of topics to rebalance
- Change brokers ids in the kafka-reassign.sh script
- Run kafka-reassign.sh in tmux
