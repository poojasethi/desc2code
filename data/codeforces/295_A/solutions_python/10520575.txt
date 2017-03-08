#!/usr/bin/env python
import sys

class Operation(object):
	def __init__(self, operation):
		self.left, self.right, self.increment = operation
		self.left -= 1
		self.right -= 1

class RangeAggregate(object):
	def __init__(self, range_sz):
		self.range_ = [ 0 ] * range_sz

	def range(self):
		current_aggregate = None
		for aggregate in self.range_:
			if current_aggregate is None:
				current_aggregate = aggregate
			else:
				current_aggregate += aggregate
			yield current_aggregate

	# left, right inclusive
	def merge(self, left, right, amount):
		self.range_[left] += amount
		if right + 1 < len(self.range_):
			self.range_[right + 1] -= amount

def merge(array_size, operations, queries):
	# merge queries
	query_aggregate = RangeAggregate(len(operations))
	for query in queries:
		query_aggregate.merge(query[0], query[1], 1)

	operation_aggregate = RangeAggregate(array_size)
	for operation, multiplier in zip(operations, query_aggregate.range()):
		operation_aggregate.merge(operation.left, operation.right, operation.increment * multiplier)

	result = operation_aggregate.range()
	return result

if __name__ == "__main__":
	array_sz, n_operations, n_queries = map(int, sys.stdin.readline().split())
	array = map(int, sys.stdin.readline().split())
	if len(array) != array_sz:
		raise Exception

	operations = [ None ] * n_operations
	for i in xrange(n_operations):
		operations[i] = Operation(map(int, sys.stdin.readline().split()))

	queries = [ None ] * n_queries
	for i in xrange(n_queries):
		queries[i] = [x - 1 for x in map(int, sys.stdin.readline().split())]

	# n_queries O(10^5), array_sz O(10^5), n_operations O(10^5)
	# n^3 too slow, need to merge queried operations
	addition = merge(array_sz, operations, queries)
	array = [sum(x) for x in zip(array, addition)]
	print " ".join(map(str, array))
