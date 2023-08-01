#!/usr/bin/env ruby
input = ARGV[0]

pattern = /hbt+n/

puts input.scan(pattern).join
